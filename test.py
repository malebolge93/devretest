
import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3, GPIO.IN) #infrared input için üçüncü pini gösterdik
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) #sekizinci pine yeşil pini atadık ve default olarak kapalı olmasını istedik
GPIO.setup(10, GPIO.OUT, initial=GPIO.HIGH) #onuncu pine kırmızı pini atadık ve default olarak açıkolmasını istedik


while True:
    val = GPIO.input(3) #Üçüncü pinden gelen sinyal verisini bir değişkene atadık.
    
    if val == 0:
        GPIO.output(8, GPIO.HIGH) 
        GPIO.output(10,GPIO.LOW)
        sleep(5) #daha az güç tüketimi için kod blokları sürekli okunmak yerine 5 saniye bekliyor
    else: 
        GPIO.output(10, GPIO.HIGH)
        GPIO.output(8, GPIO.LOW)
        sleep(5)
    
	
        
        

    
