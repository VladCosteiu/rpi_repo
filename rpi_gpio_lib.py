import RPi.GPIO as GPIO
import time
import multiprocessing
import os
import subprocess

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class data:
	port = 0
	timer = 0
	path = 0

def set_port(sent_port):
	data.port = int(sent_port)

def set_timer(sent_timer):
	data.timer = int(sent_timer)

def set_path(sent_path):
	data.path = sent_path
	
		
def on_after_timer():
	GPIO.setup(data.port, GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	time.sleep(data.timer)
	GPIO.output(data.port, GPIO.HIGH)
	
def off_after_timer():
	GPIO.setup(data.port, GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	time.sleep(data.timer)
	GPIO.output(data.port, GPIO.LOW)

def script():
	print data.path
	test = data.path
	print test[24:29]
	import blink

def run_temp_script():
	import temp
	
def run_on_after_timer():
	worker_1 = multiprocessing.Process(name='test1', target=on_after_timer)
	worker_1.start()

def run_off_after_timer():
	worker_2 = multiprocessing.Process(name='test2', target=off_after_timer)
	worker_2.start()

def run_my_script():
	worker_3 = multiprocessing.Process(name='test3', target=script)
	worker_3.start()

def run_temp():
	worker_4 = multiprocessing.Process(name='test4', target=run_temp_script)
	worker_4.start()
