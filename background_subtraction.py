import cv2
import numpy as np


cap = cv2.VideoCapture("C:\\Users\\DELL\\PycharmProjects\\opencv_project\\test_images\\car.mp4")
_,first_frame = cap.read() # ilk frame çekilir okunur
first_frame = cv2.resize(first_frame,(640,480))
first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY) # 1 - resmi gri tonu yaparız ki iyi sonuç çıksın
first_gray = cv2.GaussianBlur(first_gray,(5,5),0) # 2 - resmi blurluyoruz yumuşatıyoruz


while 1:
    _,frame = cap.read()  # ilk frame çekilir okunur
    frame = cv2.resize(frame,(640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 1 - resmi gri tonu yaparız ki iyi sonuç çıksın
    gray = cv2.GaussianBlur(gray, (5, 5), 0)  # 2 - resmi blurluyoruz yumuşatıyoruz


    diff = cv2.absdiff(first_gray,gray) # ilk frame ile dğer rame karşılaştırıp aynı olanları siyah farklı olanları beyaz yapıyor fonksiyon
    _,diff = cv2.threshold(diff,50,255,cv2.THRESH_BINARY) # siyaha yakın olanlar siyah beyaza yakın olanlar beyaza çevrilir THRESH_BINERY ile
                                                                        # böylelikle threshold uygulayarak gri tonlar kaybolur

    cv2.imshow("frame",frame)
    cv2.imshow("first",first_frame)
    cv2.imshow("diff",diff)

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()