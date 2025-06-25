import tkinter 
from tkinter import * 
import pymysql
from companysave import *
from companyfind import *
from companydelete import *
from companyupdate import *
from companytext import *
from companynavigate import *

def showcompanydashboard():
    
    t=tkinter.Tk()
    t.geometry('500x500')
    
    def cts():
        t.destroy()
    
    d=Canvas(t,width=500,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20,20,480,480,fill='black')
    d.create_rectangle(25,25,475,475,fill='#FFEDD1')

    h1=Label(d,text='COMPANY DASHBOARD',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=55,y=40)
    
    bt1=Button(d,text='Save',font=('Biome',15),bg='#FFEDD1',command=showcompanysave)
    bt1.place(x=80,y=120)
    
    bt2=Button(d,text='Find',font=('Biome',15),bg='#FFEDD1',command=showcompanyfind)
    bt2.place(x=200,y=120)
    
    bt3=Button(d,text='Delete',font=('Biome',15),bg='#FFEDD1',command=showcompanydelete)
    bt3.place(x=320,y=120)
    
    bt4=Button(d,text='Update',font=('Biome',15),bg='#FFEDD1',command=showcompanyupdate)
    bt4.place(x=80,y=220)
    
    bt5=Button(d,text='Show',font=('Biome',15),bg='#FFEDD1',command=showcompanytext)
    bt5.place(x=200,y=220)
    
    bt6=Button(d,text='Navigate',font=('Biome',15),bg='#FFEDD1',command=showcompanynavigate)
    bt6.place(x=320,y=220)
    
    bt7=Button(d,text='CLOSE',font=('Biome',20),bg='#FFEDD1',command=cts)
    bt7.place(x=170,y=320)
    
    t.mainloop()
    
#showcompanydashboard()