from tkinter import *
import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.geometry("500x500")
window.configure(background='#A7754D')
window.title("ROV GUI")
window.resizable(width='False',height="False")


#### Rounded btn ("doesn't work" , "don't have text attr")
# class RoundedButton(tk.Canvas):
#     def __init__(self, parent, width, height, cornerradius, padding, color, bg, command=None):
#         tk.Canvas.__init__(self, parent, borderwidth=0, 
#             relief="flat", highlightthickness=0, bg=bg)
#         self.command = command

#         if cornerradius > 0.5*width:
#             print("Error: cornerradius is greater than width.")
#             return None

#         if cornerradius > 0.5*height:
#             print("Error: cornerradius is greater than height.")
#             return None

#         rad = 2*cornerradius
#         def shape():
#             self.create_polygon((padding,height-cornerradius-padding,padding,cornerradius+padding,padding+cornerradius,padding,width-padding-cornerradius,padding,width-padding,cornerradius+padding,width-padding,height-cornerradius-padding,width-padding-cornerradius,height-padding,padding+cornerradius,height-padding), fill=color, outline=color)
#             self.create_arc((padding,padding+rad,padding+rad,padding), start=90, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding-rad,padding,width-padding,padding+rad), start=0, extent=90, fill=color, outline=color)
#             self.create_arc((width-padding,height-rad-padding,width-padding-rad,height-padding), start=270, extent=90, fill=color, outline=color)
#             self.create_arc((padding,height-padding-rad,padding+rad,height-padding), start=180, extent=90, fill=color, outline=color)


#         id = shape()
#         (x0,y0,x1,y1)  = self.bbox("all")
#         width = (x1-x0)
#         height = (y1-y0)
#         self.configure(width=width, height=height)
#         self.bind("<ButtonPress-1>", self._on_press)
#         self.bind("<ButtonRelease-1>", self._on_release)

#     def _on_press(self, event):
#         self.configure(relief="sunken")

#     def _on_release(self, event):
#         self.configure(relief="raised")
#         if self.command is not None:
#             self.command()
# button = RoundedButton(window, 50,25, 10, 2, 'red', '#A7754D')
# button.place(relx=.1, rely=.1)

lab1 = Label(window,text = "OVERFLOW ROV GUI",pady = 30,padx=10,background="#A7754D")
lab1.grid(row=0,column=1)

#Main buttons
btn1 = Button(window,text = "Start",pady = 8,padx=15,background="#DCCCBB")
btn1.grid (row=3,column=0)

btn2 = Button(window,text = "End",pady = 8,padx=15,background="#DCCCBB")
btn2.grid (row=3,column=1)

btn3 = Button(window,text = "Refresh",pady = 8,padx=15,background="#DCCCBB")
btn3.grid (row=3,column=3)

#Reading labels
depth = 14
lab2 = Label(window,text = "Depth = %s" %(depth),pady = 20,padx=10,bg="#A7754D")
lab2.grid(row=5,column=1)

angelX = 90
lab3 = Label(window,text = "Angel x = %s" %(angelX),pady = 15,padx=10,bg="#A7754D")
lab3.grid(row=6,column=1)

angelY = 80
lab4 = Label(window,text = "Angel y = %s" %(angelY),pady = 20,padx=10,bg="#A7754D")
lab4.grid(row=7,column=1)

#Comboboxes
# Arduino combobox 
n = tk.StringVar() 
arduinoPorts = ttk.Combobox(window, width = 20, textvariable = n) 
ttk.Label(window, text = "Select Arduino port :",background="#A7754D").grid(column = 0,row = 8, padx = 30, pady = 20) 

arduinoPorts['values'] = ('COM1',
                            'COM2',
                            'COM3') 
arduinoPorts.grid(column = 0, row = 9) 
arduinoPorts.current()


# joystick combobox 
ttk.Label(window, text = "Select Joystick port :",background="#A7754D").grid(column = 3,row = 8, padx = 30, pady = 20) 
e = tk.StringVar() 
joystickPorts = ttk.Combobox(window, width = 20, textvariable = e,background="#646E78") 

joystickPorts['values'] = ('JOY1',
                            'JOY2',
                            'JOY3') 
joystickPorts.grid(column = 3, row = 9) 
joystickPorts.current()

################################################
window.mainloop()


