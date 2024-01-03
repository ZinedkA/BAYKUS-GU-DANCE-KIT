import numpy as np
import cv2
import subprocess
import pigpio
import time

# Haar Cascade sınıflandırıcısını yükle
aircraft_cascade = cv2.CascadeClassifier('BAYKUS_HC.xml')

#Video çerçevesinin ortasını bulmak için
cap = cv2.VideoCapture(1)
#cap = cv2.VideoCapture('trainning.mp4')
cap.set(3, 640)  # Genişlik
cap.set(4, 480)  # Yükseklik


cross_center = (int(cap.get(3) / 2), int(cap.get(4) / 2))

# Ekranı 15 eşit parçaya bölme işlevi
def get_region(x, y, width, height):
    div_x, div_y = 5, 3
    region_width, region_height = width // div_x, height // div_y
    region_num_x, region_num_y = (x // region_width) + 1, (y // region_height) + 1
    return region_num_x, region_num_y

def draw_line(x1, y1, x2, y2, color, thickness):
    cv2.line(frame, (x1, y1), (x2, y2), color, thickness)
'''
def get_rpi_temperature():
    result = subprocess.run(['vcgencmd', 'measure_temp'], capture_output=True, text=True)
    temperature_str = result.stdout.strip()
    temperature = float(temperature_str.split('=')[1].split('\'')[0])
    return temperature
'''
#######################################################################
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Gri tonlamaya dönüştür
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Uçakları tespit et
    aircrafts = aircraft_cascade.detectMultiScale(gray, 1.1, 2)

    # En büyük çemberi bul
    max_radius = 0
    max_circle = None
    for (x, y, w, h) in aircrafts:
        cX, cY = x + w // 2, y + h // 2
        radius = w // 2
        if radius > max_radius:
            max_radius = radius
            max_circle = (cX, cY, radius)

    xd1, yd1 = 0, 0
    xd2, yd2 = 130, 30
    cv2.rectangle(frame, (xd1, yd1), (xd2, yd2), (0, 0, 0), thickness=cv2.FILLED)

    if max_circle is not None:
        # Uçağın bulunduğu bölgeyi hesapla
        region_x, region_y = get_region(max_circle[0], max_circle[1], frame.shape[1], frame.shape[0])
        text = f"HEDEF:  ({region_x}, {region_y})"
        cv2.putText(frame, text, (7, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.circle(frame, (max_circle[0], max_circle[1]), 10, (0, 0, 255), 2)
        cv2.circle(frame, (max_circle[0], max_circle[1]), 2, (255, 255, 255), 1)
        '''
        if (region_x == 1) and (region_y == 1):
            HAREKET_ALGORITMASI.algoritma11()
        if (region_x == 1) and (region_y == 2):
            HAREKET_ALGORITMASI.algoritma12()
        if (region_x == 1) and (region_y == 3):
            HAREKET_ALGORITMASI.algoritma13()
        if (region_x == 2) and (region_y == 1):
            HAREKET_ALGORITMASI.algoritma21()
        if (region_x == 2) and (region_y == 2):
            HAREKET_ALGORITMASI.algoritma22()
        if (region_x == 2) and (region_y == 3):
            HAREKET_ALGORITMASI.algoritma23()
        if (region_x == 3) and (region_y == 1):
            HAREKET_ALGORITMASI.algoritma31()
        if (region_x == 3) and (region_y == 2):
            HAREKET_ALGORITMASI.algoritma32()
        if (region_x == 3) and (region_y == 3):
            HAREKET_ALGORITMASI.algoritma33()
        if (region_x == 4) and (region_y == 1):
            HAREKET_ALGORITMASI.algoritma41()
        if (region_x == 4) and (region_y == 2):
            HAREKET_ALGORITMASI.algoritma42()
        if (region_x == 4) and (region_y == 3):
            HAREKET_ALGORITMASI.algoritma43()
        if (region_x == 5) and (region_y == 1):
            HAREKET_ALGORITMASI.algoritma51()
        if (region_x == 5) and (region_y == 2):
            HAREKET_ALGORITMASI.algoritma52()
        if (region_x == 5) and (region_y == 3):
            HAREKET_ALGORITMASI.algoritma53()
        '''            
            
    #temperature = get_rpi_temperature()
    #print(f"Raspberry Pi Sıcaklık: {temperature} °C")       

    # Sonuçları göster
    cv2.imshow('Video', frame)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Pencereleri kapat ve video çerçevesini serbest bırak
cap.release()
cv2.destroyAllWindows()
