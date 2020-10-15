import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}

# resp = requests.get('https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0&genres=喜剧',headers=headers)
# for moview in resp.json()['data']:
# print(moview)

moview = {'directors': ['闫非', '彭大魔'], 'rate': '6.6', 'cover_x': 679, 'star': '35', 'title': '西虹市首富',
          'url': 'https://movie.douban.com/subject/27605698/', 'casts': ['沈腾', '宋芸桦', '张一鸣', '张晨光', '常远'],
          'cover': 'https://img1.doubanio.com/view/photo/s_ratio_poster/public/p2529206747.jpg', 'id': '27605698',
          'cover_y': 950}
lines = """
{},
{},
{},
{}
""".format(  "片名:{}".format(moview['title']), "评分:{}".format(moview['rate']),
           "导演:{}".format(",".join(moview['directors'])), "主演:{}".format(",".join(moview['casts'])))

import qrcode

img = qrcode.make(lines)
img.save('test.png')

