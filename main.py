import UI
root, label, button = UI.load_ui()

def on_click():
    print("Button was clicked!")
    label.config(text="You clicked the button!")

button.config(command=on_click)

# Run the app
root.mainloop()
