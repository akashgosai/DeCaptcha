import cv2
#import tensorflow as tf

img=cv2.imread("EAO.png")
# img=cv2.resize(img, (300,300))
import numpy as np 

kernel = np.ones((2,2), np.uint8) 

height, width, channels = img.shape

# white = [255,255,255]
# black = [0,0,0]

# for x in range(0,width):
#     for y in range(0,height):
#         channels_xy = img[y,x]
#         # if all(channels_xy == white):    
#         #     img[y,x] = black

#         # elif all(channels_xy == black):
#         #     img[y,x] = white
#         if all(channels_xy == img[0,0]):
#             img[y,x] = 0

# img_erosion = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_erosion = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(img_erosion[0,0])
# (thresh, img_erosion) = cv2.adaptiveThreshold(img_erosion, 255, cv2.ADAPTIVE_THRESH_MEAN_C   | cv2.THRESH_BINARY, 11,2)
ret,img_erosion = cv2.threshold(img_erosion,100,255,cv2.THRESH_BINARY)
img_erosion = cv2.dilate(img_erosion, kernel, iterations=2) 


# ret,img_erosion = cv2.threshold(img_erosion,127,255,cv2.THRESH_BINARY
# img_erosion = cv2.normalize(img_erosion, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

#tf.nn.max_pool(img_erosion,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
cv2.imwrite('akash.png',img_erosion)

cv2.waitKey(0)
