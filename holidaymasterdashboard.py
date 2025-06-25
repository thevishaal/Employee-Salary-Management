import tkinter 
from tkinter import * 
import pymysql
from holidaymastersave import *
from holidaymasterfind import *
from holidaymasterdelete import *
from holidaymasterupdate import *
from holidaymastertext import *
from holidaymasternavigate import *

def showholidaymasterdashboard():

    t=tkinter.Tk()
    t.geometry('500x500')
    
    def cts():
        t.destroy()
    
    d=Canvas(t,width=500,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,480,480,fill='black')
    d.create_rectangle(25,25,475,475,fill='light green')

    h1=Label(d,text='HOLIDAY MASTER DASHBOARD',font=('arial',20),bg='light green')
    h1.place(x=42,y=40)
    
    bt1=Button(d,text='Save',font=('Biome',15),bg='light blue',command=showholidaymastersave)
    bt1.place(x=80,y=120)
    
    bt2=Button(d,text='Find',font=('Biome',15),bg='light Blue',command=showholidaymasterfind)
    bt2.place(x=200,y=120)
    
    bt3=Button(d,text='Delete',font=('Biome',15),bg='light Blue',command=showholidaymasterdelete)
    bt3.place(x=320,y=120)
    
    bt4=Button(d,text='Update',font=('Biome',15),bg='light Blue',command=showholidaymasterupdate)
    bt4.place(x=80,y=220)
    
    bt5=Button(d,text='Show',font=('Biome',15),bg='light Blue',command=showholidaymastertext)
    bt5.place(x=200,y=220)
    
    bt6=Button(d,text='Navigate',font=('Biome',15),bg='light Blue',command=showholidaymasternavigate)
    bt6.place(x=320,y=220)
    
    bt7=Button(d,text='CLOSE',font=('Biome',20),bg='light Blue',command=cts)
    bt7.place(x=170,y=320)
    
    t.mainloop()
    
#showholidaymasterdashboard()