"""
    #USEFULL LATER, maybe
    image = Image.open("test.jpg")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()
"""

"""
    s = StringVar()
    s.set('a')
    om = OptionMenu(config_window, s, 'a', 'b', 'c', 'd')
    om.pack()
"""

"""
    # get_data_from_conf():
    # old stuff, bad stuff :)
    while(ct < 25): # magic number
        line = conf.readline()
        if(line.startswith("type=")):
            print "i found type"
            print line[5:]
            if line[5:] == "0\n":
                print "create interface for type=0 -> input"
                line = conf.readline() #read 2 lines to get to label, very stupid implementation, should read again all file
                line = conf.readline()
                if line.startswith("label="):
                    print "am gasit label"
                    print line[6:]
                    label_line = line[6:]
                    next_label = 10
                    output_label = Label(main_window, text=label_line)
                    output_label.place(x=20, y=next_label+20)
            if line[5:1] == "1\n":
                print "create interface for type=0 -> output"
        ct = ct + 1
"""
"""
    ct_input = 0
    ct = 0
    while(ct<5):
        if(gpio_array[ct].gpio_type == "1\n"):
            print "input"
            ct_input = ct_input + 1
        ct = ct + 1

    ct = 0
    pos_y = 15

    while(ct<ct_input):
        ct_label = Label(main_window, text=ct)
        test_button = Button(main_window, text="Test", width=10, command=do_something)

        test_button.place(x=30, y=pos_y)
        ct_label.place(x=10, y=pos_y)


        pos_y = pos_y + 30
        ct = ct + 1
"""
"""
    print "====================="
    print gpio_array[0].gpio_type[0]
    print gpio_array[1].gpio_type[0]
    print gpio_array[2].gpio_type[0]
    print gpio_array[3].gpio_type[0]
    print gpio_array[4].gpio_type[0]
    print "====================="
    print gpio_array[0].gpio_label[0]
    print gpio_array[0].gpio_label[1]
    print gpio_array[0].gpio_label
"""