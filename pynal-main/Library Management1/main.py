from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error
from AddBook import *
from ViewBooks import *
from DeleteBook import *
from IssueBook import *
from ReturnBook import *
from SearchBook import *
from ViewMember import *

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
create_connection(r"library.db")


root = Tk()
root.title("Dashboard")
root.minsize(width=600, height=500)
root.geometry("600x500")

#Add background Image
class bg(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)
        self.image = Image.open("lib.jpg")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
    def _resize_image(self,event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
e = bg(root)
e.pack(fill=BOTH, expand=YES)

btn1 = Button(root, text="Add Book Details", bg="black", fg="white", command=addBook)
btn1.place(relx=0.2, rely=0.15, relwidth=0.6, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=delete)
btn2.place(relx=0.2, rely=0.25, relwidth=0.6, relheight=0.1)

btn3 = Button(root, text="All Book", bg="black", fg="white", command=View)
btn3.place(relx=0.2, rely=0.35, relwidth=0.6, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg="black", fg="white", command=issueBook)
btn4.place(relx=0.2, rely=0.45, relwidth=0.6, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnBook)
btn5.place(relx=0.2, rely=0.55, relwidth=0.6, relheight=0.1)

btn6 = Button(root, text="Search Book", bg="black", fg="white", command=search)
btn6.place(relx=0.2, rely=0.65, relwidth=0.6, relheight=0.1)

btn7 = Button(root, text="Show Issue/Return Log", bg="black", fg="white", command=ViewMem)
btn7.place(relx=0.2, rely=0.75, relwidth=0.6, relheight=0.1)

root.mainloop()
