import json

import requests


data=[
  {
    "id": 1174,
    "shopId": 843,
    "name": "TOKOPEDIA-3A",
    "itemSku": "charlie-sku-10000",
    "images": "https://ecs7.tokopedia.net/img/cache/700/product-1/2020/9/16/4734339/4734339_de94cc69-e2e8-43bb-a90d-ce6bc39b7fb3.jpg,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/9/16/4734339/4734339_e06e73c7-edc0-44f2-8a91-0c0379fb3337.jpg,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/9/16/4734339/4734339_f4f2978f-7434-481a-88a6-e72df12a6adf.jpg,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/9/16/4734339/4734339_1014fc84-e69c-4315-94c9-37e82480baa8.jpg,https://ecs7.tokopedia.net/img/cache/700/product-1/2020/9/16/4734339/4734339_782b95d0-6d59-4063-b02d-76a8b3556cd2.jpg",
    "price": 115819,
    "salePrice": "22235",
    "saleStartDate": "2020-10-16 00:00:00",
    "saleEndDate":  "2020-10-27 23:59:00",
    "stock": 999983,
    "weight": 100,
    "length": "12",
    "width": "22",
    "height": "22",
    "unitId": 1,
    "productType": 1,
    "variationEditVos": None
  }
]
requests.post('http://localhost:8080/listing/sendo/editBatchSave.json',data=json.dumps(data),headers={
    'Content-Type': 'application/json;charset=UTF-8',
    'Cookie': '_ga=GA1.1.1819001414.1599449838; _ati=263102032090; rememberMe=61rZilsKKlxLI9RI4Psz/36l0aLbGzPxxzJpknLKCQKPP8Z8iVd2j5Zk2aUC5tO9E9vs+uNhwtPN+D/v64vtnqevxtO8vpxNZE/An2BR3pIIdgtRbEBaHhSCw7842Mc8AJZIxLsJXTViukE6PP31Lmb3/13topojhRNuxaERThz+Vg1jTKFaDm6Ork0w12hD5aED46Dw94yek1SL5K5z2Qe2vveYl3Th/H41qilDeW8bcvOO5RaHOu2GoMRu6QPDPi/ePvhFoREr8QZ4CEluKE4zZ7EUlzvugSDs19IwM+jbvG41UGr18FT1T+nDevA8xN0NCqKpoSKPsP3XpnUwD82Y3CZIqQf7+1t977lOm4dSxsi/pnROSpKMG4h5/CBdG39hwyI4oGRE65fJysENgz/DJArJDdV6NHl2kp1DdY5reL6N/siV+LIoG9LpcnJqhDlVqyJgBkmIyomKtTXRhY9wMu9ahjTnOGZBGH86fOvG740scRy+f/Viwq/qvyRe9Mq0wRjTHzmaaNvLepDaSyesvPm5JOmfm7TS3gJ8BdVMoimQtp8w0ZsQ76JndOYa; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; rememberMe_BG=J8WC40BMekr0lvaOcLYzt7LIiUGGTKhV2y32oGZzE+CjLKQszW60dcslqw23VA8+ZqYfVgnTYM0mrqInQIvqDnhWN6pUHn6lJcQcIoor9tT40Cwyq4PikcYWP2tG5AeRhbrGpwWHipt05AFlQ9Q1/oBhS4tlyEZjawpna3GjpLa8BDtB69oIDG9Mez4MuJkBLcPegWsR5FUZftE7AikT+XcL56AQns4+O0wAMhe8XTUo38K95TJhye2PEwlVRyRCoOQaovY6V6dEUZajkFZcMETIn+i4Fq57BzmSKvEXgKpOHQAJ9HjPxPLmE38o0UU8YvHoJkDZijvDDjrbE7CHVzR8DCAd3ynUzKOBBMaJ0z44LrzUgY6b/YUZRmp/IoRD+xRvbh8dorQc5baPikjk3Ae0Li+p1cAwPN89VLLPbbY9IhiT8bIHGVLvoT4b5+8u5RlOT6q5SkYgkfx7y6Ud14yOhhNavUMgQtkhxvrGQtvDjoAfxKi+AOgT1D4slnbOkWUKiMLn2dzSboO+q1HvZeZ4ufqIVRrKDH/+VNzAJ5pqX2vXpMz0iYkUmY6rRSC0; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1602766145,1602811889,1602831451,1603069049; SHAREJSESSIONID_BG=36aa748f-a888-4f64-acff-83383f27ec98; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1603090138; _gid=GA1.1.268081325.1603092538; SHAREJSESSIONID=242bd4a5-e66d-4daa-8c56-841ff3829eaa; JSESSIONID=5CBD5E77064412A7954A93D7FBB66517'
})