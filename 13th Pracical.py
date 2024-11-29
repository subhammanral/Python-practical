import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    course = entry_course.get()
    roll_no = entry_roll_no.get()
    age = entry_age.get()

    if not name or not course or not roll_no or not age:
        messagebox.showerror("Error", "All fields must be filled!")
        return

    if not age.isdigit():
        messagebox.showerror("Error", "Age must be a number!")
        return

    messagebox.showinfo("Success", "Registration Successful!")

    r_win.quit()

r_win = tk.Tk()
r_win.title("Event Registration")

tk.Label(r_win, text="Name:").grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(r_win)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(r_win, text="Course:").grid(row=1, column=0, padx=10, pady=5)
entry_course = tk.Entry(r_win)
entry_course.grid(row=1, column=1, padx=10, pady=5)

tk.Label(r_win, text="Roll No.:").grid(row=2, column=0, padx=10, pady=5)
entry_roll_no = tk.Entry(r_win)
entry_roll_no.grid(row=2, column=1, padx=10, pady=5)

tk.Label(r_win, text="Age:").grid(row=3, column=0, padx=10, pady=5)
entry_age = tk.Entry(r_win)
entry_age.grid(row=3, column=1, padx=10, pady=5)

submit_button = tk.Button(r_win, text="Submit", command=submit)
submit_button.grid(row=4, columnspan=2, pady=10)

r_win.mainloop()
