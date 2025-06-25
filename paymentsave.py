import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showpaymentsave():

    t=tkinter.Tk()
    t.geometry('700x500')
    
    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='#FFEDD1')
    
    def emp():
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
        xd=int(e4.get())
        xe=int(bte1.get())
        xf=float(bte2.get())
        xg=float(bte3.get())
        sql="insert into payment values(%d,'%s',%d,%d,%d,%f,%f)"%(xa,xb,xc,xd,xe,xf,xg)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is recorded'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        bte1.delete(0,100)
        bte2.delete(0,100)
        bte3.delete(0,100)
        db.close()
        
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select empsalary.monthsalary,employee.deptid,holidaymaster.noofleaves from employee,empsalary,holidaymaster where employee.empid=empsalary.empid and employee.empid=holidaymaster.empid and employee.empid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e2.insert(0,str(data[0]))
        e3.insert(0,str(data[1]))
        e4.insert(0,str(data[2]))
        db.close()
    
    pay=0
    dt=0
    
    def payment():
        xa=int(e2.get())
        xb=int(e4.get())
        global dt
        dt=xa/30
        net=round((31-xb)*dt)
        bte1.delete(0,100)
        bte1.insert(0,str(net))
        
    def tax():
        global dt
        pay=int(bte1.get())
        if pay >=0 and pay <100000:
            tax=10
        elif pay>=100000 and pay <300000:
            tax=15
        elif pay>=300000 and pay <500000:
            tax=20
        elif pay>=500000:
            tax=30
        else:
            messagebox.showinfo('Message','Sorry Babu! Tumhare bss ki na h tax dena')
            
        tx=(pay*tax)/100
        bte2.delete(0,100)
        bte2.insert(0,str(round(tx)))
        
    def netpay():
        xa=int(bte1.get())
        xb=int(bte2.get())
        xd=xa-xb
        bte3.delete(0,100)
        bte3.insert(0,str(round(xd)))
    
    h1=Label(d,text='EMPLOYEE PAYMENT',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=170,y=40)

    a1=Label(d,text='Emp ID',font=('biome',15),bg='#FFEDD1')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    emp()
    e1.place(x=80,y=150)

    btn=Button(d,text='Find',font=('biome',15),bg='#FFEDD1',command=finddata)
    btn.place(x=265,y=130)

    a2=Label(d,text='Monthly Salary',font=('biome',15),bg='#FFEDD1')
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

    bt1=Button(d,text='Payment',font=('arial',13),bg='#FFEDD1',command=payment)
    bt1.place(x=80,y=310)
    bte1=Entry(d,width=25)
    bte1.place(x=80,y=350)

    bt2=Button(d,text='Tax',font=('biome',13),bg='#FFEDD1',command=tax)
    bt2.place(x=265,y=310)
    bte2=Entry(d,width=25)
    bte2.place(x=265,y=350)

    bt3=Button(d,text='Net Pay',font=('biome',13),bg='#FFEDD1',command=netpay)
    bt3.place(x=460,y=310)
    bte3=Entry(d,width=25)
    bte3.place(x=460,y=350)

    bt4=Button(d,text='Save',font=('biome',15),bg='#FFEDD1',command=savedata)
    bt4.place(x=280,y=400)

    t.mainloop()
    
#showpaymentsave()
