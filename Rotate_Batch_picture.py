# Batch rotate picture 360 degrees and store
import os
import sys
#import numpy as np
import cv2

NowDir = os.path.split(os.path.realpath(__file__))[0]
for  f  in  os.listdir( NowDir ):
	angle = 0
	while angle < 359:

		#Ignore the program itself
		if f == sys.argv[0]:
			continue


				
		img = cv2.imread(f)
		print(f)

		sp=img.shape
		height = sp[0]
		width = sp[1]
		#Image scaling
		ratio = 1
		#ratio = 1.414

		M = cv2.getRotationMatrix2D((width/2,height/2),angle,ratio)
		dst = cv2.warpAffine(img,M,(width,height))
		

		#Each rotation angle
		angle += 4
		if angle >= 360:
			sys.exit()
				
		cv2.imshow('name',dst)
		cv2.waitKey(3)

		if    f[1]=='.' :
			fo = f [0:1]
		elif  f[2]=='.' :
			fo = f [0:2]
		elif  f[3]=='.' :
			fo = f [0:3]
		elif  f[4]=='.' :
			fo = f [0:4]
		elif  f[5]=='.' :
			fo = f [0:5]
		outn = '%s_%s.png' % ( fo, angle )
		print (outn)
		cv2.imwrite(outn,dst)
