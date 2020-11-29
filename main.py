
#!/usr/bin/env python
import RPi.GPIO as GPIO
import time
import os


IMPULS_PIN		= 23	#Pin leading to transitor
SLEEP_TIME		= 20	#Sleept time till next temperatur mesurement
MAX_CPU_TEMP	= 40	#Temperatur cooler starts
STOP_CPU_TEMP	= 35    #Temperatur cooler stops 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def get_cpu_temperature():
	temp = os.popen('vcgencmd measure_temp').readline()
	return float(temp.replace("temp=","").replace("'C\n",""))



def main():

	#Init
	GPIO.setup(IMPULS_PIN, GPIO.OUT)
	GPIO.output(IMPULS_PIN, False)
	 
	while True:
		cpu_temp = get_cpu_temperature()
		print(cpu_temp)
		if cpu_temp >= MAX_CPU_TEMP  :
			GPIO.output(IMPULS_PIN, True)
		if cpu_temp < STOP_CPU_TEMP:
			GPIO.output(IMPULS_PIN, False)
		time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()
	
