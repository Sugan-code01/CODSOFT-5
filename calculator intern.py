import tkinter as tk
from tkinter import messagebox

def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            entry.delete(0, tk.END)
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)

# Create the main window
root = tk.Tk()
root.title("Colorful Calculator")

# Entry widget to display and input numbers and operations
entry = tk.Entry(root, font=('Arial', 25), borderwidth=5, relief=tk.SUNKEN, bg="lightgray")
entry.grid(row=0, column=0, columnspan=4)

# Button layout and colors
buttons = [
    ('7', 'lightblue'), ('8', 'lightblue'), ('9', 'lightblue'), ('/', 'orange'),
    ('4', 'lightblue'), ('5', 'lightblue'), ('6', 'lightblue'), ('*', 'orange'),
    ('1', 'lightblue'), ('2', 'lightblue'), ('3', 'lightblue'), ('-', 'orange'),
    ('C', 'red'), ('0', 'lightblue'), ('=', 'green'), ('+', 'orange')
]

# Create and place buttons
row_val = 1
col_val = 0
for (button_text, color) in buttons:
    button = tk.Button(root, text=button_text, font=('Arial', 20), padx=20, pady=20, bg=color)
    button.grid(row=row_val, column=col_val, sticky="nsew")
    button.bind("<Button-1>", click)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Make buttons expand and fill the available space
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Start the main event loop
root.mainloop()
