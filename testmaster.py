from tkinter import *
import sqlite3

def view_saved_data():
    if not hasattr(base, 'saved_data_window'):
        base.saved_data_window = Toplevel(base)
        base.saved_data_window.geometry("500x500")
        base.saved_data_window.title("Saved Doctor Information")
    else:
        base.saved_data_window.destroy()
        base.saved_data_window = Toplevel(base)
        base.saved_data_window.geometry("500x500")
        base.saved_data_window.title("Saved Doctor Information")

    # Create a connection to the SQLite database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    # Retrieve data from the "doctors" table
    cursor.execute("SELECT * FROM Tests")
    doctor_data = cursor.fetchall()

    for row in doctor_data:
        doctor_info = f"Test Code: {row[0]}\Test Name: {row[1]}\nspecimen type: {row[2]}\ndepartment: {row[3]}\nreport format: {row[4]}\nreporting rate: {row[5]}\n\n"
        doctor_label = Label(base.saved_data_window, text=doctor_info, font=("arial", 12))
        doctor_label.pack()

    conn.close()

base = Tk()
base.geometry("500x500")
base.title("Add Tests")

Button(base, text="View Saved Data", width=15, command=view_saved_data).place(x=300, y=400)

base.mainloop()
