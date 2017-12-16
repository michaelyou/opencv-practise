import cv2

image = cv2.imread('image/dinosaur.jpg')
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
flipped = cv2.flip(image, 0)
cv2.imshow("Flipped Vertically", flipped)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)
