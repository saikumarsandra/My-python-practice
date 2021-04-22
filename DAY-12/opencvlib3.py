import cv2 as c
source=c.VideoCapture(0)#0capture image using web cam can add video path as a parameter,1 for usb cam
#loop through video until we capture every frame in video
while True:

    ret,img=source.read()
    print(ret)
    if (ret==False):
        break

    c.imshow('IMG',img)
    key=c.waitKey(1)#10msec
    if key==27:#ascii value for escape
        break
#c.imwrite('sai.jpg',img)
c.destroyAllWindows()

    