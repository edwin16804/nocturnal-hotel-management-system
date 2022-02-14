from tkinter import *
import mysql.connector as ms

class guestlist():
    def gstlist(self):
        
        glist=Tk()
        glist.geometry("600x600")
        glist.title("GUEST LIST")
        Label(glist, bg='white').place(x=0,y=0,relwidth=1,relheight=1)
        
        db=ms.connect(
                    host="localhost",
                    user="root",
                    passwd="edchaz168",
                    database="home"
                    )
        
        mc=db.cursor()
        mc.execute("select * from guestdetails")
        data=mc.fetchall()            
        a=70
        
        Label(glist, text="GUEST NAME", font=("calibre",20),fg="#eab676",bg='white').place(x=10,y=0)
        Label(glist, text="ROOM NO.", font=("calibre",20),fg="#eab676",bg='white').place(x=400,y=0)
        for row in data:
               
               Label(glist, text=row[0]+' '+row[1], font=("calibre",15),bg='white',bd=0,fg='black').place(x=10,y=a)
               Label(glist, text=row[5], font=("calibre",15),bg='white',bd=0,fg='black').place(x=500,y=a)
               a=a+50
               

        glist.mainloop()

