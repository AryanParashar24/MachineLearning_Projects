import cv2

cap = cv2.VideoCapture(0)
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

while True:

    # ret To retrun a value after running som einpout as say on the display or the frame
    ret, frame = cap.read()

    if ret:
        faces = classifier.detectMultiScale(frame)

        for face in faces:
            x, y, w, h = face
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        # For breaking down the occurence that occurs in the process and retrun some key as the output
        cv2.imshow("My window", frame)

    # Here in this coed the wait key is for the rest it is taking in refreshin gthe code or the input being given to it if the wait
    # is increased to lets say 1000 then the camera will lag a lot
    # We generally never provide the waitkey as even 1 isn't the smallest on eit will be the framerate of about 1 and it refresh the image for
    # about 1 millisecond
    key = cv2.waitKey(1)


    # here we are giving it a key to get it something to do somethin gin order to acknoledge it taht some actions are being taking place
    # So we placed the q key as in the value and ord value of it that is the unicode value of the q iun the process
    # Also here if in the waitkey if in the time interval of lets say 1000 then it will wait for lets say 100 and then it will check
    # if q key is pressed and if the key is pressed then it will break out of the loop
    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()