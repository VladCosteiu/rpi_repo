import os
import glob
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(12,GPIO.OUT)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

temp_log = open("temp_log.txt", "w")

#base_dir = 'sys/bus/w1/devices/'
#device_folder = base_dir + '28-000008863ad1'
device_file = '/sys/bus/w1/devices/28-000008863ad1/w1_slave'

def read_temp_raw():
	f = open(device_file, 'r')
	lines = f.readlines()
	f.close()
	return lines
	
def read_temp():
	lines = read_temp_raw()
	while lines[0].strip()[-3:] != 'YES':
		time.sleep(0.2)
		lines = read_temp_raw()
	equals_pos = lines[1].find('t=')
	if equals_pos != -1:
		temp_string = lines[1][equals_pos+2:]
		temp_c = float(temp_string) / 1000.0
		return temp_c
		
while True:
	print(read_temp())
	temp_log.writelines(str(read_temp()) + "\r\n")
	#temp_log.close()
	if read_temp() > 25:
		GPIO.output(12,GPIO.HIGH)
	if read_temp() < 25:
		GPIO.output(12,GPIO.LOW)
	time.sleep(1)
