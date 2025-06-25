import tkinter 
from tkinter import * 
from companydashboard import *
from departmentdashboard import *
from hodtabledashboard import *
from employeedashboard import *
from employeesalarydashboard import *
from holidaymasterdashboard import *
from paymentdashboard import *

def showmaindashboard():

    t=tkinter.Tk()
    t.geometry('600x500')
    
    def cts():
        t.destroy()
    
    d=Canvas(t,width=600,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,580,480,fill='black')
    d.create_rectangle(25,25,575,475,fill='#3ff8f5')

    h1=Label(d,text='MAIN DASHBOARD',font=('arial',25),bg='#3ff8f5')
    h1.place(x=150,y=40)
    
    bt1=Button(d,text='Company Master',font=('Biome',15),bg='#d5fb22',command=showcompanydashboard)
    bt1.place(x=50,y=120)
    
    bt2=Button(d,text='Department',font=('Biome',15),bg='#d5fb22',command=showdepartmentdashboard)
    bt2.place(x=250,y=120)
    
    bt3=Button(d,text='HOD TABLE',font=('Biome',15),bg='#d5fb22',command=showhodtabledashboard)
    bt3.place(x=420,y=120)
    
    bt4=Button(d,text='Employee',font=('Biome',15),bg='#d5fb22',command=showemployeedashboard)
    bt4.place(x=100,y=220)
    
    bt5=Button(d,text='Employee Salary',font=('Biome',15),bg='#d5fb22',command=showemployeesalarydashboard)
    bt5.place(x=290,y=220)
    
    bt6=Button(d,text='Holiday Master',font=('Biome',15),bg='#d5fb22',command=showholidaymasterdashboard)
    bt6.place(x=80,y=320)
    
    bt7=Button(d,text='Payment',font=('Biome',15),bg='#d5fb22',command=showpaymentdashboard)
    bt7.place(x=320,y=320)
    
    bt8=Button(d,text='CLOSE',font=('Biome',20),bg='#d5fb22',fg='red',command=cts)
    bt8.place(x=220,y=400)

    t.mainloop()
    
showmaindashboard()