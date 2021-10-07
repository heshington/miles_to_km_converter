from tkinter import *

window = Tk()
window.title("Mile to Km Converter")

window.config(padx=20, pady=20)


def calculate_miles_km():
    miles = float(miles_input.get())
    kilometres = round(miles * 1.609, 2)
    km_label.config(text=kilometres)

#Input

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to", font=("Arial", 12))
is_equal_to.grid(column=0, row=1)
#
km_label = Label(text="0", font=("Arial", 12))
km_label.grid(column=1, row=1)
#
km = Label(text="Km", font=("Arial", 12))
km.grid(column=2, row=1)
#
calculate = Button(text="Calculate", command=calculate_miles_km)
calculate.grid(column=1, row=2)



window.mainloop()