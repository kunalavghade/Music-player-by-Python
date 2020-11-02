# import musicFind as mF
from tkinter import *
# from Tkinter import*

class MusicLive():
    def __init__(self,window):
        self.root = window
        self.windows = Frame(self.root,bg="#000")
        self.header()
        self.windows.place(relheight=1,relwidth=1)

    def header(self):
        self.myMusicL =Label(self.windows,text="My Music",fg="#fff",font ="arial 22 ",pady=0,bg="#000")
        self.myMusicL.place(relheight=0.08,relwidth=0.2,relx=0,rely=0.08)

        self.btnFrame = Frame(self.windows,bg="#000")
        self.headerBtn()
        self.btnFrame.place(relheight=0.06,relwidth=0.9,relx=0.05,rely=0.18)

        self.blueLine = Frame(self.windows,bg="#0090aa")
        self.blueLine.place(relheight=0.01,relwidth=0.1,relx=0.05,rely=0.245)

        self.linePartition = Frame(self.windows,bg="#fff")
        self.linePartition.place(relheight=0.0001,relwidth=0.9,relx=0.05,rely=0.25)

        self.songListFrame = Frame(self.windows,bg="#000")
        self.scroll = Scrollbar(self.songListFrame,width=20,troughcolor="black",bd=0)
        self.scroll.pack(side =RIGHT,fill=Y)
        self.musicList()
        self.songListFrame.place(relheight=0.7,relwidth=0.94,relx=0.03,rely=0.27)


    def headerBtn(self):
        self.songsBtn = Button(self.btnFrame,text="Songs",font ="arial 15 bold",fg="#aaa",bg="#000",activebackground="#222",activeforeground="#fff",borderwidth=0,command = self.songsBtnFunc)
        self.songsBtn.grid(row =0 ,column =0)
        self.space1 = Label(self.btnFrame,text = "         ",bg="#000")
        self.space1.grid(row =0 ,column =1)

        self.artistBtn = Button(self.btnFrame,text="Artists",font ="arial 15 bold",fg="#aaa",bg="#000",activebackground="#222",activeforeground="#fff",borderwidth=0,command = self.artistBtnFunc)
        self.artistBtn.grid(row =0 ,column =2)
        self.space2 = Label(self.btnFrame,text = "         ",bg="#000")
        self.space2.grid(row =0 ,column =3)

        self.albumsBtn = Button(self.btnFrame,text="Albums",font ="arial 15 bold",fg="#aaa",bg="#000",activebackground="#222",activeforeground="#fff",borderwidth=0,command = self.albumsBtnFunc)
        self.albumsBtn.grid(row =0 ,column =4)

    def songsBtnFunc(self):
        self.blueLine.place_configure(relx=0.05)

    def artistBtnFunc(self):
        self.blueLine.place_configure(relx=0.193)

    def albumsBtnFunc(self):
        self.blueLine.place_configure(relx=0.34)

    def musicList(self):
        # song =mF.returnLength()
        self.songListViwe = Listbox(self.songListFrame,yscrollcommand=self.scroll.set,bg="#000",fg="#fff",height=15,borderwidth=0,font="arial 15",highlightthickness=0)
        self.songListViwe.place(relheight=1,relwidth=0.8,relx=0.05)
        for i in range(20):
            self.songListViwe.insert(i,f"lists {i}")
        self.scroll.config(command=self.songListViwe.yview)
