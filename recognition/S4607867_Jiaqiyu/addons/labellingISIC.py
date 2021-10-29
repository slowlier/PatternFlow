# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 19:16:25 2021

@author: Jiaqi Yu
"""


import os
import cv2

def read_directory(directory_name):
    
    array_of_name=[]
    array_of_output=[]
    """this loop is for read each image in this foder,directory_name is the foder name with images."""
    for filename in os.listdir(r"./"+directory_name):
        if "txt" not in filename:
            img = cv2.imread(directory_name + "/" + filename)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        size = img.shape
        x_len=size[1]
        y_len=size[0]
        
        ret,thresh =cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
        contours, hier = cv2.findContours(thresh,cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    
        """only need the first contour"""
        #print(len(contours))
        for c in contours:
            # find bounding box coordinates
            x,y,w,h = cv2.boundingRect(c)
            output="0 "    
            x_center=round((x+w/2)/x_len,6)
            y_center=round((y+h/2)/y_len,6)
            w_normalized=round(w/x_len,6)
            h_normalized=round(h/y_len,6)
            output+=str(x_center)+" "
            output+=str(y_center)+" "
            output+=str(w_normalized)+" "
            output+=str(h_normalized)        
            cv2.rectangle(img, (x,y), (x+w, y+h), (255, 255, 0), 2)
            
        cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
    
        """show image"""
        #img = cv2.resize(img, (1502, 1024))
        #cv2.imshow("contours", img)
        #cv2.waitKey()
        #cv2.destroyAllWindows()
        """collect output"""
        print(output)
        array_of_output.append(output)
        del img
        array_of_name.append(filename)
        #print(img)
        #print(img.shape)
    return array_of_output,array_of_name


array_of_output,names=read_directory("validation label")

array_of_name=[]
for name in names:
    name=name.strip('_segmentation.png')
    array_of_name.append(name)









    
    
    
    
    
    
    
    
    
if not os.path.exists("./validation label output"):
    os.makedirs("./validation label output")
for i in range(len(array_of_name)):
    
    with open("./validation label output/"+array_of_name[i]+".txt","w") as f:
        f.write(array_of_output[i])
    
    
    
           