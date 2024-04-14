# Write a GUI-based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius. The interface should have labeled entry fields for these two values. These components should be arranged in a grid where the labels occupy the first row and the corresponding fields occupy the second row. At start-up, the Fahrenheit field should contain 32.0, and the Celsius field should contain 0.0. The third row in the window contains two command buttons, labeled >> >> and <<<<. When the user presses the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, which should then be output to the Celsius field. The second button should perform the inverse function

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


root = tk.Tk()
root.title("Temperature Converter")

# Fahrenheit label and entry
fahrenheit_label = tk.Label(root, text="Fahrenheit:")
fahrenheit_label.grid(row=0, column=0, padx=5, pady=5)
fahrenheit_entry = tk.Entry(root)
fahrenheit_entry.insert(0, "32.0")
fahrenheit_entry.grid(row=1, column=0, padx=5, pady=5)

# Celsius label and entry
celsius_label = tk.Label(root, text="Celsius:")
celsius_label.grid(row=0, column=1, padx=5, pady=5)
celsius_entry = tk.Entry(root)
celsius_entry.insert(0, "0.0")
celsius_entry.grid(row=1, column=1, padx=5, pady=5)

# Convert to Celsius button
to_celsius_button = tk.Button(root, text=">>>>", command=convert_to_celsius)
to_celsius_button.grid(row=2, column=0, padx=5, pady=5)

# Convert to Fahrenheit button
to_fahrenheit_button = tk.Button(
    root, text="<<<<", command=convert_to_fahrenheit)
to_fahrenheit_button.grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
