import tkinter as tk

def on_click(symbol):
    """Append the clicked button's text to the entry field"""
    entry.insert(tk.END, symbol)

def clear():
    """Clear the entry field"""
    entry.delete(0, tk.END)

def calculate():
    """Evaluate the expression in entry field and show result"""
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create main window
root = tk.Tk()
root.title("Simple Calculator 🧮")

# Entry field
entry = tk.Entry(root, width=25, borderwidth=3, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button labels
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        b = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'C':
        b = tk.Button(root, text=text, width=5, height=2, command=clear)
    else:
        b = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: on_click(t))
    b.grid(row=row, column=col, padx=2, pady=2)

# Run the app
root.mainloop()
