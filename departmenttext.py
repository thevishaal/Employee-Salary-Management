import tkinter 
from tkinter import * 
import pymysql

def showdepartmenttext():

    t=tkinter.Tk()
    t.geometry('600x500')
    
    d=Canvas(t,width=600,height=500)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,580,480,fill='black')
    d.create_rectangle(25,25,575,475,fill='white')
    
    def filldata():
        db=db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        sql="select * from department"
        cur.execute(sql)
        data=cur.fetchall()
        msg=''
        for res in data :
            msg=msg+str(res[0])+"\t"
            msg=msg+str(res[1])+"\t"
            msg=msg+str(res[2])+"\t"
            msg=msg+"\n"
        db.close()
        w.insert(END,msg)
            
    
    w=Text(t,width=68,height=28)
    w.place(x=25,y=25)
    filldata()
    
    t.mainloop()
    
#showdepartmenttext()