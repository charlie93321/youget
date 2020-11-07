import json
import traceback
from time import sleep

import requests

from com.dxm.driver_test import proxyutils


def save_cookie(language,email,passwrod,DRIVER_PATH):
    import selenium
    from selenium import webdriver
    options = webdriver.ChromeOptions()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')

    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    try:
        driver.set_window_size(1920, 1080)
        driver.get('https://sellercenter.lazada.vn/product/newpublish/index')
        sleep(2)
        user = driver.find_element_by_name("TPL_username")
        user.clear()
        user.send_keys(email)
        pwd = driver.find_element_by_name("TPL_password")
        pwd.clear()
        pwd.send_keys(passwrod)

        btn = driver.find_element_by_class_name('button-submit').find_element_by_tag_name("button")

        btn.click()
        if language == "en":
            sleep(5)
            btns = driver.find_elements_by_class_name('next-dialog-btn')
            try:
                btns[1].click()
            except Exception as e:
                print('str(e):\t\t', str(e))
                print('repr(e):\t', repr(e))
                # 以下两步都是输出错误的具体位置的
                traceback.print_exc()
            langItems = driver.find_elements_by_class_name('layout-menu')
            for langItem in langItems:
                if langItem.text =='Vietnam':
                    langItem.click()
            sleep(1)
            items = driver.find_elements_by_class_name("layout-menu-item")
            for item in items:
                if item.get_attribute("title") == "English":
                    item.click()
                    break
        sleep(5)
        cookies = driver.get_cookies()
        # time.sleep(5)
        # driver.refresh('http://adnet.qq.com/index')
        if language == "en":
            with open("cookies_en.txt", "w") as fp:
                json.dump(cookies, fp)
        else:
            with open("cookies_vn.txt", "w") as fp:
                json.dump(cookies, fp)
        driver.close()
    except Exception as e2:
        driver.close()
        print('str(e):\t\t', str(e2))
        print('repr(e):\t', repr(e2))
        # 以下两步都是输出错误的具体位置的
        traceback.print_exc()


# 将selenium的cookies放到session中
def readCookies(lang):
    if lang == "en":
        file = 'cookies_en.txt'
    else:
        file = 'cookies_vn.txt'
    with open(file, 'r') as f:
        line = f.readline()
        return json.loads(line)


def query_attr(lang):
    session = requests.Session()
    session.headers.clear()
    for cookie in readCookies(lang=lang):
        session.cookies.set(cookie['name'], cookie['value'])
    url = 'https://sellercenter.lazada.vn/product/newpublish/api.product.post.render.v1?_timezone=-8&__ARMS_PID__=giiryrcz16@65cb05a587d7ea3&userId=200163978075&optType=selectCategory&productId=947090429&catId=4763'

    proxy_list = proxyutils.get_proxy_ip()
    data = session.get(url, proxies=proxy_list[0]).json()
    print(data)
    attrMap = {}
    if data is not None and "data" in data:
        attrs = data["data"]
        for attr in attrs:
            if "label" in attr:
                label = str(attr['label']).strip().replace("\n", "")
                attrMap[attr['name']] = label
                if label == 'Product Attributes' or label == 'Thông Tin Sản Phẩm':
                    pattrs = attr["dataSource"]
                    for pattr in pattrs:
                        attrMap[pattr['name']] = pattr['label']
                elif label == "Variation Information" or label == 'Thông tin biến thể':
                    vattrs = attr["dataSource"]
                    for vattr in vattrs:
                        attrMap[vattr['name']] = vattr['label']
                    vattrMap = attr['attributes']
                    keys = attr['sequence']
                    for key in keys:
                        if key in vattrMap:
                            if 'label' in vattrMap[key]:
                                attrMap[vattrMap[key]['name']] = vattrMap[key]['label']
    return attrMap


# query_attr()

#attrMap = query_attr('en')

#print(json.dumps(attrMap))
