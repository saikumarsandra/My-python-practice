import cv2 as c
source=c.VideoCapture(0)#capture image using web cam can add video path as a parameter
ret,img=source.read()
print(ret)
c.imshow('IMG',img)
c.waitKey(0)
#c.imwrite('sai.jpg',img)
c.destroyAllWindows()