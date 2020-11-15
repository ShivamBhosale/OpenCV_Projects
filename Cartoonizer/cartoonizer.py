#!/usr/bin/env python
# coding: utf-8

# In[2]:


import cv2 as cv
import numpy as np


# In[3]:


#Reading the Image
img= cv.imread("me.jpg")


# In[4]:


#edges
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray=cv.medianBlur(gray,5)
edges=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,9,9)


# In[6]:


#cartoonization
color=cv.bilateralFilter(img,9,250,250)
cartoon=cv.bitwise_and(color,color, mask=edges)
cartoon=cv.resize(cartoon, (960, 540))


# In[ ]:


cv.imshow("Image",img)
cv.imshow("edges",edges)
cv.imshow("cartoon",cartoon)
cv.imshow("cartoon",cartoon)
cv.waitKey(0)
cv.destroyAllwindows()


# In[ ]:




