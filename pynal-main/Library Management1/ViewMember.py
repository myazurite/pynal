from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
con = create_connection(r"library.db")
cur = con.cursor()

member="memberInfo"

def ViewMem():

    root = Tk()
    root.title("Member Information")
    root.minsize(width=900, height=400)
    root.geometry("900x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.7)

    textLabel = Label(LabelFrame, text="%10s %15s %20s %30s %30s %30s"%('Book ID','Name','Issue Date','Expected return date','Return date','fine'),
                    bg="black", fg="white")
    textLabel.place(relx=0.07, rely=0.1)

    y = 0.25
    getBooks = "select * from "+ member
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(LabelFrame, text="%10s %20s %23s %28s %37s %31s"%(i[0],i[1],i[2],i[3],i[4],i[5]),
                    bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Close", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()