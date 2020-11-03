from tkinter import *
from tkinter import ttk
import musicFind as mm

class MusicLive():
    def __init__(self,window):
        self.mf = mm.MusicDataBase()
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

    def playSong(self,x):
        c=self.mf.getPath(x+1)
        print(c)
        path=c[0][0]+"\\"+c[0][1]+c[0][2]
        self.mf.playFile(path)



    def musicList(self):
        my_canvas =  Canvas(self.songListFrame,bg="#000")
        my_canvas.pack(fill=BOTH,expand=1,side=LEFT)
        my_Scroll = ttk.Scrollbar(self.songListFrame,orient=VERTICAL,command = my_canvas.yview,)
        my_Scroll.pack(side= RIGHT,fill=Y)
        my_canvas.configure(yscrollcommand=my_Scroll.set)
        my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox("all")))
        self.secondFrame = Frame(my_canvas)
        my_canvas.create_window((0,0),window = self.secondFrame ,anchor="nw")
        images = PhotoImage(file = 'asset/searchP.png')
        for j in self.mf.getLength():
            for i in range(j[0]):
                    c=self.mf.getSongName(i+1)
                    print(c)
                    if i%2 != 0:
                        play = Button(self.secondFrame,text="▶",bg="#000",fg="#aaa",borderwidth=0,font="15",activeforeground="#fff",activebackground="#333",height=2,width=5,command = lambda x = i : self.playSong(x)).grid(row=i,column=0)
                        songName = Button(self.secondFrame,text=c[0][0],height=2,width=38,anchor="w",bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=1)
                        artist = Button(self.secondFrame,text=c[0][1],height=2,width=16,bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=2)
                        albums = Button(self.secondFrame,text=c[0][2],height=2,width=16,bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=3)

                    else:   
                        play = Button(self.secondFrame,text="▶",bg="#444",fg="#ccc",borderwidth=0,font="15",activeforeground="#fff",activebackground="#333",height=2,width=5,command = lambda x = i : self.playSong(x)).grid(row=i,column=0)
                        songName = Button(self.secondFrame,text=c[0][0],height=2,width=38,anchor="w",bg="#444",fg="#ccc",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=1)
                        artist = Button(self.secondFrame,text=c[0][1],height=2,width=16,bg="#444",fg="#ccc",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=2)
                        albums = Button(self.secondFrame,text=c[0][2],height=2,width=16,bg="#444",fg="#ccc",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=3)


