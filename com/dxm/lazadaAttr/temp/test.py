import datetime
import json
import time

import redis
from numpy import long

import requests
from redis import StrictRedis

url = 'http://localhost:19080/listing/sendo/editBatchPublish.json'
data = [{"id": 1377, "shopId": 898, "name": "Masker Anak Karakter Lucu/Premium 2 Ply-BELI 4 GRATIS 1-Kain Non Medis",
         "itemSku": "MASKER-ANAK-MOTIF",
         "images": "https://media3.scdn.vn/img4/2020/10_22/e77JeJ2wlszYJKxG4SAy.jpg,https://media3.scdn.vn/img4/2020/10_22/aC4wBjkK0TzSmw9hM0m1.jpg,https://media3.scdn.vn/img4/2020/10_22/B5PXvexyqLSRFsalU4EW.jpg,https://media3.scdn.vn/img4/2020/10_22/ZHbznLs5cNqrC6JRWUL7.jpg,https://media3.scdn.vn/img4/2020/10_22/Hget1jXXJTrSNTgluzD0.jpg",
         "stock": None, "saleEndDate": None, "saleStartDate": None, "salePrice": None, "price": None, "weight": 15,
         "length": "33", "width": "33", "height": "33", "unitId": 3, "productType": 1, "variationEditVos": [
        {"id": 10837, "variationSku": "MASKER-ANAK-MOTIF-As picture show", "price": 22415, "stock": 15,
         "salePrice": 22222, "saleStartDate": "2020-10-20", "saleEndDate": "2020-11-29"}]}]

headers={
   "Content-Type": "application/json",
   "Cookie": "_ga=GA1.1.1819001414.1599449838; _ati=263102032090; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; rememberMe_BG=J8WC40BMekr0lvaOcLYzt7LIiUGGTKhV2y32oGZzE+CjLKQszW60dcslqw23VA8+ZqYfVgnTYM0mrqInQIvqDnhWN6pUHn6lJcQcIoor9tT40Cwyq4PikcYWP2tG5AeRhbrGpwWHipt05AFlQ9Q1/oBhS4tlyEZjawpna3GjpLa8BDtB69oIDG9Mez4MuJkBLcPegWsR5FUZftE7AikT+XcL56AQns4+O0wAMhe8XTUo38K95TJhye2PEwlVRyRCoOQaovY6V6dEUZajkFZcMETIn+i4Fq57BzmSKvEXgKpOHQAJ9HjPxPLmE38o0UU8YvHoJkDZijvDDjrbE7CHVzR8DCAd3ynUzKOBBMaJ0z44LrzUgY6b/YUZRmp/IoRD+xRvbh8dorQc5baPikjk3Ae0Li+p1cAwPN89VLLPbbY9IhiT8bIHGVLvoT4b5+8u5RlOT6q5SkYgkfx7y6Ud14yOhhNavUMgQtkhxvrGQtvDjoAfxKi+AOgT1D4slnbOkWUKiMLn2dzSboO+q1HvZeZ4ufqIVRrKDH/+VNzAJ5pqX2vXpMz0iYkUmY6rRSC0; _gid=GA1.1.268081325.1603092538; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1602811889,1602831451,1603069049,1603179672; rememberMe=iPUv7LJ63Kl6XmFEjRMVAaaGGiay9kZ4L7m/g1k79N8y+ErmguL/xIojNkmz4D4btvTcgYVH7KBq4iWyRSuUXCLYOiYShc2R632eIS4mDB68IfdXieMmmaXuLIMeOvHjPoVxP4pwIu9d0VQHwa69DBKjZsUfg+VkAsR+rsz4wIsE285+bR1/9DgBoF2XhhgJbZ31+dyI36G6w686JCAuw0X/t3MMBrk2hkDVRHEQO45ISj1lYo9bu+HRMqQdvAx9Sbw+/SvCo+PWJzt8gdi+/qyP6C8i9COBuclnQIk7JMWlvNaR5fKJpqx/SiOPXu0FOLUOJLu02oQcn5222LEesjS9Hn+gmMFkmojwWHIBms7Nvc4A+j90e5DEw4eqAiDKadgYaxUIPmsb2TKGkPR3TpxCvOYl87x8vNr/4VPxF+aDU2GR47rg8rO8o+QDhWb+fqfwJoCLST7wo0LqoGJ08byoURvPyPbEg+VHE22EvAOss0FbrKMjLC6dTYjsuqwFBvA741oV5O2jyuXoTGpMcqPGkdmpX/KnDenVf9/0OUwmj5f1K1WlUrg0VUFUGs/5; JSESSIONID=9739AF5B644FF170337055E686FE8650; SHAREJSESSIONID=10adf284-4fe8-49ab-875a-db6192f0729f"
}
resp = requests.post(url=url,data=json.dumps(data),headers=headers)

print(resp.status_code)
result = resp.json()
print(result)
if result['code']==0:
    redis = StrictRedis(host='192.168.1.201', port=8531,  password='dxm!123@321#')
    key = result['data']
    while True:
        time.sleep(0.5)
        redisData = redis.get(key)
        print(redisData)
        redisDataJson = json.loads(redisData,encoding='utf-8')
        if redisDataJson['code']==1:
            break
