# Rotate one picture 360 degree and save it 
# Preset each rotation angle  : 10 degrees
# Default input : lena.jpg
# Default output file name  : lena10.png ,lena20.png,lena30.png,.....


import sys
#import numpy as np
import cv2

angle = 0
while angle < 30:
	
	# Preset each rotation angle  : 10 degrees
	angle += 10
	
	i = sys.argv[1]
	print (i)
	img = cv2.imread('i') 
	
	sp = img.shape
	height = sp[0]
	width  = sp[1]
	M = cv2.getRotationMatrix2D((width/2,height/2),angle,1) 
	dst = cv2.warpAffine(img,M,(width,height))
	
	cv2.imshow('name',dst) 
	cv2.waitKey(23)
	
	# Default output file name  : lena10.png ,lena20.png,lena30.png,.....
	if    i[1]=='.' :
		fo = i [0:1]
	elif  i[2]=='.' :
		fo = i [0:2]
	elif  i[3]=='.' :
		fo = i [0:3]
	elif  i[4]=='.' :
		fo = i [0:4]
	elif  i[5]=='.' :
		fo = i [0:5]
	outname = '%s_%s.png' % ( fo, angle )
	cv2.imwrite(outname,dst)
