from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("registration form")  
  
lb1= Label(base, text="UHID", width=10, font=("arial",12))  
lb1.place(x=19, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
  
lb3= Label(base, text="PATIENT NAME", width=10, font=("arial",12))  
lb3.place(x=19, y=140)  
en3= Entry(base)  
en3.place(x=200, y=140)  

list_of_cntry = ("MR", "MRS", "SMT", "DR")  
cv = StringVar()  
drplist= OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("MR")  
lb2= Label(base, text="TITLE", width=13,font=("arial",12))  
lb2.place(x=19,y=160)  
drplist.place(x=200, y=160) 

lb4= Label(base, text="DOB", width=13,font=("arial",12))  
lb4.place(x=19, y=180)  
en4= Entry(base)  
en4.place(x=200, y=180)  

lb4= Label(base, text="AGE", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  

lb4= Label(base, text="EMAIL ID", width=13,font=("arial",12))  
lb4.place(x=19, y=220)  
en4= Entry(base)  
en4.place(x=200, y=220)    
  
  
lb4= Label(base, text="PHONE NUMBER", width=13,font=("arial",12))  
lb4.place(x=19, y=240)  
en4= Entry(base)  
en4.place(x=200, y=240)  
  
lb5= Label(base, text="GENDER", width=15, font=("arial",12))  
lb5.place(x=19, y=260)  
vars = IntVar()  
Radiobutton(base, text="Male", padx=5,variable=vars, value=1).place(x=120, y=260)  
Radiobutton(base, text="Female", padx =10,variable=vars, value=2).place(x=300,y=260)  
Radiobutton(base, text="others", padx=15, variable=vars, value=3).place(x=360,y=260)  
  
lb4= Label(base, text="Patient Category", width=13,font=("arial",12))  
lb4.place(x=19, y=280)  
en4= Entry(base)  
en4.place(x=200, y=280)

lb4= Label(base, text="Ref Dr", width=13,font=("arial",12))  
lb4.place(x=19, y=300)  
en4= Entry(base)  
en4.place(x=200, y=300)

lb4= Label(base, text="Select Test", width=13,font=("arial",12))  
lb4.place(x=19, y=320)  
en4= Entry(base)  
en4.place(x=200, y=320)


  
 
  
Button(base, text="Register", width=10).place(x=200,y=400)  
base.mainloop()  