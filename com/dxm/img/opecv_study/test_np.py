import numpy as np
import cv2 as cv


def test_1():
    img: np.ndarray = cv.imread('p2529206747.jpg')

    print(type(img))

    print(img.shape)

    for row in range(0, img.shape[0]):
        for col in range(0, img.shape[1]):
            for channel in range(img.shape[2]):
                pv = img[row, col, channel]
                img[row, col, channel] = pv

    cv.imshow('img-show', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

#BGR
img = np.ones([100,500,3], np.uint8)
img[:,:,0]= 255
print(img)
cv.imshow('show',img)
cv.waitKey(0)
cv.destroyAllWindows()


