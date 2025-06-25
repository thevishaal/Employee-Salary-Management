import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def showdepartmentupdate():

    t=tkinter.Tk()
    t.geometry('500x400')
    
    d=Canvas(t,width=500,height=400)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,380,fill='black')
    d.create_rectangle(25,25,475,375,fill='sky blue')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select dname, description from department where deptid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.delete(0,100)
        e3.delete(0,100)
        
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.commit()
        db.close()
        
    def updatedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=e3.get()
        sql="update department set dname='%s',description='%s' where deptid=%d"%(xb,xc,xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is updated.'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select deptid from department "
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt
    
    h1=Label(d,text='DEPARTMENT',font=('arial',25),bg='sky blue')
    h1.place(x=140,y=40)
    
    a1=Label(d,text='Dept ID',font=('biome',15),bg='sky blue')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)
    
    bt=Button(d,text='Find',font=('biome',15),bg='sky blue',command=finddata)
    bt.place(x=270,y=130)
    
    a2=Label(d,text='Dept Name',font=('biome',15),bg='sky blue')
    a2.place(x=80,y=220)
    e2=Entry(d,width=25)
    e2.place(x=80,y=250)
    
    a3=Label(d,text='Description',font=('biome',15),bg='sky blue')
    a3.place(x=270,y=220)
    e3=Entry(d,width=25)
    e3.place(x=270,y=250)
    
    bt2=Button(t,text='Update',font=('biome',15),bg='sky blue',command=updatedata)
    bt2.place(x=190,y=310)
    
    t.mainloop()
#showdepartmentupdate()