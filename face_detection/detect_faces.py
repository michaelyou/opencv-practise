from facedetector import FaceDetector
import cv2

image = cv2.imread('china.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade_path = 'haarcascade_frontalface_default.xml'
fd = FaceDetector(face_cascade_path)
faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(3, 3))
print("I found {} face(s)".format(len(faceRects)))

for (x, y, w, h) in faceRects:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Faces", image)
cv2.waitKey(0)
