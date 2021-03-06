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

#declare the name of table
issueTable = "books_issued"
bookTable = "books"
issueTo = "memberInfo"

allBid = []

def issue():
    global issuebtn, labelFrame, book_id, mem_name, lb1, quitBtn, root, Canvas1, status

    bid = book_id.get()        #take the book id with get()
    issueto = mem_name.get()    #take the name to whom it is issued

    issuebtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    book_id.destroy()
    mem_name.destroy()
    
    extractBid = "select bid from "+ bookTable

    try:
        cur.execute(extractBid)
        con.commit()

        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

            if check == 'available':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error", "Book Id not present")

    except:
        messagebox.showinfo("Error", "Can't fetch the Book Id")

    issueSql = "insert into "+issueTo+" (bid,name) values ('"+bid+"', '"+issueto+"');"
    issueSql1 = "insert into " + issueTable + " values ('" + bid + "', '" + issueto + "');"
    updateStatus = "update "+ bookTable+" set status = 'issued' where bid = '"+bid+"';"
    updateIssue = "update "+issueTo+" set issueDate = date('now') where bid = '"+bid+"';"
    updateEReturn = "update " + issueTo + " set e_returnDate = date('now','+7 days') where bid = '" + bid + "';"

    try:
        if bid in allBid and status == True:
            cur.execute(issueSql1)
            con.commit()
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            cur.execute(updateIssue)
            con.commit()
            cur.execute(updateEReturn)
            con.commit()
            messagebox.showinfo("Success", "Book Issued successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message", "Book Already Issued")
            root.destroy()
            return

    except:
        messagebox.showinfo("Search Error", "The value insert is wrong, Try again")
        root.destroy()

    allBid.clear()

def issueBook():
    global issuebtn, labelFrame, book_id, mem_name, lb1, quitBtn, root, Canvas1, status

    root=Tk()
    root.title("Issue Book")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #Book Id
    lb1 = Label(labelFrame, text="Book ID", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.3)

    book_id = Entry(labelFrame)
    book_id.place(relx=0.3, rely=0.3, relwidth=0.62)

    #to whom book is issued, student name
    lb2 = Label(labelFrame, text="Issue To", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.5)

    mem_name = Entry(labelFrame)
    mem_name.place(relx=0.3, rely=0.5, relwidth=0.62)

    #Issue Button
    issuebtn = Button(root, text="Issue", bg="#d1ccc0", fg="black", command=issue)
    issuebtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Close", bg="#aaa69d", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()

