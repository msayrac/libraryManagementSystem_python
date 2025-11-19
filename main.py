from tkinter import *
from tkinter import ttk
import sqlite3
import addBook,addMember
 


con = sqlite3.connect("library.db")
cur = con.cursor()

class Main(object):
    def __init__(self,master):
        self.master = master

        def displayBooks(self):
            books = cur.execute("SELECT * FROM books").fetchall()

            count = 0
            for book in books:
                print(book)
                self.list_books.insert(count,str(book[0])+ "-" + book[1])
                count += 1
            
            def bookInfo(evt):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute("SELECT * FROM books WHERE book_id =?",(id,))
                book_info = book.fetchall()
                print(book_info)

                self.list_details.delete(0,'end')

                self.list_details.insert(0,"Kitap adı :"+book_info[0][1])
                self.list_details.insert(1,"Yazar adı :"+book_info[0][2])
                self.list_details.insert(2,"Sayfa :"+book_info[0][3])
                self.list_details.insert(3,"Dil :"+book_info[0][4])

                if book_info[0][5] == 0:
                    self.list_details.insert(4, "Status : Available")
                else:
                    self.list_details.insert(4, "Status : Not Available")




            self.list_books.bind('<<ListboxSelect>>',bookInfo)

        # frames
        mainFrame =Frame(self.master)
        mainFrame.pack()
        # top Frames
        topFrame = Frame(mainFrame, width=1350, height =70, bg = "#f8f8f8",
                         padx=20, relief=SUNKEN,borderwidth=2)
        topFrame.pack(side =TOP, fill=X)

        # centerFrame
        centerFrame = Frame(mainFrame,width=1350, relief=RIDGE,bg="#e0f0f0",
                            height=680)
        centerFrame.pack(side=TOP)

        # center Left Frame
        centerLeftFrame = Frame(centerFrame,width=900,height=700,bg="#e0f0f0",
                                borderwidth=2, relief="sunken")
        centerLeftFrame.pack(side=LEFT)

        #center right Frame
        centerRightFrame = Frame(centerFrame,width=450,height=700,bg="#e0f0f0",
                                 borderwidth=2,relief="sunken")
        centerRightFrame.pack()

        # searchBar
        search_bar = LabelFrame(centerRightFrame,width=440,height=75,
                                text="Arama Kutusu",bg="#9bc9ff")
        search_bar.pack(fill=BOTH)
        self.lbl_search = Label(search_bar,text="Arama yapın : ",font="arial 12 bold",
                                bg="#9bc9ff",fg="white")
        self.lbl_search.grid(row=0,column=0,padx=20,pady=10)
        self.ent_search = Entry(search_bar,width=30,bd=10)
        self.ent_search.grid(row = 0, column = 1, columnspan = 3, padx = 10,pady=10)
        self.btn_search = Button(search_bar, text="Arama Yap",font="arial 12 bold",
                                 bg="#fcc324",fg="white", command = self.searchBooks)
        self.btn_search.grid(row=0,column=4,padx=20,pady=10)


        # List bar
        list_bar = LabelFrame(centerRightFrame,width=440,height=175,
                              text="Listeleme",bg="#fcc324")
        list_bar.pack(fill=BOTH)
        lbl_list = Label(list_bar,text = "Sıralama",font="times 16 bold",
                         fg="#2488ff",bg="#fcc324")
        lbl_list.grid(row=0,column=2)
        self.listChoice = IntVar()
        rb1 =Radiobutton(list_bar,text="Tüm Kitaplar",var =self.listChoice,
                         value = 1,bg = "#fcc324")
        rb2 =Radiobutton(list_bar,text="Kütüphane Mevcut Kitaplar",var =self.listChoice,
                         value = 2,bg = "#fcc324")
        rb3 =Radiobutton(list_bar,text="Kitap Ödünç Al",var =self.listChoice,
                         value = 3,bg = "#fcc324")
        rb1.grid(row=1,column=0)
        rb2.grid(row=1,column=1)
        rb3.grid(row=1,column=2)

        btn_list = Button(list_bar, text = "Listele", bg = "#2488ff",
                          fg = "white",font="arial 12 bold")
        btn_list.grid(row=1,column=3, padx = 40, pady = 10)

        # title and image
        image_bar = Frame(centerRightFrame, width =440, height = 350)
        image_bar.pack(fill=BOTH)
        self.title_right =Label(image_bar, text="Kütüphanemize Hoş Geldiniz",font="arial 16 bold")
        self.title_right.grid(row=0)
        self.img_library = PhotoImage(file="icons/library.png")
        self.lblImg = Label(image_bar,image=self.img_library)
        self.lblImg.grid(row=1)
        

        ################################## Tool BAR ##############################
        # add book
        self.iconbook = PhotoImage(file ="icons/add_book.png",width=5,height=5)
        self.btnbook = Button(topFrame,text="Kitap Ekle",image=self.iconbook,compound=LEFT,
                              font="arial 12 bold",command=self.addBook)
        self.btnbook.pack(side=LEFT, padx=10)

        #add member button
        self.iconmember =PhotoImage(file="icons/users.png",width=5,height=5)
        self.btnmember = Button(topFrame,text="Üye Ekle",font="arial 12 bold",padx=10,command=self.addMember1)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT,padx=10)

        # give book
        self.icongive = PhotoImage(file="icons/givebook.png",width=5,height=5)
        self.btngive = Button(topFrame,text="Kitap Teslim",font="arial 12 bold",compound=LEFT)
        self.btngive.pack(side=LEFT)

################################## Tabs #############################################
            ################## Tab1######################
        self.tabs = ttk.Notebook(centerLeftFrame, width = 900, height =660)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file = "icons/add_book.png")
        self.tab2_icon = PhotoImage(file = "icons/members.png")

        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)

        self.tabs.add(self.tab1,text="Kütüphane Yönetimi",image = self.tab1_icon,compound=LEFT)
        self.tabs.add(self.tab2,text="İstatikler",image = self.tab2_icon,compound=LEFT)

        # list books
        self.list_books = Listbox(self.tab1, width=40,height=30,bd=5, font="times 12 bold")
        self.sb = Scrollbar(self.tab1,orient=VERTICAL)
        self.list_books.grid(row=0,column=0,padx =(10,0), pady =10, sticky=N)
        self.sb.config(command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column = 0, sticky=N+S+E)

        # list detail
        self.list_details = Listbox(self.tab1,width=80, height=30, bd=5, font = "times 12 bold")
        self.list_details.grid(row=0,column=1,padx=(10,0), pady=10, sticky=N)
        
            ################## Tab1######################
            ############# statistics###############
        self.lbl_book_count = Label(self.tab2,text="",pady=20,font="vergana 14 bold")
        self.lbl_book_count.grid(row=0)
        self.lbl_member_count =Label(self.tab2,text="",pady=20,font="vergana 14 bold")
        self.lbl_member_count.grid(row=1,sticky=W)
        self.lbl_taken_count = Label(self.tab2,text="",pady=20, font="verdana 14 bold")
        self.lbl_taken_count.grid(row=2,sticky=W)

        # functions
        displayBooks(self)




    def addBook(self):
        add = addBook.AddBook()

    def addMember1(self):
        member = addMember.AddMember()


    def searchBooks(self):
        value = self.ent_search.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%'+value+'%',)).fetchall()
        print(search)
        self.list_books.delete(0,END)

        count=0

        for book in search:
            self.list_books.insert(count,str(book[0])+"-"+book[1])
            count += 1

        


def main():
    root = Tk()
    app = Main(root)
    root.title("Ktüphane Yönetim Sistemi")
    root.geometry("1350x750+350+200")
    # root.iconbitmap("icons/icon.icon")
    root.mainloop()

if __name__ == "__main__":
    main()








