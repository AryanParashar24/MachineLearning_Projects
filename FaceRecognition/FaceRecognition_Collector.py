import cv2
import numpy as np

# To check whether a particular fiel already exist int he code or not fopr tha we could use the library
import os

cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

name = input("Enter your name:")

frames = []
outputs = []

while True:

# ret To retrun a value after running som einpout as say on the display or the frame
    ret, frame = cap.read()

    if ret:
        faces = detector.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face

            cut = frame[y:y+h, x:x+w]

            fix = cv2.resize(cut, (100, 100))
            gray = cv2.cvtColor(fix, cv2.COLOR_BGR2GRAY)

            cv2.imshow("My Face", gray)

# For breaking down the occurence that occurs in the process and return some key as the output
        cv2.imshow("My screen", frame)

    key = cv2.waitKey(1)
# here we are giving it a key to get it something to do somethin gin order to acknoledge it taht some actions are being taking place
# So we placed the q key as in the value and ord value of it that is the unicode value of the q iun the process
    if key == ord("q"):
        break

    if key == ord("c"):
        # cv2.imwrite(name + ".jpg", frame)
        frames.append(gray.flatten())
        outputs.append([name])

X = np.array(frames)
y = np.array(outputs)

## now in the process we will be saving the data of the person's face as in the horizontal stack
## So we will be doing hroizontal stacking, same as in the arrays we had the first element as y and the remaining elements in the array as X
data = np.hstack([y, X])


## Here in the code we written ealier we will be saving a face along with th e features of the face as well but then if we wish to save the pic and then record or repeat the process
## then it will delete the earleir pic in the array as the code was arranged in the horizontal way so

## Now, here we will have to make a vertical satck for saving the later pic saved by us in the array in the bottom of the previous one so that the data can be saved and the real recognition can be performed eventually
f_name = "face_data2.npy"

if os.path.exists(f_name):
    old = np.load(f_name)
    ##Here wht happenning is that if the data or the file is already present then it will load the old data and will now craete a horizontal stack inspite of vertical one
    ##as a result of which the data that will be captured later will be stored as the original data in place of the earlier or the older one
    data = np.hstack([old, data])

np.save(f_name, data)

cap.release()
cv2.destroyAllWindows()