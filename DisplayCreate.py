import tkinter
from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import ImageTk, Image
from random import randint
from DisplaySetting import SettingScreen


class CreateScreen:
    widoCreate = None
    SettingScreen.open = False
    stt_entry = None
    sensor_entry = None
    device_entry = None
    address_entry = None
    low_range_entry = None
    high_range_entry = None
    unit_entry = None
    location_entry = None
    signal_entry = None



    @classmethod
    def select_signal(cls, event):
        cls.signal_entry = cls.signal_drop.get()
        print(type(cls.signal_entry))

    @classmethod
    def displaycreate(cls):
        # cls.widoEdit = Tk()
        cls.widoCreate = Toplevel()
        cls.widoCreate.minsize(310, 200)
        cls.widoCreate.maxsize(310, 200)

        frame1 = Frame(cls.widoCreate)
        frame1.pack()
        # stt = Label(frame1, text="Stt:")
        # stt.grid(column=0, row=0, pady=2, sticky=W)
        # cls.stt_entry = Entry(frame1, width=10)
        # cls.stt_entry.grid(column=1, row=0, pady=2)

        sensor = Label(frame1, text="Sensor:")
        sensor.grid(column=2, row=0, pady=2, sticky=W)
        cls.sensor_entry = Entry(frame1, width=10)
        cls.sensor_entry.grid(column=3, row=0, pady=2)

        device = Label(frame1, text="Device:")
        device.grid(column=0, row=1, pady=2, sticky=W)
        cls.device_entry = Entry(frame1, width=10)
        cls.device_entry.grid(column=1, row=1, pady=2)

        address = Label(frame1, text="Address:")
        address.grid(column=2, row=1, pady=2, sticky=W)
        cls.address_entry = Entry(frame1, width=10)
        cls.address_entry.grid(column=3, row=1, pady=2)

        Range = Label(frame1, text="Range:")
        Range.grid(column=0, row=2, pady=2, sticky=W)
        cls.low_range_entry = Entry(frame1, width=10)
        cls.low_range_entry.grid(column=1, row=2, pady=2)
        gach = Label(frame1, text="-")
        gach.grid(column=2, row=2, pady=2)
        cls.high_range_entry = Entry(frame1, width=10)
        cls.high_range_entry.grid(column=3, row=2, pady=2)

        unit = Label(frame1, text="Unit:")
        unit.grid(column=0, row=3, pady=2, sticky=W)
        cls.unit_entry = Entry(frame1, width=10)
        cls.unit_entry.grid(column=1, row=3, pady=2)

        list_signal = [
            "0-20mA",
            "4-20mA",
            "0-10V",
            "2-10V",
            "0-5V",
            "1-5V",
            "Value",
        ]
        signal = Label(frame1, text="Signal:")
        signal.grid(column=0, row=4, pady=2, sticky=W)
        cls.signal_drop = ttk.Combobox(frame1, value=list_signal, width=10)
        cls.signal_drop.current(0)
        cls.signal_entry = list_signal[0]
        cls.signal_drop.bind("<<ComboboxSelected>>", cls.select_signal)
        cls.signal_drop.grid(column=1, row=4)

        location = Label(frame1, text="Location:")
        location.grid(column=0, row=5, pady=2, sticky=W)
        cls.location_entry = Entry(frame1, width=35)
        cls.location_entry.grid(column=1, row=5, pady=2, columnspan=3)

        button_create = Button(frame1, text="Create", width=10, command=cls.create)
        button_create.grid(column=0, row=6, columnspan=4, rowspan=2)
        print(cls.signal_entry)

        cls.widoCreate.protocol('WM_DELETE_WINDOW', cls.on_close)
        cls.widoCreate.mainloop()

    @classmethod
    def on_close(cls):
        print('close')
        cls.widoCreate.destroy()
        SettingScreen.open = False


    @classmethod
    def create(cls):
        conn = sqlite3.connect('setting.db')
        c = conn.cursor()

        sql =             f"""INSERT INTO Information (sensor, device, address, location, low_range, high_range, signal, unit) 
            VALUES ('{cls.sensor_entry.get()}',
                '{cls.device_entry.get()}',
                '{cls.address_entry.get()}',
                '{cls.location_entry.get()}',
                '{cls.low_range_entry.get()}',
                '{cls.high_range_entry.get()}',
                '{cls.signal_entry}',
                '{cls.unit_entry.get()}')"""
        print(sql)
        c.execute(sql)
        conn.commit()
        conn.close()

        cls.sensor_entry.delete(0, END)
        cls.device_entry.delete(0, END)
        cls.address_entry.delete(0, END)
        cls.low_range_entry.delete(0, END)
        cls.high_range_entry.delete(0, END)
        cls.unit_entry.delete(0, END)
        cls.location_entry.delete(0, END)
