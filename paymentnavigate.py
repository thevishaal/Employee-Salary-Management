import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

def showpaymentnavigate():
    
    t=tkinter.Tk()
    t.geometry('700x500')
    
    d=Canvas(t,width=700,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,680,480,fill='black')
    d.create_rectangle(25,25,676,475,fill='#FFEDD1')
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    xe=[]
    xf=[]
    xg=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        e5.delete(0,100)
        e6.delete(0,100)
        e7.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        e5.insert(0,xe[i])
        e6.insert(0,xf[i])
        e7.insert(0,xg[i])
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        sql="select empid, month, deptid, noofleaves, payment,tax, netpay from payment"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(str(res[2]))
            xd.append(str(res[3]))
            xe.append(str(res[4]))  
            xf.append(str(res[5]))
            xg.append(str(res[6]))
        db.commit()
        db.close()
        
    h1=Label(d,text='EMPLOYEE PAYMENT',font=('arial',25),fg='#556EE6',bg='#FFEDD1')
    h1.place(x=170,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='#FFEDD1')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Monthly Salary',font=('biome',15),bg='#FFEDD1')
    a2.place(x=270,y=120)
    e2=Entry(d,width=25)
    e2.place(x=270,y=150)
    
    a3=Label(d,text='Dept ID',font=('biome',15),bg='#FFEDD1')
    a3.place(x=460,y=120)
    e3=Entry(d,width=25)
    e3.place(x=460,y=150)
    
    a4=Label(d,text='No of Leaves',font=('biome',15),bg='#FFEDD1')
    a4.place(x=80,y=220)
    e4=Entry(d,width=25)
    e4.place(x=80,y=250)
    
    a5=Label(d,text='Payment',font=('biome',15),bg='#FFEDD1')
    a5.place(x=270,y=220)
    e5=Entry(d,width=25)
    e5.place(x=270,y=250)
    
    a6=Label(d,text='Tax',font=('biome',15),bg='#FFEDD1')
    a6.place(x=460,y=220)
    e6=Entry(d,width=25)
    e6.place(x=460,y=250)
    
    a7=Label(d,text='Net Pay',font=('biome',15),bg='#FFEDD1')
    a7.place(x=80,y=320)
    e7=Entry(d,width=25)
    e7.place(x=80,y=350)
    
    bt1=Button(d,text='First',font=('biome',15),bg='#FFEDD1',command=first)
    bt1.place(x=100,y=410)
    
    bt2=Button(d,text='Next',font=('biome',15),bg='#FFEDD1',command=nt)
    bt2.place(x=220,y=410)
    
    bt3=Button(d,text='Previous',font=('biome',15),bg='#FFEDD1',command=pt)
    bt3.place(x=350,y=410)
    
    bt4=Button(d,text='Last',font=('biome',15),bg='#FFEDD1',command=lt)
    bt4.place(x=520,y=410)
    
    filldata()
    
    t.mainloop()
#showpaymentnavigate()