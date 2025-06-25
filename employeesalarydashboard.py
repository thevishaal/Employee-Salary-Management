import tkinter 
from tkinter import * 
import pymysql
from employeesalarysave import *
from employeesalaryfind import *
from employeesalarydelete import *
from employeesalaryupdate import *
from employeesalarytext import *
from employeesalarynavigate import *

def showemployeesalarydashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    def cts():
        t.destroy()
    
    d=Canvas(t,width=500,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,480,480,fill='black')
    d.create_rectangle(25,25,475,475,fill='light pink')

    h1=Label(d,text='EMP SALARY DASHBOARD',font=('arial',23),bg='light pink')
    h1.place(x=52,y=40)
    
    bt1=Button(d,text='Save',font=('Biome',15),bg='cyan',command=showemployeesalarysave)
    bt1.place(x=80,y=120)
    
    bt2=Button(d,text='Find',font=('Biome',15),bg='cyan',command=showemployeesalaryfind)
    bt2.place(x=200,y=120)
    
    bt3=Button(d,text='Delete',font=('Biome',15),bg='cyan',command=showemployeesalarydelete)
    bt3.place(x=320,y=120)
    
    bt4=Button(d,text='Update',font=('Biome',15),bg='cyan',command=showemployeesalaryupdate)
    bt4.place(x=80,y=220)
    
    bt5=Button(d,text='Show',font=('Biome',15),bg='cyan',command=showemployeesalarytext)
    bt5.place(x=200,y=220)
    
    bt6=Button(d,text='Navigate',font=('Biome',15),bg='cyan',command=showemployeesalarynavigate)
    bt6.place(x=320,y=220)
    
    bt7=Button(d,text='CLOSE',font=('Biome',20),bg='cyan',command=cts)
    bt7.place(x=170,y=320)
    
    t.mainloop()
    
#showemployeesalarydashboard()