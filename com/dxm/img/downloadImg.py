import json

import requests

import requests
from bs4 import BeautifulSoup

urlSet= set()

def downImg(url):
    if url  not in urlSet:
        resp = requests.get(url=url)
        with open(r'D:\imgs\tokopedia\{}'.format(url.split("/")[-1]), mode='wb') as f:
            f.write(resp.content)
        urlSet.add(url)
    else:
        print("{}已经被下载过了,跳过".format(url))


url = 'https://test.bigseller.com/listing/tokopedia/index.htm?bsStatus=1'
headers = {
    'Cookie': '_ga=GA1.2.783650283.1599030915; _ati=2883770674564; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; rememberMe=JQzzMwtoqa8qpGA51ym7QflSEvi0a3HlW2IwMQWOrivJTzM0pWg2O462qGZurvwfwYsi0fe9vA1D1NIXcSb2/T1+qSAmd4CWjuOhMDZs0cSjqO3nBGw2GHW9nv7KiH/nb/lPGDdk1RmscxAz4xatBtsPDfQTWSsS7QYA5BqXDFUmcXwXLljxBhjWXAymKkacOO92qgIs9DyZkiIkMnHf98aZ9v4qiJnRO4GpcgUEfIpMercxuHBjep1v+6r303rV5Oz0MMZLcUuHL0PI3t2NRSeLXZ4jwQosDTkaT+8QIrKmzFa+N2PSzlPDam1Az333+bEORxXtE6bh3FrcHr0D1VLJ/78VHgfuJVMBoi6lhxFVwx9WKnmfJjJTgLUTglQ1X2KZeT/c+oTosk+qaDnqyQ+7Cp6mQLVyejKFpbsb3xiamYPwH9eBjvS+BIG/nzWdkbyGhzTo0PDApmJvsHN23YzQSOcdAvlxL1QUTK3Bpr/6Zkx2Gv+94IYyJpX5wVoLntOMjvdKPDGJgdgIj+WeywAJAhqpEhIfcskBK/s6EEHiZGAU91t2Z8+yeQcHv9is; _gid=GA1.2.244480512.1602597261; SHAREJSESSIONID=22029ce8-0a50-4b6d-9ba5-e2edfc6428cf; _gat_gtag_UA_144755561_1=1'
}
resp = requests.get(url=url, headers=headers)

soup = BeautifulSoup(resp.text, "html.parser")

for item in soup.select(".list_items"):
    productId = item.find("tr")["data-id"]
    resp = requests.get(url='https://test.bigseller.com/listing/tokopedia/edit/{}.htm'.format(productId), headers=headers)
    shopInfo = BeautifulSoup(resp.text, "html.parser").find(id='shopInfo')
    '''
    varInfos = shopInfo['data-variationsstr']
    infos = json.loads(varInfos)
    for info in infos:
        imgList = info['imageList']
        if imgList is not None:
            for img in imgList:
                try:
                    downImg(img)
                    print("下载图片======================>{}成功,pid={}".format(img, productId))
                except:
                    print("下载图片======================>{}失败,pid={}".format(img, productId))
    '''
    #print(shopInfo)

    imgs = shopInfo['data-image'].split(",")
    for img in imgs:
        try:
            downImg(img)
            print("下载图片======================>{}成功,pid={}".format(img, productId))
        except:
            print("下载图片======================>{}失败,pid={}".format(img, productId))



def renameFile():
    import os
    dir = r"D:\imgs\tokopedia"
    fs = os.listdir(dir)
    for f in fs:
        flag = f.endswith(".jpg")
        if not flag:
            os.rename('{}/{}'.format(dir, f), '{}/{}.png'.format(dir, f))