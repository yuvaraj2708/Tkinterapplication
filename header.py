import tkinter as tk
from tkinter import ttk
import sqlite3
import qrcode

class HomePage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        
        # Configure the AquaMarine style
        self.configure(bg="aquamarine")
        
        label = tk.Label(self, text="Home Page", font=("Arial", 20), fg="white", bg="aquamarine")
        label.pack(pady=50)


#patient registration

class PatientRegistrationPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.configure(bg="aquamarine")
        self.label = tk.Label(self, text="Patient Registration Page", font=("Arial", 20),bg="aquamarine")
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
        # Insert data into the "patientregister" table
        cursor.execute('''
            INSERT INTO patientregister(patientcode, patientname, title, dob, age, emailid, phonenumber, gender)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patientcode, patientname, title, dob, age, emailid, phonenumber, gender))
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
        self.setup_registration_form() 
    def generate_uhid(self):
      conn = sqlite3.connect("student.db")
      cursor = conn.cursor()

    # Get the current maximum UHID from the database
      cursor.execute("SELECT MAX(`patientcode`) FROM patientregister")
      max_uhid = cursor.fetchone()[0]

      if max_uhid:
        # Extract the numeric part of the UHID and increment it
        numeric_part = int(max_uhid[1:]) + 1
        new_uhid = f"P{numeric_part:05d}"
      else:
        # If no UHID exists, start from P00001
        new_uhid = "P00001"

      conn.close()
      return new_uhid

  
  
    def setup_registration_form(self):
        uhid = self.generate_uhid()
        lb1 = tk.Label(self, text="patient code", width=10, font=("arial", 12))
        lb1.place(x=20, y=120)
        self.en1 = tk.Entry(self)
        self.en1.insert(0, uhid)  # Set the generated UHID as the default value
        self.en1.config(state="readonly")  # Make the UHID field read-only
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

class ViewSavedDataPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.view_patientsaved_data()

    def view_patientsaved_data(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM patientregister")
        patient_data = cursor.fetchall()

        # Create a Treeview widget
        self.tree = ttk.Treeview(self, columns=("Patient Code", "Patient Name", "Title", "Date of Birth", "Age", "Email ID", "Phone Number", "Gender"), show="headings")
        
        # Define column headings
        self.tree.heading("Patient Code", text="Patient Code")
        self.tree.heading("Patient Name", text="Patient Name")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Date of Birth", text="Date of Birth")
        self.tree.heading("Age", text="Age")
        self.tree.heading("Email ID", text="Email ID")
        self.tree.heading("Phone Number", text="Phone Number")
        self.tree.heading("Gender", text="Gender")
        
        self.tree.column("Patient Code", width=40)
        self.tree.column("Patient Name", width=40)
        self.tree.column("Title", width=40)
        self.tree.column("Date of Birth", width=40)
        self.tree.column("Age", width=40)
        self.tree.column("Email ID", width=40)
        self.tree.column("Phone Number", width=40)
        self.tree.column("Gender", width=40)
        
       
        
        # Insert data into the table
        for row in patient_data:
            self.tree.insert("", "end", values=row)
        
        # Add Treeview widget to the frame
        self.tree.pack(fill="both", expand=True)
        
        for patient_row in patient_data:
          patient_id = patient_row[0]  # Assuming visit_id is the first column in the visit table
          delete_button = tk.Button(self, text="Delete", command=lambda vid=patient_id: self.delete_patient(vid))
          delete_button.pack()
          
          
        # Add a delete button
        self.addvisit_button = tk.Button(self, text="add visit", command=self.add_visit)
        self.addvisit_button.pack()
        conn.close()
         
    def delete_patient(self, patient_id):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM patientregister WHERE id=?", (patient_id,))
        conn.commit()

        # Delete the corresponding item from the Treeview
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values and str(patient_id) == values[0]:
                self.tree.delete(item)

        conn.close()
            
            # Remove the item from the tree
    def add_visit(self):
        selected_item = self.tree.selection()
        if selected_item:
            item_id = selected_item[0]
            values = self.tree.item(item_id, "values")
            self.selected_patient = {
                "patient_code": values[0],
                "patient_name": values[1],
                "title": values[2],
                "date_of_birth": values[3],
                "age": values[4],
                "email_id": values[5],
                "phone_number": values[6],
                "gender": values[7]
            }
            
            # Open the window for adding visit details and pass the selected patient's details
            self.open_add_visit_window()

    def open_add_visit_window(self):
        if self.selected_patient:
            add_visit_page = ViewVisitDataPage(self, patient_details=self.selected_patient)
            add_visit_page.pack()
    
            
#add visit
class ViewVisitDataPage(tk.Frame):
    def __init__(self, master=None, patient_details=None, **kwargs):
        super().__init__(master, **kwargs)
        self.patient_details = patient_details
        self.patient_category_var = tk.StringVar()
        self.ref_doctor_var = tk.StringVar()
        self.select_test_var = tk.StringVar()
        
        self.display_patient_details()
        self.display_additional_fields()
        self.display_buttons()

    def display_patient_details(self):
        label = tk.Label(self, text="Patient Details")
        label.pack()
        
        for field, value in self.patient_details.items():
            detail_label = tk.Label(self, text=f"{field}: {value}")
            detail_label.pack()

    def display_additional_fields(self):
        # Patient Category
        patient_category_label = tk.Label(self, text="Patient Category")
        patient_category_label.pack()
        patient_category_entry = tk.Entry(self, textvariable=self.patient_category_var)
        patient_category_entry.pack()

        # Ref Dr
        ref_doctor_label = tk.Label(self, text="Ref Dr")
        ref_doctor_label.pack()
        ref_doctor_entry = tk.Entry(self, textvariable=self.ref_doctor_var)
        ref_doctor_entry.pack()

        # Select Test
        select_test_label = tk.Label(self, text="Select Test")
        select_test_label.pack()
        select_test_entry = tk.Entry(self, textvariable=self.select_test_var)
        select_test_entry.pack()

    def display_buttons(self):
        save_button = tk.Button(self, text="Save Visit", command=self.save_visit)
        save_button.pack()

    def save_visit(self):
        patient_code = self.patient_details["patient_code"]
        patient_name = self.patient_details["patient_name"]
        patient_category = self.patient_category_var.get()
        ref_doctor = self.ref_doctor_var.get()
        selected_test = self.select_test_var.get()

        # Connect to the visit database
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        # Insert visit details into the visit table
        cursor.execute("INSERT INTO visit (patient_code, patient_name, patient_category, ref_doctor, selected_test) VALUES (?, ?, ?, ?, ?)",
                       (patient_code, patient_name, patient_category, ref_doctor, selected_test))

        conn.commit()
        conn.close()
        
        self.destroy()
        # Create and pack the ViewAllVisitsFrame
        view_all_visits_frame = ViewAllVisitsFrame(self.master)
        view_all_visits_frame.pack()

class ViewAllVisitsFrame(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.view_all_visits()

    def view_all_visits(self):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM visit")
        visit_data = cursor.fetchall()

        # Create a Treeview widget
        self.tree = ttk.Treeview(self, columns=("Visit ID", "Patient Code", "Patient Name", "Patient Category", "Ref Dr", "Selected Test", "Delete"), show="headings", height=10)

        # Define column headings
        self.tree.heading("Visit ID", text="Visit ID")
        self.tree.heading("Patient Code", text="Patient Code")
        self.tree.heading("Patient Name", text="Patient Name")
        self.tree.heading("Patient Category", text="Patient Category")
        self.tree.heading("Ref Dr", text="Ref Dr")
        self.tree.heading("Selected Test", text="Selected Test")
        self.tree.heading("Delete", text="Delete")
        
        self.tree.column("Visit ID", width=40)
        self.tree.column("Patient Code", width=60)
        self.tree.column("Patient Name", width=80)
        self.tree.column("Patient Category", width=100)
        self.tree.column("Ref Dr", width=120)
        self.tree.column("Selected Test", width=150)
        self.tree.column("Delete", width=120)  # New column width

        
        # Insert data into the table
        for visit_row in visit_data:
            visit_id = visit_row[0]
            
            delete_button = tk.Button(self.tree, text="Delete", command=lambda vid=visit_id: self.delete_visit(vid))
            delete_button.pack()
            
            qrcode_button = tk.Button(self.tree, text="Generate QR Code", command=lambda row=visit_row: self.generate_qr_code(row))
            qrcode_button.pack()

            self.tree.insert("", "end", values=visit_row + (delete_button, qrcode_button), tags=("button",))

            self.tree.insert("", "end", values=visit_row + (delete_button, qrcode_button), tags=("button",))
        # Set row height
        self.tree['height'] = len(visit_data)

        # Add Treeview widget to the frame
        self.tree.pack(fill="both", expand=True)

    def delete_visit(self, visit_id):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM visit WHERE id=?", (visit_id,))
        conn.commit()

        # Delete the corresponding item from the Treeview
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values and visit_id == values[0]:
                self.tree.delete(item)

        conn.close()
    
    def generate_qr_code(self, row):
        patient_id = row[0]  # Assuming patient_id is the first column in the visit table
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM visit WHERE id=?", (patient_id,))
        visit_data = cursor.fetchone()
        conn.close()

        qr_code_data = f"Patient Name: {visit_data[1]}\nPatient Code: {visit_data[2]}\nPatient Category: {visit_data[3]}\nRef Dr: {visit_data[4]}\nSelected Test: {visit_data[5]}"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(qr_code_data)
        qr.make(fit=True)
        qr_img = qr.make_image(fill_color="black", back_color="white")

        qr_img.show()  


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
                
    def generate_testuhid(self):
      conn = sqlite3.connect("student.db")
      cursor = conn.cursor()

    # Get the current maximum UHID from the database
      cursor.execute("SELECT MAX(`Testcode`) FROM tests")
      max_testuhid = cursor.fetchone()[0]

      if max_testuhid:
        # Extract the numeric part of the UHID and increment it
        numeric_part = int(max_testuhid[1:]) + 1
        new_testuhid = f"T{numeric_part:05d}"
      else:
        # If no UHID exists, start from P00001
        new_testuhid = "T00001"

      conn.close()
      return new_testuhid
  
    def test_registration_form(self):
       uhid = self.generate_testuhid()
       lb1 = tk.Label(self, text="Test code", width=10, font=("arial", 12))
       lb1.place(x=20, y=120)
       self.en1 = tk.Entry(self)
       self.en1.insert(0, uhid)  # Set the generated UHID as the default value
       self.en1.config(state="readonly")  # Make the UHID field read-only
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
        
        self.tree = ttk.Treeview(self, columns=("Test Code", "Test Name", "specimen type", "department", "report format", "reporting rate"), show="headings")
        
        # Define column headings
        self.tree.heading("Test Code", text="Test Code")
        self.tree.heading("Test Name", text="Test Name")
        self.tree.heading("specimen type", text="specimen type")
        self.tree.heading("department", text="ndepartment")
        self.tree.heading("report format", text="report format")
        self.tree.heading("reporting rate", text="reporting rate")
        
        self.tree.column("Test Code", width=40)
        self.tree.column("Test Name", width=40)
        self.tree.column("specimen type", width=40)
        self.tree.column("department", width=40)
        self.tree.column("report format", width=40)
        self.tree.column("reporting rate", width=40)
        
        for row in doctor_data:
            self.tree.insert("", "end", values=row)
        
        # Add Treeview widget to the frame
        self.tree.pack(fill="both", expand=True)
        for tests_row in doctor_data:
            tests_id = tests_row[0]
            
            delete_button = tk.Button(self.tree, text="Delete", command=lambda vid=tests_id: self.delete_test(vid))
            delete_button.pack()
               
    def delete_test(self, test_id):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM tests WHERE id=?", (test_id,))
        conn.commit()

        # Delete the corresponding item from the Treeview
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values and test_id == values[0]:
                self.tree.delete(item)
                
        
        conn.close()


#add refdr 
class refdrRegistrationPage(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        
        self.label = tk.Label(self, text="Doctor Registration Page", font=("Arial", 20))
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
    
    def generate_refdruhid(self):
      conn = sqlite3.connect("student.db")
      cursor = conn.cursor()

    # Get the current maximum UHID from the database
      cursor.execute("SELECT MAX(`code`) FROM doctors")
      max_doctoruhid = cursor.fetchone()[0]

      if max_doctoruhid:
        # Extract the numeric part of the UHID and increment it
        numeric_part = int(max_doctoruhid[1:]) + 1
        new_doctoruhid = f"D{numeric_part:05d}"
      else:
        # If no UHID exists, start from P00001
        new_doctoruhid = "D00001"

      conn.close()
      return new_doctoruhid
  
    
       
    
    def setup_refdrregistration_form(self):
        uhid = self.generate_refdruhid()
        lb1 = tk.Label(self, text="Doctor code", width=10, font=("arial", 12))
        lb1.place(x=20, y=120)
        self.en1 = tk.Entry(self)
        self.en1.insert(0, uhid)  # Set the generated UHID as the default value
        self.en1.config(state="readonly")  # Make the UHID field read-only
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
         
        self.tree = ttk.Treeview(self, columns=("Doctor Code", "Doctor Name", "Qualification", "Specialisation", "Address", "Mobile","PIN Code","Email ID"), show="headings")
        
        # Define column headings
        self.tree.heading("Doctor Code", text="Test Code")
        self.tree.heading("Doctor Name", text="Doctor Name")
        self.tree.heading("Qualification", text="Qualification")
        self.tree.heading("Specialisation", text="Specialisation")
        self.tree.heading("Address", text="Address")
        self.tree.heading("Mobile", text="Mobile")
        self.tree.heading("PIN Code", text="PIN Code")
        self.tree.heading("Email ID", text="Email ID")
        
        self.tree.column("Doctor Code", width=40)
        self.tree.column("Doctor Name", width=40)
        self.tree.column("Qualification", width=40)
        self.tree.column("Specialisation", width=40)
        self.tree.column("Address", width=40)
        self.tree.column("Mobile", width=40)
        self.tree.column("PIN Code", width=40)
        self.tree.column("Email ID", width=40)
   
        for row in refdoctor_data:
            self.tree.insert("", "end", values=row)
        
        # Add Treeview widget to the frame
        self.tree.pack(fill="both", expand=True)

        conn.close() 
     
        for doctor_row in refdoctor_data:
            doctor_id = doctor_row[0]
            
            delete_button = tk.Button(self.tree, text="Delete", command=lambda vid=doctor_id: self.delete_refdr(vid))
            delete_button.pack()
               
    def delete_refdr(self, test_id):
        conn = sqlite3.connect("student.db")
        cursor = conn.cursor()

        cursor.execute("DELETE FROM doctors WHERE id=?", (test_id,))
        conn.commit()

        # Delete the corresponding item from the Treeview
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if values and test_id == values[0]:
                self.tree.delete(item)
                
        
        conn.close()




class DashboardApp:
    def __init__(self, root):
        self.root = root
        
        self.root.title("Dashboard")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(f"{screen_width}x{screen_height}")
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
           "registrationsummary":ViewAllVisitsFrame(self.main_frame)
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
