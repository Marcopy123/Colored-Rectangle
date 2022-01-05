import cv2

width=640
height=360

cam=cv2.VideoCapture(1,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

deltaX = 1
deltaY = 2

rowMin = 60
rowMax = 120
columnMin = 140
columnMax = 280

while True:
    ignore,  frame = cam.read()

    if rowMax >= height or rowMin <= 0:
        deltaX = -deltaX

    if columnMax >= width or columnMin <= 0:
        deltaY = -deltaY

    rowMin += deltaX
    rowMax += deltaX

    columnMin += deltaY
    columnMax += deltaY
    

    frameROIBGR = frame[rowMin:rowMax, columnMin:columnMax] # this is the position of what is actually gonna be displayed in the box

    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    BGRframe = cv2.cvtColor(grayFrame, cv2.COLOR_GRAY2BGR)

    BGRframe[rowMin:rowMax, columnMin:columnMax] = frameROIBGR # this is the position of the box

    cv2.imshow('my WEBcam', BGRframe)
    cv2.moveWindow('my WEBcam',0,0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()