import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def showpaymentupdate():

    t=tkinter.Tk()
    t.geometry('700x500')

    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='#FFEDD1')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select month,deptid , noofleaves, payment, tax, netpay from payment where empid=%d "%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        bte1.delete(0,100)
        bte2.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        e5.insert(0,data[3])
        bte1.insert(0,data[4])
        bte2.insert(0,data[5])
        db.commit()
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=int(e3.get())
        xd=int(e4.get())
        xe=int(e5.get())
        xf=float(bte1.get())
        xg=float(bte2.get())
        sql="update payment set month='%s',deptid=%d,noofleaves=%d,payment=%d,tax=%f,netpay=%f where empid=%d"%(xb,xc,xd,xe,xf,xg,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is updated,'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        bte1.delete(0,100)
        bte2.delete(0,100)
        db.close()
        
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select empid from payment"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.commit()
        db.close()
        e1['values']=lt
    
    h1=Label(t,text='EMPLOYEE PAYMENT',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=170,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='#FFEDD1')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)

    bt=Button(d,text='Find',font=('biome',15),bg='#FFEDD1',command=finddata)
    bt.place(x=265,y=130)

    a2=Label(d,text='Month',font=('biome',15),bg='#FFEDD1')
    a2.place(x=80,y=220)
    e2=Entry(d,width=25)
    e2.place(x=80,y=250)

    a3=Label(d,text='Dept ID',font=('biome',15),bg='#FFEDD1')
    a3.place(x=265,y=220)
    e3=Entry(d,width=25)
    e3.place(x=265,y=250)

    a4=Label(d,text='No of Leaves',font=('biome',15),bg='#FFEDD1')
    a4.place(x=460,y=220)
    e4=Entry(d,width=25)
    e4.place(x=460,y=250)

    a5=Label(d,text='Payment',font=('arial',15),bg='#FFEDD1')
    a5.place(x=80,y=320)
    e5=Entry(d,width=25)
    e5.place(x=80,y=350)

    bt1=Button(d,text='Tax',font=('biome',13),bg='#FFEDD1')
    bt1.place(x=265,y=310)
    bte1=Entry(d,width=25)
    bte1.place(x=265,y=350)

    bt=Button(d,text='Net Pay',font=('biome',13),bg='#FFEDD1')
    bt.place(x=460,y=310)
    bte2=Entry(d,width=25)
    bte2.place(x=460,y=350)
    
    bt3=Button(d,text='Update',font=('biome',15),bg='#FFEDD1',command=updatedata)
    bt3.place(x=265,y=400)
    
    t.mainloop()
    
#showpaymentupdate()