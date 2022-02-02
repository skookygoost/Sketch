import cv2

filename = '' #file name goes in here
img = cv2.imread(filename)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

inverted_gray_img = cv2.bitwise_not(gray_img)


blurred_img = cv2.GaussianBlur(inverted_gray_img, (21, 21), 0)

inverted_blurred_img = cv2.bitwise_not(blurred_img)

pencil_sketch_IMG = cv2.divide(gray_img, inverted_blurred_img, scale=256.0)

cv2.imwrite('', pencil_sketch_IMG) #new file name goes in here