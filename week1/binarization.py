import cv2
import numpy as np 
import tools as tl

img = cv2.imread("sudoku.png",0)# to be black-white

ret, th = cv2.threshold(img, 127,255,cv2.THRESH_BINARY)
ret, th_inv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)

th_adap11 = cv2.adaptiveThreshold(img,255,
					cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
					cv2.THRESH_BINARY,11,2)
th_adap5 = cv2.adaptiveThreshold(img,255,
					cv2.ADAPTIVE_THRESH_MEAN_C, 
					cv2.THRESH_BINARY,5,2)

#adaptive treshold divivedv the picture and нахожит порог для каждого
#поэтому он ничего не возвращает

ret_0, th_0 = cv2.threshold(img, 0,255,cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
print (ret_0)
print (cv2.THRESH_BINARY+cv2.THRESH_OTSU)

row1 = tl.concat_hor((img,th, th_0))
row2 = tl.concat_hor((img, th_adap5, th_adap11))
final_img = tl.concat_ver((row1,row2))


cv2.imshow("Sodoku", final_img)
cv2.waitKey(0)