# HOW TO CAPTURE LIVE STREAM FROM DEFAULT CAMERA
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')                # OR ('x', 'v', 'i','d')

# 1st argument is about the name of file and extension
# 2nd argument is about fourCC codes study it from http://fourcc.org/codecs.php
# 3rd argument is about frames per second
# 4th argument is about size of frame
out = cv2.VideoWriter('Output.avi', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    if ret == True:

        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        out.write(frame)        # out is the instance of videowriter and write will save file

        grey = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

        cv2.imshow("Messy", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()