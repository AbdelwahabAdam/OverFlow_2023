from tkinter import * 
from tkinter import messagebox
from tkinter.ttk import Combobox

window = Tk()
window.title("ROV GUI")
window.config(bg = "#ADD8E6")
window.geometry("300x450")
# window.resizable(width="false", height="false")

###############################################################################

banner = Label(window,fg="black", text="ROV GUI ",font="Helvetica 12  bold",bg = "#ADD8E6")
banner.place (x= 120, y = 0)

###############################################################################
                    # Start , stop , refresh buttons 

def Start():
    msg=messagebox.showinfo( "Start button","The program is running now !")

Start_button = Button(window, text ="Start" ,font="Times 10 italic bold", command = Start)
Start_button.place(x=20,y=50)



def Stop():
    msg=messagebox.showinfo( "Stop button","The program is stopped !")

Stop_button = Button(window, text ="Stop",font="Times 10 italic bold", command = Stop)
Stop_button.place(x=120,y=50)



def Refresh():
    msg=messagebox.showinfo("Refresh button", "the program is refreshing !")

Refresh_button = Button(window, text ="Refresh",font="Times 10 italic bold", command = Refresh)
Refresh_button.place(x=220,y=50)

###############################################################################
                            # COM combobox


COM = Label(window, text = "Select the COM :", font = "Times 10 italic bold")
COM.place(x = 0, y= 150)


n = StringVar()
port = Combobox(window, width = 27, textvariable = n)


port['values'] = (' COM 1',
                'COM 2',
                'COM 3',
                'COM 4')

port.place(x = 100, y = 150)

###############################################################################
#                           Joy stick COMBOBOX 

joystick_port=Label(window, text = "Select joyStick port:",  font = "Times 8 italic bold")
joystick_port.place(x = 0, y= 200)

y = StringVar()
Jport = Combobox(window, width = 27, textvariable = n)

Jport['values'] = ('Port 1',
                    'Port 2',
                    'Port 3',
                    'Port 4',
                    )

Jport.place(x = 100, y = 200)

##############################################################################
#                           Depth & angle

depth = Label(window, text="Depth:",width = 10)
depth.place(x = 0, y= 250)

angle = Label(window, text="Angle:",width = 10)
angle.place(x = 0, y= 280)

def input_reading(depth, angle):
    depth.config(text="Depth: {}".format(depth))
    angle.config(text="Angle: {}".format(angle))

##############################################################################
#                                   State

ON_state_label = Label(window, text="ON",bg="#90EE90" ,font = "Times 10 italic bold",width= 20,justify = CENTER)
ON_state_label.place(x= 0 , y= 360)

OFF_state_label = Label(window, text="OFF",bg="#ffcccb" ,font = "Times 10 italic bold",width= 20,justify = CENTER)
OFF_state_label.place(x= 0 , y= 320)

pause_state_label = Label(window, text="Pause",bg="#FFFFED" ,font = "Times 10 italic bold",width= 20,justify = CENTER)
pause_state_label.place(x= 0 , y= 400)

window.mainloop()