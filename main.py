from tkinter import *
from tkinter import ttk

class Main(object):
    def __init__(self,master):
        self.master = master

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

        # List bar
        list_bar = LabelFrame(centerRightFrame,width=440,height=175,
                              text="Listeleme",bg="#fcc324")
        list_bar.pack(fill=BOTH)

        # add book button
        self.iconbook = PhotoImage(file ="icons/add_book.png",width=5,height=5)
        self.btnbook = Button(topFrame,text="Kitap Ekle",image=self.iconbook,compound=LEFT,
                              font="arial 12 bold")
        self.btnbook.pack(side=LEFT, padx=10)

        #add member button
        self.iconmember =PhotoImage(file="icons/users.png",width=5,height=5)
        self.btnmember = Button(topFrame,text="Üye Ekle",font="arial 12 bold",padx=10)
        self.btnmember.configure(image=self.iconmember,compound=LEFT)
        self.btnmember.pack(side=LEFT)

        # give book

        self.icongive = PhotoImage(file="icons/givebook.png",width=5,height=5)
        self.btngive = Button(topFrame,text="Kitap Teslim",font="arial 12 bold",compound=LEFT)
        self.btngive.pack(side=LEFT)

def main():
    root = Tk()
    app = Main(root)
    root.title("Ktüphane Yönetim Sistemi")
    root.geometry("1350x750+350+200")
    # root.iconbitmap("icons/icon.icon")
    root.mainloop()

if __name__ == "__main__":
    main()

print("Hello")













