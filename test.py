import cv2
import numpy as np
from sklearn.externals import joblib
import numSplit

if __name__ == '__main__':
    
    img = cv2.imread( '1.jpg', 0 )
    #read image
    
    res = numSplit.splitNum(img)
    #split the num in image,return position(x,y),width,height
    
    clf = joblib.load( './model/finalKnnOcr.pickle')#load model
    
    num = -1
    ret,mask = cv2.threshold(img,175,255,cv2.THRESH_BINARY_INV) #er zhi hua
    kernel = np.ones((3,3),np.uint8) #use to dilate and erode

    for i in res:
        num = num + 1
        x,y,w,h = i[0],i[1],i[2],i[3]
        imag =  mask[y-1:y+h+1,x-1:x+w+1] #+1 and -1 is uses to make sure that the whole num is included
        imag = cv2.resize(imag,(28,28))

        #lower the position of nums are,more accurate the result is
        if num >= 9:
          imag = cv2.dilate(imag,kernel,iterations = 1) #let num be more familiar with train set          
          ret,imag = cv2.threshold(imag,175,255,cv2.THRESH_BINARY_INV) #let the background be black
        pre = clf.predict( imag.reshape(1,784) )
        cv2.imshow('%d'%num, imag)
        print( num,' ', pre)
        if num == 13:
          #num must be on the bottom
          break
    cv2.waitKey(0)
