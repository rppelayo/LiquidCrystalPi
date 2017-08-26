import RPi.GPIO as GPIO
import LiquidCrystalPi
import time as time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LCD = LiquidCrystalPi.LCD(29, 31, 33, 35, 37, 38)

LCD.begin(16,2)

time.sleep(0.5)
LCD.write("Hello World")
