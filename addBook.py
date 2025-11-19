from tkinter import *
from tkinter import messagebox
import sqlite3

# connection to sqlite3
con = sqlite3.connect("library.db")
cur = con.cursor()

class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x750+550+200")
        self.title("Kitap Ekle")
        self.resizable(False,False)

        ################## Frames ##################
        self.topFrame = Frame(self, height =150, bg = "white")
        self.topFrame.pack(fill = X)

        #Bottom Frame
        self.bottomFrame = Frame(self,height=600, bg="#fcc324")
        self.bottomFrame.pack(fill=X)

        # heading, image and date
        self.top_image = PhotoImage(file = "icons/add_book.png",width=200, height=100)
        top_image_lbl = Label(self.topFrame,image=self.top_image, bg="white")
        top_image_lbl.place(x=120, y=10)
        heading = Label(self.topFrame,text=" Kitap Ekle ",font="arial 22 bold", fg="#003f8a", bg="white")
        heading.place(x=290,y=60)

        ################## Entries and Labels ##################

        #name
        self.lbl_name = Label(self.bottomFrame, text = "Kitap:", font = "arial 15 bold", fg ="white", bg = "#fcc324")
        self.lbl_name.place(x=40, y=40)
        self.ent_name = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_name.insert(0, "Kitap ismi giriniz : ")
        self.ent_name.place(x=150,y=45)

        #author
        self.lbl_author = Label(self.bottomFrame, text = "Yazar:", font = "arial 15 bold", fg ="white", bg = "#fcc324")
        self.lbl_author.place(x=40, y=80)
        self.ent_author = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_author.insert(0, "Yazar:")
        self.ent_author.place(x=150,y=85)

        # page
        self.lbl_page = Label(self.bottomFrame, text = "Sayfa:", font = "arial 15 bold", fg ="white", bg = "#fcc324")
        self.lbl_page.place(x=40, y=120)
        self.ent_page = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_page.insert(0, "Sayfa:")
        self.ent_page.place(x=150,y=125)

        # language
        self.lbl_language = Label(self.bottomFrame, text = "Dil:", font = "arial 15 bold", fg ="white", bg = "#fcc324")
        self.lbl_language.place(x=40, y=160)
        self.ent_language = Entry(self.bottomFrame, width=30, bd=4)
        self.ent_language.insert(0, "Dil:")
        self.ent_language.place(x=150,y=165)

        # button
        button = Button(self.bottomFrame, text = "Ekle", command=self.addBook)
        button.place(x=270, y=200)
    
    def addBook(self):
        name = self.ent_name.get()
        author = self.ent_author.get()
        page = self.ent_page.get()
        language = self.ent_language.get()

        if (name and author and page and language !=""):
            try:
                query = "INSERT INTO 'books' (book_name, book_author, book_page, book_language) VALUES(?,?,?,?)"
                cur.execute(query,(name,author,page,language))
                con.commit()
                messagebox.showinfo("Başarılı","Ekleme işlemi başarılı", icon="info")

            except:
                messagebox.showinfo("Hata","Ekleme işlemi hatalı", icon="warning")
        else:
            messagebox.showinfo("Hata","Boş alan olmamalı", icon="warning")






