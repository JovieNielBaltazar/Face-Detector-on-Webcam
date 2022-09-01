import cv2, time
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    img_1 = frame
    gray_img_1 = cv2.cvtColor(img_1, cv2.COLOR_BGR2GRAY)

    face = face_cascade.detectMultiScale(gray_img_1, scaleFactor=1.1, minNeighbors=10)

    for x, y, w, h in face:
        img_1 = cv2.rectangle(img_1, (x, y), ((x+w),(y+h)), (0, 0, 255), 2)

    cv2.imshow("Hello from camera", img_1)
    key = cv2.waitKey(1)

    if key==ord("q"):
        break


cv2.destroyAllWindows()
video.release()