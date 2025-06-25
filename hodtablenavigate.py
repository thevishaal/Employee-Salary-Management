import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

def showhodtablenavigate():

    t=tkinter.Tk()
    t.geometry('500x400')
    
    d=Canvas(t,width=500,height=400)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,380,fill='black')
    d.create_rectangle(25,25,475,375,fill='light blue')
    
    xa=[]
    xb=[]
    xc=[]
    xd=[]
    i=0
    
    def first():
        global i
        i=0
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def nt():
        global i
        i=i+1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def pt():
        global i
        i=i-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def lt():
        global i
        i=len(xa)-1
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
        
        e1.insert(0,xa[i])
        e2.insert(0,xb[i])
        e3.insert(0,xc[i])
        e4.insert(0,xd[i])
        
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        sql="select hodid, hodname, deptid, remarks from hodtable"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
            xd.append(res[3])
        db.commit()
        db.close()
        
    h1=Label(d,text='HOD TABLE',font=('arial',25),bg='light blue')
    h1.place(x=150,y=40)
    
    a1=Label(d,text='Hod ID',font=('biome',15),bg='light blue')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Hod Name',font=('biome',15),bg='light blue')
    a2.place(x=270,y=120)
    e2=Entry(d,width=25)
    e2.place(x=270,y=150)
    
    a3=Label(d,text='Dept ID',font=('biome',15),bg='light blue')
    a3.place(x=80,y=220)
    e3=Entry(d,width=25)
    e3.place(x=80,y=250)
    
    a4=Label(d,text='Remarks',font=('biome',15),bg='light blue')
    a4.place(x=270,y=220)
    e4=Entry(d,width=25)
    e4.place(x=270,y=250)
    
    bt1=Button(d,text='First',font=('biome',15),bg='light blue',command=first)
    bt1.place(x=60,y=310)
    
    bt2=Button(d,text='Next',font=('biome',15),bg='light blue',command=nt)
    bt2.place(x=150,y=310)
    
    bt3=Button(d,text='Previous',font=('biome',15),bg='light blue',command=pt)
    bt3.place(x=255,y=310)
    
    bt4=Button(d,text='Last',font=('biome',15),bg='light blue',command=lt)
    bt4.place(x=390,y=310)
    
    filldata()
    
    t.mainloop()
    
#showhodtablenavigate()