import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

def showholidaymasterupdate():

    t=tkinter.Tk()
    t.geometry('500x350')
    
    d=Canvas(t,width=500,height=350)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,330,fill='black')
    d.create_rectangle(25,25,475,325,fill='light green')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select holidayname,noofleaves from holidaymaster where empid=%d"%(xa)
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
        xc=int(e3.get())
        sql="update holidaymaster set holidayname='%s',noofleaves=%d where empid=%d"%(xb,xc,xa)
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
        sql="select empid from holidaymaster "
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt
    
    h1=Label(d,text='HOLIDAY MASTER',font=('arial',25),bg='light green')
    h1.place(x=100,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='light green')
    a1.place(x=80,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=80,y=150)
    
    bt1=Button(d,text='Find',font=('biome',15),bg='light green',command=finddata)
    bt1.place(x=270,y=130)
    
    a2=Label(d,text='Holiday Name',font=('biome',15),bg='light green')
    a2.place(x=80,y=200)
    e2=Entry(d,width=25)
    e2.place(x=80,y=230)
    
    a3=Label(d,text='No of Leaves',font=('biome',15),bg='light green')
    a3.place(x=270,y=200)
    e3=Entry(d,width=25)
    e3.place(x=270,y=230)
    
    bt2=Button(d,text='Update',font=('biome',15),bg='light green',command=updatedata)
    bt2.place(x=200,y=270)
    
    t.mainloop()
    
#showholidaymasterupdate()