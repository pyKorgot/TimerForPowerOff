"""GUI Interface for application
    """


import tkinter
import tkinter as tk
from tkinter.ttk import Combobox
import main


def start():
    hour = comb_hour.get()
    minutes = comb_minute.get()
    seconds = comb_second.get()
    main.alarm([hour, minutes, seconds])


window = tk.Tk()

window.resizable(width=False, height=False)
window.geometry('429x100')
window.title('Timer for Power off')

lbl1 = tk.Label(window, text='Hello, enter second to turn off your PC.')
lbl1.grid(row=0, column=0, columnspan=3)


lbl_hour = tk.Label(window, text='Hours')
lbl_hour.grid(column=0, row=1)

comb_hour = Combobox(window)
comb_hour['values'] = [x for x in range(25)]
comb_hour.current(0)
comb_hour.configure(state='readonly')
comb_hour.grid(column=0, row=2)


lbl_minute = tk.Label(window, text='Minutes')
lbl_minute.grid(column=1, row=1)

comb_minute = Combobox(window)
comb_minute['values'] = [x for x in range(60)]
comb_minute.current(0)
comb_minute.configure(state='readonly')
comb_minute.grid(column=1, row=2)


lbl_seconds = tk.Label(window, text='Seconds')
lbl_seconds.grid(column=2, row=2)

comb_second = Combobox(window)
comb_second['values'] = [x for x in range(60)]
comb_second.current(0)
comb_second.configure(state='readonly')
comb_second.grid(column=2, row=2)

btn_ok = tk.Button(window, text='Okay', command=start)
btn_ok.grid(column=1, row=3)

tk.mainloop()
