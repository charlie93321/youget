from PIL import Image
def getBitValue(value):
    if value>10:
        return 255
    else:
        return 0

def demo_1():
    img = Image.open('p2529206747.jpg')
    print(img.format,img.size,img.height,img.width)
    for i in range(0,img.width):
        for j in range(0,img.height):
            rgb = img.getpixel((i,j))
            print("{}点所在的像素信息:{}".format((i,j),img.getpixel((i,j))))
            rgb2=(getBitValue(rgb[0]),getBitValue(rgb[1]),getBitValue(rgb[2]))
            img.putpixel((i,j),rgb2)
    img.show()

def demo_混合_透明度():
    img1 =Image.open('test.png').convert("RGB")
    print(img1.size,type(img1.size))
    img2 = Image.new(mode='RGB',size=img1.size,color='green')

    img3 = Image.blend(img1,img2,0.1)
    img3.show()


def demo_混合_遮罩():
    img1 =Image.open('test.png')
    img2 = Image.open('p2529206747.jpg')
    #img1=img1.resize(img2.size)
    r,g,b=img1.split()
    img3 = Image.composite(img1,img2,b)
    #img3.show()
    img3.save("test3.png")

demo_混合_遮罩()