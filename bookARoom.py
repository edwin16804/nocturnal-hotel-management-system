
from tkinter import *

import mysql.connector as ms


class BookARoom():
    
    #mc.execute("create table guestdetails(firstname char(50),lastname char(50),phonenumber int,adhaar int unique)")

    
    


    def book(self):
        main1=Tk()
        main1.geometry("400x200")
        main1.title("ROOMS")
        
        Label(main1, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
        Button(main1, text='<<',font=("Goudy Old Style", 15),bg='white',bd=0,activebackground='white',command=lambda:main1.destroy()).place(x=0,y=0)
        Button(main1, text='1] Input Details For Booking',font=("Goudy Old Style", 20),bg='white',bd=0,activebackground='white',command=lambda:booking()).place(x=0,y=80)
        Button(main1, text='2] Edit or Cancel Booking',font=("Goudy Old Style", 20),bg='white',bd=0,activebackground='white',command=lambda:editing()).place(x=0,y=130)


        def editing():
            edit=Tk()
            edit.geometry("600x600")
            edit.title("EDIT DETAILS")
            Label(edit, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
            Label(edit, text="First Name", font=("calibre",15),bg='white').place(x=0,y=50)
            Label(edit, text="Last Name", font=("calibre",15),bg='white').place(x=0,y=80)
            fn=Text(edit , width=15,height=1, font=("calibre",15),bg='#F2F2F2')
            ln=Text(edit , width=15,height=1, font=("calibre",15),bg='#F2F2F2')
            fn.place(x=135,y=50)
            ln.place(x=135,y=80)
            Button(edit ,text='Check',command=lambda:check(), font=("calibre",10),bg='#F2F2F2').place(x=200,y=120)
            def check():
                db=ms.connect(
                    host="localhost",
                    user="root",
                    passwd="edchaz168",
                    database="home"
                    )
                
                mc=db.cursor()
                fname= fn.get(1.0,END).strip()
                lname= ln.get(1.0,END).strip()
                name=fname+''+lname
                mc.execute("select * from guestdetails")
                names=mc.fetchall()
        
                for row in names:
                    if row[0]+''+row[1]==name:
                        Label(edit, text="Valid guest                  ", font=("calibre",15),bg='white').place(x=0,y=150)
                        Button(edit,text="Edit details", state=ACTIVE,font=("calibre",15),bg='white').place(x=10,y=200)
                        Button(edit,text="Cancel booking", state=ACTIVE,font=("calibre",15),bg='white').place(x=10,y=250)
                        break
                    else:
                        Label(edit,text="No such guest found", font=("calibre",15),bg='white').place(x=0,y=150)
                        Button(edit,text="Edit details", state=DISABLED,font=("calibre",15),bg='white').place(x=10,y=200)
                        Button(edit,text="Cancel booking", state=DISABLED,font=("calibre",15),bg='white').place(x=10,y=250)
        def booking():

            bar=Tk()
            bar.geometry("600x600")
            bar.title("BOOK A ROOM")
                
            Label(bar, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
            global a
            a="Single Room"
            global b
            b="Double Room"
            global c
            c="Deluxe Room"

            
            def roomchoice1():
                global l
                l=a
            def roomchoice2():
                global l
                l=b
            def roomchoice3():
                global l
                l=c
            def submit():
                
                db=ms.connect(
                    host="localhost",
                    user="root",
                    passwd="edchaz168",
                    database="home"
                    )
                
                mc=db.cursor()
                fname= fn.get(1.0,END).strip()
                lname= ln.get(1.0,END).strip()
                phone= ph.get(1.0,END).strip()
                aadhaar= ad.get(1.0,END).strip()
                no_gst=ng.get(1.0,END).strip()
                c_in=dt.get()+'-'+month.get()+'-'+year.get()
                c_out=dtout.get()+'-'+mout.get()+'-'+yrout.get()
                roomno=0
                
                #qry="insert into guestdetails values('{}','{}','{}','{}')".format(fname,lname,phone,aadhaar)
                mc.execute("insert into guestdetails values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(fname,lname,phone,aadhaar,no_gst,roomno,l,c_in,c_out))
                db.commit()
                
                
                
                bar.destroy()
                
                                
                    
                    
            
            Button(bar,text='<<',font=("Goudy Old Style", 10),bg='white',bd=0,activebackground='white',command=lambda:bar.destroy()).place(x=0,y=0)
        
            Label(bar, text="ENTER YOUR DETAILS", font=("calibre",25),fg="#eab676",bg='white').place(x=100,y=0)

            #name details
            Label(bar, text="First Name", font=("calibre",15),bg='white').place(x=0,y=50)
            fn=Text(bar , width=30,height=1, font=("calibre",15),bg='#F2F2F2')
               
        
            
            Label(bar, text="Last Name", font=("calibre",15),bg='white').place(x=0,y=80)
            ln=Text(bar , width=30,height=1, font=("calibre",15),bg='#F2F2F2')
            

            
            #Other details
            Label(bar, text="Phone number", font=("calibre",15),bg='white').place(x=0,y=110)
            ph=Text(bar , width=30,height=1, font=("calibre",15),bg='#F2F2F2')
            
            Label(bar, text="No. of guest staying", font=("calibre",15),bg='white').place(x=0,y=140)
            ng=Text(bar , width=3,height=1, font=("calibre",15),bg='#F2F2F2')
            

            #verification
            Label(bar, text="Aadhar card number",font=("calibre",15),bg='white').place(x=0,y=170)
            ad=Text(bar , width=25,height=1, font=("calibre",15),bg='#F2F2F2')

            Label(bar, text="Address",font=("calibre",15),bg='white').place(x=0,y=200)
            adr=Text(bar, width=30,height=2,font=("calibre",15),bg='#F2F2F2')

            
            #Room options
            
            Label(bar, text="Choose the room type :", font=("calibre",15),bg='white').place(x=0,y=250)
            Button(bar, text=a ,font=("calibre",10), width=10 ,height=1,bg='white',activebackground='#404959',command=lambda:roomchoice1()).place(x=300,y=290)
            Button(bar, text=b ,font=("calibre",10),  width=10 , height=1,bg='white',activebackground='#404959',command=lambda:roomchoice2()).place(x=300,y=320)
            Button(bar, text=c ,font=("calibre",10), width=10 , height=1,bg='white',activebackground='#404959',command=lambda:roomchoice3()).place(x=300,y=350)

            # Check in   
            mo=["January","February","March","April","May","June","July","August","September","October","November","December"]
            l1=[]
            for i in range(1,32):
                l1.append(i)
            yr=[2022,2023]
            Label(bar, text="Check-in date :", font=("calibre",15),bg='white').place(x=0,y=400)
            month = StringVar(bar)
            dt=StringVar(bar)
            year=StringVar(bar)
            dt.set("Date")
            month.set("Month")
            year.set("Year")
            OptionMenu(bar , dt , *l1).place(x=150,y=400)
            OptionMenu(bar , month , *mo).place(x=230,y=400)
            OptionMenu(bar , year , *yr).place(x=330,y=400)

            #Check out
            mo=["January","February","March","April","May","June","July","August","September","October","November","December"]
            l1=[]
            for i in range(1,32):
                l1.append(i)
            yr=[2022,2023]
            Label(bar, text="Check-out date :", font=("calibre",15),bg='white').place(x=0,y=450)
            mout = StringVar(bar)
            dtout=StringVar(bar)
            yrout=StringVar(bar)
            dtout.set("Date")
            mout.set("Month")
            yrout.set("Year")
            OptionMenu(bar , dtout , *l1).place(x=150,y=450)
            OptionMenu(bar , mout , *mo).place(x=230,y=450)
            OptionMenu(bar , yrout , *yr).place(x=330,y=450)


            fn.place(x=135,y=50)
            ln.place(x=135,y=80)
            ph.place(x=135,y=110)
            ng.place(x=190,y=140)
            ad.place(x=190,y=170)
            adr.place(x=135,y=200)
            
            
            Button(bar, text="Confirm",font=("calibre",10),command=submit).place(x=250,y=550)
            
            bar.mainloop()

        main1.mainloop()
