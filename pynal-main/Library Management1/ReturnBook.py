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

issueTable = "books_issued"
bookTable = "books"
member="memberInfo"

allBid = []

def Return():
    global submitBtn, quitBtn, LabelFrame, lb1, Canvas1, book_id, root, status

    bid = book_id.get()
    extractBid = "select bid from "+issueTable

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

            if check == 'issued':
                status = True
            else:
                status = False
        
        else:
            messagebox.showinfo("Error", "Book Id is not Present")

    except:
        messagebox.showinfo("Error", "Can't Fetch the book Id")

    #remove that book from issueTable
    issueSql = "delete from " + issueTable + " where bid = '" + bid + "';"
    updateStatus = "update "+bookTable+" set status = 'available' where bid='"+bid+"';"
    setReturn = "update "+member+" set returnDate = date('now') where bid='"+bid+"';"
    setFine = "update " + member +" set fine = (select julianday(returnDate) - julianday(e_returnDate) from memberInfo)*2 where bid='" + bid + "';"
    checkFine = "update "+member+" set fine = case when fine < 0 then 0 else fine end where bid='" + bid + "';"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            cur.execute(setReturn)
            con.commit()
            cur.execute(setFine)
            con.commit()
            cur.execute(checkFine)
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")
        else:
            allBid.clear()
            messagebox.showinfo('Message', "Please check the book id")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "the value you entered is wrong, try again!")

    allBid.clear()
    root.destroy()    

def returnBook():
    global root, con, cur, labelFrame, submitBtn, quitBtn, Canvas1, book_id, lb1

    root = Tk()
    root.title("Return Book")
    root.minsize(width=400, height=200)
    root.geometry("500x300")

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#5F9EA0")
    Canvas1.pack(expand=True, fill=BOTH)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

    #book id
    lb1 = Label(labelFrame, text="Book ID", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.5)

    book_id = Entry(labelFrame)
    book_id.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit Button
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=Return)
    submitBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Close", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.8, relwidth=0.18, relheight=0.08)

    root.mainloop()
