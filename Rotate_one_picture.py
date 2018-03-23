# Rotate one picture 360 degree and save it
# Default input: lena.jpg 預設輸入: lena.jpg

#import numpy as np
import cv2

angle = 0
while angle < 30:
	angle += 10
	img = cv2.imread('lena.jpg') 
	sp = img.shape
	height = sp[0]
	width  = sp[1]
	M = cv2.getRotationMatrix2D((width/2,height/2),angle,1) 
	dst = cv2.warpAffine(img,M,(width,height))
	
	cv2.imshow('name',dst) 
	cv2.waitKey(30)
	outname = 'lena%d.png' %  (angle)
	cv2.imwrite(outname,dst)
