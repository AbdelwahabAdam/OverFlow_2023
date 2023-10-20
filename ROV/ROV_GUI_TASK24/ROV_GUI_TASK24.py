import tkinter as tk
from tkinter import ttk
from tkinter import *
import serial.tools.list_ports
import serial
import time 
from pyjoystick.sdl2 import Key, Joystick, run_event_loop
commandd=""





class SerialApp(tk.Tk): 
    def __init__(self):
        super().__init__()
        self.geometry("400x240")
        self.config(bg="#67E5C1")
        self.selected_port = None
        self.selected_port_var = tk.StringVar(self)
       
    def refresh_serial_port_list(self):
        self._available_ports = [port.device for port in serial.tools.list_ports.comports()]

    def select_serial_port(self):
        self.refresh_serial_port_list()

        monthchoosen = ttk.Combobox(self, width = 27, textvariable = self.selected_port_var)
        monthchoosen['values'] = (self._available_ports)
        monthchoosen.grid(column = 1, row = 5)

        select_button = tk.Button(self, text="Select", command=self.set_port)
        select_button.grid(column = 2, row = 5)
        
        self.state_labels = Label(self,bg='red',width='5',height='2')
        self.state_labels.grid(row=3,column=1)
        self.state_labels.config(bg='red')

        refresh_button = tk.Button(self, text="Refresh", command=self.select_serial_port)
        refresh_button.grid(column = 3, row = 5)

        Start_button = tk.Button(self, text="Start", command=self.joySend)
        Start_button.grid(column = 2, row = 6)
        
        self.mainloop()

    def globread(self):
        arduino = serial.Serial(port = self.selected_port,   baudrate=9600, timeout=.1)
        def write_read(x):
            arduino.write(bytes(x,   'utf-8'))
            data = arduino.readline()
            return   data
            num = commandd
            value   = write_read(num)
            print(value)
            
    def set_port(self):
        self.selected_port = self.selected_port_var.get()
        self.state_labels.config(bg='green')
        self.globread()
    def joySend(self):
        def print_add(joy):
            print("add",joy)

        def print_remove(joy):
            print("removed",joy)
        def key_received(key):
            if key.keytype == Key.BUTTON and key.number == 0:
                if key.value == 1:
                    print("4FIN")
                else:
                    pass
            elif key.keytype == Key.BUTTON and key.number == 1:
                if key.value == 1:
                    print("RG")
                else:
                    pass
            elif key.keytype == Key.BUTTON and key.number == 2:
                if key.value == 1:
                    print("LG")
                else:
                    pass
            elif key.keytype == Key.BUTTON and key.number == 3:
                if key.value == 1:
                    commandd="y"
                else:
                    pass

            elif key.value == Key.HAT_UP:
                print("fwr")
            elif key.value == Key.HAT_DOWN:
                print("back")
            elif key.value == Key.HAT_LEFT:
                print("LEFT")
            elif key.value == Key.HAT_UPLEFT:
                print("UP_LEFT")
            elif key.value == Key.HAT_DOWNLEFT:
                print("DOWN_LEFT")
            elif key.value == Key.HAT_RIGHT:
                print("RIGHT")
            elif key.value == Key.HAT_UPRIGHT:
                print("UP_RIGHT")
            elif key.value == Key.HAT_DOWNRIGHT:
                print("DOWN_RIGHT")
        run_event_loop(print_add, print_remove, key_received)

    
app = SerialApp()
app.select_serial_port()







