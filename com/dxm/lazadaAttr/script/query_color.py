import json
import os

import requests
import xlrd

def read_unknow_color():
    x1 = xlrd.open_workbook('../lazada分类/Color 颜色到处找不到对应的-泰语.xlsx')
    sheet = x1.sheet_by_name('Sheet1')

    rows = sheet.get_rows()
    vals = []
    for row in rows:
        vals.append(row[0].value)
        #if str(row[0].value).strip() != '…':
            #continue
        url = 'https://manage.bigseller.com/translate/lazadaCategory/queryColorCategoryInfo.json?color={}&site={}'
        resp = requests.get(url=url.format('Hotpink', 'VN'), headers={
            'Cookie': '_ga=GA1.2.783650283.1599030915; _ati=2883770674564; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=en_US; rememberMe_BG=WE81PMaUtSZE8WLCjOUxsi490oWF+lWbWlUW6yMqOhvYxHtMC7iiKTGfw+pPDT6EKS4/bNTt6o+Fl+eN4F7T5895Dby9i7fvgcbZjgJUWVLZD0iqXobV4C24IsHjeYfFxqSq8+Pnhw0KCcN1hpi2F3nYCZNgSnXkvQQergUcGZXfQ+Jcu8FtBOiTVjIfurvZ2QnvBo2kfMmzevByMKETQKaUSyS0IGx4B7UMrAirRpRLTa8p6Q6W70YNXMABazfm+dfxVn7F/jCcgp4XX4epoe3LCIscx/Y+jpWGa1URzu2ZTAaISCAH1JtWKdHhdm8FB1Ux+BikKsC3Z+biaNyTgmzuBHXMd4WUnNPyUtYjat5WqYD3OmBsNnL+UmwyzisaJhxx8RonWLyFwJLHrmHza0mhX9XC+P8qH+UtKUqqSpmwqyioDoZs8KXpHOMBxGTmlTj/tFDca65fSpJMxcoPpF7dHOjQecSvfQgLRWeFvzzNhfMNXRqEmteIIuFntRMBW77A+sPhuFRp12jKO2oNnVCdoM6o8hI7rMUoQQC6pX5d9jS7dWCntsv0MavLzAcx; Hm_lvt_d97abf6d61c21d773f97835defbdef4e=1603176631,1603455393,1603522492,1603677175; SHAREJSESSIONID_BG=14063bd7-f69b-4734-908f-15a3cbb178eb; Hm_lpvt_d97abf6d61c21d773f97835defbdef4e=1603694232'
        })
        print('color={}'.format(row[0].value))
        with open('../temp/color/data_{}.json'.format(row[0].value), mode='w', encoding='utf-8') as f:
            datas = resp.json()['data']
            dataList = []
            for data in datas[:10]:
                data['options']=''
                dataList.append(data)
            f.write(json.dumps(dataList, ensure_ascii=False))

    x1.release_resources()


def dd():
    fs = os.listdir('../temp/color')
    for name in fs:
        with open('../temp/color/{}'.format(name), mode='r', encoding='utf-8') as f:
            data = json.loads(f.read(), encoding='utf-8')
            entity = data[0]
            print(entity)

dd()