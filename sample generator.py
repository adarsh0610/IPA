import cv2

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) #create a video capture object which is helpful to capture videos through webcam
cam.set(3, 640) # set video framewidth
cam.set(4,480) # set video frameheight

detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

face_id = input("Enter a numeric user ID here:  ")
#use integer id for every new face (0,1,2,3,4,5,6......)

print("Taking samples, look at camera.....")
count = 0 #initializing sampling face count

while True:
    ret, img = cam.read()#read the frames using the above created object
    converted_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(converted_image, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        count += 1

        cv2.imwrite("samples/face." + str(face_id) + '.' + str(count) + ".jpg", converted_image[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27: #press ESC to stop
        break
    elif count >= 10:
        break

print("Samples taken now closing the program....")
cam.release()
cv2.destroyAllWindows()