from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
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

bookTable = "books"
issue_Table = "books_issued"
log_table = "memberInfo"

def deleteBook():
    bid = bookInfo1.get()
    deleteSql = "delete from "+ bookTable+ " where bid = '" +bid+"'"
    deleteIssue = "delete from "+issue_Table+ " where bid = '" +bid+"' "
    deleteLog = "delete from "+log_table+" where bid = '" +bid+"' "

    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        cur.execute(deleteLog)
        con.commit()
        messagebox.showinfo("Success", "Book Deleted Successfully")

    except:
        messagebox.showinfo("Error", "Please check Book Id")


    bookInfo1.delete(0, END)
    root.destroy()

def delete():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, cur, con, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="lightgreen")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Delete Book", bg="black", fg="white", font=('Courier',15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    lb2 = Label(LabelFrame, text="Book Id: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=deleteBook)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()
