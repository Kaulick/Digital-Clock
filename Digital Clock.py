import tkinter as tk
import time

def time_update():
    current_time = time.strftime('%I:%M:%S %p')
    time_part, am_pm_part = current_time[:-3], current_time[-2:]
    clock_label.config(text=time_part)
    am_pm_label.config(text=am_pm_part)
    clock_label.after(1000, time_update)

root = tk.Tk()
root.title("Digital Clock")

root.attributes('-fullscreen', True)
root.configure(background='black')

root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))

frame = tk.Frame(root, background='black')
frame.pack(expand=True)

clock_label = tk.Label(frame, font=('DS-Digital', 250, ''), background='black', foreground='red')
clock_label.pack(side='left')

am_pm_label = tk.Label(frame, font=('DS-Digital', 50, 'bold'), background='black', foreground='red')
am_pm_label.pack(side='left', padx= 10)

time_update()

root.mainloop()
