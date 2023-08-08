from tkinter import *
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create the "doctors" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctors (
        id INTEGER PRIMARY KEY,
        code TEXT,
        name TEXT,
        qualification TEXT,
        specialisation TEXT,
        address TEXT,
        mobile TEXT,
        pincode TEXT,
        email TEXT
    )
''')
conn.commit()

def register_doctor():
    code = en1.get()
    name = en3.get()
    qualification = en4.get()
    specialisation = en5.get()
    address = en6.get()
    mobile = en7.get()
    pincode = en8.get()
    email = en9.get()

    # Insert data into the "doctors" table
    cursor.execute('''
        INSERT INTO doctors (code, name, qualification, specialisation, address, mobile, pincode, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (code, name, qualification, specialisation, address, mobile, pincode, email))
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

base = Tk()
base.geometry("500x400")
base.title("Add Doctor")

lb1 = Label(base, text="Doctor Code", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb3 = Label(base, text="Doctor Name", width=10, font=("arial", 12))
lb3.place(x=19, y=140)
en3 = Entry(base)
en3.place(x=200, y=140)

lb4 = Label(base, text="Qualification", width=13, font=("arial", 12))
lb4.place(x=19, y=160)
en4 = Entry(base)
en4.place(x=200, y=160)

lb5 = Label(base, text="Specialisation", width=13, font=("arial", 12))
lb5.place(x=19, y=180)
en5 = Entry(base)
en5.place(x=200, y=180)

lb6 = Label(base, text="Address", width=13, font=("arial", 12))
lb6.place(x=19, y=200)
en6 = Entry(base)
en6.place(x=200, y=200)

lb7= Label(base, text="Mobile", width=13,font=("arial",12))  
lb7.place(x=19, y=220)  
en7= Entry(base)  
en7.place(x=200, y=220)    
  
  
lb8= Label(base, text="PIN Code", width=13,font=("arial",12))  
lb8.place(x=19, y=240)  
en8= Entry(base)  
en8.place(x=200, y=240)  

lb9= Label(base, text="Email ID", width=13,font=("arial",12))  
lb9.place(x=19, y=260)  
en9= Entry(base)  
en9.place(x=200, y=260) 

  
  

Button(base, text="Register", width=10, command=register_doctor).place(x=200, y=400)
base.mainloop()












  
  
  