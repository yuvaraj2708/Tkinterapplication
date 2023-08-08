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
    cursor.execute("SELECT * FROM doctors")
    doctor_data = cursor.fetchall()

    for row in doctor_data:
        doctor_info = f"Doctor Code: {row[0]}\nDoctor Name: {row[1]}\nQualification: {row[2]}\nSpecialisation: {row[3]}\nAddress: {row[4]}\nMobile: {row[5]}\nPIN Code: {row[6]}\nEmail ID: {row[7]}\n\n"
        doctor_label = Label(base.saved_data_window, text=doctor_info, font=("arial", 12))
        doctor_label.pack()

    conn.close()

base = Tk()
base.geometry("500x500")
base.title("Add Doctor")

Button(base, text="View Saved Data", width=15, command=view_saved_data).place(x=300, y=400)

base.mainloop()
