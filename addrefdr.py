from tkinter import *  
base = Tk()  
base.geometry("500x500")  
base.title("Add Doctor")  
  
  
lb1= Label(base, text="Doctor Code", width=10, font=("arial",12))  
lb1.place(x=20, y=120)  
en1= Entry(base)  
en1.place(x=200, y=120)  
  
lb3= Label(base, text="Doctor Name", width=10, font=("arial",12))  
lb3.place(x=19, y=160)  
en3= Entry(base)  
en3.place(x=200, y=160)  

list_of_cntry = ("MR", "MRS", "SMT", "DR")  
cv = StringVar()  
drplist= OptionMenu(base, cv, *list_of_cntry)  
drplist.config(width=15)  
cv.set("MR")  
lb2= Label(base, text="Qualification", width=13,font=("arial",12))  
lb2.place(x=14,y=280)  
drplist.place(x=200, y=275) 

lb4= Label(base, text="Specialisation", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  


lb4= Label(base, text="Address", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  
lb4= Label(base, text="Mobile", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)    
  
  
lb4= Label(base, text="PIN Code", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200)  

lb4= Label(base, text="Email ID", width=13,font=("arial",12))  
lb4.place(x=19, y=200)  
en4= Entry(base)  
en4.place(x=200, y=200) 

  

 
  
lb6= Label(base, text="Enter Password", width=13,font=("arial",12))  
lb6.place(x=19, y=320)  
en6= Entry(base, show='*')  
en6.place(x=200, y=320)  
  
lb7= Label(base, text="Re-Enter Password", width=15,font=("arial",12))  
lb7.place(x=21, y=360)  
en7 =Entry(base, show='*')  
en7.place(x=200, y=360)  
  
Button(base, text="Register", width=10).place(x=200,y=400)  
base.mainloop()  