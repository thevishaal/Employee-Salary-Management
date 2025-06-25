import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showcompanyupdate():
    
    t=tkinter.Tk()
    t.geometry('700x500')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select compname,address,city,phone,email from companymaster where compid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        db.commit()
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        xd=e4.get()
        xe=e5.get()
        xf=e6.get()
        sql="update companymaster set compname='%s',address='%s',city='%s',phone='%s',email='%s' where compid=%d"%(xb,xc,xd,xe,xf,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is updated.'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select compid from companymaster "
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt    
        
    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='#FFEDD1')
    
    h1=Label(t,text='COMPANY MASTER',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=180,y=40)
    
    a1=Label(d,text='Comp ID',font=('biome',15),bg='#FFEDD1')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)
    
    bt1=Button(d,text='Find',font=('biome',15),bg='#FFEDD1',command=finddata)
    bt1.place(x=265,y=130)
    
    a2=Label(d,text='Comp Name',font=('biome',15),bg='#FFEDD1')
    a2.place(x=80,y=220)
    e2=Entry(d,width=25)
    e2.place(x=80,y=250)

    a3=Label(d,text='Address',font=('biome',15),bg='#FFEDD1')
    a3.place(x=265,y=220)
    e3=Entry(d,width=25)
    e3.place(x=265,y=250)
    
    a4=Label(d,text='City',font=('biome',15),bg='#FFEDD1')
    a4.place(x=460,y=220)
    e4=Entry(d,width=25)
    e4.place(x=460,y=250)
    
    a5=Label(d,text='Phone',font=('arial',15),bg='#FFEDD1')
    a5.place(x=80,y=320)
    e5=Entry(d,width=25)
    e5.place(x=80,y=350)
    
    a6=Label(d,text='Email',font=('biome',15),bg='#FFEDD1')
    a6.place(x=265,y=320)
    e6=Entry(d,width=25)
    e6.place(x=265,y=350)
    
    bt2=Button(d,text='Update',font=('biome',15),bg='#FFEDD1',command=updatedata)
    bt2.place(x=265,y=410)
    
    t.mainloop()
    
#showcompanyupdate()