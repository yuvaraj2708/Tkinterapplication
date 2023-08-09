import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create the visit table
cursor.execute('''CREATE TABLE IF NOT EXISTS visit (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  patient_code TEXT,
                  patient_name TEXT,
                  patient_category TEXT,
                  ref_doctor TEXT,
                  selected_test TEXT,
                  FOREIGN KEY (patient_code) REFERENCES patientregister (patientcode)
                 )''')

conn.commit()
conn.close()
