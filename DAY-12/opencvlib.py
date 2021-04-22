import cv2
img=cv2.imread(r'c:\users\saileo\pictures\low.jpg')
#print(img[100,100])
#print(img.shape)
img1=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#color converted to gray
cv2.rectangle(img,(40,120),(75,75),(0,255,0),2)#marked eye on img,(img,(40,120),(75,75),(0,255,0),2)
cv2.rectangle(img1,(40,120),(75,75),(255,255,255),2)#marked eye on img,(img,(40,120),(75,75),(255,255,255),2)
img[100,100]=[0,255,0]
cv2.imshow('Live',img)
cv2.imshow('live2',img1)
#cv2.imwrite('new.png',img,)
cv2.waitKey(0)
cv2.destroyAllWindows()