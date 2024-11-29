import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import csv

def save_student_details():
    roll_no = entry_roll_no.get()
    enrollment_no = entry_enrollment_no.get()
    name = entry_name.get()
    course = course_combobox.get()
    semester = semester_combobox.get()

    if not roll_no or not enrollment_no or not name or not course or not semester:
        messagebox.showerror("Input Error", "All fields must be filled out.")
        return
    
    with open("student_details.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, enrollment_no, name, course, semester])
    
    entry_roll_no.delete(0, tk.END)
    entry_enrollment_no.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    course_combobox.set('')
    semester_combobox.set('')
    
    messagebox.showinfo("Success", "Student details saved successfully!")

s_win = tk.Tk()
s_win.title("Student Registration Form")
s_win.geometry("300x350")

tk.Label(s_win, text="Student Registration Form", font=("Arial", 16)).grid(row=0, column=0, columnspan=2, pady=20)

tk.Label(s_win, text="Roll No:").grid(row=1, column=0, padx=10, pady=10)
entry_roll_no = tk.Entry(s_win, width=20)
entry_roll_no.grid(row=1, column=1, padx=10, pady=10)

tk.Label(s_win, text="Enrollment No:").grid(row=2, column=0, padx=10, pady=10)
entry_enrollment_no = tk.Entry(s_win, width=20)
entry_enrollment_no.grid(row=2, column=1, padx=10, pady=10)

tk.Label(s_win, text="Name:").grid(row=3, column=0, padx=10, pady=10)
entry_name = tk.Entry(s_win, width=20)
entry_name.grid(row=3, column=1, padx=10, pady=10)

tk.Label(s_win, text="Course:").grid(row=4, column=0, padx=10, pady=10)
course_combobox = ttk.Combobox(s_win, width=20, state="readonly")
course_combobox['values'] = [
    "B.Sc. PSCS", "B.Sc. CS", "B.Sc. PSCh", "B.Sc. Physics", "B.Sc. Chemistry",
    "B.Sc. Mathematics", "B.Sc. MTS", "B.A.", "B.Com", "BMS"
]
course_combobox.grid(row=4, column=1, padx=10, pady=10)

tk.Label(s_win, text="Semester:").grid(row=5, column=0, padx=10, pady=10)
semester_combobox = ttk.Combobox(s_win, width=20, state="readonly")
semester_combobox['values'] = ["1", "2", "3", "4", "5", "6"]
semester_combobox.grid(row=5, column=1, padx=10, pady=10)

save_button = tk.Button(s_win, text="Save Details", font=("Arial", 14), command=save_student_details)
save_button.grid(row=6, columnspan=2, pady=20)

s_win.mainloop()
