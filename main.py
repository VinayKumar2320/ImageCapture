import cv2
cam = cv2.VideoCapture(1)
cv2.namedWindow("Python ss app")

img_counter=0
while True:
    ret,frame=cam.read()
    if not ret:
        print("failed")
        break 
    cv2.imshow("test",frame)
    k=cv2.waitKey(1)
    if k%256==27:
        print("close the app")
        break
    elif k%256==32:
        img_name="opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name,frame)
        print("SS Taken")
        img_counter+=1
cam.release()