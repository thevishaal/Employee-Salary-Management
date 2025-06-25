import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

def showcompanysave():

    t=tkinter.Tk()
    t.geometry('700x500')
    
    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='#FFEDD1')
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        sql="insert into companymaster values(%d,'%s','%s','%s','%s','%s')"%(xa,xb,xc,xd,xe,xf)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','Your %s company is recorded.'%(xb))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        db.close()
    
    h1=Label(d,text='COMPANY MASTER',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=170,y=40)
    
    a1=Label(d,text='Comp ID',font=('biome',15),bg='#FFEDD1')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Comp Name',font=('biome',15),bg='#FFEDD1')
    a2.place(x=270,y=120)
    e2=Entry(d,width=25)
    e2.place(x=270,y=150)
    
    a3=Label(d,text='Address',font=('biome',15),bg='#FFEDD1')
    a3.place(x=460,y=120)
    e3=Entry(d,width=25)
    e3.place(x=460,y=150)
    
    a4=Label(d,text='City',font=('biome',15),bg='#FFEDD1')
    a4.place(x=80,y=220)
    e4=Entry(d,width=25)
    e4.place(x=80,y=250)
    
    a5=Label(d,text='Phone',font=('biome',15),bg='#FFEDD1')
    a5.place(x=270,y=220)
    e5=Entry(d,width=25)
    e5.place(x=270,y=250)
    
    a6=Label(d,text='Email',font=('biome',15),bg='#FFEDD1')
    a6.place(x=460,y=220)
    e6=Entry(d,width=25)
    e6.place(x=460,y=250)
    
    bt=Button(d,text='Save',font=('biome',15),bg='#FFEDD1',command=savedata)
    bt.place(x=280,y=310)
    
    t.mainloop()
    
#showcompanysave()