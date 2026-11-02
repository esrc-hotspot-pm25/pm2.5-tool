window.PM25_CFG={
 "meta": {
  "title": "PM2.5 ภาคเหนือตอนบน",
  "updated": "2026-10-30"
 },
 "settings": {
  "th": 37.5,
  "who": 15,
  "groupMethod": "province",
  "smokeMonths": [
   2,
   3,
   4,
   5
  ]
 },
 "sets": [
  {
   "id": "k11",
   "label": "11 สถานี",
   "sub": "กรมควบคุมมลพิษ",
   "years": [
    2012,
    2025
   ],
   "minCoverage": 0.75,
   "sampled": false,
   "source": "กรมควบคุมมลพิษ (ข้อมูลรายวัน 11 สถานี)",
   "note": ""
  },
  {
   "id": "s3",
   "label": "3 สถานี",
   "sub": "CM · LP · LI",
   "years": [
    2026,
    2026
   ],
   "minCoverage": 0,
   "sampled": true,
   "source": "ข้อมูล CM · LP · LI (ไฟล์ PM2.5-PSCF) มี.ค.–ส.ค. 2026",
   "note": "ชุดข้อมูลนี้เป็นตัวอย่างที่เก็บไม่ครบทุกวัน (ราว 15 วันต่อเดือน) ค่าเฉลี่ย ค่าสูงสุด และจำนวนวันที่เกินมาตรฐานคำนวณจากวันที่มีตัวอย่างเท่านั้น จึงไม่ใช่จำนวนวันจริงทั้งเดือน"
  }
 ],
 "groups": [
  {
   "id": "g8",
   "label": "8 จังหวัด",
   "provinces": [
    "เชียงใหม่",
    "เชียงราย",
    "ลำปาง",
    "ลำพูน",
    "แม่ฮ่องสอน",
    "น่าน",
    "พะเยา",
    "แพร่"
   ],
   "color": "#222222"
  },
  {
   "id": "g9",
   "label": "9 จังหวัด",
   "provinces": [
    "เชียงใหม่",
    "เชียงราย",
    "ลำปาง",
    "ลำพูน",
    "แม่ฮ่องสอน",
    "น่าน",
    "พะเยา",
    "แพร่",
    "ตาก"
   ],
   "color": "#B2182B"
  }
 ],
 "stations": [
  {
   "code": "36t",
   "set": "k11",
   "location": "ต. ศรีภูมิ อ. เมือง",
   "province": "เชียงใหม่",
   "lat": 18.791,
   "lon": 98.988
  },
  {
   "code": "57t",
   "set": "k11",
   "location": "ต. เวียง อ. เมือง",
   "province": "เชียงราย",
   "lat": 19.912,
   "lon": 99.832
  },
  {
   "code": "73t",
   "set": "k11",
   "location": "ต. เวียงพางคำ อ. แม่สาย",
   "province": "เชียงราย",
   "lat": 20.427,
   "lon": 99.883
  },
  {
   "code": "37t",
   "set": "k11",
   "location": "ต. พระบาท อ. เมือง",
   "province": "ลำปาง",
   "lat": 18.278,
   "lon": 99.507
  },
  {
   "code": "68t",
   "set": "k11",
   "location": "ต. บ้านกลาง อ. เมือง",
   "province": "ลำพูน",
   "lat": 18.059,
   "lon": 99.057
  },
  {
   "code": "58t",
   "set": "k11",
   "location": "ต. จองคำ อ. เมือง",
   "province": "แม่ฮ่องสอน",
   "lat": 19.284,
   "lon": 97.967
  },
  {
   "code": "67t",
   "set": "k11",
   "location": "ต. ในเวียง อ. เมือง",
   "province": "น่าน",
   "lat": 18.782,
   "lon": 100.786
  },
  {
   "code": "75t",
   "set": "k11",
   "location": "ต. ห้วยโก๋น อ. เฉลิมพระเกียรติ",
   "province": "น่าน",
   "lat": 19.575,
   "lon": 101.082
  },
  {
   "code": "70t",
   "set": "k11",
   "location": "ต. บ้านต๋อม อ. เมือง",
   "province": "พะเยา",
   "lat": 19.154,
   "lon": 99.873
  },
  {
   "code": "69t",
   "set": "k11",
   "location": "ต. นาจักร อ. เมือง",
   "province": "แพร่",
   "lat": 18.118,
   "lon": 100.162
  },
  {
   "code": "76t",
   "set": "k11",
   "location": "ต. แม่ปะ อ. แม่สอด",
   "province": "ตาก",
   "lat": 16.74,
   "lon": 98.605
  },
  {
   "code": "CM",
   "set": "s3",
   "location": "อ.เมืองเชียงใหม่",
   "province": "เชียงใหม่",
   "lat": 18.80173,
   "lon": 98.953406
  },
  {
   "code": "LP",
   "set": "s3",
   "location": "อ.เมืองลำพูน",
   "province": "ลำพูน",
   "lat": 18.58892,
   "lon": 99.03947
  },
  {
   "code": "LI",
   "set": "s3",
   "location": "อ.ลี้",
   "province": "ลำพูน",
   "lat": 17.80283,
   "lon": 98.95053
  }
 ],
 "roni": {
  "2012": {
   "smoke": {
    "v": -0.45,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": 0.325,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "ann": {
    "v": -0.17,
    "type": "Neutral",
    "cat": "Neutral"
   }
  },
  "2013": {
   "smoke": {
    "v": -0.5,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": -0.375,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "ann": {
    "v": -0.22,
    "type": "Neutral",
    "cat": "Neutral"
   }
  },
  "2014": {
   "smoke": {
    "v": -0.05,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": 0.075,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "ann": {
    "v": 0.47,
    "type": "Weak El Nino",
    "cat": "El Nino"
   }
  },
  "2015": {
   "smoke": {
    "v": 0.675,
    "type": "Weak El Nino",
    "cat": "El Nino"
   },
   "non": {
    "v": 1.65,
    "type": "Strong El Nino",
    "cat": "El Nino"
   },
   "ann": {
    "v": 1.39,
    "type": "Very Strong El Nino",
    "cat": "El Nino"
   }
  },
  "2016": {
   "smoke": {
    "v": 0.975,
    "type": "Moderate El Nino",
    "cat": "El Nino"
   },
   "non": {
    "v": -0.85,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -0.55,
    "type": "Weak La Nina",
    "cat": "La Nina"
   }
  },
  "2017": {
   "smoke": {
    "v": -0.175,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": -0.525,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -0.68,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   }
  },
  "2018": {
   "smoke": {
    "v": -0.725,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "non": {
    "v": 0.325,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "ann": {
    "v": 0.49,
    "type": "Weak El Nino",
    "cat": "El Nino"
   }
  },
  "2019": {
   "smoke": {
    "v": 0.525,
    "type": "Weak El Nino",
    "cat": "El Nino"
   },
   "non": {
    "v": 0.025,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "ann": {
    "v": -0.06,
    "type": "Neutral",
    "cat": "Neutral"
   }
  },
  "2020": {
   "smoke": {
    "v": -0.175,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": -1.05,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -1.08,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   }
  },
  "2021": {
   "smoke": {
    "v": -0.975,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   },
   "non": {
    "v": -0.85,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -1.06,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   }
  },
  "2022": {
   "smoke": {
    "v": -1.2,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   },
   "non": {
    "v": -1,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -0.68,
    "type": "Moderate La Nina",
    "cat": "La Nina"
   }
  },
  "2023": {
   "smoke": {
    "v": -0.375,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": 0.9,
    "type": "Weak El Nino",
    "cat": "El Nino"
   },
   "ann": {
    "v": 0.67,
    "type": "Moderate El Nino",
    "cat": "El Nino"
   }
  },
  "2024": {
   "smoke": {
    "v": 0.225,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": -0.65,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -0.71,
    "type": "Weak La Nina",
    "cat": "La Nina"
   }
  },
  "2025": {
   "smoke": {
    "v": -0.625,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "non": {
    "v": -0.675,
    "type": "Weak La Nina",
    "cat": "La Nina"
   },
   "ann": {
    "v": -0.44,
    "type": "Weak La Nina",
    "cat": "La Nina"
   }
  },
  "2026": {
   "smoke": {
    "v": -0.175,
    "type": "Neutral",
    "cat": "Neutral"
   },
   "non": {
    "v": 1.4,
    "type": "Strong El Nino",
    "cat": "El Nino"
   },
   "ann": {
    "v": 1.55,
    "type": "Strong El Nino",
    "cat": "El Nino"
   }
  }
 }
};
