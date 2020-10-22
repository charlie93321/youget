import cv2 as cv
import numpy as np
def vedio():
    capture = cv.VideoCapture(0)
    while True:
        ret,frame = capture.read()

        cv.imshow("video",frame)
        c = cv.waitKey(50)
        if c==27:
            break


def get_img_info(img):
    print(type(img))
    print(img.shape)
    print(img.size)
    # 每个像素点有3个通道 每个通道的字节数
    print(img.dtype)
    pixel_data = np.array(img)
    print(pixel_data)
src = cv.imread(r'p2529206747.jpg')
cv.namedWindow("input image",cv.WINDOW_AUTOSIZE)
cv.imshow("input image",src)

cv.waitKey(0)

get_img_info(src)

cv.destroyAllWindows()
