from cv2 import cv2

img = cv2.imread('man.png') # must pass valid file directory
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #converting the image into grayscale image



face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")



faces = face_cascade.detectMultiScale(gray_img, scaleFactor = 1.05, minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (255, 255, 250),3)



cv2.imshow("ImageWindow", img) # displaying the image
cv2.waitKey(0) #waitKey is set to 0, that means the image window will close as soon as any key is pressed.
cv2.destroyAllWindows() 