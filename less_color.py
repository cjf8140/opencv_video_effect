import cv2
vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)


lesser = 32

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,30)
fontScale              = 1
fontColor              = (255, 255, 255)
thickness              = 4
lineType               = 2

while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    #_frame = (frame * lesser) * lesser
    _frame = (255-frame)
    cv2.imshow('frame', frame)
    cv2.putText(_frame, str(lesser), bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
    cv2.imshow('LessColoredFrame', _frame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    if cv2.getWindowProperty('LessColoredFrame',cv2.WND_PROP_VISIBLE) < 1:        
        break   
    if k == 45: #   -
        lesser-=2
    if k == 61: #   = +
        lesser+=2
    if(lesser<=0):
        lesser=1
vid.release()
cv2.destroyAllWindows()