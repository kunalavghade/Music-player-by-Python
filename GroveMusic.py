from tkinter import *
import recent as r
import musicList as m
import searchWin as s

class GroveMusic():
	# initialize root window 
	def __init__(self):
		self.window = Tk()
		self.cliked = True
		self.window.title("Grove Music")
		self.window.geometry("800x650+270+60")
		self.window.wm_overrideredirect(True)
		self.window.resizable(False,False)
		self.starting()
		self.window.mainloop()

	# Looding Icon - Blue Frame
	def starting(self):
		self.GroveIcon = PhotoImage(file = "asset/Grove.png")
		self.blueFrame = Frame(self.window,bg="#0090FF")
		self.Icon = Label(self.blueFrame,image = self.GroveIcon,bg="#0090FF")
		self.Icon.place(relheight=1,relwidth=1)
		self.blueFrame.place(relheight=1,relwidth=1)
		self.blueFrame.after(2000,self.deleteFrame)

	# delete loading frame
	def deleteFrame(self):
		self.window.geometry("800x620+270+60")
		self.window.wm_overrideredirect(False)
		self.blueFrame.destroy()
		self.mainWindow()

	# create functionnig window
	def mainWindow(self):
		self.height = 0.83
		self.width = 0.06
		self.bar = Frame(self.window,bg="#313131")
		self.barFunc()
		self.bar.place(relheight=0.83,relwidth=self.width)
		self.listFrame = Frame(self.window,bg="black")
		self.MusicList = Frame(self.listFrame,bg="black")
		self.musicFunc()
		self.MusicList.place(relheight=1,relwidth=1)
		self.listFrame.place(relheight = self.height,relwidth = (1-self.width),relx = self.width)

		self.playerFrame = Frame(self.window,bg = "#005099")
		self.playerFrame.place(relheight = (1-self.height),relwidth = 1,rely = self.height)

	# function bar creation
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
		self.playingBtn = Button(self.playingFrame,image=self.playingIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0)
		self.playingBtn.grid(row = 0 ,column =0)
		# serch input
		self.playing = Button(self.playingFrame,bg="#313131",font="arial 12 ",bd=0,text="Now playing                                       ",fg="#fff",activebackground="#626262",activeforeground="#fff",pady=7,)
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
		self.settingBtn = Button(self.settingFrame,image=self.settingIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0)
		self.settingBtn.grid(row = 0 ,column =0)
		# seting input
		self.settings = Button(self.settingFrame,bg="#313131",font="arial 12 ",bd=0,text="Settings                                              ",fg="#fff",activebackground="#626262",activeforeground="#fff",pady=7,)
		self.settings.grid(row=0,column=1)
		self.settingFrame.place(rely=0.9,relwidth=1,relheight=0.09)
		# ----------------------------------------------------------------------------------------------------------------------------
	
	# fuction bar scalling
	def resizeViwe(self):
		if self.cliked:
			for i in range(6,401):
				self.width = i/1000
				self.bar.place_configure(relwidth = self.width)
				self.listFrame.place_configure(relheight = self.height,relwidth = (1-self.width),relx = self.width)
				self.cliked = False
			self.fullViwe()
			self.searchBtn.configure(command= self.searchFunc)
			print(self.width)
		else :
			for i in range(0,341):
				self.width = (400-i)/1000
				self.bar.place_configure(relwidth = self.width)
				self.listFrame.place_configure(relheight = self.height,relwidth = (1-self.width),relx = self.width)
				self.cliked = True
			self.searchBtn.configure(command= self.resizeViwe)
			self.smallViwe()
			print(self.width)

	# miximized bar (function)
	def fullViwe(self):
		self.fullViweBtn.place_configure(relwidth=0.15)
		self.searchFrame.place_configure(relwidth=0.94,relx=0.03)
		self.searchBtn.configure(bg = "#212121",activebackground="#FFF",activeforeground="#AAA",image = self.searchIconDark)
		self.entry.grid_configure(row = 0 ,column=0)
		self.partitionFrame.place_configure(relx=0.05,rely=0.89,relheight = 0.001,relwidth=0.9)
		self.partitionFrame1.place_configure(relx=0.05,rely=0.5,relheight = 0.001,relwidth=0.9)
		self.searchBtn.grid_configure(row = 0 ,column=1)

	# minimized bar (function)
	def smallViwe(self):
		self.searchFrame.place_configure(relwidth=1,relx=0)
		self.fullViweBtn.place_configure(relwidth=1)
		self.searchBtn.configure(image=self.searchIcon,bg = "#313131",activebackground="#626262",activeforeground="#fff")
		self.entry.grid_configure(row = 0 ,column=1)
		self.partitionFrame.place_configure(relx=0.,rely=1,relheight= 0,relwidth=0)
		self.partitionFrame1.place_configure(relx=0.,rely=1,relheight= 0,relwidth=0)
		self.searchBtn.grid_configure(row = 0 ,column=0)

	# serching music
	def searchFunc(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		s.SearchWin(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

	def musicFunc(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		m.MusicLive(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

	def recent(self):
		self.MusicList.destroy()
		self.MusicList = Frame(self.listFrame,bg="black")
		r.RecentWin(self.MusicList)
		self.MusicList.place(relheight=1,relwidth=1)

if __name__ == "__main__":
	GroveMusic()
	