from tkinter import *

class BottomBar():
	def __init__(self,window):
		self.master=window
		self.firstFrame = Frame(master=self.master,bg="red")
		self.firstFrameCon()
		self.firstFrame.place(relheight=1,relwidth=0.33)

		self.secondFrame = Frame(master=self.master,bg="green")
		self.secondFrameCon()
		self.secondFrame.place(relheight=1,relwidth=0.34,relx=0.33)

		self.thirdFrame = Frame(master=self.master,bg="#000")
		self.thirdFrame.place(relheight=1,relwidth=0.33,relx=0.67)


	def firstFrameCon(self):
		self.songImage = Button(self.firstFrame,text="click Me!")
		self.songImage.place(relheight=1,relwidth=0.4)
		self.songName  = Button(self.firstFrame,text="click Me 2 !")
		self.songName.place(relwidth=0.6,relheight=1,relx=0.4)

	def secondFrameCon(self):
		self.backBtn = Button(self.secondFrame,text="backBtn")
		self.backBtn.place(relheight=1,relwidth=0.33)
		self.middlekBtn = Button(self.secondFrame,text="middlekBtn")
		self.middlekBtn.place(relheight=1,relwidth=0.34,relx=0.33)
		self.nextBtn = Button(self.secondFrame,text="nextBtn")
		self.nextBtn.place(relheight=1,relwidth=0.33,relx=0.67)
		

	def thirdFrameCon():
		pass 