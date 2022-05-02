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
root.title("Library")
root.minsize(width=600, height=500)
root.geometry("600x500")

#Add background Image
same = True
n = 0.28
bg_image = Image.open("lib.jpg")
[imageSizeWidth, imageSizeHeight] = bg_image.size

newImageSizeWidth = int(imageSizeWidth * n)

if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

bg_image = bg_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)

#add image to canva
img = ImageTk.PhotoImage(bg_image)
canvas1 = Canvas(root)
canvas1.create_image(300, 340, image=img)
canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
canvas1.pack(expand=True, fill=BOTH)

btn1 = Button(root, text="Add Book Details", bg="black", fg="white", command=addBook)
btn1.place(relx=0.28, rely=0.15, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=delete)
btn2.place(relx=0.28, rely=0.25, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="All Book", bg="black", fg="white", command=View)
btn3.place(relx=0.28, rely=0.35, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg="black", fg="white", command=issueBook)
btn4.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnBook)
btn5.place(relx=0.28, rely=0.55, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Search Book", bg="black", fg="white", command=search)
btn6.place(relx=0.28, rely=0.65, relwidth=0.45, relheight=0.1)

btn7 = Button(root, text="Show Member Info", bg="black", fg="white", command=ViewMem)
btn7.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

root.mainloop()
