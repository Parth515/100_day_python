# The Miles to Kilometer Converter GUI

from tkinter import *

def miles_to_kilo():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kilo_result_label.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kilo_result_label = Label(text="Km")
kilo_result_label.grid(column=1, row=1)

calculate_button = Button(text="calculate", command=miles_to_kilo)
calculate_button.grid(column=2, row=1)

window.mainloop()
