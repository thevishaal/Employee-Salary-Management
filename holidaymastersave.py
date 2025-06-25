import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showholidaymastersave():

    t=tkinter.Tk()
    t.geometry('500x350')
    
    d=Canvas(t,width=500,height=350)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,330,fill='black')
    d.create_rectangle(25,25,475,325,fill='light green')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select empid from employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1['values']=lt
        
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=int(e3.get())
        sql="insert into holidaymaster values(%d,'%s',%d)"%(xa,xb,xc)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Empid %d is recorded'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        db.close()
    
        
    h1=Label(d,text='HOLIDAY MASTER',font=('arial',25),bg='light green')
    h1.place(x=100,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='light green')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Holiday Name',font=('biome',15),bg='light green')
    a2.place(x=80,y=200)
    e2=Entry(d,width=25)
    e2.place(x=80,y=230)
    
    a3=Label(d,text='No of Leaves',font=('biome',15),bg='light green')
    a3.place(x=270,y=200)
    e3=Entry(d,width=25)
    e3.place(x=270,y=230)
    
    bt=Button(d,text='Save',font=('biome',15),bg='light green',command=savedata)
    bt.place(x=200,y=270)
    
    t.mainloop()
    
#showholidaymastersave()