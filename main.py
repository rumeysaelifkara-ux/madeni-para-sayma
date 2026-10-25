
import cv2
from coin_detector import madeni_para_say

resim_yolu = "images/para.jpg"
resim = cv2.imread(resim_yolu)

if resim is None:
    print("Fotoğraf bulunamadı. images klasörünü kontrol edin.")
else:
    para_sayisi, sonuc_resim = madeni_para_say(resim)
    print("Tespit edilen madeni para sayısı:", para_sayisi)
    cv2.imwrite("sonuc.jpg", sonuc_resim)
    print("Sonuç görüntüsü sonuc.jpg dosyasına kaydedildi.")
