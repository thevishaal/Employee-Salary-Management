import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showemployeedelete():

    t=tkinter.Tk()
    t.geometry('400x300')

    d=Canvas(t,width=400,height=300)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,380,280,fill='black')
    d.create_rectangle(25,25,376,275,fill='white')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from employee where empid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is deleted'%(xa))
        e1.delete(0,100)
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
            
    
    h1=Label(t,text='EMPLOYEE DETAIL',font=('arial',20),fg='#556EE6',bg='white')
    h1.place(x=70,y=40)
    
    a1=Label(d,text='Emp ID',font=('biome',15),bg='white')
    a1.place(x=120,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=120,y=150)

    bt=Button(d,text='Delete',font=('biome',15),bg='white',command=deletedata)
    bt.place(x=140,y=200)
    
    t.mainloop()
    
#showemployeedelete()