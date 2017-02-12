# libs
import os
import log_creator
import Tkinter
import tkMessageBox
from Tkinter import Tk, Frame, Menu, Label
#from PIL import Image, ImageTk
from Tkinter import *
import RPi.GPIO as GPIO
import time
import rpi_gpio_lib
import subprocess
from tkFileDialog   import askopenfilename

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

class Gpio_Config:
    gpio_type = 0
    gpio_port = "empty"
    gpio_label = "empty"
    
class timers:
    timer_1 = 0
    timer_2 = 0
    timer_3 = 0
    val = 0

timer_set = 0
    
gpio_array = []
for i in range(5):
    gpio_array.append(Gpio_Config())

main_window = Tkinter.Tk() # ai voie doar o instanta de Tk(), restul trebe sa fie Toplevel
main_window.title("RPI")
main_window.geometry("500x700")

# gui
def gui_main_window():
    #main_window = Tkinter.Tk() # ai voie doar o instanta de Tk(), restul trebe sa fie Toplevel
    #main_window.title("RPI GPIO Manager")
    #main_window.geometry("200x200")

    menu_bar = Menu(main_window)
    main_window.config(menu=menu_bar)

    file_menu = Menu(menu_bar)  # menu item 1
    config_menu = Menu(menu_bar)  # menu item 2
    settings_menu = Menu(menu_bar) # menu item 3

    # menu item 1
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Load Configuration", command=load_configuration)
    file_menu.add_command(label="Exit", command=exit_app)

    # menu item 2
    menu_bar.add_cascade(label="Configure", menu=config_menu)
    config_menu.add_command(label="GPIO Layout", command=gui_gpio_layout)
    config_menu.add_command(label="Configure GPIO", command=gui_config_window)
    config_menu.add_command(label="Configure Timers", command=gui_timers_window)

    # menu item 3
    menu_bar.add_cascade(label="Settings", menu=settings_menu)
    settings_menu.add_command(label="Options", command=gui_options_window)

    main_window.mainloop()
    log_creator.log_write("Main Window opened")

def exit_app():
    exit(0)

def gui_gpio_layout():
    gpio_layout_frame = Tkinter.Toplevel() # ai voie doar o instanta de Tk()
    gpio_layout_frame.title("GPIO Layout")
    gpio_layout_frame.geometry("400x500")

    gpio_1_label = Tkinter.Label(gpio_layout_frame, text="3V3 _____________________ 1")
    gpio_2_label = Tkinter.Label(gpio_layout_frame, text="2 _________________ 5V")
    gpio_3_label = Tkinter.Label(gpio_layout_frame, text="GPIO00 _________________ 3")
    gpio_4_label = Tkinter.Label(gpio_layout_frame, text="4 _________________ 5V")
    gpio_5_label = Tkinter.Label(gpio_layout_frame, text="GPIO01 _________________ 5")
    gpio_6_label = Tkinter.Label(gpio_layout_frame, text="6 _________________ GROUND")
    gpio_7_label = Tkinter.Label(gpio_layout_frame, text="GPIO04 _________________ 7")
    gpio_8_label = Tkinter.Label(gpio_layout_frame, text="8 _________________ GPIO14")
    gpio_9_label = Tkinter.Label(gpio_layout_frame, text="GROUND ________________ 9")
    gpio_10_label = Tkinter.Label(gpio_layout_frame, text="10 ________________ GPIO15")
    gpio_11_label = Tkinter.Label(gpio_layout_frame, text="GPIO17 ________________ 11")
    gpio_12_label = Tkinter.Label(gpio_layout_frame, text="12 ________________ GPIO18")
    gpio_13_label = Tkinter.Label(gpio_layout_frame, text="GPIO21 ________________ 13")
    gpio_14_label = Tkinter.Label(gpio_layout_frame, text="14 ________________ GROUND")
    gpio_15_label = Tkinter.Label(gpio_layout_frame, text="GPI022 ________________ 15")
    gpio_16_label = Tkinter.Label(gpio_layout_frame, text="16 ________________ GPIO23")
    gpio_17_label = Tkinter.Label(gpio_layout_frame, text="3V3 ____________________ 17")
    gpio_18_label = Tkinter.Label(gpio_layout_frame, text="18 ________________ GPIO24")
    gpio_19_label = Tkinter.Label(gpio_layout_frame, text="GPIO10 ________________ 19")
    gpio_20_label = Tkinter.Label(gpio_layout_frame, text="20 ________________ GROUND")
    gpio_21_label = Tkinter.Label(gpio_layout_frame, text="GPIO09 ________________ 21")
    gpio_22_label = Tkinter.Label(gpio_layout_frame, text="22 ________________ GPIO25")
    gpio_23_label = Tkinter.Label(gpio_layout_frame, text="GPIO11 ________________ 23")
    gpio_24_label = Tkinter.Label(gpio_layout_frame, text="24 ________________ GPIO08")
    gpio_25_label = Tkinter.Label(gpio_layout_frame, text="GROUND ______________ 25")
    gpio_26_label = Tkinter.Label(gpio_layout_frame, text="26 ________________ GPIO07")

    gpio_1_label.place(x=20, y=20)
    gpio_2_label.place(x=200, y=20)
    gpio_3_label.place(x=20, y=50)
    gpio_4_label.place(x=200, y=50)
    gpio_5_label.place(x=20, y=80)
    gpio_6_label.place(x=200, y=80)
    gpio_7_label.place(x=20, y=110)
    gpio_8_label.place(x=200, y=110)
    gpio_9_label.place(x=20, y=140)
    gpio_10_label.place(x=200, y=140)
    gpio_11_label.place(x=20, y=170)
    gpio_12_label.place(x=200, y=170)
    gpio_13_label.place(x=20, y=200)
    gpio_14_label.place(x=200, y=200)
    gpio_15_label.place(x=20, y=230)
    gpio_16_label.place(x=200, y=230)
    gpio_17_label.place(x=20, y=260)
    gpio_18_label.place(x=200, y=260)
    gpio_19_label.place(x=20, y=290)
    gpio_20_label.place(x=200, y=290)
    gpio_21_label.place(x=20, y=320)
    gpio_22_label.place(x=200, y=320)
    gpio_23_label.place(x=20, y=350)
    gpio_24_label.place(x=200, y=350)
    gpio_25_label.place(x=20, y=380)
    gpio_26_label.place(x=200, y=380)
    
    
def gui_timers_window():
    timers_window = Tkinter.Toplevel() # ai voie doar o instanta de Tk()
    timers_window.title("Timers")
    timers_window.geometry("400x250")

    load_timers_frame(timers_window)
    log_creator.log_write("Configure window opened")
    
def gui_config_window():
    config_window = Tkinter.Toplevel() # ai voie doar o instanta de Tk()
    config_window.title("Configuration")
    config_window.geometry("500x350")

    load_config_frame(config_window)
    log_creator.log_write("Configure window opened")

def gui_options_window():
    option_window = Tkinter.Toplevel()
    option_window.title("Options")
    option_window.geometry("600x200")

    load_options_frame(option_window)
    log_creator.log_write("Options window opened")

def load_timers_frame(timers_window):
    frame = Tkinter.Frame(timers_window)
    frame.pack(fill='both', expand='yes')
    
    timer_1_label = Tkinter.Label(frame, text="Timer 1:")
    timer_2_label = Tkinter.Label(frame, text="Timer 2:")
    timer_3_label = Tkinter.Label(frame, text="Timer 3:")
	
    timer_1_label.place(x=20, y=20)
    timer_2_label.place(x=20, y=60)
    timer_3_label.place(x=20, y=100)	   
    t1 = StringVar()
    t2 = StringVar()
    t3 = StringVar()
    
    timer_1_textbox = Entry(frame , textvariable=t1)
    timer_2_textbox = Entry(frame , textvariable=t2)
    timer_3_textbox = Entry(frame , textvariable=t3)
    
    timer_1_textbox.place(x=80, y=20)
    timer_2_textbox.place(x=80, y=60)
    timer_3_textbox.place(x=80, y=100)
    
    def save_timers():
		timers = open("timers.txt", "wb")
		timers.write("timer_1 =" + str(t1.get()) + "\r\n")
		timers.write("timer_2 =" + str(t2.get()) + "\r\n")
		timers.write("timer_3 =" + str(t3.get()) + "\r\n")
		timers.close()
		tkMessageBox.showinfo("save", "Saved Timers to timers.txt")
		log_creator.log_write("Saved new timers values to timers.txt")
        
    save_timers = Button(frame, text="Save Timers", width=15, command=save_timers)
    save_timers.place(x=200, y=200)     
	
def save_conf():
	timers = open("timers_test.txt", "wb")
	timers.write(timer_1_textbox)
	
def load_config_frame(config_window):
    frame = Tkinter.Frame(config_window)
    frame.pack(fill='both', expand='yes')

    gpio1_label = Tkinter.Label(frame, text="GPIO 1:")
    gpio2_label = Tkinter.Label(frame, text="GPIO 2:")
    gpio3_label = Tkinter.Label(frame, text="GPIO 3:")
    gpio4_label = Tkinter.Label(frame, text="GPIO 4:")
    gpio5_label = Tkinter.Label(frame, text="GPIO 5:")

    var_gpio1 = IntVar() # 0=input ; 1=output ; 2 = invalid
    var_gpio2 = IntVar()
    var_gpio3 = IntVar()
    var_gpio4 = IntVar()
    var_gpio5 = IntVar()

    gpio1_radio_1 = Tkinter.Radiobutton(config_window, text="input", value=0, variable=var_gpio1)
    gpio1_radio_2 = Tkinter.Radiobutton(config_window, text="output", value=1, variable=var_gpio1)
    gpio2_radio_1 = Tkinter.Radiobutton(config_window, text="input", value=0, variable=var_gpio2)
    gpio2_radio_2 = Tkinter.Radiobutton(config_window, text="output", value=1, variable=var_gpio2)
    gpio3_radio_1 = Tkinter.Radiobutton(config_window, text="input", value=0, variable=var_gpio3)
    gpio3_radio_2 = Tkinter.Radiobutton(config_window, text="output", value=1, variable=var_gpio3)
    gpio4_radio_1 = Tkinter.Radiobutton(config_window, text="input", value=0, variable=var_gpio4)
    gpio4_radio_2 = Tkinter.Radiobutton(config_window, text="output", value=1, variable=var_gpio4)
    gpio5_radio_1 = Tkinter.Radiobutton(config_window, text="input", value=0, variable=var_gpio5)
    gpio5_radio_2 = Tkinter.Radiobutton(config_window, text="output", value=1, variable=var_gpio5)

    gpio1_label.place(x=20, y=20)
    gpio2_label.place(x=20, y=80)
    gpio3_label.place(x=20, y=140)
    gpio4_label.place(x=20, y=200)
    gpio5_label.place(x=20, y=260)

    gpio1_radio_1.place(x=70, y=20)
    gpio1_radio_2.place(x=70, y=40)
    gpio2_radio_1.place(x=70, y=80)
    gpio2_radio_2.place(x=70, y=100)
    gpio3_radio_1.place(x=70, y=140)
    gpio3_radio_2.place(x=70, y=160)
    gpio4_radio_1.place(x=70, y=200)
    gpio4_radio_2.place(x=70, y=220)
    gpio5_radio_1.place(x=70, y=260)
    gpio5_radio_2.place(x=70, y=280)

    optionList = ('3', '5', '7', '8', '10', '11', '12', '13', '15', '16', '18', '19', '21', '22', '23', '24', '26')
    gpio1_op = StringVar()
    gpio1_op.set(optionList[0])
    gpio2_op = StringVar()
    gpio2_op.set(optionList[1])
    gpio3_op = StringVar()
    gpio3_op.set(optionList[2])
    gpio4_op = StringVar()
    gpio4_op.set(optionList[3])
    gpio5_op = StringVar()
    gpio5_op.set(optionList[4])

    om_gpio1 = OptionMenu(config_window, gpio1_op, *optionList)
    om_gpio2 = OptionMenu(config_window, gpio2_op, *optionList)
    om_gpio3 = OptionMenu(config_window, gpio3_op, *optionList)
    om_gpio4 = OptionMenu(config_window, gpio4_op, *optionList)
    om_gpio5 = OptionMenu(config_window, gpio5_op, *optionList)

    om_gpio1.place(x=150, y=20)
    om_gpio2.place(x=150, y=80)
    om_gpio3.place(x=150, y=140)
    om_gpio4.place(x=150, y=200)
    om_gpio5.place(x=150, y=260)

    label_port = Label(frame, text="Label/Name:")
    label_port.place(x=290, y=0)
    
    label_actuall_port = Label(frame, text="Port:")
    label_actuall_port.place(x=130, y=0)

    gpio_1_text_label = StringVar()
    gpio_1_label_textbox = Entry(frame, textvariable=gpio_1_text_label)
    gpio_1_label_textbox.place(x=250, y=20)
    gpio_2_text_label = StringVar()
    gpio_2_label_textbox = Entry(frame, textvariable=gpio_2_text_label)
    gpio_2_label_textbox.place(x=250, y=80)
    gpio_3_text_label = StringVar()
    gpio_3_label_textbox = Entry(frame, textvariable=gpio_3_text_label)
    gpio_3_label_textbox.place(x=250, y=140)
    gpio_4_text_label = StringVar()
    gpio_4_label_textbox = Entry(frame, textvariable=gpio_4_text_label)
    gpio_4_label_textbox.place(x=250, y=200)
    gpio_5_text_label = StringVar()
    gpio_5_label_textbox = Entry(frame, textvariable=gpio_5_text_label)
    gpio_5_label_textbox.place(x=250, y=260)

    def save_conf():
        conf = open("conf.txt", "wb")
        conf.write("===== GPIO 1 =====\r\n")
        conf.write("type=" + str(var_gpio1.get()) + "\r\n")
        conf.write("port=" + str(gpio1_op.get()) + "\r\n")
        conf.write("label=" + str(gpio_1_text_label.get()) + "\r\n")
        conf.write("==================\r\n")
        conf.write("===== GPIO 2 =====\r\n")
        conf.write("type=" + str(var_gpio2.get()) + "\r\n")
        conf.write("port=" + str(gpio2_op.get()) + "\r\n")
        conf.write("label=" + str(gpio_2_text_label.get()) + "\r\n")
        conf.write("==================\r\n")
        conf.write("===== GPIO 3 =====\r\n")
        conf.write("type=" + str(var_gpio3.get()) + "\r\n")
        conf.write("port=" + str(gpio3_op.get()) + "\r\n")
        conf.write("label=" + str(gpio_3_text_label.get()) + "\r\n")
        conf.write("==================\r\n")
        conf.write("===== GPIO 4 =====\r\n")
        conf.write("type=" + str(var_gpio4.get()) + "\r\n")
        conf.write("port=" + str(gpio4_op.get()) + "\r\n")
        conf.write("label=" + str(gpio_4_text_label.get()) + "\r\n")
        conf.write("==================\r\n")
        conf.write("===== GPIO 5 =====\r\n")
        conf.write("type=" + str(var_gpio5.get()) + "\r\n")
        conf.write("port=" + str(gpio5_op.get()) + "\r\n")
        conf.write("label=" + str(gpio_5_text_label.get()) + "\r\n")
        conf.write("==================\r\n")
        conf.close()
        tkMessageBox.showinfo("save", "Saved Configuration to conf.txt")
        log_creator.log_write("Saved new configuration to conf.txt")

    save_button = Button(frame, text="Save Config", width=10, command=save_conf)
    save_button.place(x=350, y=300)

def load_configuration():
    log_creator.log_write("Load configuration conf.txt")
    get_data_from_conf()
    log_creator.log_write("Loaded Configuration conf.txt")

def load_options_frame(option_window):
    frame = Tkinter.Frame(option_window)
    frame.pack(fill='both', expand='yes')

    change_config_button = Button(frame, text="Change Config File", width=15, command=unimplementedCallBack)
    change_config_button.place(x=20, y=20)
    change_config_label = Tkinter.Label(frame, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\conf.txt")
    change_config_label.place(x=175, y=20)

    change_log_button = Button(frame, text="Change Log File", width=15, command=unimplementedCallBack)
    change_log_button.place(x=20, y=60)
    change_log_label = Tkinter.Label(frame, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")
    change_log_label.place(x=175, y=60)

    check_config_button = Button(frame, text="Check Log File !", width=15, command=check_conf)
    check_config_button.place(x=20, y=150)

def check_conf():
    if open("conf.txt", "wb") != 0:
        tkMessageBox.showinfo("unimplemented", "Config File Status = OK !")
    else:
        tkMessageBox.showinfo("unimplemented", "Config File Status = NOK !")

def get_data_from_conf():
    conf = open("conf.txt", "r")
    ct = 0
    gpio_type_ct = 0
    gpio_port_ct = 0
    gpio_label_ct = 0

    while(ct < 25): # magic number
        line = conf.readline()
        if(line.startswith("type=")):
            gpio_array[gpio_type_ct].gpio_type = line[5:]  # get type -> 0-input 1-output
            print gpio_array[gpio_type_ct].gpio_type
            gpio_type_ct = gpio_type_ct + 1

        if(line.startswith("port=")):
            gpio_array[gpio_port_ct].gpio_port = line[5:]  # get port
            #print gpio_array[gpio_port_ct].gpio_port
            gpio_port_ct = gpio_port_ct + 1

        if(line.startswith("label=")):
            gpio_array[gpio_label_ct].gpio_label = line[6:]  # get label
            #print gpio_array[gpio_label_ct].gpio_label
            gpio_label_ct = gpio_label_ct + 1
        ct = ct + 1
	
	get_data_from_timers()
    create_config_gui()

def get_data_from_timers():
    conf = open("timers.txt", "r")
    ct = 0
    timers_ct = 0
	
    while(ct < 25): # magic number
        line = conf.readline()
        if(line.startswith("timer_1 =")):
            timers.timer_1 = line[9:]  # get timer_1

        if(line.startswith("timer_2 =")):
            timers.timer_2 = line[9:]  # get timer_2

        if(line.startswith("timer_3 =")):
            timers.timer_3 = line[9:]  # get timer_3
        ct = ct + 1
        
def create_config_gui():
    input_label = Label(main_window, text="INPUTS")
    input_label.place(x=0, y=0)

    log_creator.log_write("Creating Configure Inputs panel ...")

    generate_inputs()

    output_label = Label(main_window, text="OUTPUTS")
    output_label.place(x=0, y=300)

    generate_outputs()

    log_creator.log_write("Finished generating Config panel")

def generate_inputs():
    if(gpio_array[0].gpio_type[0] == "0"):
        gpio_1_label = Label(main_window, text= gpio_array[0].gpio_label)
        gpio_1_label.place(x=30, y=30)

        gpio_input_button_1 = Button(main_window, text="Get Data", width=10, command=get_store_input_gpio_5)
        gpio_input_button_1.place(x=50, y=50)

        gpio_1_label_store = Label(main_window, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\temp_log.txt")
        gpio_1_label_store.place(x=150, y=50)

        log_creator.log_write("Finished creating input GPIO 1")

    if(gpio_array[1].gpio_type[0] == "0"):
        gpio_2_label = Label(main_window, text=gpio_array[1].gpio_label)
        gpio_2_label.place(x=30, y=80)

        gpio_input_button_2 = Button(main_window, text="Get Data", width=10, command=get_store_input_gpio_5)
        gpio_input_button_2.place(x=50, y=100)

        gpio_2_label_store = Label(main_window, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\temp_log.txt")
        gpio_2_label_store.place(x=150, y=100)

        log_creator.log_write("Finished creating input GPIO 2")

    if(gpio_array[2].gpio_type[0] == "0"):
        gpio_3_label = Label(main_window, text=gpio_array[2].gpio_label)
        gpio_3_label.place(x=30, y=130)

        gpio_input_button_3 = Button(main_window, text="Get Data", width=10, command=get_store_input_gpio_5)
        gpio_input_button_3.place(x=50, y=150)

        gpio_3_label_store = Label(main_window, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\temp_log.txt")
        gpio_3_label_store.place(x=150, y=150)

        log_creator.log_write("Finished creating input GPIO 3")

    if(gpio_array[3].gpio_type[0] == "0"):
        gpio_4_label = Label(main_window, text=gpio_array[3].gpio_label)
        gpio_4_label.place(x=20, y=20)

        gpio_input_button_4 = Button(main_window, text="Get Data", width=10, command=get_store_input_gpio_5)
        gpio_input_button_4.place(x=30, y=40)

        #gpio_4_label_store = Label(main_window, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")
        #gpio_4_label_store.place(x=150, y=30)

        log_creator.log_write("Finished creating input GPIO 4")

    if(gpio_array[4].gpio_type[0] == "0"):
        gpio_5_label = Label(main_window, text=gpio_array[4].gpio_label)
        gpio_5_label.place(x=30, y=230)

        gpio_input_button_5 = Button(main_window, text="Get Data", width=10, command=get_store_input_gpio_5)
        gpio_input_button_5.place(x=50, y=250)

        gpio_5_label_store = Label(main_window, text="D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\temp_log.txt")
        gpio_5_label_store.place(x=150, y=250)

        log_creator.log_write("Finished creating input GPIO 5")

    log_creator.log_write("Finished generating Inputs panel")

def generate_outputs():
    if(gpio_array[0].gpio_type[0] == "1"):
        gpio_1_label = Label(main_window, text= gpio_array[0].gpio_label)
        gpio_1_label.place(x=30, y=330)

        gpio_output_1_on = Button(main_window, text="ON", width=3, command=gpio_output_1_on_command)
        gpio_output_1_on.place(x=50, y=350)
        optionList = ('Timer_1', 'Timer_2', 'Timer_3')
        timers_op = StringVar()
        timers_op.set(optionList[0])
        om_gpio1 = OptionMenu(main_window, timers_op, *optionList)
        
        om_gpio1.place(x=320, y=350)
        def set_timer_op():
			timers.val = timers_op.get()
			tkMessageBox.showinfo("Timer Dialog", timers.val + " was set !")
        set_timers_button = Button(main_window, text="Set", width=3, command=set_timer_op)
        set_timers_button.place(x=400, y=350)
        
        gpio_output_1_stay_awake = Button(main_window, text="ON after", width=6, command=gpio_output_1_on_after_timer)
        gpio_output_1_stay_awake.place(x=170, y=350)
        gpio_output_1_off_after = Button(main_window, text="OFF after", width=6, command=gpio_output_1_off_after_timer)
        gpio_output_1_off_after.place(x=240, y=350)
          
        gpio_output_1_off = Button(main_window, text="OFF", width=3, command=gpio_output_1_off_command)
        gpio_output_1_off.place(x=100, y=350)
        gpio_output_1_script = Button(main_window, text="Run Script", width=5, command=gpio_output_script)
        gpio_output_1_script.place(x=300, y=450)
        
        log_creator.log_write("Finished creating output GPIO 1")

    if(gpio_array[1].gpio_type[0] == "1"):
        gpio_2_label = Label(main_window, text=gpio_array[1].gpio_label)
        gpio_2_label.place(x=30, y=380)

        gpio_input_2_on = Button(main_window, text="ON", width=10, command=gpio_output_2_on_command)
        gpio_input_2_on.place(x=50, y=400)

        gpio_input_2_off = Button(main_window, text="OFF", width=10, command=gpio_output_2_off_command)
        gpio_input_2_off.place(x=150, y=400)

        log_creator.log_write("Finished creating output GPIO 2")

    if(gpio_array[2].gpio_type[0] == "1"):
        gpio_3_label = Label(main_window, text=gpio_array[2].gpio_label)
        gpio_3_label.place(x=30, y=430)

        gpio_input_3_on = Button(main_window, text="ON", width=10, command=gpio_output_3_on_command)
        gpio_input_3_on.place(x=50, y=450)

        gpio_input_3_off = Button(main_window, text="OFF", width=10, command=gpio_output_3_off_command)
        gpio_input_3_off.place(x=150, y=450)

        log_creator.log_write("Finished creating output GPIO 3")

    if(gpio_array[3].gpio_type[0] == "1"):
        gpio_4_label = Label(main_window, text=gpio_array[3].gpio_label)
        gpio_4_label.place(x=30, y=480)

        gpio_input_4_on = Button(main_window, text="ON", width=10, command=gpio_output_4_on_command)
        gpio_input_4_on.place(x=50, y=500)

        gpio_input_4_off = Button(main_window, text="OFF", width=10, command=gpio_output_4_off_command)
        gpio_input_4_off.place(x=150, y=500)

        log_creator.log_write("Finished creating output GPIO 4")

    if(gpio_array[4].gpio_type[0] == "1"):
        gpio_5_label = Label(main_window, text=gpio_array[4].gpio_label)
        gpio_5_label.place(x=30, y=530)

        gpio_input_5_on = Button(main_window, text="ON", width=10, command=gpio_output_5_on_command)
        gpio_input_5_on.place(x=50, y=550)

        gpio_input_5_off = Button(main_window, text="OFF", width=10, command=gpio_output_5_off_command)
        gpio_input_5_off.place(x=150, y=550)

        log_creator.log_write("Finished creating output GPIO 5")

    log_creator.log_write("Finished generating Outputs panel")

def gpio_output_1_on_command():
	GPIO.setup(int(gpio_array[0].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[0].gpio_port), GPIO.HIGH)
	#rpi_gpio_lib.run()
	#subprocess.rpi_gpio_lib.run()
	#subprocess.call("/home/pi/dizertatie/app/rpi_gpio_lib.py", shell=True)
	#rpi_gpio_lib.run(int(gpio_array[0].gpio_port), 15)
	
	#print type(gpio_array[0].gpio_port)
	#print int(gpio_array[0].gpio_port)
	#print type(int(gpio_array[0].gpio_port))

	
	message =  "GPIO 1 -> ___ " + gpio_array[0].gpio_label + " ___ ON ! "
	log_creator.log_write(message)

def gpio_output_1_on_after_timer():
	if(timers.val == "Timer_1"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "ON after timer: " + timers.timer_1 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_1) # timer from timers.txt
		rpi_gpio_lib.run_on_after_timer()
		
	if(timers.val == "Timer_2"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "ON after timer: " + timers.timer_2 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_2) # timer from timers.txt
		rpi_gpio_lib.run_on_after_timer()
	
	if(timers.val == "Timer_3"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "ON after timer: " + timers.timer_3 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_3) # timer from timers.txt
		rpi_gpio_lib.run_on_after_timer()
			
	message =  "GPIO 1 -> ___ " + gpio_array[0].gpio_label + " ___ ON ! "
	log_creator.log_write(message)


def gpio_output_1_off_after_timer():
	if(timers.val == "Timer_1"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "OFF after timer: " + timers.timer_1 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_1) # timer from timers.txt
		rpi_gpio_lib.run_off_after_timer()
	
	if(timers.val == "Timer_2"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "OFF after timer: " + timers.timer_2 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_2) # timer from timers.txt
		rpi_gpio_lib.run_off_after_timer()
		
	if(timers.val == "Timer_3"):
		tkMessageBox.showinfo("unimplemented", "GPIO: " + gpio_array[0].gpio_label + "Port: " + gpio_array[0].gpio_port + "OFF after timer: " + timers.timer_3 + "(seconds)")
		rpi_gpio_lib.set_port(gpio_array[0].gpio_port)
		rpi_gpio_lib.set_timer(timers.timer_3) # timer from timers.txt
		rpi_gpio_lib.run_off_after_timer()
		
	message =  "GPIO 1 -> ___ " + gpio_array[0].gpio_label + " ___ ON ! "
	log_creator.log_write(message)
	
def gpio_output_script():
	name= askopenfilename() 
	rpi_gpio_lib.set_path(name)
	rpi_gpio_lib.run_my_script()
	
	message =  "Loaded " + name + " script"
	log_creator.log_write(message)
		
def gpio_output_1_off_command():
	GPIO.setup(int(gpio_array[0].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[0].gpio_port), GPIO.LOW)
	
	message =  "GPIO 1 -> ___ " + gpio_array[0].gpio_label + " ___ OFF ! "
	log_creator.log_write(message)

def gpio_output_2_on_command():
	GPIO.setup(int(gpio_array[1].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[1].gpio_port), GPIO.HIGH)
	
	message =  "GPIO 2 -> ___ " + gpio_array[1].gpio_label + " ___ ON ! "
	log_creator.log_write(message)

def gpio_output_2_off_command():
	GPIO.setup(int(gpio_array[1].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[1].gpio_port), GPIO.LOW)
	
	message =  "GPIO 2 -> ___ " + gpio_array[1].gpio_label + " ___ OFF ! "
	log_creator.log_write(message)

def gpio_output_3_on_command():
	GPIO.setup(int(gpio_array[2].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[2].gpio_port), GPIO.HIGH)
	
	message =  "GPIO 3 -> ___ " + gpio_array[2].gpio_label + " ___ ON ! "
	log_creator.log_write(message)

def gpio_output_3_off_command():
	GPIO.setup(int(gpio_array[2].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[2].gpio_port), GPIO.LOW)
	
	message =  "GPIO 3 -> ___ " + gpio_array[2].gpio_label + " ___ OFF ! "
	log_creator.log_write(message)

def gpio_output_4_on_command():
	GPIO.setup(int(gpio_array[3].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[3].gpio_port), GPIO.HIGH)
	
	message =  "GPIO 4 -> ___ " + gpio_array[3].gpio_label + " ___ ON ! "
	log_creator.log_write(message)

def gpio_output_4_off_command():
	GPIO.setup(int(gpio_array[3].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[3].gpio_port), GPIO.LOW)
	
	message =  "GPIO 4 -> ___ " + gpio_array[3].gpio_label + " ___ OFF ! "
	log_creator.log_write(message)

def gpio_output_5_on_command():
	GPIO.setup(int(gpio_array[4].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[4].gpio_port), GPIO.HIGH)
	
	message =  "GPIO 5 -> ___ " + gpio_array[4].gpio_label + " ___ ON ! "
	log_creator.log_write(message)

def gpio_output_5_off_command():
	GPIO.setup(int(gpio_array[4].gpio_port), GPIO.OUT) # must be int (string not allowed)(comes as string when reading from conf file)
	GPIO.output(int(gpio_array[4].gpio_port), GPIO.LOW)
	
	message =  "GPIO 5 -> ___ " + gpio_array[4].gpio_label + " ___ OFF ! "
	log_creator.log_write(message)

def get_store_input_gpio_1():
    # call gpio function that gets data from selected GPIO 1
    tkMessageBox.showinfo("unimplemented", "Getting data from GPIO:\n\n" + gpio_array[0].gpio_label + "\nand storing it to: D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")

def get_store_input_gpio_2():
    # call gpio function that gets data from selected GPIO 2
    tkMessageBox.showinfo("unimplemented", "Getting data from GPIO:\n\n" + gpio_array[1].gpio_label + "\nand storing it to: D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")

def get_store_input_gpio_3():
    # call gpio function that gets data from selected GPIO 3
    tkMessageBox.showinfo("unimplemented", "Getting data from GPIO:\n\n" + gpio_array[2].gpio_label + "\nand storing it to: D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")

def get_store_input_gpio_4():
    # call gpio function that gets data from selected GPIO 4
    tkMessageBox.showinfo("unimplemented", "Getting data from GPIO:\n\n" + gpio_array[3].gpio_label + "\nand storing it to: D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\log.txt")

def get_store_input_gpio_5():
    # call gpio function that gets data from selected GPIO 5
    tkMessageBox.showinfo("unimplemented", "Getting data from GPIO:\n\n" + gpio_array[4].gpio_label + "\nand storing it to: D:\\USERDATA\\E4COSVL\\Personal\\Dizertatie\\app\\temp_log.txt")
    rpi_gpio_lib.run_temp()

def unimplementedCallBack():
    tkMessageBox.showinfo("unimplemented", "Unimplemented !")


# start gui
gui_main_window()
log_creator.log_create()
