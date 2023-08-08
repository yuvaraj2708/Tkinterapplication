from tkinter import *
import sqlite3

def view_saved_data():
    if not hasattr(base, 'saved_data_window'):
        base.saved_data_window = Toplevel(base)
        base.saved_data_window.geometry("500x500")
        base.saved_data_window.title("Saved patient Information")
    else:
        base.saved_data_window.destroy()
        base.saved_data_window = Toplevel(base)
        base.saved_data_window.geometry("500x500")
        base.saved_data_window.title("Saved patient Information")

    # Create a connection to the SQLite database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()

    # Retrieve data from the "patients" table
    cursor.execute("SELECT * FROM patientregister")
    patient_data = cursor.fetchall()

    for row in patient_data:
        patient_info = f"patientcode: {row[1]}\npatientname: {row[2]}\ntitle: {row[3]}\ndob: {row[4]}\nage: {row[5]}\nemailid: {row[6]}\nphonenumber: {row[7]}\ngender: {row[8]}\n\n"
        patient_label = Label(base.saved_data_window, text=patient_info, font=("arial", 12))
        patient_label.pack()

    conn.close()

base = Tk()
base.geometry("500x500")
base.title("Add patients")

Button(base, text="View Saved Data", width=15, command=view_saved_data).place(x=300, y=450)

base.mainloop()