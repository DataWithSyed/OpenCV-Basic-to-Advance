# HOW TO CAPTURE LIVE STREAM FROM DEFAULT CAMERA

import cv2

cap = cv2.VideoCapture(0)

# This ret will store TRUE or FALSE if the frame is available
# This frame will store the captured frame if frame is available to ret that means it becomes TRUE


# print(cap.isOpened())         # will print the boolean answer of this cap.isOpened()

# This ret will store TRUE or FALSE if the frame is available
# This frame will store the captured frame if frame is available to ret that means it becomes TRUE

# True can be replaced by cap.isOpened()
# if cap.isOpened() is used then ot will not give any error
while True:
    ret, frame = cap.read()


    cv2.imshow("Messy", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()