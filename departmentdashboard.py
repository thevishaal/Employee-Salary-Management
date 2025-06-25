import tkinter 
from tkinter import * 
import pymysql
from departmentsave import *
from departmentfind import *
from departmentdelete import *
from departmentupdate import *
from departmenttext import *
from departmentnavigate import *

def showdepartmentdashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    def cts():
        t.destroy()
    
    d=Canvas(t,width=500,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,480,480,fill='black')
    d.create_rectangle(25,25,475,475,fill='sky blue')

    h1=Label(d,text='DEPARTMENT DASHBOARD',font=('arial',22),bg='sky blue')
    h1.place(x=55,y=40)
    
    bt1=Button(d,text='Save',font=('Biome',15),bg='skyblue',command=showdepartmentsave)
    bt1.place(x=80,y=120)
    
    bt2=Button(d,text='Find',font=('Biome',15),bg='sky blue',command=showdepartmentfind)
    bt2.place(x=200,y=120)
    
    bt3=Button(d,text='Delete',font=('Biome',15),bg='sky blue',command=showdepartmentdelete)
    bt3.place(x=320,y=120)
    
    bt4=Button(d,text='Update',font=('Biome',15),bg='sky blue',command=showdepartmentupdate)
    bt4.place(x=80,y=220)
    
    bt5=Button(d,text='Show',font=('Biome',15),bg='sky blue',command=showdepartmenttext)
    bt5.place(x=200,y=220)
    
    bt6=Button(d,text='Navigate',font=('Biome',15),bg='sky blue',command=showdepartmentnavigate)
    bt6.place(x=320,y=220)
    
    bt7=Button(d,text='CLOSE',font=('Biome',20),bg='sky blue',command=cts)
    bt7.place(x=170,y=320)
    
    t.mainloop()
    
#showdepartmentdashboard()