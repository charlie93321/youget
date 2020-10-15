# ！/usr/bin/env python
# -*-coding:utf-8-*-
"""
@Author  : xiaofeng
@Time    : 2018/12/25 10:26
@Desc : Less interests,More interest.
@Project : python_appliction
@FileName: you-get.py
@Software: PyCharm
@Blog    ：https://blog.csdn.net/zwx19921215
"""
import sys
import you_get


def download(url, path):
    sys.argv = ['you-get', '-o', path, url]
    you_get.main()


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV17K4y1h7Li?spm_id_from=333.851.b_7265706f7274466972737431.7'
    # 视频输出的位置
    path = r'F:\bilibili'
    download(url, path)