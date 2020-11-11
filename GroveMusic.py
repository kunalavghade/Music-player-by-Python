from tkinter import *
from tkinter import filedialog
import recent as r
from tkinter import ttk
import musicFind as mm
import searchWin as s
# import nowPlaying as np
import time
from mutagen.mp3 import MP3

BOTTOMBAR="#051C2A"
BOTTOMBARBRIGHT="#0B3F5E"

class GroveMusic():
	# initialize root window 
	def __init__(self):
		self.window = Tk()
		self.cliked = True
		self.songNameToEdit=""
		self.Midlebutton_image = False
		self.middleBtnClick = True
		self.songNo = 0
		self.vol_clicked=True
		self.get_song_length=""
		self.converted_current_time=""
		self.pause = PhotoImage(file = "asset/pause.png")
		self.play = PhotoImage(file = "asset/play.png")
		self.scaleIcon = PhotoImage(file = "asset/scale.png")
		self.albumIcon = PhotoImage(file = "asset/album.png")
		self.backBtnIcon = PhotoImage(file = "asset/back.png")
		self.nextBtnIcon = PhotoImage(file = "asset/next.png")
		self.fullVol = PhotoImage(file = "asset/full_vol.png")
		self.seventy = PhotoImage(file = "asset/80.png")
		self.fifty = PhotoImage(file = "asset/60.png")
		self.Twenty_five = PhotoImage(file = "asset/40.png")
		self.no_vol = PhotoImage(file = "asset/no.png")
		self.window.title("Grove Music")
		self.window.geometry("800x650+270+60")
		self.window.wm_overrideredirect(True)

		self.window.resizable(False,False)
		self.starting()
		self.window.mainloop()

	# --------------------------Looding Icon - Blue Frame---------------------------------
	def starting(self):
		self.GroveIcon = PhotoImage(file = "asset/Grove.png")
		self.blueFrame = Frame(self.window,bg="#0090FF")
		self.Icon = Label(self.blueFrame,image = self.GroveIcon,bg="#0090FF")
		self.Icon.place(relheight=1,relwidth=1)
		self.blueFrame.place(relheight=1,relwidth=1)
		self.blueFrame.after(2000,self.deleteFrame)

	# ------------------------- delete loading frame ----------------------------------
	def deleteFrame(self):
		# # self.window.geometry("800x620+270+60")
		self.window.wm_overrideredirect(False)
		self.blueFrame.destroy()
		self.mainWindow()

	def quitWin(self):
		self.window.quit()
		self.mf.stop()

	# ------------------------ create functionnig window --------------------------------
	def mainWindow(self):
		# barWin = Frame(self.window,bg="#fff",height=10,width=800,)
		# b=Button(barWin,text="X",bg="#000",fg="#000",bd=0,activebackground="#f00",activeforeground="#fff",command=self.quitWin).place(relheight=1,relx=0.94,relwidth=0.06)
		# barWin.pack()
		self.windowSub = Frame(self.window,height=650,width=800)
		self.windowSub.pack()
		self.height = 0.83
		self.width = 0.06
		self.bar = Frame(self.windowSub,bg="#313131")
		self.barFunc()
		self.bar.place(relheight=0.83,relwidth=self.width)

		self.listFrame = Frame(self.windowSub,bg="black")
		self.MusicList = Frame(self.listFrame,bg="black")
		self.MusicLiveWindow(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)
		self.listFrame.place(relheight = self.height,relwidth = (1-self.width),relx = self.width)

		self.playerFrame = Frame(self.windowSub,bg = "#005099")
		# bb.BottomBar(self.playerFrame)
		self.bottomBar()
		self.playerFrame.place(relheight = (1-self.height),relwidth = 1,rely = self.height)

	# ------------------------- Right bar creation -------------------------------------
	def barFunc(self):
		# full viwe button
		self.line = PhotoImage(file="asset/lines.png")
		self.fullViweBtn = Button(self.bar, bg = "#313131",activebackground="#626262",text = "=",activeforeground="#fff",borderwidth=0, command = self.resizeViwe,image = self.line)
		self.fullViweBtn.place(rely = 0.1, relwidth = 1,relheight=0.09)
		# -------------------------------------------------- Arrow Icon --------------------------------------------------------------
		self.arrowIcon = PhotoImage(file="asset/Arrow.png")
		self.arrowFrame = Frame(self.bar,bg="#313131")
		# Search button
		self.arrow = Button(self.arrowFrame,image=self.arrowIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0)
		self.arrow.grid(row = 0 ,column =0)
		# serch input
		self.Grove = Label(self.arrowFrame,bg="#313131",font="arial 12 ",bd=0,text="Groove music                                            ",fg="#fff",pady=7)
		self.Grove.grid(row=0,column=1)
		self.arrowFrame.place(rely=0.01,relwidth=1,relheight=0.09)
		# --------------------------------------------------------------------------------------------------------------------------------
		#------------------------------------------- Search Frame----------------------------------------------------------------
		self.searchIcon = PhotoImage(file = "asset/search.png")
		self.searchIconDark = PhotoImage(file = "asset/searchP.png")
		self.searchFrame = Frame(self.bar,bg="#212121")
		# Search button
		self.searchBtn = Button(self.searchFrame,image=self.searchIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command = self.resizeViwe)
		self.searchBtn.grid(row = 0 ,column =0)
		# serch input
		self.entry = Entry(self.searchFrame,bg="#212121",width=28,font="arial 12",bd=0,fg="#fff",)
		self.entry.grid(row=0,column=1)
		self.searchFrame.place(rely=0.2,relwidth=1,relheight=0.08)
		# -------------------------------------------------------------------------------------------------------------------------
		# -------------------------------------------------- music Icon --------------------------------------------------------------
		self.musicIcon = PhotoImage(file="asset/music.png")
		self.musicFrame = Frame(self.bar,bg="#313131")
		# Search button
		self.musicBtn = Button(self.musicFrame,image=self.musicIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command=self.musicFunc)
		self.musicBtn.grid(row = 0 ,column =0)
		# serch input
		self.muMusic = Button(self.musicFrame,bg="#313131",font="arial 12 ",bd=0,text="My music                                              ",fg="#fff",activebackground="#626262",activeforeground="#fff",command=self.musicFunc)
		self.muMusic.grid(row=0,column=1)
		self.musicFrame.place(rely=0.3,relwidth=1,relheight=0.09)
		# -----------------------------------------------------------------------------------------------------------------------------
		# -------------------------------------------------- recent Icon --------------------------------------------------------------
		self.recentIcon = PhotoImage(file="asset/resent.png")
		self.recentFrame = Frame(self.bar,bg="#313131")
		# Search button
		self.recentBtn = Button(self.recentFrame,image=self.recentIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command=self.recent)
		self.recentBtn.grid(row = 0 ,column =0)
		# serch input
		self.recent = Button(self.recentFrame,bg="#313131",font="arial 12 ",bd=0,text="Recent playes                                      ",fg="#fff",activebackground="#626262",activeforeground="#fff",pady=7,command=self.recent)
		self.recent.grid(row=0,column=1)
		self.recentFrame.place(rely=0.4,relwidth=1,relheight=0.09)
		# -----------------------------------------------------------------------------------------------------------------------------
		# -----------------------------------------------------partition------------------------------------
		self.partitionFrame1 = Frame(self.bar,bg="#fff")
		self.partitionFrame1.place()
		# -------------------------------------------------------------------------------------------------
		# ------------------------------------------- Now Playing -------------------------------------------
		self.playingIcon = PhotoImage(file="asset/NowPlaying.png")
		self.playingFrame = Frame(self.bar,bg="#313131")
		# Search button
		self.playingBtn = Button(self.playingFrame,image=self.playingIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command=self.NowPlayingFunc)
		self.playingBtn.grid(row = 0 ,column =0)
		# serch input
		self.playing = Button(self.playingFrame,bg="#313131",font="arial 12 ",bd=0,text="Now playing                                       ",fg="#fff",activebackground="#626262",activeforeground="#fff",pady=7,command=self.NowPlayingFunc)
		self.playing.grid(row=0,column=1)
		self.playingFrame.place(rely=0.51,relwidth=1,relheight=0.09)
		# -----------------------------------------------------------------------------------------------------
		# -----------------------------------------------------partition------------------------------------
		self.partitionFrame = Frame(self.bar,bg="#fff")
		self.partitionFrame.place()
		# -------------------------------------------------------------------------------------------------
		# -------------------------------------------------- Setting Icon --------------------------------------------------------------
		self.settingIcon = PhotoImage(file="asset/setting.png")
		self.settingFrame = Frame(self.bar,bg="#313131")
		# setting button
		self.settingBtn = Button(self.settingFrame,image=self.settingIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command=self.settingsBtnFunc)
		self.settingBtn.grid(row = 0 ,column =0)
		# seting input
		self.settings = Button(self.settingFrame,bg="#313131",font="arial 12 ",bd=0,text="Settings                                              ",fg="#fff",activebackground="#626262",activeforeground="#fff",pady=7,command=self.settingsBtnFunc)
		self.settings.grid(row=0,column=1)
		self.settingFrame.place(rely=0.9,relwidth=1,relheight=0.09)
		# ----------------------------------------------------------------------------------------------------------------------------
	
	# ----------------------------- Bottom Player Bar -----------------------------------
	def bottomBar(self):
		self.songImage = Button(self.playerFrame,image=self.albumIcon,bg="#333",activebackground="#444",bd=0,command=self.NowPlayingFunc)
		self.songImage.place(relheight=1,relwidth=0.12)
		self.songName  = Button(self.playerFrame,text=self.songNameToEdit,activebackground=BOTTOMBARBRIGHT,activeforeground="#eee",borderwidth=0,bg=BOTTOMBAR,fg="#ccc",anchor='w',font="12",command=self.NowPlayingFunc)
		self.songName.place(relwidth=0.2,relheight=1,relx=0.12)
		backBtn = Button(self.playerFrame,image=self.backBtnIcon,activebackground=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,bg=BOTTOMBAR,command=self.playBack,anchor="e").place(relheight=0.6,relwidth=0.1,relx=0.32)
		if self.Midlebutton_image==True:
			self.middleBtn = Button(self.playerFrame,image=self.pause,activebackground=BOTTOMBAR,bg=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,command=self.middleBtnFunc)
		else:
			self.middleBtn = Button(self.playerFrame,image=self.play,activebackground=BOTTOMBAR,bg=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,command=self.middleBtnFunc)
		self.middleBtn.place(relheight=0.6,relwidth=0.12,relx=0.42)
		nextBtn = Button(self.playerFrame,image=self.nextBtnIcon,activebackground=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,bg=BOTTOMBAR,command=self.playNext,anchor="w").place(relheight=0.6,relwidth=0.1,relx=0.54)
		sliderFrame = Frame(self.playerFrame,bg=BOTTOMBAR)
		self.songSlider = Scale(sliderFrame, from_=0, to=100, orient=HORIZONTAL,bg="#0090aa",borderwidth=0,highlightthickness=0,sliderrelief=FLAT,troughcolor="#777",fg=BOTTOMBAR,width=8,length=180,highlightcolor="#0090ff",command=self.go_to_pos)
		self.songSlider.pack()
		coverFrame=Frame(sliderFrame,bg=BOTTOMBAR)
		coverFrame.place(relwidth=1,relheight=0.442)
		self.temp_lable = Label(coverFrame,text=self.converted_current_time,bg=BOTTOMBAR,fg="#fff")
		self.temp_lable.pack(side=LEFT,padx=25)
		self.song_length_lable = Label(coverFrame,text=self.get_song_length,bg=BOTTOMBAR,fg="#fff")
		self.song_length_lable.pack(side=RIGHT,padx=25)
		sliderFrame.place(relx=0.32,relwidth=0.32,relheight=0.4,rely=0.6)
		self.volBtn = Button(self.playerFrame,image=self.fullVol,activebackground=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,bg=BOTTOMBAR,anchor="e",command=self.vol_mute)
		self.volBtn.place(relheight=0.6,relwidth=0.1,relx=0.64)
		volScliderFrame = Frame(self.playerFrame,bg=BOTTOMBAR)
		self.volScal = Scale(volScliderFrame, from_=0, to=100,command = self.vol_controll, orient=HORIZONTAL,bg="#0090aa",borderwidth=0,highlightthickness=0,sliderrelief=FLAT,troughcolor="#777",fg=BOTTOMBAR,width=8,length=125,highlightcolor="#0090ff")
		self.volScal.set(100)
		self.volScal.pack(pady=7)
		self.coverframe = Frame(volScliderFrame,bg=BOTTOMBAR).place(relwidth=1,relheight=0.45)
		volScliderFrame.place(relheight=0.6,relwidth=0.17,relx=0.74)
		scaleWindow = Button(self.playerFrame,image=self.scaleIcon,activebackground=BOTTOMBAR,activeforeground=BOTTOMBAR,borderwidth=0,bg=BOTTOMBAR,).place(relheight=0.6,relwidth=0.09,relx=0.91)
		bottomCorner = Frame(self.playerFrame,bg=BOTTOMBAR).place(rely=0.6,relheight=0.4,relwidth=0.36,relx=0.64)



	# ---------------------------- Rightbar Bar Scalling -------------------------------
	def resizeViwe(self):
		if self.cliked:
			for i in range(6,401):
				self.width = i/1000
				self.bar.place_configure(relwidth = self.width)
				self.listFrame.place_configure(relheight = self.height,relwidth = (1-self.width),relx = self.width)
				self.cliked = False
			self.fullViwe()
			self.searchBtn.configure(command= self.searchFunc)
		else :
			for i in range(0,341):
				self.width = (400-i)/1000
				self.bar.place_configure(relwidth = self.width)
				self.listFrame.place_configure(relheight = self.height,relwidth = (1-self.width),relx = self.width)
				self.cliked = True
			self.searchBtn.configure(command= self.resizeViwe)
			self.smallViwe()

	# ------------------------- Right Bar miximized (function) --------------------------
	def fullViwe(self):
		self.fullViweBtn.place_configure(relwidth=0.15)
		self.searchFrame.place_configure(relwidth=0.94,relx=0.03)
		self.searchBtn.configure(bg = "#212121",activebackground="#FFF",activeforeground="#AAA",image = self.searchIconDark)
		self.entry.grid_configure(row = 0 ,column=0)
		self.partitionFrame.place_configure(relx=0.05,rely=0.89,relheight = 0.001,relwidth=0.9)
		self.partitionFrame1.place_configure(relx=0.05,rely=0.5,relheight = 0.001,relwidth=0.9)
		self.searchBtn.grid_configure(row = 0 ,column=1)

	#-------------------------- Right Bar minimized (function) ---------------------------
	def smallViwe(self):
		self.searchFrame.place_configure(relwidth=1,relx=0)
		self.fullViweBtn.place_configure(relwidth=1)
		self.searchBtn.configure(image=self.searchIcon,bg = "#313131",activebackground="#626262",activeforeground="#fff")
		self.entry.grid_configure(row = 0 ,column=1)
		self.partitionFrame.place_configure(relx=0.,rely=1,relheight= 0,relwidth=0)
		self.partitionFrame1.place_configure(relx=0.,rely=1,relheight= 0,relwidth=0)
		self.searchBtn.grid_configure(row = 0 ,column=0)

	# -------------------------------- Searching Window --------------------------------
	def searchFunc(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		s.SearchWin(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

	# --------------------------- music List window creation ---------------------------
	def musicFunc(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		self.MusicLiveWindow(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

	#------------------------------ recent window creation ------------------------------
	def recent(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		r.RecentWin(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

	#  ------------------------------ Midlebutton function ------------------------------
	def middleBtnFunc(self):
		if self.middleBtnClick == True :
			self.middleBtn.configure(image=self.pause)
			self.middleBtnClick = False
			self.Midlebutton_image = True
			self.mf.unPause()
		else:
			self.middleBtn.configure(image=self.play)
			self.middleBtnClick = True
			self.Midlebutton_image = True
			self.mf.pause()

	# ----------------------------- Now playing window --------------------------------
	def NowPlayingFunc(self):
		self.windowSub.destroy()
		self.fullListWindow = Frame(self.window,bg="red")
		song_info_frame = Frame(self.fullListWindow,bg="#000")
		self.songImage = Button(song_info_frame,image=self.albumIcon,bg="#333",activebackground="#444",bd=0)
		self.songImage.place(relheight=0.7,relwidth=0.15,rely=0.13,relx=0.08)
		self.songName  = Button(song_info_frame,text=self.songNameToEdit,activebackground="#000",activeforeground="#fff",borderwidth=0,bg="#000",fg="#fff",anchor='w',font="arial 15 bold")
		self.songName.place(relwidth=0.7,relheight=0.6,relx=0.25,rely=0.13)
		song_info_frame.place(relheight=0.25,relwidth=1)
		
		slider_frame = Frame(self.fullListWindow,bg="#000")
		self.temp_lable = Label(slider_frame,font="arial 13",text=self.converted_current_time,bg="#000",fg="#fff",anchor=E)
		self.temp_lable.place(relwidth=0.1,relheight=1)
		s = Frame(slider_frame,bg="#000")
		self.songSlider = Scale(s, from_=0, to=100, orient=HORIZONTAL,bg="#0090aa",borderwidth=0,highlightthickness=0,sliderrelief=FLAT,troughcolor="#777",fg="#000",width=8,length=600,highlightcolor="#0090ff",command=self.go_to_pos)
		self.songSlider.pack()
		cover = Frame(s,bg="#000")
		cover.place(relwidth=1,relheight=0.7)
		s.place(relwidth=0.8,relx=0.1,relheight=1)
		self.song_length_lable = Label(slider_frame,font="arial 13",text=self.get_song_length,bg="#000",fg="#fff",anchor=W)
		self.song_length_lable.place(relwidth=0.1,relheight=1,relx=0.9)
		slider_frame.place(relheight=0.05,relwidth=1,rely=0.25)

		player_frame = Frame(self.fullListWindow,bg="green")
		backBtn = Button(player_frame,image=self.backBtnIcon,activebackground="#000",activeforeground="#000",borderwidth=0,bg="#000",command=self.playBack,anchor="e").place(relheight=1,relwidth=0.1)
		if self.Midlebutton_image==True:
			self.middleBtn = Button(player_frame,image=self.pause,activebackground="#000",bg="#000",activeforeground="#000",borderwidth=0,command=self.middleBtnFunc)
		else:
			self.middleBtn = Button(player_frame,image=self.play,activebackground="#000",bg="#000",activeforeground="#000",borderwidth=0,command=self.middleBtnFunc)

		self.middleBtn.place(relheight=1,relwidth=0.12,relx=0.1)
		nextBtn = Button(player_frame,image=self.nextBtnIcon,activebackground="#000",activeforeground="#000",borderwidth=0,bg="#000",command=self.playNext,anchor="w").place(relheight=1,relwidth=0.1,relx=0.22)
		self.volBtn = Button(player_frame,image=self.fullVol,activebackground="#000",activeforeground="#000",borderwidth=0,bg="#000",anchor="e",command=self.vol_mute)
		self.volBtn.place(relheight=1,relwidth=0.1,relx=0.32)
		v = Frame(player_frame,bg="#000")
		self.volScal = Scale(v, from_=0, to=100,command = self.vol_controll, orient=HORIZONTAL,bg="#0090aa",borderwidth=0,highlightthickness=0,sliderrelief=FLAT,troughcolor="#777",fg=BOTTOMBAR,width=8,length=200,highlightcolor="#0090ff")
		self.volScal.set(100)
		self.volScal.pack(pady=8)
		c=Frame(v,bg="#000")
		c.place(relwidth=1,relheight=0.45)
		v.place(relheight=1,relwidth=0.3,relx=0.42)
		b=Frame(player_frame,bg="#000").place(relheight=1,relwidth=0.18,relx=0.72)
		scaleWindow = Button(player_frame,image=self.scaleIcon,activebackground="#000",activeforeground="#000",borderwidth=0,bg="#000",anchor=W).place(relheight=1,relwidth=0.1,relx=0.9)
		player_frame.place(relheight=0.1,relwidth=1,rely=0.3)

		song_list_frame = Frame(self.fullListWindow,bg="blue")
		my_canvas =  Canvas(song_list_frame,bg="#000")
		my_canvas.pack(fill=BOTH,expand=1,side=LEFT)
		my_Scroll = ttk.Scrollbar(song_list_frame,orient=VERTICAL,command = my_canvas.yview,)
		my_Scroll.pack(side= RIGHT,fill=Y)
		my_canvas.configure(yscrollcommand=my_Scroll.set)
		my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox("all")))
		self.secondFrame = Frame(my_canvas)
		my_canvas.create_window((0,0),window = self.secondFrame ,anchor="nw")
		images = PhotoImage(file = 'asset/searchP.png')
		for j in self.mf.getLength():
			for i in range(j[0]):
				c=self.mf.getSongName(i+1)
				play = Button(self.secondFrame,text="▶",bg="#000",fg="#aaa",borderwidth=0,font="15",activeforeground="#fff",activebackground="#333",height=2,width=5,command = lambda x = i : self.playSong(x)).grid(row=i,column=0)
				songName = Button(self.secondFrame,text=c[0][0],height=2,width=45,anchor="w",bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=1)
				artist = Button(self.secondFrame,text=c[0][1],height=2,width=18,bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=2)
				albums = Button(self.secondFrame,text=c[0][2],height=2,width=18,bg="#000",fg="#aaa",borderwidth=0,font="12",activeforeground="#fff",activebackground="#333",command = lambda x = i : self.playSong(x)).grid(row=i,column=3)
		song_list_frame.place(relwidth=1,relheight=0.6,rely=0.4)

		self.fullListWindow.place(relheight=1,relwidth=1)
		self.cancelBtn = Button(self.window,image=self.arrowIcon,width=47,bg = "#000",activebackground="#626262",height=30,activeforeground="#fff",borderwidth=0,command=self.cancelBtnFunc)
		self.cancelBtn.place(relx=0)
	
	# ---------------------------- Back To Main Window ----------------------------
	def cancelBtnFunc(self):
		self.fullListWindow.destroy()
		self.cancelBtn.destroy()
		self.mainWindow()
	
	# ------------------------------- Music list window ----------------------------
	def MusicLiveWindow(self,windowS):
		self.mf = mm.MusicDataBase()
		self.baseListFrame = windowS
		self.musicListWindow = Frame(self.baseListFrame,bg="#000")
		self.header()
		self.musicListWindow.place(relheight=1,relwidth=1)

	# ----------------------- Heading of Music List Window -------------------------
	def header(self):
		self.myMusicL =Label(self.musicListWindow,text="My Music",fg="#fff",font ="arial 22 ",pady=0,bg="#000")
		self.myMusicL.place(relheight=0.08,relwidth=0.2,relx=0,rely=0.08)

		self.btnFrame = Frame(self.musicListWindow,bg="#000")
		self.headerBtn()
		self.btnFrame.place(relheight=0.06,relwidth=0.9,relx=0.05,rely=0.18)

		self.blueLine = Frame(self.musicListWindow,bg="#0090aa")
		self.blueLine.place(relheight=0.01,relwidth=0.1,relx=0.05,rely=0.245)

		self.linePartition = Frame(self.musicListWindow,bg="#fff")
		self.linePartition.place(relheight=0.0001,relwidth=0.9,relx=0.05,rely=0.25)

		self.songListFrame = Frame(self.musicListWindow,bg="#000")
		self.musicList()
		self.songListFrame.place(relheight=0.7,relwidth=0.94,relx=0.03,rely=0.27)

	# ------------------- Buttons in Heading of Music List Window -------------------
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

	# ----------------------------- Song button List ---------------------------
	def songsBtnFunc(self):
		self.blueLine.place_configure(relx=0.05)

	# ----------------------------- Artist button List ---------------------------
	def artistBtnFunc(self):
		self.blueLine.place_configure(relx=0.193)

	# ----------------------------- Ablum button List ---------------------------
	def albumsBtnFunc(self):
		self.blueLine.place_configure(relx=0.34)

	# ---------------------------- playe List Song ------------------------------------
	def playSong(self,x):
		self.playMusic(x+1)
		self.playingVar=True

	# ----------------------------- play Next function -----------------------------
	def playNext(self):
		self.songNo+=1
		self.playMusic(self.songNo)

	# ------------------------------- play previous Function ---------------------------------
	def playBack(self):
		self.songNo-=1
		self.playMusic(self.songNo)

	# -------------------------------- Setting button function -------------------------------------
	def settingsBtnFunc(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		self.settingWindow()
		self.MusicList.place(relheight=1,relwidth=1)

	# ------------------------------- Create setting window -----------------------------------
	def settingWindow(self):
		settingLabel = Label(self.MusicList,text = "Settings",font="arial 25 ",bg="#000",fg="#fff",anchor="w").place(rely = 0.1,relwidth=0.3,relheight=0.1,relx=0.05)
		settingMusic = Label(self.MusicList,text = "Music on this PC ",font="arial 17 ",bg="#000",fg="#fff",anchor="nw").place(rely = 0.2,relwidth=0.3,relheight=0.1,relx=0.05)
		settingMusicBtn = Button(self.MusicList,text = "Chose where we look for music",bg="#000",fg="#0080bb",activeforeground="#fff",activebackground="#000",anchor="nw",font="14",bd=0,command=self.getMusicDir).place(rely = 0.27,relwidth=0.3,relheight=0.1,relx=0.05)
		settingMusicBtn = Label(self.MusicList,text = "Reset location where to look for",bg="#000",fg="#fff",anchor="nw",font="16",bd=0,).place(rely = 0.33,relwidth=0.3,relheight=0.1,relx=0.05)
		settingMusicBtn = Button(self.MusicList,text = "Reset",bg="#000",fg="#0080bb",activeforeground="#fff",activebackground="#000",anchor="nw",font="14",bd=0,command=self.deleteDb).place(rely = 0.37,relwidth=0.3,relheight=0.1,relx=0.05)
	
	# --------------------------------- get Music DIrectory --------------------------------
	def getMusicDir(self):
		try:
			self.mf.createDataBase()
		except :
			pass
		getDir = filedialog.askdirectory()
		self.mf.detection(getDir)

	# --------------------------------- Reset DataBase ------------------------------------
	def deleteDb(self):
		self.mf.delete_table()
	# ---------------------------- Creting buttons in List window ----------------------
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

	# ---------------------------------- play Main fun --------------------------------------
	def playMusic(self,y):
		self.songNo=y
		temp = self.mf.getSongName(self.songNo)
		self.songNameToEdit = temp[0][0]
		self.songName.configure(text=self.songNameToEdit)
		c=self.mf.getPath(self.songNo)
		self.path=c[0][0]+"\\"+c[0][1]+c[0][2]
		self.middleBtnClick = True
		self.mf.playFile(self.path)
		self.get_time()
		self.middleBtnFunc()

	# ------------------------------- controll Volume -----------------------------------
	def vol_controll(self,x):
		self.current_volume = x
		x = int(x)
		if x >= 70 and x <= 100:
			self.volBtn.configure(image=self.fullVol)
		elif x >= 40 and x < 70:
			self.volBtn.configure(image=self.seventy)
		elif x >= 20 and x < 40:
			self.volBtn.configure(image=self.fifty)
		elif x >= 1 and x < 20:
			self.volBtn.configure(image=self.Twenty_five)
		elif x == 0:
			self.volBtn.configure(image=self.no_vol)
		self.mf.vol_Val(x/100)

	# --------------------------------- volume mute button function --------------------------------
	def vol_mute(self):
		if self.vol_clicked == True:
			self.volBtn.configure(image=self.no_vol)
			self.vol_clicked = False 
			self.mf.vol_Val(0)
		else:
			self.vol_clicked = True 
			self.vol_controll(self.current_volume)

	# ------------------------------------- time function -------------------------------------
	def get_time(self):
		current_time = self.mf.get_curret_time()/1000
		self.converted_current_time = time.strftime('%M:%S',time.gmtime(current_time))
		song = MP3(self.path)
		get_song_length = song.info.length
		self.get_song_length = time.strftime('%M:%S',time.gmtime(get_song_length))
		if self.converted_current_time == self.get_song_length:
			self.playNext()
		try:
			self.songSlider.configure(from_=0,to=int(get_song_length))
			self.song_length_lable.configure(text=self.get_song_length)
			self.songSlider.set(int(current_time))
			self.temp_lable.configure(text=self.converted_current_time)
		except:
			pass
		self.window.after(1000,self.get_time)

	def go_to_pos(self,x):
		pass


if __name__ == "__main__":
	GroveMusic()
	