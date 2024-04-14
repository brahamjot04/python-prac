# Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius. The interface should have labeled entry fields for these two values. These components should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the second row. At start-up, the Fahrenheit field should contain 32.0, and the Celsius field should contain 0.0. The third row in the window contains two command buttons, labeled >> >> and << << . When the user presses the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, which should then be output to the Celsius field. The second button should perform the inverse function
# Modify the temperature conversion program so that it responds to the user’s press of the return or enter key. If the user presses this key when the insertion point is in a given field, the action which uses that field for input is triggered

import tkinter as tk


def convert_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5/9
    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, str(celsius))


def convert_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = celsius * 9/5 + 32
    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, str(fahrenheit))


def on_enter(event):
    if event.widget == fahrenheit_entry:
        convert_to_celsius()
    elif event.widget == celsius_entry:
        convert_to_fahrenheit()


root = tk.Tk()
root.title("Temperature Converter")

fahrenheit_label = tk.Label(root, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=0)

celsius_label = tk.Label(root, text="Celsius")
celsius_label.grid(row=0, column=1)

fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.insert(0, "32.0")
fahrenheit_entry.grid(row=1, column=0)
fahrenheit_entry.bind("<Return>", on_enter)

celsius_entry = tk.Entry(root)
celsius_entry.insert(0, "0.0")
celsius_entry.grid(row=1, column=1)
celsius_entry.bind("<Return>", on_enter)

convert_to_celsius_button = tk.Button(
    root, text=">> >>", command=convert_to_celsius)
convert_to_celsius_button.grid(row=2, column=0)

convert_to_fahrenheit_button = tk.Button(
    root, text="<< <<", command=convert_to_fahrenheit)
convert_to_fahrenheit_button.grid(row=2, column=1)

root.mainloop()
