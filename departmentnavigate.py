import tkinter 
from tkinter import *
from tkinter import messagebox
import pymysql

def showdepartmentnavigate():

    t=tkinter.Tk()
    t.geometry('500x400')
    
    d=Canvas(t,width=500,height=400)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,380,fill='black')
    d.create_rectangle(25,25,475,375,fill='sky blue')
    
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
        sql="select deptid, dname, description from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            xa.append(str(res[0]))
            xb.append(res[1])
            xc.append(res[2])
        db.commit()
        db.close()
    
    h1=Label(d,text='DEPARTMENT',font=('arial',25),bg='sky blue')
    h1.place(x=140,y=40)
    
    a1=Label(d,text='Dept ID',font=('biome',15),bg='sky blue')
    a1.place(x=80,y=120)
    e1=Entry(d,width=25)
    e1.place(x=80,y=150)
    
    a2=Label(d,text='Dept Name',font=('biome',15),bg='sky blue')
    a2.place(x=80,y=220)
    e2=Entry(d,width=25)
    e2.place(x=80,y=250)
    
    a3=Label(d,text='Description',font=('biome',15),bg='sky blue')
    a3.place(x=270,y=220)
    e3=Entry(d,width=25)
    e3.place(x=270,y=250)
    
    bt1=Button(d,text='First',font=('biome',15),bg='sky blue',command=first)
    bt1.place(x=60,y=310)
    
    bt2=Button(d,text='Next',font=('biome',15),bg='sky blue',command=nt)
    bt2.place(x=150,y=310)
    
    bt3=Button(d,text='Previous',font=('biome',15),bg='sky blue',command=pt)
    bt3.place(x=250,y=310)
    
    bt4=Button(d,text='Last',font=('biome',15),bg='sky blue',command=lt)
    bt4.place(x=380,y=310)
    
    filldata()
    
    t.mainloop()
    
#showdepartmentnavigate()