import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def convert():
    # Code for currency conversion

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create the entry widget
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4)

# Create the number buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 1
col = 0

for button in buttons:
    btn = tk.Button(window, text=button, width=5, height=2, command=lambda button=button: entry.insert(tk.END, button))
    btn.grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Create the clear button
clear_btn = tk.Button(window, text="C", width=5, height=2, command=clear)
clear_btn.grid(row=row, column=col)

# Create the calculate button
calculate_btn = tk.Button(window, text="=", width=5, height=2, command=calculate)
calculate_btn.grid(row=row, column=col+1)

# Create the convert button
convert_btn = tk.Button(window, text="Convert", width=10, height=2, command=convert)
convert_btn.grid(row=row+1, column=0, columnspan=4)

# Run the main loop
window.mainloop()
