import json
import os

import requests
import logging


def get_proxy_ip():
    logging.basicConfig(filename=os.path.join(os.getcwd(), 'log.txt', ), level=logging.DEBUG)
    logging.debug('this is a message')

    proxy_list = []

    proxy_req_url = ''
    resp = requests.get(url=proxy_req_url)
    resp = resp.json()
    code = resp['code']
    logging.info("请求到的代理IP的resp-status-code:{}".format(code))
    if code == 200:
        datas = resp['data']
        for data in datas:
            proxy = {
                "http": "http://{}".format(data['key']),
                "https": "https://{}".format(data['key'])
            }
            logging.info("请求到代理IP为:{}".format(json.dumps(proxy)))
            proxy_list.append(proxy)
    else:
        logging.error("请求代理ip失败")
    return proxy_list
