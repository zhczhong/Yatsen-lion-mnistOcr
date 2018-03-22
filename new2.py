import cv2
import numpy as np
# 获取每一帧
imag=cv2.imread('1.jpg',0)
#img = cv2.cvtColor(imag,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imag,210,255,0)
image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cnt = contours[1]
#M = cv2.moments(cnt)
#hull = cv2.convexHull(cnt)
i=0
#perimeter = cv2.arcLength(cnt,True)
#epsilon = 0.1*cv2.arcLength(cnt,True)
#approx = cv2.approxPolyDP(cnt,epsilon,True)
#image, contours,hicontours,hierarchy = cv2.findContours(thresh, 1, 2)erarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#th2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
#blur = cv2.GaussianBlur(img,(3,3),0)
#ret2,th2 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
#ret,thresh1=cv2.threshold(img,210,255,cv2.THRESH_BINARY)
#ret,th1 = cv2.threshold(img,0,255,cv2.THRESH_OTSU)
#11 为 Block size, 2 为 C 值
#th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,211,2)
#th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
for cnt in contours:
    i = i + 1
    area = cv2.contourArea(cnt)
    x,y,w,h = cv2.boundingRect(cnt)
    rectArea = w * h
    extent = area / rectArea
    if extent > 0.7 and extent < 1.3:
        #imag = cv2.rectangle(imag,(x,y),(x+w,y+h),(0,255,0),2)
#rect =  cv2.minAreaRect(cnt)
#box = cv2.boxPoints(rect)
#imag = cv2.drawContours(imag,hull,-1,(0,255,0),3)
        cv2.imshow('frame%d'%i, thresh[y:y+h,x:x+w])
#print(approx)
#print(hull)
#print(hierarchy)
