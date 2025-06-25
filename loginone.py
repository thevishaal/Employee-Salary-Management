import tkinter 
from tkinter import *  
from tkinter import messagebox
from maindashboard import *
import pymysql
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

t=tkinter.Tk()
t.title('loginpage')
t.geometry('400x420')

def check():
    db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
    cur=db.cursor()
    xa=e1.get()
    xb=e2.get()
    sql="select count(*) from logintable where loginid='%s' and  password='%s' "%(xa,xb)
    cur.execute(sql)
    data=cur.fetchone()
    if data [0]==0:
        messagebox.showerror('Message','Account is not found.')
    else:
        showmaindashboard()
    db.close()
    
def signup():
    d=Canvas(t,width=400,height=420)
    d.place(x=0,y=0)

    d.create_rectangle(20, 20,380,400,fill='black')
    d.create_rectangle(25,25,375,395,fill='#FFEDD1')
    
    def cts():
        d.destroy()
        
    def lts():
        d.destroy()
    
    def savedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=e1.get()
        xb=e2.get()
        sql="select count(*) from logintable where loginid='%s' and  password='%s' "%(xa,xb)
        cur.execute(sql)
        data=cur.fetchone()
        if data [0]==0:
            if e1.get()=='' or e2.get()=='':
                messagebox.showerror('Message','Pls fill all columns.')
            else:
                if '@'in xa:
                    dc=pymysql.connect(host='localhost',user='root',password='root',database='esm')
                    cur=dc.cursor()
                    xa=e1.get()
                    xb=e2.get()
                    sql="insert into logintable values('%s','%s')"%(xa,xb)
                    cur.execute(sql)
                    dc.commit()
                    messagebox.showinfo('Message','Your account is created successfully.')
                    cts()
                    dc.close()
                else:
                    messagebox.showerror('Error','your email is invalid.')
        else:
            messagebox.showinfo('Message for You','Your account is already exist.')
            cts()
        db.close()

    h1=Label(d,text='Sign Up',font=('arial',30),bg='#FFEDD1')
    h1.place(x=150,y=60)

    a1=Label(d,text='Email',font=(5),bg='#FFEDD1')
    a1.place(x=80,y=150)
    e1=Entry(d,width=40)
    e1.place(x=80,y=180)

    a2=Label(d,text='Password',font=(5),bg='#FFEDD1')
    a2.place(x=80,y=230)
    e2=Entry(d,width=40,show='*')
    e2.place(x=80,y=260)

    bt1=Button(d,text='Sign up',font=(2),bg='#FFEDD1',command=savedata)
    bt1.place(x=160,y=310)
    
    a3=Label(d,text="Already have an account?",font=(5),bg='#FFEDD1')
    a3.place(x=90,y=350)
    
    bt2=Button(d,text='Login here',bg='#FFEDD1',command=lts)
    bt2.place(x=280,y=350)
    
def forgot():
    d2=Canvas(t,width=400,height=420)
    d2.place(x=0,y=0)

    d2.create_rectangle(20, 20,380,400,fill='black')
    d2.create_rectangle(25,25,375,395,fill='#FFEDD1')
    
    h1=Label(d2,text='RESET PASSWORD',font=('arial',23),bg='#FFEDD1')
    h1.place(x=50,y=60)
    
    a1=Label(d2,text='UserId',font=(5),bg='#FFEDD1')
    a1.place(x=80,y=130)
    y1=Entry(d2,width=40)
    y1.place(x=80,y=160)
       
    def sendotp():
        from_address = "vb3121982@gmail.com"
        to_address = y1.get()
        
        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = 'OTP'
        msg['From'] = from_address
        msg['To'] = to_address
        r=random.random()*50000
        st=str(round(r))
        
        # Create the message (HTML).
        html = "OTP is ..."+st
        
        # Record the MIME type - text/html.
        part1 = MIMEText(html, 'html')
        
        # Attach parts into message container
        msg.attach(part1)
        
        # Credentials
        username = 'vb3121982@gmail.com'  
        password = 'alztdvsptiepwwle'

        # Sending the email
        ## note - this smtp config worked for me, I found it googling around, you may have to tweak the # (587) to get yours to work
        server = smtplib.SMTP('smtp.gmail.com', 587) 
        server.ehlo()
        server.starttls()
        server.login(username,password)  
        server.sendmail(from_address, to_address, msg.as_string())  
        server.quit()
        
        #sql 
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        sql="select count(*) from login where loginid='%s'"%(to_address)
        cur.execute(sql)
        data=cur.fetchone()
        if data [0]==0:
            dc=pymysql.connect(host='localhost',user='root',password='root',database='esm')
            cur=dc.cursor()
            sql="insert into login values('%s','%s')"%(to_address,st)
            cur.execute(sql)
            dc.commit()
            messagebox.showinfo('Message','Send OTP')
            dc.close()
        else:
            dx=pymysql.connect(host='localhost',user='root',password='root',database='esm')
            cur=dx.cursor()
            sql="update login set otp='%s' where loginid='%s'"%(st,to_address)
            cur.execute(sql)
            dx.commit()
            messagebox.showinfo('Message','Send OTP')
            dx.close()
        db.close()
        
    bt1=Button(d2,text='Send OTP',font=(2),bg='#FFEDD1',command=sendotp)
    bt1.place(x=150,y=200)
    
    a2=Label(d2,text='Enter OTP',font=(5),bg='#FFEDD1')
    a2.place(x=80,y=250)
    e2=Entry(d2,width=40)
    e2.place(x=80,y=280)
    
    def verify():
        db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
        cur=db.cursor()
        xa=y1.get()
        xb=e2.get()
        sql="select count(*) from login where loginid='%s' and otp='%s'"%(xa,xb)
        cur.execute(sql)
        data=cur.fetchone()
        if data [0]==0:
            if y1.get()=='' and e2.get()=='':
                messagebox.showerror('Message','Pls fill all data')
            else:
                messagebox.showerror('Message','OTP is not matched!')
        else:
            password()
        db.close()
    
    bt2=Button(d2,text='Verify',font=(2),bg='#FFEDD1',command=verify)
    bt2.place(x=160,y=320)
    
    def password():
        d3=Canvas(t,width=400,height=420)
        d3.place(x=0,y=0)
    
        d3.create_rectangle(20, 20,380,400,fill='black')
        d3.create_rectangle(25,25,375,395,fill='#FFEDD1')
        
        ya=y1.get()
            
        def cts():
            d3.destroy()
            d2.destroy()
            
        def cp():
            if e1.get()==e2.get():
                db=pymysql.connect(host='localhost',user='root',password='root',database='esm')
                cur=db.cursor()
                xa=e1.get()
                sql="update logintable set password='%s' where loginid='%s'"%(xa,ya)
                cur.execute(sql)
                db.commit()
                messagebox.showinfo('Message','Your password is changed.')
                cts()
                db.close()
            else:
                messagebox.showinfo('Message','password is not confirm!')
                
        h1=Label(d3,text='CREATE PASSWORD',font=('arial',23),bg='#FFEDD1')
        h1.place(x=40,y=60)
        
        a1=Label(d3,text='Create New Password',font=(5),bg='#FFEDD1')
        a1.place(x=80,y=130)
        e1=Entry(d3,width=40)
        e1.place(x=80,y=160)
        
        a2=Label(d3,text='Re-Enter Password',font=(5),bg='#FFEDD1')
        a2.place(x=80,y=210)
        e2=Entry(d3,width=40)
        e2.place(x=80,y=240)
        
        bt=Button(d3,text='Submit',font=(2),bg='#FFEDD1',command=cp)
        bt.place(x=150,y=290)
    
d1=Canvas(t,width=400,height=420)
d1.place(x=0,y=0)

d1.create_rectangle(20, 20,380,400,fill='black')
d1.create_rectangle(25,25,375,395,fill='#FFEDD1')

h1=Label(d1,text='Sign in',font=('arial',30),bg='#FFEDD1')
h1.place(x=150,y=60)

a1=Label(d1,text='UserId',font=(5),bg='#FFEDD1')
a1.place(x=80,y=150)
e1=Entry(d1,width=40)
e1.place(x=80,y=180)

a2=Label(d1,text='Password',font=(5),bg='#FFEDD1')
a2.place(x=80,y=230)
e2=Entry(d1,width=40,show='*')
e2.place(x=80,y=260)

bt=Button(d1,text='Forgot Password?',bg='#FFEDD1',command=forgot)
bt.place(x=220,y=280)

bt1=Button(d1,text='Login',font=(2),bg='#FFEDD1',command=check)
bt1.place(x=160,y=310)

a3=Label(d1,text="Don't have an account?",font=(5),bg='#FFEDD1')
a3.place(x=90,y=350)

bt2=Button(d1,text='Register here',command=signup,bg='#FFEDD1')
bt2.place(x=260,y=350)

t.mainloop()


