import cv2
import time
import os

# Capture a picture
cam = cv2.VideoCapture(1)
cv2.namedWindow("Python Alarm App")
ret, frame = cam.read()
if not ret:
    print("Failed to capture image")
    exit()
cv2.imwrite("verification.png", frame)
print("Verification image captured")
cam.release()

# Set the timer
timer = int(input("Enter the time in seconds: "))
start_time = time.time()

# Start the alarm
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time >= timer:
        os.system("mpg123 alarm.mp3 &")
        break
    cam = cv2.VideoCapture(1)
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture image")
        continue
    cv2.imshow("Python Alarm App", frame)
    k = cv2.waitKey(1)
    if k == 27:
        print("Closing the app")
        exit()
    cam.release()

# Verify the picture
while True:
    cam = cv2.VideoCapture(1)
    ret, frame = cam.read()
    if not ret:
        print("Failed to capture image")
        continue
    if cv2.imread("verification.png").shape != frame.shape:
        print("Verification failed")
        cv2.imshow("Python Alarm App", frame)
        k = cv2.waitKey(1)
        if k == 27:
            print("Closing the app")
            exit()
    else:
        print("Verification successful")
        break
    cam.release()
cv2.destroyAllWindows()

# Stop the alarm
os.system("pkill mpg123")
