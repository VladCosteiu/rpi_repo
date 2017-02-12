#!/usr/bin/python
# -*- coding: utf-8 -*-
import tkMessageBox
import Tkinter
from PIL import Image, ImageTk
from Tkinter import Tk, Canvas, Frame, BOTH, NW
from Tkinter import Tk, Frame, Menu, Label

class Config(Frame):
    def __init__(self, test):
        Frame.__init__(self, test)

        self.parent = test
        self.initUI()

    def initUI(self):
        self.parent.title("Config")
        """
        image = Image.open("test.jpg")
        photo = ImageTk.PhotoImage(image)
        label = Label(image=photo)
        label.image = photo # keep a reference!
        label.pack()
        """
        B = Tkinter.Button(config_window, text ="test", command = load)

class Main(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()


    def initUI(self):

        self.parent.title("Main")
        menubar = Menu(self.parent)
        self.parent.config(menu=menubar)

        fileMenu = Menu(menubar) #menu item 1
        configMenu = Menu(menubar) # menu item 2

        #menu item 1
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Exit", command=self.onExit)

        # menu item 2
        menubar.add_cascade(label="Config", menu=configMenu)
        configMenu.add_command(label="Config GPIO", command=config)

    def onExit(self):
        self.quit()

def load():
    tkMessageBox.showinfo( "Hello Python", "Hello World")

def main():
    root = Tk()
    root.geometry("200x200")
    app = Main(root)
    root.mainloop()

def config():
    config_window = Tk()
    config_window.geometry("500x600")
    conf = Config(config_window)
    B = Tkinter.Button(config_window, text ="test", command = load)
    B.pack()
    config_window.mainloop()


def unimplementedCallBack():
        tkMessageBox.showinfo("unimplemented", "Unimplemented !")

if __name__ == '__main__':
    main()