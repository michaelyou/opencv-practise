import cv2


image_path = "image/dinosaur.jpg"

image = cv2.imread(image_path)
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# image[start_y:end_y, start_x:end_x]
image[0:10, 0:image.shape[1]] = (0, 0, 255)

cv2.imshow("Original", image)
cv2.waitKey(0)
