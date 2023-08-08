from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("Add Test")  
  


from tkinter import *
import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create the "doctors" table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tests (
        id INTEGER PRIMARY KEY,
        Testcode TEXT,
        Testname TEXT,
        specimentype TEXT,
        department TEXT,
        reportformat TEXT,
        reportingrate TEXT
        
    )
''')
conn.commit()

def register_test():
    Testcode = en1.get()
    Testname = en3.get()
    specimentype = en4.get()
    department = en5.get()
    reportformat = en6.get()
    reportingrate = en7.get()
    
    # Insert data into the "doctors" table
    cursor.execute('''
        INSERT INTO tests (Testcode, Testname, specimentype, department, reportformat, reportingrate)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (Testcode, Testname, specimentype, department, reportformat, reportingrate))
    conn.commit()

    # Clear the entry fields
    en1.delete(0, END)
    en3.delete(0, END)
    en4.delete(0, END)
    en5.delete(0, END)
    en6.delete(0, END)
    en7.delete(0, END)
    

base = Tk()
base.geometry("500x400")
base.title("Add Doctor")

lb1 = Label(base, text="Test Code", width=10, font=("arial", 12))
lb1.place(x=20, y=120)
en1 = Entry(base)
en1.place(x=200, y=120)

lb3 = Label(base, text="Test Name", width=10, font=("arial", 12))
lb3.place(x=19, y=140)
en3 = Entry(base)
en3.place(x=200, y=140)

lb4 = Label(base, text="specimentype", width=13, font=("arial", 12))
lb4.place(x=19, y=160)
en4 = Entry(base)
en4.place(x=200, y=160)

lb5 = Label(base, text="department", width=13, font=("arial", 12))
lb5.place(x=19, y=180)
en5 = Entry(base)
en5.place(x=200, y=180)

lb6 = Label(base, text="reportformat", width=13, font=("arial", 12))
lb6.place(x=19, y=200)
en6 = Entry(base)
en6.place(x=200, y=200)

lb7= Label(base, text="reportingrate", width=13,font=("arial",12))  
lb7.place(x=19, y=220)  
en7= Entry(base)  
en7.place(x=200, y=220)    

Button(base, text="Register", width=10, command=register_test).place(x=200, y=400)
base.mainloop()

  
  