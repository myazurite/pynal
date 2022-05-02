from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn
con = create_connection(r"library.db")
cur = con.cursor()

#enter table names here
bookTable = "books"

def View():

    root = Tk()
    root.title("All Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.13, relwidth=0.8, relheight=0.7)

    #add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%10s %40s %30s %20s"%('Book ID','Title','Author','Status'), bg="black", fg="white")
    textLabel.place(relx=0.08, rely=0.1)

    y = 0.2
    getBooks = "select * from "+ bookTable
    try:
        cur.execute(getBooks)
        con.commit()

        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %30s"%(i[0],i[1],i[2],i[3]), bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("Error","Failed to Fetch files from database")

    quitBtn = Button(root, text="Close", fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
