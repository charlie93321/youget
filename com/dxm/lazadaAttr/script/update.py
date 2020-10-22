import json

import requests

headers = {
    "Authorization": "bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJTdG9yZUlkIjoiODA4NTE2IiwiVXNlck5hbWUiOiIiLCJTdG9yZVN0YXR1cyI6IjIiLCJTaG9wVHlwZSI6IjEiLCJTdG9yZUxldmVsIjoiOTkiLCJleHAiOjE2MDMzNTg4MjIsImlzcyI6IjgwODUxNiIsImF1ZCI6IjgwODUxNiJ9.4iEc5lseSjPg-chMfiDCBHOeaVgZHGaNR8p6IVgG2g0"
    , "Content-Type": "application/json"
}
url='https://open.sendo.vn/api/partner/product'

data='''{
  "id": 35858106,
  "name": "LOA BLUETOOTH G01 CHARGE MINI 3+- PIN  6000MAH -PIN CH1edc 72H- H1ed4 TR1ee2 M00c0NG L1eccC CH1ed0NG N01af1edaC -GI00c1 D00d9NG TH1eec CHO 01101ee2T QU00c3NG B00c1 TH01af01a0NG HI1ec6U G01",
  "sku": "find-date",
  "price": 124200.0,
  "weight": 33.0,
  "stock_availability": true,
  "stock_quantity": 1285,
  "description": "<p style=\"margin:0;display: block;width: 100%;\"><img src=\"//media3.scdn.vn/img4/2020/10_21/MChgbPoSHdYDa1TXTkMO.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/FUs3ePH31v4jgSSUub7I.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/yLSqvW54FsMY3hV6Hizu.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/kEjCWb5DTGpbeCKAhEJd.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/eyvWaA08Pk1Z89AbYXga.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/xP4FwhLmLew8hPrCrxlK.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/KNRk5bqQU0rKOcAz1JBD.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/9arH1xES3zE11xvv3iDH.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/0PEuvjPYHTwClAgNeXu6.jpg\"><img src=\"//media3.scdn.vn/img4/2020/10_21/aLH0f30FUw7WRFY69b77.jpg\"></p>",
  "cat_4_id": 609,
  "status": 2,
  "tags": null,
  "updated_date_timestamp": 1603274500.0,
  "created_date_timestamp": 1603273013.0,
  "seo": "{\"score\":\"0\",\"seo_description\":\"\",\"seo_keyword\":\"\",\"seo_title\":\"\"}",
  "link": "https://www.sendo.vn/loa-bluetooth-g01-charge-mini-3-pin-6000mah-pin-cho-72h-ho-tro-mang-loc-chong-nuoc-gia-dung-thu-cho-dot-quang-ba-thuong-hieu-g01-35858106.html",
  "relateds": [],
  "seo_keyword": null,
  "seo_title": null,
  "seo_description": null,
  "seo_score": 0,
  "image": "https://media3.scdn.vn/img4/2020/10_21/E8hTflM9iSUoydsK1vx8.jpg",
  "category_4_name": "01101ed3ng h1ed3 treo t01b01eddng",
  "promotion_price": 120000.0,
  "brand_id": 0,
  "brand_name": null,
  "updated_user": "2035780304",
  "url_path": "khong-gian-song/trang-tri-tuong/dong-ho",
  "video_links": null,
  "height": 22.0,
  "length": 22.0,
  "width": 22.0,
  "unit_id": 2,
  "avatar": {
    "picture_url": "https://media3.scdn.vn/img4/2020/10_21/E8hTflM9iSUoydsK1vx8.jpg"
  },
  "pictures": [
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/E8hTflM9iSUoydsK1vx8.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/vHrWhUXhwg0CRmc2sN9O.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/gTrwFr9rKxb9XVF2yQE3.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/M9E0ZZRAq2VsYnAOfPcO.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/YHmvH2MIljfal8eU7lHZ.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/ppbaYBjwP1WX89sIpBCD.jpg"
    },
    {
      "picture_url": "https://media3.scdn.vn/img4/2020/10_21/bIl2TMe4OK78s9L9PwcS.jpg"
    }
  ]
  "attributes": [
    {
      "attribute_id": 753,
      "attribute_type": 3,
      "attribute_name": "Ch1ea5t li1ec7u",
      "attribute_is_required": false,
      "attribute_code": "chat_lieu_kgs",
      "attribute_is_custom": false,
      "attribute_is_checkout": false,
      "attribute_is_image": false,
      "attribute_values": [
        {
          "id": 14160,
          "value": "Gi1ea5y",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14161,
          "value": "Nh1ef1a t1ed5ng h1ee3p",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14162,
          "value": "N1ebfn",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14163,
          "value": "V1ea3i, v1ea3i n1ec9, v1ea3i d1ea1",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14164,
          "value": "Th1ee7y tinh",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14165,
          "value": "G1ed1m, s1ee9",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14166,
          "value": "01101ea5t s00e9t",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14167,
          "value": "Kim lo1ea1i",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14168,
          "value": "D1ea7u th1ef1c v1eadt",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14169,
          "value": "Simili",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14170,
          "value": "Len",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14171,
          "value": "Ch1ec9 th00eau",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14172,
          "value": "G1ed7 nh00e2n t1ea1o",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14173,
          "value": "G1ed7",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14174,
          "value": "V1ecf c00e2y",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14175,
          "value": "Decal",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14176,
          "value": "S00e1p(n1ebfn)",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14177,
          "value": "Tinh d1ea7u t1ed5ng h1ee3p",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14178,
          "value": "Mica",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14179,
          "value": "H1ea1t g1ea1o",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14180,
          "value": "C00e1t",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14181,
          "value": "V1ecf s00f2 - 1ed1c bi1ec3n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14182,
          "value": "Phale",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14183,
          "value": "011000e1 qu00fd",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14184,
          "value": "Hoa kh00f4",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14185,
          "value": "0110ang c1eadp nh1eadt",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14186,
          "value": "011000e1 trang tr00ed",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14187,
          "value": "S1eebng",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14188,
          "value": "L00e1 c00e2y",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14233,
          "value": "G1ed7 MDF",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14235,
          "value": "Th1ea1ch cao",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14300,
          "value": "Nhung",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 14301,
          "value": "Nh1ef1a PVC",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        }
      ]
    },
    {
      "attribute_id": 754,
      "attribute_type": 3,
      "attribute_name": "K00edch th01b01edbc",
      "attribute_is_required": false,
      "attribute_code": "kichthuoc_kgs",
      "attribute_is_custom": false,
      "attribute_is_checkout": false,
      "attribute_is_image": false,
      "attribute_values": [
        {
          "id": 0,
          "value": null,
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        }
      ]
    },
    {
      "attribute_id": 284,
      "attribute_type": 1,
      "attribute_name": "M00e0u s1eafc",
      "attribute_is_required": true,
      "attribute_code": "mau_sac",
      "attribute_is_custom": false,
      "attribute_is_checkout": true,
      "attribute_is_image": true,
      "attribute_values": [
        {
          "id": 602,
          "value": "N00e2u",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 603,
          "value": "V00e0ng",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 604,
          "value": "Tr1eafng",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 605,
          "value": "0110en",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 606,
          "value": "H1ed3ng",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 607,
          "value": "Xanh l00e1",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 608,
          "value": "Xanh n01b01edbc bi1ec3n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 609,
          "value": "Xanh ng1ecdc",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 610,
          "value": "Xanh 0111en",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 613,
          "value": "X00e1m",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 614,
          "value": "T00edm",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 628,
          "value": "01101ecf",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 629,
          "value": "Cam",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 631,
          "value": "Kem",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1495,
          "value": "Xanh r00eau",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1497,
          "value": "H1ecda ti1ebft",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1476,
          "value": "Kh00e1c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1577,
          "value": "B1ea1c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 15439,
          "value": "H1ed3ng ph1ea5n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 22750405,
          "value": "M00e0u 01111ecf",
          "attribute_img": null,
          "is_selected": true,
          "is_custom": true
        },
        {
          "id": 22750406,
          "value": "M00e0u 0111en",
          "attribute_img": null,
          "is_selected": true,
          "is_custom": true
        },
        {
          "id": 22750407,
          "value": "Blue",
          "attribute_img": null,
          "is_selected": true,
          "is_custom": true
        },
        {
          "id": 22750404,
          "value": "M00e0u xanh ng1ecdc",
          "attribute_img": null,
          "is_selected": true,
          "is_custom": true
        }
      ]
    },
    {
      "attribute_id": 333,
      "attribute_type": 3,
      "attribute_name": "Xu1ea5t x1ee9",
      "attribute_is_required": false,
      "attribute_code": "xuat_xu",
      "attribute_is_custom": false,
      "attribute_is_checkout": false,
      "attribute_is_image": false,
      "attribute_values": [
        {
          "id": 1418,
          "value": "M1ef9",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1419,
          "value": "Nh1eadt B1ea3n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1420,
          "value": "Ph00e1p",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1421,
          "value": "01101ee9c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1422,
          "value": "Anh",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1424,
          "value": "Th00e1i Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1426,
          "value": "Vi1ec7t Nam",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1429,
          "value": "Canada",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1431,
          "value": "Ha0300 Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1433,
          "value": "Indonesia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1439,
          "value": "Nga",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1435,
          "value": "Malaysia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1445,
          "value": "00dd",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1436,
          "value": "Mexico",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1438,
          "value": "New Zealand",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1434,
          "value": "Madagascar",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1417,
          "value": "H00e0n Qu1ed1c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1443,
          "value": "Trung Qu1ed1c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1446,
          "value": "011000e0i Loan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1444,
          "value": "00dac",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1440,
          "value": "Singapore",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 1441,
          "value": "T00e2y Ban Nha",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 19996,
          "value": "0110an M1ea1ch",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23638,
          "value": "Ba Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23771,
          "value": "Pakistan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23827,
          "value": "Brazil",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23850,
          "value": "Afghanistan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23852,
          "value": "Algeria",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23854,
          "value": "Andorra",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23856,
          "value": "Antigua and Barbuda",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23858,
          "value": "Armenia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23860,
          "value": "Azerbaijan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23862,
          "value": "Barbados",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23866,
          "value": "Benin",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23868,
          "value": "Bolivia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23870,
          "value": "Botswana",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23872,
          "value": "Bulgaria",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23874,
          "value": "Burundi",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23876,
          "value": "Cameroon",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23878,
          "value": "Central African Republic",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23880,
          "value": "Chile",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23882,
          "value": "Colombia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23884,
          "value": "Costa Rica",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23886,
          "value": "Croatia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23888,
          "value": "Cyprus",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23890,
          "value": "Democratic Republic of the Congo",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23892,
          "value": "Djibouti",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23894,
          "value": "Dominican Republic",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23896,
          "value": "Ecuador",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23898,
          "value": "El Salvador",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23900,
          "value": "Eritrea",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23902,
          "value": "Ethiopia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23906,
          "value": "Gabon",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23912,
          "value": "Guatemala",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23914,
          "value": "Guinea-Bissau",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23916,
          "value": "Haiti",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23918,
          "value": "Hungary",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23922,
          "value": "Iraq",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23924,
          "value": "Israel",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23926,
          "value": "Jamaica",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23928,
          "value": "Jordan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23930,
          "value": "Kenya",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23934,
          "value": "Kyrgyzstan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23936,
          "value": "Latvia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23938,
          "value": "Lesotho",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23940,
          "value": "Libya",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23942,
          "value": "Macedonia (FYROM)",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23944,
          "value": "Maldives",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23946,
          "value": "Malta",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23948,
          "value": "Mauritania",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23950,
          "value": "Micronesia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23952,
          "value": "Monaco",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23954,
          "value": "Montenegro",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23956,
          "value": "Mozambique",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23958,
          "value": "Namibia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23960,
          "value": "Nepal",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23962,
          "value": "Niger",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23968,
          "value": "Palau",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23970,
          "value": "Panama",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23972,
          "value": "Paraguay",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23974,
          "value": "Peru",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23978,
          "value": "Qatar",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23980,
          "value": "Republic of the Congo",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23984,
          "value": "Rwanda",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23986,
          "value": "Saint Vincent and the Grenadines",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23988,
          "value": "San Marino",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23990,
          "value": "Saudi Arabia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23992,
          "value": "Senegal",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23994,
          "value": "Seychelles",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23996,
          "value": "Slovakia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23998,
          "value": "Solomon Islands",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24000,
          "value": "Somaliland",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24006,
          "value": "Sudan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24008,
          "value": "Swaziland",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24014,
          "value": "Tanzania",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24016,
          "value": "The Bahamas",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24020,
          "value": "Tonga",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24022,
          "value": "Trinidad and Tobago",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24026,
          "value": "Tuvalu",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24028,
          "value": "Ukraine",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24032,
          "value": "Uruguay",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24034,
          "value": "Vanuatu",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24036,
          "value": "Venezuela",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24038,
          "value": "Wales",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24040,
          "value": "Yemen",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24042,
          "value": "Zimbabwe",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24044,
          "value": "KUNKUN",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25684,
          "value": "00dac",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25686,
          "value": "B1ec9",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25688,
          "value": "C1ed9ng h00f2a S00e9c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25690,
          "value": "Ai C1eadp",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25692,
          "value": "Ph00e1p",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25694,
          "value": "Hy L1ea1p",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25696,
          "value": "00dd",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25700,
          "value": "Tri1ec1u Ti00ean",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25702,
          "value": "Ba Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25708,
          "value": "Th1ee5y s0129",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25712,
          "value": "Th1ed5 Nh0129 K1ef3",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23929,
          "value": "Kazakhstan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23931,
          "value": "Kiribati",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23857,
          "value": "Argentina",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23933,
          "value": "Kuwait",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23937,
          "value": "Lebanon",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23939,
          "value": "Liberia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23861,
          "value": "Bahrain",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23941,
          "value": "Luxembourg",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23943,
          "value": "Malawi",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23863,
          "value": "Belarus",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23945,
          "value": "Mali",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23947,
          "value": "Marshall Islands",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23865,
          "value": "Belize",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23949,
          "value": "Mauritius",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23951,
          "value": "Moldova",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23867,
          "value": "Bhutan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23953,
          "value": "Mongolia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23955,
          "value": "Morocco",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23869,
          "value": "Bosnia and Herzegovina",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23957,
          "value": "Nagorno-Karabakh",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23959,
          "value": "Nauru",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23871,
          "value": "Brunei",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23961,
          "value": "Nicaragua",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23963,
          "value": "Nigeria",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23873,
          "value": "Burkina Faso",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23965,
          "value": "Northern Cyprus",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23967,
          "value": "Oman",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23875,
          "value": "Cambodia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23969,
          "value": "Palestine",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 19251,
          "value": "B1ec9",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23971,
          "value": "Papua New Guinea",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23877,
          "value": "Cape Verde",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23975,
          "value": "Philippines",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23879,
          "value": "Chad",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23981,
          "value": "Romania",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23983,
          "value": "Russian",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23883,
          "value": "Comoros",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23985,
          "value": "Saint Kitts and Nevis",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23987,
          "value": "Samoa",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23885,
          "value": "C00f4te d'Ivoire",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23989,
          "value": "S00e3o Tom00e9 and Pr00edncipe",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23991,
          "value": "Scotland",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23887,
          "value": "Cuba",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23993,
          "value": "Serbia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23995,
          "value": "Sierra Leone",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23997,
          "value": "Slovenia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23999,
          "value": "Somalia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24003,
          "value": "South Ossetia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23893,
          "value": "Dominica",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24005,
          "value": "Sri Lanka",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24007,
          "value": "Suriname",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23895,
          "value": "East Timor",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24011,
          "value": "Syria",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24013,
          "value": "Tajikistan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23899,
          "value": "Equatorial Guinea",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24017,
          "value": "The Gambia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 19991,
          "value": "Myanmar",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24019,
          "value": "Togo",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23901,
          "value": "Estonia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24021,
          "value": "Transnistria",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24023,
          "value": "Tunisia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23903,
          "value": "Fiji",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24025,
          "value": "Turkmenistan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23354,
          "value": "Bangladesh",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24027,
          "value": "Uganda",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24029,
          "value": "United Arab Emirates",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23907,
          "value": "Georgia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24033,
          "value": "Uzbekistan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23758,
          "value": "Th1ee5y 0110i1ec3n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24035,
          "value": "Vatican City",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23909,
          "value": "Ghana",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24039,
          "value": "Western Sahara",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23911,
          "value": "Grenada",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24041,
          "value": "Zambia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23814,
          "value": "Th1ed5 Nh0129 K1ef3",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 24043,
          "value": "HongKong",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23913,
          "value": "Guinea",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25685,
          "value": "00c1o",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23915,
          "value": "Guyana",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23849,
          "value": "Abkhazia",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25689,
          "value": "0110an M1ea1ch",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23917,
          "value": "Honduras",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25691,
          "value": "Ph1ea7n Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25693,
          "value": "01101ee9c",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23919,
          "value": "Iceland",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25695,
          "value": "4n 9",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23851,
          "value": "Albania",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25697,
          "value": "Nht Bu1e3n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23921,
          "value": "Iran",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25699,
          "value": "L o",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25701,
          "value": "Na Uy",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23923,
          "value": "Ireland",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25703,
          "value": "B\     \ o Nha",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25705,
          "value": "Nam Phi",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25707,
          "value": "Th y  i n",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25711,
          "value": "H  Lan",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 23855,
          "value": "Angola",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25713,
          "value": "Anh",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 25715,
          "value": "Vi t Nam",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        },
        {
          "id": 26425,
          "value": "C ng h a Litva",
          "attribute_img": null,
          "is_selected": false,
          "is_custom": false
        }
      ]
    }
  ],
  "special_price": 120000.0,
  "promotion_from_date_timestamp": null,
  "promotion_to_date_timestamp": null,
  "is_promotion": true,
  "extended_shipping_package": {
    "is_using_instant": false,
    "is_using_in_day": false,
    "is_self_shipping": false
  },
  "variants": [
    {
      "variant_attributes": [
        {
          "attribute_id": 284,
          "attribute_code": "mau_sac",
          "option_id": 22750405
        }
      ],
      "variant_is_promotion": 1,
      "variant_sku": "find-date-M u  ",
      "variant_price": 124200.0,
      "variant_special_price": 120000.0,
      "variant_quantity": 257,
      "variant_promotion_start_date_timestamp": 1603213200.0,
      "variant_promotion_end_date_timestamp": 1604077199.0,
      "variant_is_flash_sales": null,
      "variant_campaign_status": null,
      "variant_attribute_hash": "22750405",
      "message": null
    },
    {
      "variant_attributes": [
        {
          "attribute_id": 284,
          "attribute_code": "mau_sac",
          "option_id": 22750406
        }
      ],
      "variant_is_promotion": 1,
      "variant_sku": "find-date-M u  en",
      "variant_price": 129000.0,
      "variant_special_price": 120000.0,
      "variant_quantity": 224,
      "variant_promotion_start_date_timestamp": 1603213200.0,
      "variant_promotion_end_date_timestamp": 1603990799.0,
      "variant_is_flash_sales": null,
      "variant_campaign_status": null,
      "variant_attribute_hash": "22750406",
      "message": null
    },
    {
      "variant_attributes": [
        {
          "attribute_id": 284,
          "attribute_code": "mau_sac",
          "option_id": 22750407
        }
      ],
      "variant_is_promotion": 1,
      "variant_sku": "find-date-Blue",
      "variant_price": 129000.0,
      "variant_special_price": 120000.0,
      "variant_quantity": 418,
      "variant_promotion_start_date_timestamp": 1603213200.0,
      "variant_promotion_end_date_timestamp": 1604077199.0,
      "variant_is_flash_sales": null,
      "variant_campaign_status": null,
      "variant_attribute_hash": "22750407",
      "message": null
    },
    {
      "variant_attributes": [
        {
          "attribute_id": 284,
          "attribute_code": "mau_sac",
          "option_id": 22750404
        }
      ],
      "variant_is_promotion": 1,
      "variant_sku": "find-date-M u xanh ng c",
      "variant_price": 129000.0,
      "variant_special_price": 120000.0,
      "variant_quantity": 386,
      "variant_promotion_start_date_timestamp": 1603213200.0,
      "variant_promotion_end_date_timestamp": 1604077199.0,
      "variant_is_flash_sales": null,
      "variant_campaign_status": null,
      "variant_attribute_hash": "22750404",
      "message": null
    }
  ],
  "is_config_variant": true,
  "is_invalid_variant": false,
  "voucher": {
    "product_type": 1,
    "start_date": null,
    "end_date": null,
    "is_check_date": null
  },
  "product_category_types": [
    1
  ],
  "is_flash_sales": false,
  "campaign_status": null,
  "can_edit": true,
  "sendo_video": []
}
'''

Dữ liệu không phù hợp
resp = requests.post(url=url,headers=headers,json=data.strip())

print(resp.status_code)
print(resp.json())