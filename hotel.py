from tkinter import *

import tkinter as tk
from bookARoom import BookARoom
from guests import guestlist


login=Tk()
login.geometry("1080x1080")
bg=PhotoImage(file=r'C:\Users\Edwin\Desktop\project\login1.png')
Label(login, image=bg).place(x=0,y=0,relwidth=1,relheight=1)
Label(login,text='ADMIN LOGIN',font=("Goudy Old Style", 35),bg='white').place(x=350,y=200)
Label(login,text='Username',font=("Goudy Old Style", 35),bg='white').place(x=100,y=300)
un=Text(login,width=15,height=1, font=("Goudy Old Style", 30),bg='#F2F2F2')
Label(login,text='Password',font=("Goudy Old Style", 35),bg='white').place(x=100,y=400)
pd=Text(login,width=15,height=1, font=("Goudy Old Style", 30),bg='#F2F2F2')
un.place(x=350,y=300)
pd.place(x=350,y=400)
Button(login, text='LOG-IN',font=("Goudy Old Style", 20),command=lambda:check()).place(x=450,y=600)





    
def check():
    user=un.get(1.0,END).strip()
    pwd=pd.get(1.0,END).strip()
    
    if user=='a'and pwd=='b':
        admin()
    else:
        ch=Tk()
        ch.geometry('450x100')
        Label(ch,text='Wrong username or password!!',font=("Goudy Old Style", 25)).pack(side=TOP)
        Button(ch,text='OK',font=("Goudy Old Style", 15),command=lambda:ch.destroy()).pack(side=BOTTOM)

def admin():
    login.destroy()
    root=Tk()
    root.geometry("1920x1080")
    root.title("HOTEL MANAGEMENT")
    bg=PhotoImage(file=r'C:\Users\Edwin\Desktop\project\bg2.png')
    Label(root, image=bg).place(x=0,y=0,relwidth=1,relheight=1)

        


            
    def bookRoom():
        room=BookARoom()
        room.book()

    def gst_():
        g=guestlist()
        g.gstlist()
        

    def cout():
        co=Tk()
        co.geometry("600x600")
        co.title("CHECK OUT")

    def eve():
        ev=Tk()
        ev.geometry("600x600")
        ev.title("EVENTS")

    def reserve():
        re=Tk()
        re.geometry("600x600")
        re.title("RESERVE A TABLE")
    
        
    Button(root, text='Rooms',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:bookRoom()).place(x=960,y=40)
    Button(root, text='Guest List',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:gst_()).place(x=1088,y=40)
    Button(root, text='Check-out',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:cout()).place(x=1260,y=40)
    Button(root, text='Events',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:eve()).place(x=1430,y=40)
    Button(root, text='Reservations',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:reserve()).place(x=1550,y=40)
    Button(root, text='Log out',font=("Goudy Old Style", 25),bg='#404959',fg='white',bd=0,activebackground='#404959',command=lambda:root.destroy()).place(x=1750,y=40)
    


    root.mainloop()



login.mainloop()  
    
