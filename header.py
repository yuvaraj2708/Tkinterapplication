import tkinter as tk
from tkinter import ttk


import sqlite3


class HomePage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        label = tk.Label(self, text="Home Page", font=("Arial", 20))
        label.pack(pady=50)


#view patient data
class ViewSavedDataPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.view_patientsaved_data()

    def view_patientsaved_data(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM patientregister")
        patient_data = cursor.fetchall()

        for row in patient_data:
            patient_info = f"patientcode: {row[1]}\npatientname: {row[2]}\ntitle: {row[3]}\ndob: {row[4]}\nage: {row[5]}\nemailid: {row[6]}\nphonenumber: {row[7]}\ngender: {row[8]}\n\n"
            patient_label = tk.Label(self, text=patient_info, font=("arial", 12))
            patient_label.pack()

        conn.close()

#patient registration

class PatientRegistrationPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.label = tk.Label(self, text="Patient Registration Page", font=("Arial", 20))
        self.label.pack(pady=50)

        self.setup_registration_form()

    def register_patient(self):
        patientcode = self.en1.get()
        patientname = self.en3.get()
        title = self.en4.get()
        dob = self.en5.get()
        age = self.en6.get()
        emailid = self.en7.get()
        phonenumber = self.en8.get()
        gender = self.en9.get()

        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        # Insert data into the "patientregister" table
        cursor.execute('''
            INSERT INTO patientregister (patientcode, patientname, title, dob, age, emailid, phonenumber, gender)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patientcode, patientname, title, dob, age, emailid, phonenumber, gender))
        conn.commit()
        conn.close()

        # Clear the entry fields
        self.en1.delete(0, tk.END)
        self.en3.delete(0, tk.END)
        self.en4.delete(0, tk.END)
        self.en5.delete(0, tk.END)
        self.en6.delete(0, tk.END)
        self.en7.delete(0, tk.END)
        self.en8.delete(0, tk.END)
        self.en9.delete(0, tk.END)

    def setup_registration_form(self):
        lb1 = tk.Label(self, text="patientcode", width=10, font=("arial", 12))
        lb1.place(x=20, y=120)
        self.en1 = tk.Entry(self)
        self.en1.place(x=200, y=120)

        lb2 = tk.Label(self, text="patientname", width=10, font=("arial", 12))
        lb2.place(x=19, y=140)
        self.en3 = tk.Entry(self)
        self.en3.place(x=200, y=140)

        lb3 = tk.Label(self, text="title", width=10, font=("arial", 12))
        lb3.place(x=19, y=160)
        self.en4 = tk.Entry(self)
        self.en4.place(x=200, y=160)

        lb5 = tk.Label(self, text="dob", width=13, font=("arial", 12))
        lb5.place(x=19, y=180)
        self.en5 = tk.Entry(self)
        self.en5.place(x=200, y=180)

        lb6 = tk.Label(self, text="age", width=13, font=("arial", 12))
        lb6.place(x=19, y=200)
        self.en6 = tk.Entry(self)
        self.en6.place(x=200, y=200)

        lb7 = tk.Label(self, text="emailid", width=13, font=("arial", 12))
        lb7.place(x=19, y=220)
        self.en7 = tk.Entry(self)
        self.en7.place(x=200, y=220)

        lb8 = tk.Label(self, text="phonenumber", width=13, font=("arial", 12))
        lb8.place(x=19, y=240)
        self.en8 = tk.Entry(self)
        self.en8.place(x=200, y=240)

        lb9 = tk.Label(self, text="gender", width=13, font=("arial", 12))
        lb9.place(x=19, y=260)
        self.en9 = tk.Entry(self)
        self.en9.place(x=200, y=260)

        register_button = tk.Button(self, text="Register", width=10, command=self.register_patient)
        register_button.place(x=200, y=400)



# add test
class TestRegistrationPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.label = tk.Label(self, text="Test Registration Page", font=("Arial", 20))
        self.label.pack(pady=50)
        
        self.test_registration_form()
    
    def register_test(self):
       Testcode =self.en1.get()
       Testname = self.en3.get()
       specimentype = self.en4.get()
       department = self.en5.get()
       reportformat =self. en6.get()
       reportingrate =self. en7.get()
       
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
    # Insert data into the "doctors" table
       cursor.execute('''
          INSERT INTO tests (Testcode, Testname, specimentype, department, reportformat, reportingrate)
          VALUES (?, ?, ?, ?, ?, ?)
    ''', (Testcode, Testname, specimentype, department, reportformat, reportingrate))
       conn.commit()

    # Clear the entry fields
       self.en1.delete(0,tk. END)
       self.en3.delete(0, tk.END)
       self.en4.delete(0,tk. END)
       self.en5.delete(0, tk.END)
       self.en6.delete(0,tk. END)
       self.en7.delete(0, tk.END)
    

    def test_registration_form(self):
       lb1 = tk.Label(self, text="Test Code", width=10, font=("arial", 12))
       lb1.place(x=20, y=120)
       self.en1 = tk.Entry(self)
       self.en1.place(x=200, y=120)

       lb3 = tk.Label(self, text="Test Name", width=10, font=("arial", 12))
       lb3.place(x=19, y=140)
       self.en3 = tk.Entry(self)
       self.en3.place(x=200, y=140)

       lb4 = tk.Label(self, text="specimentype", width=13, font=("arial", 12))
       lb4.place(x=19, y=160)
       self.en4 = tk.Entry(self)
       self.en4.place(x=200, y=160)

       lb5 = tk.Label(self, text="department", width=13, font=("arial", 12))
       lb5.place(x=19, y=180)
       self.en5 = tk.Entry(self)
       self.en5.place(x=200, y=180)

       lb6 = tk.Label(self, text="reportformat", width=13, font=("arial", 12))
       lb6.place(x=19, y=200)
       self.en6 = tk.Entry(self)
       self.en6.place(x=200, y=200)

       lb7= tk.Label(self, text="reportingrate", width=13,font=("arial",12))  
       lb7.place(x=19, y=220)  
       self.en7= tk.Entry(self)  
       self.en7.place(x=200, y=220)    

       register_button = tk.Button(self, text="Register", width=10, command=self.register_test)
       register_button.place(x=200, y=400)

 #view test 
class ViewtestDataPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.view_testsaved_data()

    def view_testsaved_data(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Tests")
        doctor_data = cursor.fetchall()

        for row in doctor_data:
            doctor_info = f"Test Code: {row[0]}\Test Name: {row[1]}\nspecimen type: {row[2]}\ndepartment: {row[3]}\nreport format: {row[4]}\nreporting rate: {row[5]}\n\n"
            doctor_label = tk.Label(self, text=doctor_info, font=("arial", 12))
            doctor_label.pack()

        conn.close()


#add refdr 
class refdrRegistrationPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.label = tk.Label(self, text="Patient Registration Page", font=("Arial", 20))
        self.label.pack(pady=50)

        self.setup_refdrregistration_form()
    
    def register_doctor(self):
       code = self.en1.get()
       name = self.en3.get()
       qualification = self.en4.get()
       specialisation = self.en5.get()
       address = self.en6.get()
       mobile = self.en7.get()
       pincode = self.en8.get()
       email = self.en9.get()
    
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
    # Insert data into the "doctors" table
       cursor.execute('''
        INSERT INTO doctors (code, name, qualification, specialisation, address, mobile, pincode, email)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (code, name, qualification, specialisation, address, mobile, pincode, email))
       conn.commit()

    # Clear the entry fields
       self.en1.delete(0, tk.END)
       self.en3.delete(0, tk.END)
       self.en4.delete(0, tk.END)
       self.en5.delete(0, tk.END)
       self.en6.delete(0, tk.END)
       self.en7.delete(0, tk.END)
       self.en8.delete(0, tk.END)
       self.en9.delete(0, tk.END)

    def setup_refdrregistration_form(self):
        lb1 = tk.Label(self, text="Doctor Code", width=10, font=("arial", 12))
        lb1.place(x=20, y=120)
        self.en1 =tk.Entry(self)
        self.en1.place(x=200, y=120)

        lb3 =tk.Label(self, text="Doctor Name", width=10, font=("arial", 12))
        lb3.place(x=19, y=140)
        self.en3 =tk.Entry(self)
        self.en3.place(x=200, y=140)

        lb4 =tk.Label(self, text="Qualification", width=13, font=("arial", 12))
        lb4.place(x=19, y=160)
        self.en4 =tk.Entry(self)
        self.en4.place(x=200, y=160)

        lb5 = tk.Label(self, text="Specialisation", width=13, font=("arial", 12))
        lb5.place(x=19, y=180)
        self.en5 =tk.Entry(self)
        self.en5.place(x=200, y=180)

        lb6 = tk.Label(self, text="Address", width=13, font=("arial", 12))
        lb6.place(x=19, y=200)
        self.en6 =tk.Entry(self)
        self.en6.place(x=200, y=200)

        lb7= tk.Label(self, text="Mobile", width=13,font=("arial",12))  
        lb7.place(x=19, y=220)  
        self.en7= tk.Entry(self)  
        self.en7.place(x=200, y=220)    
  
  
        lb8= tk.Label(self, text="PIN Code", width=13,font=("arial",12))  
        lb8.place(x=19, y=240)  
        self.en8= tk.Entry(self)  
        self.en8.place(x=200, y=240)  

        lb9= tk.Label(self, text="Email ID", width=13,font=("arial",12))  
        lb9.place(x=19, y=260)  
        self.en9=tk.Entry(self)  
        self.en9.place(x=200, y=260) 
        register_button = tk.Button(self, text="Register", width=10, command=self.register_doctor)
        register_button.place(x=200, y=400)


#viewrefdr

class ViewdoctorDataPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.view_doctorsaved_data()

    def view_doctorsaved_data(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM doctors")
        refdoctor_data = cursor.fetchall()

        for row in refdoctor_data:
            refdoctor_info = f"Doctor Code: {row[0]}\nDoctor Name: {row[1]}\nQualification: {row[2]}\nSpecialisation: {row[3]}\nAddress: {row[4]}\nMobile: {row[5]}\nPIN Code: {row[6]}\nEmail ID: {row[7]}\n\n"
            refdrdoctor_label = tk.Label(self, text=refdoctor_info, font=("arial", 12))
            refdrdoctor_label.pack()


        conn.close()




class DashboardApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Dashboard")

        self.main_frame = ttk.Notebook(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.pages = {
            "home": HomePage(self.main_frame),
            "patientregister": PatientRegistrationPage(self.main_frame),
            "viewsaveddata": ViewSavedDataPage(self.main_frame),
            "Add test": TestRegistrationPage(self.main_frame),
            "viewtest":  ViewtestDataPage(self.main_frame),
            "Add refdr":refdrRegistrationPage(self.main_frame),
           "viewrefdr": ViewdoctorDataPage(self.main_frame),
           
        }
        for page_name, page_instance in self.pages.items():
            self.main_frame.add(page_instance, text=page_name.capitalize())

        self.menu_frame = tk.Frame(self.root)
        self.menu_frame.pack()

        for page_name in self.pages:
            button = tk.Button(self.menu_frame, text=page_name.capitalize(),
                               command=lambda name=page_name: self.show_page(name))
            button.pack(side=tk.LEFT, padx=10)
            

    def show_page(self, page_name):
        self.main_frame.select(self.pages[page_name])

def main():
    root = tk.Tk()
    app = DashboardApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
