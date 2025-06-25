import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

def showholidaymasternavigate():

    t=tkinter.Tk()
    t.geometry('500x350')
    
    d=Canvas(t,width=500,height=350)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,330,fill='black')
    d.create_rectangle(25,25,475,325,fill='light green')
    
    xa=[]
    xb=[]
    xc=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
    
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        sql="select empid, holidayname, noofleaves from holidaymaster"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
        db.commit()
        db.close()
     
    
    h1=Label(d,text='HOLIDAY MASTER',font=('arial',25),bg='light green')
    h1.place(x=100,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='light green')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Holiday Name',font=('biome',15),bg='light green')
    a2.place(x=80,y=200)
    e2=Entry(d,width=25)
    e2.place(x=80,y=230)
    
    a3=Label(d,text='No of Leaves',font=('biome',15),bg='light green')
    a3.place(x=270,y=200)
    e3=Entry(d,width=25)
    e3.place(x=270,y=230)
    
    bt1=Button(d,text='First',font=('biome',15),bg='light green',command=first)
    bt1.place(x=60,y=270)
    
    bt2=Button(d,text='Next',font=('biome',15),bg='light green',command=nt)
    bt2.place(x=160,y=270)
    
    bt3=Button(d,text='Previous',font=('biome',15),bg='light green',command=pt)
    bt3.place(x=260,y=270)
    
    bt4=Button(d,text='Last',font=('biome',15),bg='light green',command=lt)
    bt4.place(x=380,y=270)
    
    filldata()
    t.mainloop()
    
