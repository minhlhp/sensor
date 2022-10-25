import tkinter
from tkinter import *
from DisplaySetting import SettingScreen
from DisplayEdit import EditScreen
from DisplayCreate import CreateScreen
import time
from PIL import ImageTk, Image
from random import randint

wido = Tk()
wido.title('MiA')
wido.minsize(450, 400)
wido.maxsize(450, 400)

frame = Frame(wido)
frame.pack()


def On_Click_Setting():
    if SettingScreen.open == False:
        print(SettingScreen.open)
        SettingScreen.open = True
        SettingScreen.displaySetting()


def On_Click_Edit():
    if SettingScreen.open == False:
        print(SettingScreen.open)
        SettingScreen.open = True
        EditScreen.displayedit()


def On_Click_Create():
    if SettingScreen.open == False:
        print(SettingScreen.open)
        SettingScreen.open = True
        CreateScreen.displaycreate()


SettingButton = Button(frame, bg="#7e788c", text="Setting", font=("Time New Roman", 8), command=On_Click_Setting)
SettingButton.grid(column=1, row=0, ipadx=6, ipady=5)
EditButton = Button(frame, bg="#7e788c", text="Edit", font=("Time New Roman", 8), command=On_Click_Edit)
EditButton.grid(column=2, row=0, ipadx=12, ipady=5)
CreateButton = Button(frame, bg="#7e788c", text="Create", font=("Time New Roman", 8), command=On_Click_Create)
CreateButton.grid(column=3, row=0, ipadx=7, ipady=5)
DeleteButton = Button(frame, bg="#7e788c", text="Delete", font=("Time New Roman", 8))
DeleteButton.grid(column=4, row=0, ipadx=15, ipady=5)

Stt = Label(frame, text="Stt", bg="#9de498", font=("Time New Roman", 10))
Stt.grid(column=0, row=1, ipadx=5, ipady=5)
Sensor = Label(frame, text="Sensor", bg="#9de498", font=("Time New Roman", 10))
Sensor.grid(column=1, row=1, ipadx=5, ipady=5)
Device = Label(frame, text="Device", bg="#9de498", font=("Time New Roman", 10))
Device.grid(column=2, row=1, ipadx=5, ipady=5)
Address = Label(frame, text="Adress", bg="#9de498", font=("Time New Roman", 10))
Address.grid(column=3, row=1, ipadx=5, ipady=5)
Location = Label(frame, text="Location", bg="#9de498", font=("Time New Roman", 10))
Location.grid(column=4, row=1, ipadx=10, ipady=5)
Value_Sensor = Label(frame, text="Value", bg="#9de498", font=("Time New Roman", 10))
Value_Sensor.grid(column=5, row=1, ipadx=5, ipady=5)
Unit = Label(frame, text="Unit", bg="#9de498", font=("Time New Roman", 10))
Unit.grid(column=6, row=1, ipadx=5, ipady=5)
Status = Label(frame, text="Status", bg="#9de498", font=("Time New Roman", 10))
Status.grid(column=7, row=1, ipadx=5, ipady=5)

wido.protocol('WM_DELETE_WINDOW', wido.destroy)

wido.mainloop()
