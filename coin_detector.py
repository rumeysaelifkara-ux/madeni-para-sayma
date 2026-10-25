
import cv2

def madeni_para_say(resim):
    gri_resim = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
    bulanik_resim = cv2.GaussianBlur(gri_resim, (9, 9), 2)

    daireler = cv2.HoughCircles(
        bulanik_resim,
        cv2.HOUGH_GRADIENT,
        dp=1.2,
        minDist=90,
        param1=100,
        param2=45,
        minRadius=15,
        maxRadius=150
    )

    sonuc_resim = resim.copy()

    if daireler is not None:
        bulunan_daireler = daireler[0].astype(int)

        for x, y, r in bulunan_daireler:
            cv2.circle(sonuc_resim, (x, y), r, (0, 255, 0), 3)
            cv2.circle(sonuc_resim, (x, y), 2, (0, 0, 255), 3)

        para_sayisi = len(bulunan_daireler)
    else:
        para_sayisi = 0

    return para_sayisi, sonuc_resim
