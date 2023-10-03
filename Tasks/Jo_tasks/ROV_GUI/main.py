from tkinter.ttk import *
from tkinter import *
import serial as s


class ROVGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ROV gui")
        self.root.geometry("400x400")
        self.root.configure(bg="#F0F0F0")

        self.arduino = None

        self.connect_b = Button(
            root,
            text="Connect Arduino",
            command=self.connect_arduino,
            bg="#4CAF50",
            fg="white",
        ).pack(pady=10)

        self.start_b = Button(
            root,
            text="Start",
            command=self.start_rov,
            bg="#4CAF50",
            fg="white",
            state=DISABLED,
        ).pack(pady=10)

        self.stop_b = Button(
            root,
            text="Stop",
            command=self.stop_rov,
            bg="#FF5733",
            fg="white",
            state=DISABLED,
        ).pack(pady=10)

        self.refresh_b = Button(
            root,
            text="Refresh",
            command=self.refresh_data,
            bg="#3498DB",
            fg="white",
            state=DISABLED,
        ).pack(pady=10)

        self.arduino_l = Label(root, text="Arduino Port:").pack()

        self.arduino_cb = Combobox(root, values=["COM1", "COM2", "COM3"]).pack(pady=5)

        self.joystick_l = Label(root, text="Joystick Port:").pack()

        self.joystick_cb = Combobox(
            root, values=["Joystick1", "Joystick2", "Joystick3"]
        ).pack(pady=5)

        self.sensor_l = Label(root, text="Sensor Readings:").pack()

        self.sensor_data = Label(root, text="", bg="white", width=40, height=5).pack(
            pady=10
        )

        self.state_l = Label(root, text="ROV State: Disconnected", bg="#F0F0F0").pack(
            pady=10
        )

    def connect_arduino(self):
        arduino_p = self.arduino_cb.get()
        joystick_p = self.joystick_cb.get()
        try:
            self.arduino = s.Serial(arduino_p, 9600, timeout=1)

            self.state_l.config(
                text=f"ROV State: Connected to Arduino - {arduino_p}, Joystick - {joystick_p}"
            )
            self.start_b.config(state=NORMAL)
            self.stop_b.config(state=NORMAL)
            self.refresh_b.config(state=NORMAL)
        except s.SerialException:
            self.state_l.config(text="ROV State: Connection Failed")

    def start_rov(self):
        self.arduino.write(b"S")
        self.state_l.config(text="ROV State: Started")

    def stop_rov(self):
        self.arduino.write(b"E")
        self.state_l.config(text="ROV State: Stopped")

    def refresh_data(self):
        self.arduino.write(b"R")
        sensor_reading = self.arduino.readline().decode().strip()
        self.sensor_data.config(text=sensor_reading)


if __name__ == "__main__":
    root = Tk()
    app = ROVGUI(root)
    root.mainloop()
    # Formatted by black "https://pypi.org/project/black/"
