#!/usr/bin/env python3
"""
สร้างไฟล์ data/geo.js (ขอบเขตแผนที่) จาก shapefile

ใช้เมื่อต้องการเปลี่ยนขอบเขตอำเภอ/จังหวัด/ประเทศ ที่แสดงบนแผนที่ เช่น เพิ่มจังหวัดใหม่

ติดตั้งไลบรารี (ครั้งเดียว):
    pip install pyshp shapely pyproj

ตัวอย่างการใช้งาน (รันที่โฟลเดอร์รากของรีโป):
    python tools/build_geo.py \
        --prov  source/9UNT_subprovince_1.shp \
        --world source/world-administrative-boundaries_1.shp \
        --config data/config.js \
        --out data/geo.js

หมายเหตุ
  * shapefile อำเภอ/จังหวัดต้องมีไฟล์ .prj (ระบบพิกัด) อยู่ข้างๆ สคริปต์จะแปลงเป็น WGS84 ให้เอง
    ถ้าไม่มี .prj ให้ระบุ --crs เช่น EPSG:32647 (UTM โซน 47N)
  * ชื่อฟิลด์ใน shapefile อำเภอ: จังหวัด/อำเภอ/พื้นที่ ปรับได้ด้วย --f-prov --f-amp --f-area
  * --config ใช้อ่านพิกัดสถานีเพื่อวางชื่อจังหวัดไม่ให้ทับวงกลมสถานี (ไม่ใส่ก็ได้)
  * ขอบเขตกรอบแผนที่ตั้งด้วย --bbox LON0 LON1 LAT0 LAT1
    (ค่าเริ่มต้น 97.10 101.65 14.95 20.75 = ครอบคลุม 9 จังหวัดภาคเหนือตอนบน)
"""
import argparse, json, math, os, sys

try:
    import shapefile
    from pyproj import Transformer, CRS
    from shapely.geometry import shape, box, Point, Polygon, MultiPolygon
    from shapely.ops import unary_union, transform
except ImportError:
    sys.exit("ต้องติดตั้งไลบรารีก่อน:  pip install pyshp shapely pyproj")

TH_NAMES = {'THA': 'ไทย', 'MMR': 'เมียนมา', 'LAO': 'ลาว', 'CHN': 'จีน', 'VNM': 'เวียดนาม', 'KHM': 'กัมพูชา'}


def read_stations(path):
    """อ่านพิกัดสถานีจาก data/config.js (ถ้ามี)"""
    if not path or not os.path.exists(path):
        return []
    txt = open(path, encoding='utf-8').read()
    body = txt[txt.index('=') + 1:].strip().rstrip(';')
    cfg = json.loads(body)
    pts = []
    for s in cfg.get('stations', []):
        try:
            pts.append((float(s['lon']), float(s['lat'])))
        except (TypeError, ValueError, KeyError):
            pass
    return pts


def drop_small_holes(g, min_area=3e-4):
    """ตัดช่องว่างเล็กๆ ที่เหลือจากการรวมอำเภอเป็นจังหวัด (ไม่ใช่เขตแดนจริง)"""
    def fix(p):
        return Polygon(p.exterior.coords, [i for i in p.interiors if Polygon(i).area >= min_area])
    if g.geom_type == 'Polygon':
        return fix(g)
    if g.geom_type == 'MultiPolygon':
        return MultiPolygon([fix(p) for p in g.geoms])
    return g


def main():
    ap = argparse.ArgumentParser(description='shapefile -> data/geo.js')
    ap.add_argument('--prov', required=True, help='shapefile อำเภอ (.shp)')
    ap.add_argument('--world', help='shapefile ขอบเขตประเทศ (.shp) ไม่ใส่ก็ได้')
    ap.add_argument('--config', default='data/config.js', help='data/config.js (ใช้อ่านพิกัดสถานี)')
    ap.add_argument('--out', default='data/geo.js')
    ap.add_argument('--crs', default=None, help='ระบบพิกัดของ shapefile อำเภอ ถ้าไม่มีไฟล์ .prj')
    ap.add_argument('--bbox', nargs=4, type=float, default=[97.10, 101.65, 14.95, 20.75], metavar=('LON0', 'LON1', 'LAT0', 'LAT1'))
    ap.add_argument('--width', type=float, default=650.0, help='ความกว้างของพิกัดแผนที่ (หน่วยจุด)')
    ap.add_argument('--simplify', type=float, default=0.0025, help='ความหยาบของเส้นอำเภอ (องศา)')
    ap.add_argument('--world-simplify', type=float, default=0.004)
    ap.add_argument('--f-prov', default='P_NAME_T')
    ap.add_argument('--f-amp', default='A_NAME_T')
    ap.add_argument('--f-area', default='Area_km2')
    a = ap.parse_args()

    LON0, LON1, LAT0, LAT1 = a.bbox
    phi = math.radians((LAT0 + LAT1) / 2)
    k = a.width / ((LON1 - LON0) * math.cos(phi))
    kx, ky = k * math.cos(phi), k
    H = round((LAT1 - LAT0) * ky, 1)
    PROJ = dict(lon0=LON0, lat1=LAT1, kx=round(kx, 4), ky=round(ky, 4), W=a.width, H=H, lat0=LAT0, lon1=LON1)

    def P(lon, lat):
        return ((lon - LON0) * kx, (LAT1 - lat) * ky)

    def ring_d(coords):
        pts, last = [], None
        for lon, lat in coords:
            x, y = P(lon, lat)
            p = (round(x, 1), round(y, 1))
            if p != last:
                pts.append(p)
                last = p
        if len(pts) < 3:
            return ''
        return 'M' + 'L'.join('%g,%g' % (x, y) for x, y in pts) + 'Z'

    def geom_d(g):
        if g.geom_type == 'Polygon':
            polys = [g]
        elif g.geom_type in ('MultiPolygon', 'GeometryCollection'):
            polys = [p for p in g.geoms if p.geom_type == 'Polygon']
        else:
            polys = []
        out = []
        for p in polys:
            out.append(ring_d(p.exterior.coords))
            for i in p.interiors:
                out.append(ring_d(i.coords))
        return ''.join(out)

    # ---- ระบบพิกัด ----
    prj = os.path.splitext(a.prov)[0] + '.prj'
    if a.crs:
        src = CRS.from_user_input(a.crs)
    elif os.path.exists(prj):
        src = CRS.from_wkt(open(prj).read())
    else:
        sys.exit('ไม่พบไฟล์ .prj ของ %s — ระบุ --crs เช่น EPSG:32647' % a.prov)
    tr = Transformer.from_crs(src, 'EPSG:4326', always_xy=True)

    # ---- อำเภอ ----
    sf = shapefile.Reader(a.prov, encoding='utf-8')
    names = [f[0] for f in sf.fields[1:]]
    for f in (a.f_prov, a.f_amp, a.f_area):
        if f not in names:
            sys.exit('ไม่พบฟิลด์ %s ใน shapefile (มี: %s) — ใช้ --f-prov/--f-amp/--f-area ระบุชื่อฟิลด์' % (f, ', '.join(names)))
    amps = []
    for sh, rec in zip(sf.shapes(), sf.records()):
        r = dict(zip(names, rec))
        g = shape(sh.__geo_interface__)
        g = transform(lambda x, y, z=None: tr.transform(x, y), g)
        if not g.is_valid:
            g = g.buffer(0)
        g = g.simplify(a.simplify, preserve_topology=True)
        amps.append(dict(prov=str(r[a.f_prov]).strip(), name=str(r[a.f_amp]).strip(), area=round(float(r[a.f_area]), 1), geom=g))
    provs = []
    for x in amps:
        if x['prov'] not in provs:
            provs.append(x['prov'])
    print('อำเภอ', len(amps), 'จังหวัด', len(provs), provs)

    stations = read_stations(a.config)
    print('พิกัดสถานีที่ใช้วางชื่อจังหวัด:', len(stations))
    sp = [Point(x, y) for x, y in stations]

    prov_geo = []
    for pn in provs:
        u = drop_small_holes(unary_union([x['geom'] for x in amps if x['prov'] == pn]))
        minx, miny, maxx, maxy = u.bounds
        best, n = None, 60
        for i in range(n + 1):
            for j in range(n + 1):
                q = Point(minx + (maxx - minx) * i / n, miny + (maxy - miny) * j / n)
                if not u.contains(q):
                    continue
                db = u.boundary.distance(q)
                ds = min([q.distance(x) for x in sp] or [9])
                sc = min(db * 1.0, ds * 1.25)
                if best is None or sc > best[0]:
                    best = (sc, q)
        rp = best[1] if best else u.representative_point()
        lx, ly = P(rp.x, rp.y)
        am_list = []
        for x in amps:
            if x['prov'] != pn:
                continue
            r2 = x['geom'].representative_point()
            ax, ay = P(r2.x, r2.y)
            am_list.append(dict(name=x['name'], area=x['area'], d=geom_d(x['geom']), lx=round(ax, 1), ly=round(ay, 1)))
        prov_geo.append(dict(name=pn, d=geom_d(u), lx=round(lx, 1), ly=round(ly, 1),
                             area=round(sum(x['area'] for x in amps if x['prov'] == pn), 1), amphoes=am_list))

    # ---- ประเทศ ----
    countries = []
    if a.world:
        ws = shapefile.Reader(a.world, encoding='utf-8')
        wn = [f[0] for f in ws.fields[1:]]
        view = box(LON0, LAT0, LON1, LAT1)
        for sh, rec in zip(ws.shapes(), ws.records()):
            r = dict(zip(wn, rec))
            iso = str(r.get('iso3', '')).strip()
            if not sh.points:
                continue
            b = sh.bbox
            if b[2] < LON0 or b[0] > LON1 or b[3] < LAT0 or b[1] > LAT1:
                continue
            g = shape(sh.__geo_interface__)
            if not g.is_valid:
                g = g.buffer(0)
            c = g.intersection(view)
            if c.is_empty:
                continue
            c = c.simplify(a.world_simplify, preserve_topology=True)
            rp = c.representative_point()
            lx, ly = P(rp.x, rp.y)
            countries.append(dict(iso=iso, name=TH_NAMES.get(iso, str(r.get('name', iso)).strip()),
                                  d=geom_d(c), lx=round(lx, 1), ly=round(ly, 1)))
        print('ประเทศ', [c['iso'] for c in countries])

    geo = dict(proj=PROJ, countries=countries, provinces=prov_geo)
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w', encoding='utf-8') as f:
        f.write('window.GEO=' + json.dumps(geo, ensure_ascii=False, separators=(',', ':')) + ';\n')
    print('เขียนไฟล์', a.out, os.path.getsize(a.out) // 1024, 'KB')


if __name__ == '__main__':
    main()
