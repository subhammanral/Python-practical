import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from datetime import datetime

def calculate_age():
    try:
        day = int(entry_day.get())
        month = month_combobox.get()
        month = datetime.strptime(month, "%B").month
        year = int(entry_year.get())
        
        dob = datetime(year, month, day)
        
        current_date = datetime.today()
        
        age = current_date.year - dob.year
        if (current_date.month, current_date.day) < (dob.month, dob.day):
            age -= 1
        
        label_result.config(text=f"Your age is: {age} years")
    
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid day, month, and year.")

age_win = tk.Tk()
age_win.title("Age Calculator")
age_win.geometry("250x300")

tk.Label(age_win, text="Enter your Date of Birth", font=("Arial", 16)).grid(row=0, column=0, columnspan=3, pady=10)

tk.Label(age_win, text="Day:").grid(row=1, column=0, padx=10, pady=5)
entry_day = tk.Entry(age_win, width=5, font=("Arial", 14))
entry_day.grid(row=1, column=1, padx=10, pady=5)

tk.Label(age_win, text="Month:").grid(row=2, column=0, padx=10, pady=5)
month_combobox = ttk.Combobox(age_win, width=10, font=("Arial", 14), state="readonly")
month_combobox['values'] = [
    "January", "February", "March", "April", "May", "June", "July", "August", "September",
    "October", "November", "December"
]
month_combobox.grid(row=2, column=1, padx=10, pady=5)

tk.Label(age_win, text="Year:").grid(row=3, column=0, padx=10, pady=5)
entry_year = tk.Entry(age_win, width=10, font=("Arial", 14))
entry_year.grid(row=3, column=1, padx=10, pady=5)

button_calculate = tk.Button(age_win, text="Calculate Age", font=("Arial", 14), command=calculate_age)
button_calculate.grid(row=4, columnspan=3, pady=20)

label_result = tk.Label(age_win, text="Your age is: ", font=("Arial", 14))
label_result.grid(row=5, columnspan=3, pady=10)

age_win.mainloop()
