from tkinter import *
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create the "doctors" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS patientregister (
        id INTEGER PRIMARY KEY,
        patientcode TEXT,
        patientname TEXT,
        title TEXT,
        dob TEXT,
        age TEXT,
        emailid TEXT,
        phonenumber TEXT,
        gender TEXT
    )
''')
conn.commit()

def register_patient():
    patientcode = en1.get()
    patientname = en3.get()
    title = en4.get()
    dob = en5.get()
    age = en6.get()
    emailid = en7.get()
    phonenumber = en8.get()
    gender = en9.get()

    # Insert data into the "doctors" table
    cursor.execute('''
        INSERT INTO patientregister (patientcode, patientname, title, dob, age, emailid, phonenumber, gender)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (patientcode, patientname, title, dob, age, emailid, phonenumber, gender))
    conn.commit()

    # Clear the entry fields
    en1.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)
    en7.delete(0, END)
    en8.delete(0, END)
    en9.delete(0, END)
    
    
def open_patient_view():
   
    import patientview
    patientview.patient_view_form()
    
    
base = Tk()
base.geometry("500x500")
base.title("Add Patientregistration")

lb1 = Label(base, text="patientcode", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb2 = Label(base, text="patientname", width=10, font=("arial", 12))
lb2.place(x=19, y=140)
en3 = Entry(base)
en3.place(x=200, y=140)

lb3 = Label(base, text="title", width=10, font=("arial", 12))
lb3.place(x=19, y=160)
en4 = Entry(base)
en4.place(x=200, y=160)

lb5 = Label(base, text="dob", width=13, font=("arial", 12))
lb5.place(x=19, y=180)
en5 = Entry(base)
en5.place(x=200, y=180)

lb6 = Label(base, text="age", width=13, font=("arial", 12))
lb6.place(x=19, y=200)
en6 = Entry(base)
en6.place(x=200, y=200)

lb7= Label(base, text="emailid", width=13,font=("arial",12))  
lb7.place(x=19, y=220)  
en7= Entry(base)  
en7.place(x=200, y=220)    
  
  
lb8= Label(base, text="phonenumber", width=13,font=("arial",12))  
lb8.place(x=19, y=240)  
en8= Entry(base)  
en8.place(x=200, y=240)  

lb9= Label(base, text="gender", width=13,font=("arial",12))  
lb9.place(x=19, y=260)  
en9= Entry(base)  
en9.place(x=200, y=260) 


  

Button(base, text="Register", width=10, command=register_patient).place(x=200, y=400)
base.mainloop()

