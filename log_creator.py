import datetime
global log_file

log_gpio_1 = "log_gpio_1.txt"
log_gpio_2 = "log_gpio_2.txt"
log_gpio_3 = "log_gpio_3.txt"
log_gpio_4 = "log_gpio_4.txt"
log_gpio_5 = "log_gpio_5.txt"

log_file_name = "log_file.txt"
log_file = open(log_file_name, 'w')

log_file_gpio_1 = open(log_gpio_1, 'w')
log_file_gpio_2 = open(log_gpio_2, 'w')
log_file_gpio_3 = open(log_gpio_3, 'w')
log_file_gpio_4 = open(log_gpio_4, 'w')
log_file_gpio_5 = open(log_gpio_5, 'w')

def log_create():
    log_file.write("===== Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")

def log_write(str):
    log_file.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")

def log_gpio_create():
    log_file_gpio_1.write("===== GPIO 1 Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")
    log_file_gpio_2.write("===== GPIO 2 Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")
    log_file_gpio_3.write("===== GPIO 3 Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")
    log_file_gpio_4.write("===== GPIO 4 Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")
    log_file_gpio_5.write("===== GPIO 5 Log File created: " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "=====\r\n\r\n")

def log_gpio_1_write(str):
    log_file_gpio_1.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")

def log_gpio_2_write(str):
    log_file_gpio_2.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")

def log_gpio_3_write(str):
    log_file_gpio_1.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")

def log_gpio_4_write(str):
    log_file_gpio_1.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")

def log_gpio_5_write(str):
    log_file_gpio_1.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " - " + str + "\r\n")