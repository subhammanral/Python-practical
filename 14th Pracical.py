import tkinter as tk

def button_click(value):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + str(value))

def calculate():
    try:
        expression = entry_display.get()
        result = eval(expression)
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

def clear():
    entry_display.delete(0, tk.END)

def backspace():
    current = entry_display.get()
    entry_display.delete(len(current)-1, tk.END)


#main program starts here
c_win = tk.Tk()
c_win.title("Calculator")

entry_display = tk.Entry(c_win, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('Clear', 5, 0), ('Back', 5, 1)
]

for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(c_win, text=text, width=5, height=2, font=("Arial", 18), command=calculate)
    elif text == "Clear":
        button = tk.Button(c_win, text=text, width=5, height=2, font=("Arial", 18), command=clear)
    elif text == "Back":
        button = tk.Button(c_win, text=text, width=5, height=2, font=("Arial", 18), command=backspace)
    else:
        button = tk.Button(c_win, text=text, width=5, height=2, font=("Arial", 18), command=lambda value=text: button_click(value))
    
    button.grid(row=row, column=col, padx=5, pady=5)

c_win.mainloop()
