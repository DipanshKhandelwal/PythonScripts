import glob
import numpy as np
import cv2
import os
from PIL import Image

from resizeimage import resizeimage

X_data = [[],[]]
training_data = [[],[]]
testing_data = [[],[]]
validation_data = [[],[]]

# Give the folder where you want to save images
dirlist = glob.glob('./training_nn/by_class/by_class/*')
#dirlist.sort()

size = (32,32)
for j in range(len(dirlist)):
        dirlist[j] = dirlist[j][32:] #adjust this according to your folder path string
        

dirlist.sort(key=int)
	
for i in range(len(dirlist)):
	y=i
	print(dirlist[i])

	files = glob.glob ('./training_nn/by_class/by_class/'+dirlist[i]+"/*.png")

	count =0
	start=0

	X_data[0].clear()
	X_data[1].clear()
	
	for file in files:
                #print(file)
                original_image = Image.open(file)
                original_image.thumbnail(size, Image.ANTIALIAS)
                original_image.save(file)
                image = cv2.imread(file)
                image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                _,image =cv2.threshold(image,128,255,cv2.THRESH_BINARY_INV)
                X_data[0].append(image)
                X_data[1].append(y)
                #print(X_data[1])
                count = count+1
	for x in range(start,int(0.8*count)):
		training_data[0].append(X_data[0][x])
		training_data[1].append(X_data[1][x])
	start+= int(0.8*count)+1

	for x in range(start,start+int(0.1*count)):
		testing_data[0].append(X_data[0][x])
		testing_data[1].append(X_data[1][x])
	start+=(int(0.1*count)+1)

	for x in range(start,count):
		validation_data[0].append(X_data[0][x])
		validation_data[1].append(X_data[1][x])



#np.savez_compressed('E:/Design Project/ocr/data_set',training_data=training_data,validation_data=validation_data,testing_data=testing_data)
print('X_data shape:', np.array(X_data).shape)
print('training_data_shape:',np.array(training_data[0]).shape)
print('testing_data_shape:',np.array(testing_data[0]).shape)
print('validation_data_shape:',np.array(validation_data[0]).shape)

# print([init_size,fin_size])


print(type(training_data))
np.savez_compressed('E:/Design Project/ocr/data_set',training_data=training_data,validation_data=validation_data,testing_data=testing_data)
