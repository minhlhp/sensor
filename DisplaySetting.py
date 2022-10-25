import tkinter
from tkinter import *
from PIL import ImageTk, Image
from random import randint

class SettingScreen:
    widoSet = None
    open = False

    @classmethod
    def displaySetting(cls):
        # cls.widoSet = Tk()
        cls.widoSet = Toplevel()
        cls.widoSet.minsize(310,200)
        cls.widoSet.maxsize(310,200)
        frame1 = Frame(cls.widoSet)
        frame1.pack()
        portLabel = Label(frame1, text="Chọn Port:")
        portLabel.grid(column=0, row=0, pady=2)
        portlistbox = Listbox(frame1, selectmode=SINGLE, exportselection=False)
        portlistbox.grid(column=0, row=1, pady=2)
        BaudLabel = Label(frame1, text="Baudrate:")
        BaudLabel.grid(column=1, row=0, pady=2)
        baudlistbox = Listbox(frame1, selectmode=SINGLE, exportselection=False)
        baudlistbox.grid(column=1, row=1, pady=2)
        listport = ["Port1", "Port2", "Port3", "Port4"]
        listbaud = ["2400", "4800", "9600", "14400", "19200", "115200"]
        for i in listport:
            portlistbox.insert(END, i)
        for i in listbaud:
            baudlistbox.insert(END, i)
        buttonSave = Button(frame1, text="Connect")
        buttonSave.grid(column=2, row=1, pady=2)
        cls.widoSet.protocol('WM_DELETE_WINDOW', cls.on_close)
        cls.widoSet.mainloop()

    @classmethod
    def on_close(cls):
        print('close')
        cls.widoSet.destroy()
        cls.open = False
