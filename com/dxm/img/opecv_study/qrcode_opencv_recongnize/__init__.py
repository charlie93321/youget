# -*- coding:utf-8 -*-
import qrcode,time
from PIL import Image
import matplotlib.pyplot as plt


# 方法3  生成带有图标的二维码
def qr_code_3():
    # 实例化QRCode生成qr对象
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=1
    )
    qr.add_data("I am your boss")# 添加数据
    qr.make(fit=True)# 填充数据
    # 生成图片
    # img = qr.make_image()fill_color="lightgreen", back_color="gray"
    img = qr.make_image()
    img = img.convert("RGBA")
    img.save("mycode.png")
