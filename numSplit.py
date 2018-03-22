import cv2
import numpy as np

def splitNum(imag):    
    ret,thresh = cv2.threshold(imag,210,255,0)
    image,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    i=0
    for cnt in contours:
        i = i + 1
        area = cv2.contourArea(cnt)
        x,y,w,h = cv2.boundingRect(cnt)
        rectArea = w * h
        extent = area / rectArea
        if extent > 0.7 and extent < 1.3:
            cv2.imshow('frame%d'%i, imag[y:y+h,x:x+w])

if __name__ == "__main__":
    imag=cv2.imread('1.jpg',0)
    splitNum(imag)
