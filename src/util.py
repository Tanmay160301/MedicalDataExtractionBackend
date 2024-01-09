import cv2
import numpy as np


#we will create a function which will preprocess the image which will remove the shadows and make it more readable for our parser
def preprocess_img(img):
    gray=cv2.cvtColor(np.array(img),cv2.COLOR_BGR2GRAY)
    resized_img=cv2.resize(gray,None,fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR)
    processed_img=cv2.adaptiveThreshold(resized_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,61,11)
    return processed_img