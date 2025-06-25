import tkinter 
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import pymysql

def showhodtablesave():

    t=tkinter.Tk()
    t.geometry('500x400')
    
    d=Canvas(t,width=500,height=400)
    d.place(x=0,y=0)
    
    d.create_rectangle(20,20,480,380,fill='black')
    d.create_rectangle(25,25,475,375,fill='light blue')
    
    def filldata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        lt=[]
        sql="select deptid from department"
        cur.execute(sql)
        data=cur.fetchall()
        for res in data:
            lt.append(res[0])
        db.close()
        e3['values']=lt
        
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=int(e1.get())
        xb=e2.get()
        xc=int(e3.get())
        xd=e4.get()
        sql="insert into hodtable values(%d,'%s',%d,'%s')"%(xa,xb,xc,xd)
        cur.execute(sql)
        db.commit()
        messagebox.showinfo('Message','%d is recorded'%(xa))
        e1.delete(0,100)
        e2.delete(0,100)
        e3.delete(0,100)
        e4.delete(0,100)
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
    e3=ttk.Combobox(d)
    filldata()
    e3.place(x=80,y=250)
    
    a4=Label(d,text='Remarks',font=('biome',15),bg='light blue')
    a4.place(x=270,y=220)
    e4=Entry(d,width=25)
    e4.place(x=270,y=250)
    
    bt=Button(d,text='Save',font=('biome',15),bg='light blue',command=savedata)
    bt.place(x=200,y=300)
    
    
    t.mainloop()
    
#showhodtablesave()