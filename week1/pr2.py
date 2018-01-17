import cv2
import numpy as np
import time
#img = cv2.imread("small.png")

#print img.shape
#print type(img)
#print type(img[0,0,0])
#from 0 to 2 its bgr
car = cv2.imread("car.jpg")
#cv2.imshow("Win",car[...,0])
#cv2.waitKey(0)


#img = np.full((50,50),255,dtype = np.uint8)
#st = time.time()
#img[20:30,20:30] = 0
#print time.time() - st
gray = car[...,0]*0.144 + car[...,1]*0.587+car[...,2]*0.299

#print type(gray)
gray = gray.astype(np.uint8)
grayOpenCv = cv2.cvtColor(car,cv2.COLOR_BGR2GRAY)
#cv2.imshow("Win",gray)
#cv2.imshow("opencv",grayOpenCv)
cv2.waitKey(0)

output = cv2.filter2D(grayOpenCv, -1, np.ones((3,3),np.float64)/9)
out = cv2.GaussianBlur(grayOpenCv,(25,25),10)

cv2.imshow("grayblur", output)
cv2.imshow("gausblur", out)
cv2.waitKey(0)


