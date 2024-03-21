import pyautogui
import cv2
import time

# When I have tried into my windows machine then it was ask to do
# But in Linux machine it will works fine without this false selection
pyautogui.FAILSAFE = False

# Creating a openCv object
video = cv2.VideoCapture(0)
# using haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
while True:
    check, img = video.read()
    g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(g_img, scaleFactor=1.05, minNeighbors=5)
    #if eyes == ():
    #    continue
    #else:
    x = eyes[0][0]
    y = eyes[0][1]
    w = eyes[0][2]
    h = eyes[0][3]
    g_img = cv2.rectangle(g_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    print(x, y)
    mx = 1.66 * x
    my = 0.66 * y
    pyautogui.moveTo(mx, my)
    cv2.imshow("Capture...", g_img)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows()
