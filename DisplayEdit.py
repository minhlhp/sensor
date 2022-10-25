import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from random import randint
from DisplaySetting import SettingScreen


class EditScreen:
    widoEdit = None
    SettingScreen.open = False
    signal_drop = None
    stt_entry = None
    sensor_entry = None
    device_entry = None
    address_entry = None
    low_range_entry = None
    high_range_entry = None
    unit_entry = None
    location_entry = None

    @classmethod
    def select_signal(cls, event):
        cls.signal_entry = cls.signal_drop.get()

    @classmethod
    def displayedit(cls):
        # cls.widoEdit = Tk()
        cls.widoEdit = Toplevel()
        cls.widoEdit.minsize(310, 200)
        cls.widoEdit.maxsize(310, 200)

        frame1 = Frame(cls.widoEdit)
        frame1.pack()
        stt = Label(frame1, text="Stt:")
        stt.grid(column=0, row=0, pady=2, sticky=W)
        cls.stt_entry = Entry(frame1, width=10)
        cls.stt_entry.grid(column=1, row=0, pady=2)

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
        cls.signal_drop.bind("<<ComboboxSelected>>", cls.select_signal)
        cls.signal_drop.grid(column=1, row=4)

        location = Label(frame1, text="Location:")
        location.grid(column=0, row=5, pady=2, sticky=W)
        cls.location_entry = Entry(frame1, width=35)
        cls.location_entry.grid(column=1, row=5, pady=2, columnspan=3)

        button_save = Button(frame1,text="Save", width=10)
        button_save.grid(column=0, row=6, columnspan=4, rowspan=2)

        cls.widoEdit.protocol('WM_DELETE_WINDOW', cls.on_close)
        cls.widoEdit.mainloop()

    @classmethod
    def on_close(cls):
        print('close')
        cls.widoEdit.destroy()
        SettingScreen.open = False
