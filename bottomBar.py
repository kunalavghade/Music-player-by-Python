from tkinter import *

class BottomBar():
	def __init__(self,window):
		self.master=window
		self.img = PhotoImage(file = "asset/pause.png")
		self.songImage = Button(self.master,text="click Me!",image=self.img)
		self.songImage.place(relheight=1,relwidth=0.12)
		self.songName  = Button(self.master,text="click Me 2 !")
		self.songName.place(relwidth=0.2,relheight=1,relx=0.12)
		self.backBtn = Button(self.master,text="backBtn")
		self.backBtn.place(relheight=1,relwidth=0.1,relx=0.32)
		self.middlekBtn = Button(self.master,text="middlekBtn")
		self.middlekBtn.place(relheight=1,relwidth=0.1,relx=0.42)
		self.nextBtn = Button(self.master,text="nextBtn")
		self.nextBtn.place(relheight=1,relwidth=0.1,relx=0.52)
		

	def thirdFrameCon():
		pass 