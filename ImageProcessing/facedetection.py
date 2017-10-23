import cv2

file = "photo.jpg"

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread(file)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Return and find face's [col, row], height, width
# Scale downscale by 5% (more passes) and how many neighbors to search
faces = face_cascade.detectMultiScale(gray_img, scaleFactor =1.2,
minNeighbors =5)

# Start top left
for x, y, w, h in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h), (0,255,0),3 )

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))

cv2.imshow("Gray",img)
cv2.waitKey(5000)
cv2.destroyAllWindows()
