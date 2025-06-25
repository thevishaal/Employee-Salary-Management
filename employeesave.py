import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showemployeesave():
    t=tkinter.Tk()
    t.geometry('700x500')

    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='white')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select deptid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e7['values']=lt
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        xg=int(e7.get())
        sql="insert into employee values(%d,'%s','%s','%s','%s','%s',%d)"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Your data is saved.')
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        db.close()
    
    h1=Label(d,text='EMPLOYEE DETAIL',font=('arial',25),bg='white',fg='#000080')
    h1.place(x=180,y=40)

    a1=Label(d,text='Emp ID',font=('biome',15),bg='white')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)

    a2=Label(d,text='Name',font=('biome',15),bg='white')
    a2.place(x=265,y=120)
    e2=Entry(d,width=25)
    e2.place(x=265,y=150)

    a3=Label(d,text='City',font=('biome',15),bg='white')
    a3.place(x=460,y=120)
    e3=Entry(d,width=25)
    e3.place(x=460,y=150)

    a4=Label(d,text='Address',font=('biome',15),bg='white')
    a4.place(x=80,y=220)
    e4=Entry(d,width=25)
    e4.place(x=80,y=250)

    a5=Label(d,text='Email',font=('biome',15),bg='white')
    a5.place(x=265,y=220)
    e5=Entry(d,width=25)
    e5.place(x=265,y=250)

    a6=Label(d,text='Phone',font=('biome',15),bg='white')
    a6.place(x=460,y=220)
    e6=Entry(d,width=25)
    e6.place(x=460,y=250)

    a7=Label(d,text='Dept ID',font=('biome',15),bg='white')
    a7.place(x=80,y=320)
    e7=ttk.Combobox(d)
    filldata()
    e7.place(x=80,y=350)

    bt=Button(d,text='Save',font=('biome',15),bg='white',command=savedata)
    bt.place(x=280,y=330)
    
    t.mainloop()
    
#showemployeesave()
    