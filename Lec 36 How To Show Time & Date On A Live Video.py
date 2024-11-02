import cv2
import datetime as dt
import numpy as np

cap = cv2.VideoCapture(0)

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3, 800)
#cap.set(4, 520)
#print(cap.get(3))
#print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width:  ' + str(cap.get(3)) + '  ,Height: ' + str(cap.get(4))
        datet = str(dt.datetime.now())
        frame = cv2.putText(frame, datet, (10,100), font, 1,(0,0,0), 5, cv2.LINE_AA)
        cv2.imshow('Messy', frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()