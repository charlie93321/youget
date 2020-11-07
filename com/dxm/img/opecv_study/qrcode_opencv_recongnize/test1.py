import cv2 as cv

img = cv.imread('mycode.png')

qrcode = cv.QRCodeDetector()
result,points,code = qrcode.detectAndDecode(img)

print(result)

print(")))))))))))))))))))))))))))))))))))))))))))))")

print(points)
print(")))))))))))))))))))))))))))))))))))))))))))))")
print(code)