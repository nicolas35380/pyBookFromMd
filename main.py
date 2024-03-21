# Informations source : 
    # - https://www.tutorialspoint.com/enable-multiple-selection-of-values-from-a-tkinter-combobox
    # - https://www.pythontutorial.net/tkinter/

import tkinter as tk
from tkinter import ttk

from function import *

if __name__ == "__main__":

    # file = read_input_file(MD_REQUIREMENT_FILES)
    # print(pdf_build(file))

    root = tk.Tk()
    root.title("Convert Markdown to Book")
    root.geometry('800x600+200+200')
    root.attributes('-alpha',0.9)

    # message = tk.Label(root, text="Hello World !")
    # message.pack()

    # tk.Label(root, text='Classic Label').pack()
    # ttk.Label(root, text='Themed Label').pack()

    ttk.Label(root, text='Fichier(s) à intégrer').pack(side="top", anchor="w")
    values = read_input_file(MD_REQUIREMENT_FILES)
    label = ttk.Label(root, text="Select values:")
    combobox = ttk.Combobox(root)
    checkbuttons_vars = [tk.BooleanVar() for value in values]

    checkbuttons = []
    for index, value in enumerate(values):
        checkbutton = ttk.Checkbutton(root, text=value, variable=checkbuttons_vars[index])
        checkbutton.pack(side="top", anchor="w")
        checkbuttons.append(checkbutton)

    # define a function to update the combobox when the user selects or deselects a value
    def update_combobox():
        selected_values = [value for value, var in zip(values, checkbuttons_vars) if var.get()]
        combobox.configure(width=40, height=7)
        combobox.delete(0, tk.END)
        combobox.insert(0, ", ".join(selected_values))

    # add a button to update the combobox
    update_button = ttk.Button(root, text="Update", command=update_combobox)
    update_button.pack(side="bottom")

    # pack the label and combobox
    label.pack(side="top", anchor="w", pady=30)
    combobox.pack(side="top")


    root.mainloop()