import cv2
vid = cv2.VideoCapture(0)

blurVal = 20

font                   = cv2.FONT_HERSHEY_SIMPLEX
bottomLeftCornerOfText = (10,30)
fontScale              = 1
fontColor              = (0,0,0)
thickness              = 4
lineType               = 2


while True:
    ret, frame = vid.read()
    frame = cv2.flip(frame, 1)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurredFrame = cv2.blur(grayFrame, (blurVal, blurVal), cv2.BORDER_DEFAULT)
    lineFrame = grayFrame / blurredFrame
    cv2.imshow('linedFrame', lineFrame)
    cv2.putText(blurredFrame, str(blurVal), bottomLeftCornerOfText, font, fontScale, fontColor, thickness, lineType)
    cv2.imshow('Frame', blurredFrame)
    k = cv2.waitKey(1)
    if k == 27:
        break
    if cv2.getWindowProperty('linedFrame',cv2.WND_PROP_VISIBLE) < 1:        
        break   
    if k == 45: #   -
        blurVal-=2
    if k == 61: #   = +
        blurVal+=2
    if(blurVal<=0):
        blurVal=2
vid.release()
cv2.destroyAllWindows()