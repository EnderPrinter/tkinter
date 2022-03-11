import time
from tkinter import *
import serial
import array
global voltage
lst = [None] * 60
ser = serial.Serial('COM7', 9600, timeout=0)
window = Tk()
text_box = Text(window)
#text_box.pack()
frame_a = window.frame()
frame_b = window.frame()
window.title("com")

window.geometry('840x640')

#lbl = Label(window, text="send")

#lbl.grid(column=0, row=0)

txt = Entry(window,width=10)

txt.grid(column=4, row=0)

def clicked():
    global voltage
    for i in range(1, 60):

        ser.write(serial.to_bytes([0x55, 0x55, 0x00, 0x00, 0xAA]))
        # time.sleep(1)
        if (ser.in_waiting > 0):
            serialString = ser.read()
            print(serialString)
            lst[i] = serialString
            #time.sleep(0.05)
            lbl = Label(window, text=str(serialString))
            lbl.grid(column=2, row=i)
            text_box.insert("1.0", str(serialString) +  "\n")
            text_box.grid(column=2, row=1)
            #frame_a.pack()
            #frame_b.pack()
    filtered_list = list(filter(None, lst))
    print(filtered_list)
    result = filtered_list[35].hex() + filtered_list[34].hex()

    string_list = list(result)
    string_list[0] = '0x'

    hex_result = "".join(string_list)

    an_integer = int(hex_result, 16)
    hex_value = hex(an_integer)

    hex_int = int(hex_value, 16)

    voltage = hex_int / 1000
    text_box.insert("1.0", "voltage: " + str(voltage) + "\n")
    text_box.grid(column=2, row=1)


def sended():
    txt.insert(0, str(voltage)+"V")

btn = Button(window, text="Send", command=clicked)

btn.grid(column=2, row=0)

btn2 = Button(window, text="voltage", command=sended)

btn2.grid(column=3, row=0)

window.mainloop()

