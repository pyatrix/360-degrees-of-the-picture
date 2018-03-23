# Rotate one picture 360 degree and save it 將一張圖片旋轉360度並保存
# Preset each rotation angle 預設每次旋轉角度 : 10 degrees
# Default input 預設輸入: lena.jpg
# Default output file name 預設輸出檔名與格式 : lena10.png ,lena20.png,lena30.png,.....



#import numpy as np
import cv2

angle = 0
while angle < 30:
	
	# Preset each rotation angle 預設每次旋轉角度 : 10 degrees
	angle += 10
	
	# Default input 預設輸入: lena.jpg
	img = cv2.imread('lena.jpg') 
	
	sp = img.shape
	height = sp[0]
	width  = sp[1]
	M = cv2.getRotationMatrix2D((width/2,height/2),angle,1) 
	dst = cv2.warpAffine(img,M,(width,height))
	
	cv2.imshow('name',dst) 
	cv2.waitKey(30)
	
	# Default output file name 預設輸出檔名與格式 : lena10.png ,lena20.png,lena30.png,.....
	outname = 'lena%d.png' %  (angle)
	cv2.imwrite(outname,dst)
