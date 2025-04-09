import tkinter as tk

# Create the main window
root = tk.Tk()

# Define the button click function
def on_button_click():
    print("Button clicked!")

# Create the button and add it to the window
button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

# Start the Tkinter event loop
root.mainloop()

#since i have created a button i will add more feature to it