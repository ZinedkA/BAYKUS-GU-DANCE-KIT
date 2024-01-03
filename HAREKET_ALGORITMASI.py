import pigpio
import time

# Raspberry Pi üzerindeki GPIO pin numaralarını ayarlayın
servo_pinas = [18]
servo_pinaas = [12]
servo_pinbs = [19]
servo_pinbbs = [13]

# Servo motorların minimum ve maksimum darbe genişlikleri (microseconds cinsinden)
servo_min_pulse = 500
servo_max_pulse = 2500

# Servo motorların minimum ve maksimum açıları
servo_min_angle = 0
servo_max_angle = 180

# Pigpio bağlantısını başlat
pi = pigpio.pi()

# Servo motorların bağlı olduğu GPIO pinlerini çıkış olarak ayarla
for servo_pina in servo_pinas:
    pi.set_mode(servo_pina, pigpio.OUTPUT)
for servo_pinaa in servo_pinaas:
    pi.set_mode(servo_pinaa, pigpio.OUTPUT)
for servo_pinb in servo_pinbs:
    pi.set_mode(servo_pinb, pigpio.OUTPUT)
for servo_pinbb in servo_pinbbs:
    pi.set_mode(servo_pinbb, pigpio.OUTPUT)

# Servo motorların açılarını ayarla
def set_servo_angle(pin, angle):
    # Verilen açıya karşılık gelen darbe genişliğini hesapla
    pulse_width = int((angle / (servo_max_angle - servo_min_angle)) * (servo_max_pulse - servo_min_pulse) + servo_min_pulse)

    # Servo motorunu belirtilen darbe genişliği ile hareket ettir
    pi.set_servo_pulsewidth(pin, pulse_width)

for servo_pina in servo_pinas:
    set_servo_angle(servo_pina, 90)
    time.sleep(0.05)
for servo_pinaa in servo_pinaas:
    set_servo_angle(servo_pinaa, 90)
    time.sleep(0.05)
for servo_pinb in servo_pinbs:
    set_servo_angle(servo_pinb, 90)
    time.sleep(0.05)
for servo_pinbb in servo_pinbbs:
    set_servo_angle(servo_pinbb, 90)
    time.sleep(0.05)
    
time.sleep(2)

def algoritma11():
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 45)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 45)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 135)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 135)
def algoritma12():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 45)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 90)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 135)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 90)
def algoritma13():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 45)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 135)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 135)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 45)
        
def algoritma21():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 65)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 45)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 115)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 135)      
def algoritma22():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 65)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 90)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 115)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 90)      
def algoritma23():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 65)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 135)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 115)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 45)
        
def algoritma31():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 90)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 45)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 90)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 135)            
def algoritma32():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 90)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 90)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 90)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 90)              
def algoritma33():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 90)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 135)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 90)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 45)
        
def algoritma41():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 115)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 45)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 65)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 135)                
def algoritma42():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 115)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 90)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 65)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 90)              
def algoritma43():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 115)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 135)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 65)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 45)
        
def algoritma51():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 135)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 45)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 45)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 135)               
def algoritma52():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 135)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 90)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 45)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 90)               
def algoritma53():    
    for servo_pina in servo_pinas:
        set_servo_angle(servo_pina, 135)
    for servo_pinb in servo_pinbs:
        set_servo_angle(servo_pinb, 135)
    for servo_pinaa in servo_pinaas:
        set_servo_angle(servo_pinaa, 45)
    for servo_pinbb in servo_pinbbs:
        set_servo_angle(servo_pinbb, 45)
'''       
algoritma11()
time.sleep(10)
algoritma13()
time.sleep(10)
algoritma33()
time.sleep(10)
algoritma53()
time.sleep(10)
algoritma51()
time.sleep(10)
algoritma31()
'''