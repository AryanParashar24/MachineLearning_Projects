import cv2

cap = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

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

# For breaking down the occurence that occurs in the process and retrun some key as the output
        cv2.imshow("My Face", gray)

    key = cv2.waitKey(1)
# here we are giving it a key to get it something to do somethin gin order to acknoledge it taht some actions are being taking place
# So we placed the q key as in the value and ord value of it that is the unicode value of the q iun the process
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()