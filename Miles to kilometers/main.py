import tkinter


def convert():
    converted_units["text"] = round((int(unit_text_entry.get()) * 1.609), 2)


# * Making the window
window = tkinter.Tk()
window.title("Miles to Kilometers converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)

# * Making the text entry to get the miles the user want to convert
unit_text_entry = tkinter.Entry(width=10)
unit_text_entry.insert(tkinter.END, string="0")
unit_text_entry.focus()
unit_text_entry.grid(column=1, row=0)

# * Making a miles label
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# * Making "is equal to" Label
equal = tkinter.Label(text="is equal to")
equal.grid(column=0, row=1)

# * Making conversion Label
converted_units = tkinter.Label(text="0")
converted_units.grid(column=1, row=1)

# * Making conversion to Label
convert_to = tkinter.Label(text="Km")
convert_to.grid(column=2, row=1)

# * Making Calculate button
calculate = tkinter.Button(text="Calculate", command=convert)
calculate.grid(column=1, row=2)

window.mainloop()
