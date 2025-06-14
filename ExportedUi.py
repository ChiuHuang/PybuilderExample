# This code is generated using PyUIbuilder: https://pyuibuilder.com

import os
import tkinter as tk

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# add   def load_ui():
main = tk.Tk()
main.title("Main Window")
main.config(bg="#E4E2E2")
main.geometry("700x400")

button = tk.Button(master=main, text="Button")
button.config(bg="#E4E2E2", fg="#000")
button.place(x=276, y=245, height=40)

label = tk.Label(master=main, text="Label")
label.config(bg="#E4E2E2", fg="#000")
label.place(x=294, y=157, height=40)

# add   return main, label, button

# remove main.mainloop()