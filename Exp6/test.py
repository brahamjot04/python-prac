import tkinter as tk

root = tk.Tk()
root.title("Test")
root.geometry("500x500")

tk.Label(root, text="Hello World!").grid()
tk.Button(root, text="Close Window", command=root.quit).grid()

root.mainloop()
