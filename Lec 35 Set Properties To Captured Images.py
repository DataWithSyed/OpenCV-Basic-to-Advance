import cv2

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# every property is associated with a number like cap_prop_frame_width replaces by 3
# Associated number for CAP_PROP_FRAME_HEIGHT is 4
cap.set(3, 3000)
cap.set(4, 3000)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()

    if ret  == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
