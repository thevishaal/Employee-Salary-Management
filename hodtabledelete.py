import tkinter 
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox
import pymysql

def showhodtabledelete():

    t=tkinter.Tk()
    t.geometry('400x300')

    d=Canvas(t,width=400,height=300)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,380,280,fill='black')
    d.create_rectangle(25,25,376,275,fill='light blue')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from hodtable where hodid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is deleted'%(xa))
        e1.delete(0,100)
        db.close()
        
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select hodid from hodtable "
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e1 ['values']=lt    
    
    h1=Label(t,text='HOD TABLE',font=('arial',20),bg='light blue')
    h1.place(x=130,y=40)
    
    a1=Label(d,text='Hod ID',font=('biome',15),bg='light blue')
    a1.place(x=120,y=120)
    e1=ttk.Combobox(d)
    filldata()
    e1.place(x=120,y=150)

    bt=Button(d,text='Delete',font=('biome',15),bg='light blue',command=deletedata)
    bt.place(x=140,y=200)
    
    
    t.mainloop()
    
#showhodtabledelete()