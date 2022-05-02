from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
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

#declare the name of tables
bookTable = "books"

def searchBook():
    root = Tk()
    root.title("Result")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    # add a text label to LabeFrame
    textLabel = Label(LabelFrame, text="%20s %25s %25s %25s" % ('Book ID', 'Title', 'Author', 'Status'),
                      bg="black", fg="white")
    textLabel.place(relx=0.06, rely=0.1)

    y = 0.25

    # query to retrieve details from books table
    bid = bookInfo1.get()

    searchSql = "select * from " + bookTable + " where bid = '" + bid + "'"
    try:
        cur.execute(searchSql)
        con.commit()

        for i in cur:
            Label(LabelFrame, text="%10s %40s %30s %20s" % (i[0], i[1], i[2], i[3]),
                  bg="black", fg="white").place(relx=0.07, rely=y)
            y += 0.1

    except:
        messagebox.showinfo("Error", "Failed to Fetch files from database")

    quitBtn = Button(root, text="Close", bg='lightblue', fg="black", command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()

def search():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, bookTable, cur, con, root

    root = Tk()
    root.title("Search Book")
    root.minsize(width=400, height=300)
    root.geometry("600x300")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    LabelFrame = Frame(root, bg="black")
    LabelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #take a book ID to delete
    lb2 = Label(LabelFrame, text="Book ID: ", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.4)

    bookInfo1 = Entry(LabelFrame)
    bookInfo1.place(relx=0.3, rely=0.4, relwidth=0.62)

    #submit button
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=searchBook)
    submitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Close", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()
