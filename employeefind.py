import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showemployeefind():
    
    t=tkinter.Tk()
    t.geometry('700x500')

    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='white')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select name,city,address,email,phone,deptid from employee where empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        db.commit()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        e6.insert(0,data[4])
        e7.insert(0,str(data[5]))
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select empid from employee"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.commit()
        db.commit()
        e1['values']=lt
            
    
    h1=Label(d,text='EMPLOYEE DETAIL',font=('arial',25),bg='white',fg='#000080')
    h1.place(x=180,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='white')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)
    
    bt=Button(d,text='Find',font=('biome',15),bg='white',command=finddata)
    bt.place(x=265,y=130)
    
    a2=Label(d,text='Name',font=('biome',15),bg='white')
    a2.place(x=80,y=220)
    e2=Entry(d,width=25)
    e2.place(x=80,y=250)

    a3=Label(d,text='City',font=('biome',15),bg='white')
    a3.place(x=265,y=220)
    e3=Entry(d,width=25)
    e3.place(x=265,y=250)

    a4=Label(d,text='Address',font=('biome',15),bg='white')
    a4.place(x=460,y=220)
    e4=Entry(d,width=25)
    e4.place(x=460,y=250)

    a5=Label(d,text='Email',font=('arial',15),bg='white')
    a5.place(x=80,y=320)
    e5=Entry(d,width=25)
    e5.place(x=80,y=350)
    
    a6=Label(d,text='Phone',font=('biome',15),bg='white')
    a6.place(x=265,y=320)
    e6=Entry(d,width=25)
    e6.place(x=265,y=350)
    
    a7=Label(d,text='Dept ID',font=('biome',15),bg='White')
    a7.place(x=460,y=320)
    e7=Entry(d,width=25)
    e7.place(x=460,y=350)
    
    t.mainloop()
    
#showemployeefind()