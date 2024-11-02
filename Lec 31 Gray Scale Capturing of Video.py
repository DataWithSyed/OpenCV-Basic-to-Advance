# HOW TO CAPTURE LIVE STREAM FROM DEFAULT CAMERA

import cv2

cap = cv2.VideoCapture(0)
# print(cap.isOpened())         # will print the boolean answer of this cap.isOpened()

# This ret will store TRUE or FALSE if the frame is available
# This frame will store the captured frame if frame is available to ret that means it becomes TRUE

# cap.isOpened() can be replaced by True
# if cap.isOpened() is used then ot will not give any error
while cap.isOpened():
    ret, frame = cap.read()

    # get() function will have prop id's which are described ahead and from https://docs.opencv.org/master/d4/d15/group__videoio__flags__base.html
    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Cvtcolor will change the color
    # 1st argument is the source which is frame which we are capturing
    # 2nd argument is the conversion
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Messy", grey)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()