from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error

def bookRegister():
    bid = book_id.get()
    title = book_title.get()
    author = book_author.get()
    status = book_status.get()
    status = status.lower()
    if status != "available" and status !="issued":
        messagebox.showinfo('Error', "Status must be either avaiable or issued!")
        return

    insertBooks = "insert into "+bookTable+" values ('"+bid+"','"+title+"','"+author+"','"+status+"')"

    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except:
        messagebox.showinfo('Error', "Can't add book to database")

    root.destroy()

def addBook():
    global book_id, book_title, book_author, book_status, Canvas1, cur, con, bookTable, root

    root = Tk()
    root.title("Add Book")
    root.minsize(width=400, height=500)
    root.geometry("600x400")

    def create_connection(db_file):
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn

    con = create_connection(r"library.db")

    cur = con.cursor()

    bookTable = "books"

    #create the canvas for info
    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.6)

    #book ID
    lb1 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)
    book_id = Entry(LabelFrame)
    book_id.place(relx=0.35, rely=0.2, relwidth=0.62, relheight=0.08)

    #title
    lb2 = Label(LabelFrame, text="Title: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)
    book_title = Entry(LabelFrame)
    book_title.place(relx=0.35, rely=0.35, relwidth=0.62, relheight=0.08)

    #author
    lb3 = Label(LabelFrame, text="Author: ", bg="black", fg="white")
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)
    book_author = Entry(LabelFrame)
    book_author.place(relx=0.35, rely=0.50, relwidth=0.62, relheight=0.08)

    #Status
    lb4 = Label(LabelFrame, text="Status(available/issued): ", bg="black", fg="white")
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)
    book_status = Entry(LabelFrame)
    book_status.place(relx=0.35, rely=0.65, relwidth=0.62, relheight=0.08)
    
    #Buttons
    SubmitBtn = Button(root, text="Submit", bg="#d1ccc0", fg="black", command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.82, relwidth=0.18, relheight=0.08)

    QuitBtn = Button(root, text="Close", bg="#f7f1e3", fg="black", command=root.destroy)
    QuitBtn.place(relx=0.53, rely=0.82, relwidth=0.18, relheight=0.08)

    root.mainloop()