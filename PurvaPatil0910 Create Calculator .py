from tkinter import *

# Create a calculator class
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Professional Calculator")

        # Create an entry widget to display the input and result
        self.entry = Entry(master, width=30, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create buttons for numbers and operators
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Initialize row and column variables
        row = 1
        col = 0

        # Create buttons using a loop
        for button in buttons:
            # Create a button with the specified text and command
            btn = Button(master, text=button, padx=20, pady=10, command=lambda button=button: self.button_click(button))
            btn.grid(row=row, column=col, padx=5, pady=5)

            # Increment the column variable
            col += 1

            # Move to the next row after every 4 buttons
            if col > 3:
                col = 0
                row += 1

    # Function to handle button clicks
    def button_click(self, button):
        current = self.entry.get()

        # Clear the entry if the button is '='
        if button == '=':
            try:
                result = eval(current)
                self.entry.delete(0, END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, END)
                self.entry.insert(0, "Error")
        # Clear the entry if the button is 'C'
        elif button == 'C':
            self.entry.delete(0, END)
        # Append the button text to the entry
        else:
            self.entry.insert(END, button)

# Create the main window
root = Tk()

# Create an instance of the calculator class
calculator = Calculator(root)

# Run the main loop
root.mainloop()
