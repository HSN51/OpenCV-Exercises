import cv2
import numpy as np


font = cv2.FONT_HERSHEY_SIMPLEX
font = cv2.FONT_HERSHEY_COMPLEX #OPENCV_FONTS

img = cv2.imread("C:\\test_images\\polygons.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #resmi 0 ile 1'lere ayrılır
_,threshold = cv2.threshold(gray,240,255,cv2.THRESH_BINARY)

contours,_ = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    epsilon = 0.01 * cv2.arcLength(cnt,True)
    approx = cv2.approxPolyDP(cnt,epsilon,True)

    cv2.drawContours(img,[approx],0,(0),5)

    x = approx.ravel()[0]#ravel fonksiyonu dik satırları satıra döker / 0 index x  1 index y işaret eder
    y = approx.ravel()[1] # yatay sıralar her bir köşeyi temsil eder

    if len(approx) == 3:
        cv2.putText(img,"Triangle",(x,y),font,1,(0))

    elif len(approx) == 4:
        cv2.putText(img,"Rectangle",(x,y),font,1,(0))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), font, 1, (0))

    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x, y), font, 1, (0))

    else:
        cv2.putText(img, "Ellipse", (x, y), font, 1, (0))


cv2.imshow("IMG",img)

cv2.waitKey(0)
cv2.destroyAllWindows()

