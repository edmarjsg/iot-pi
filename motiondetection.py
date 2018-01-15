import RPi.GPIO as GPIO
import time
import os

pirsensor = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(pirsensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

while True:
   time.sleep(0.1)
   previous_state = current_state
   current_state = GPIO.input(pirsensor)
   if current_state != previous_state:
      if current_state:
         print('Motion Detected!')
	 os.system("python pushgcm.py")
