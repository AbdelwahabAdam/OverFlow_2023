
from tkinter import *

window = Tk()

window.title("ROV GUI")

window.resizable(width=False, height=False)
window.geometry("350x250")


def start():
    pass
def stop():
    pass
def refresh():
    pass


Start = Button(window, text='Start', command=start, bg='green', width=10, height=4)
Start.grid(row=0,column=0)

Stop = Button(window, text='Stop', command=stop, bg='red', width=10, height=4)
Stop.grid(row=0,column=1)

Refresh = Button(window, text=' Refresh', command=refresh, bg='cyan', width=10, height=4)
Refresh.grid(row=0, column=2)

Arduino_Port = Label(window, text='Arduino Port: ')
Arduino_Port.grid(row=1, column=0)

Joystick_Port = Label(window, text='Joystick Port: ')
Joystick_Port.grid(row=2, column=0)

Depth_Sensor = Label(window, text='Depth: ')
Depth_Sensor.grid(row=3, column=0)

Angle_Sensor = Label(window, text='Angle: ')
Angle_Sensor.grid(row=4, column=0)

Depth_Reading = Entry(window)
Depth_Reading.insert('end','')  # insert the default value for depth sensor reading in entry box
Depth_Reading.grid(row=3, column=1)

Angle_Reading = Entry(window)
Angle_Reading.insert('end','')  # insert the default value for angle sensor reading in entry box
Angle_Reading.grid(row=4, column=1)

State = Label(window, text='State of ROV: ')
State.grid(row=6, column=0)

State_Of_ROV = Entry(window)
State_Of_ROV.insert('end','')   # insert the default state of rov into entry box
State_Of_ROV.grid(row=6, column=1)



port_list = ['COM1','COM2','COM3']

x = 0
y = 0
Arduino = IntVar()
Joystick = IntVar()
def fun():
    if Arduino.get() == 1:
        x = 1
    elif Arduino.get() == 2:
        x = 2
    elif Arduino.get() == 3:
        x = 3

def fun1():
    if Joystick.get() == 1:
        x = 1
    elif Joystick.get() == 2:
        x = 2
    elif Joystick.get() == 3:
        x = 3



Arduino_Port1 = Radiobutton(window, text='COM1', value=1, variable=Arduino,command=fun)
Arduino_Port1.grid(row=1, column=1) 

Arduino_Port2 = Radiobutton(window, text='COM2', value=2, variable=Arduino,command=fun)
Arduino_Port2.grid(row=1, column=2) 

Arduino_Port3 = Radiobutton(window, text='COM3', value=3, variable=Arduino,command=fun)
Arduino_Port3.grid(row=1, column=3) 

Joystick_Port1 = Radiobutton(window, text='Port 1', value=1, variable=Joystick,command=fun)
Joystick_Port1.grid(row=2, column=1) 

Joystick_Port2 = Radiobutton(window, text='Port 2', value=2, variable=Joystick,command=fun)
Joystick_Port2.grid(row=2, column=2) 

Joystick_Port3 = Radiobutton(window, text='Port 3', value=3, variable=Joystick,command=fun)
Joystick_Port3.grid(row=2, column=3) 

window.mainloop()