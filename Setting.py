from tkinter import *
import tkinter

Open_Setting = False
# wido.geometry("500x500")
# wido.minsize(400, 400)
# wido.maxsize(400, 400)
# widoSet.tk.call('wm', 'iconphoto', widoSet._w, tkinter.PhotoImage(file='E:\HeaterUserInterface\Ảnh 1.png'))
def Save():
    pass
def on_close():
    print('close')
    global widoSet
    widoSet.destroy()
    Open_Setting = False
def Dis_Save():
    global widoSet
    widoSet = Tk()
    frame1 = Frame(widoSet)
    frame1.place(width=widoSet.winfo_screenwidth(), height=widoSet.winfo_screenheight(), x=0, y=0)
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
    buttonSave = Button(frame1, text="Connect", command=Save)
    buttonSave.grid(column=2, row=1, pady=2)
    widoSet.protocol('WM_DELETE_WINDOW',on_close)
    widoSet.mainloop()