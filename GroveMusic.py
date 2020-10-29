from tkinter import *

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
		self.listFrame.place(relheight = self.height,relwidth = (1-self.width),relx = self.width)

		self.playerFrame = Frame(self.window,bg = "#005099")
		self.playerFrame.place(relheight = (1-self.height),relwidth = 1,rely = self.height)

	# function bar creation
	def barFunc(self):
		# full viwe button
		self.line = PhotoImage(file="asset/lines.png")
		self.fullViweBtn = Button(self.bar, bg = "#313131",activebackground="#626262",text = "=",activeforeground="#fff",borderwidth=0, command = self.resizeViwe,image = self.line)
		self.fullViweBtn.place(rely = 0.1, relwidth = 1,relheight=0.09)

		# Search Frame
		self.searchIcon = PhotoImage(file = "asset/search.png")
		self.searchFrame = Frame(self.bar,bg="#fff")

		# Search button
		self.searchBtn = Button(self.searchFrame,image=self.searchIcon,width=47,bg = "#313131",activebackground="#626262",height=44,activeforeground="#fff",borderwidth=0,command = self.resizeViwe)
		self.searchBtn.grid(row = 0 ,column =0)

		# serch input
		self.entry = Entry(self.searchFrame,bg="#fff",width=23,font="arial 15",bd=0)
		self.entry.grid(row=0,column=1)

		self.searchFrame.place(rely=0.2,relwidth=1,relheight=0.09)

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
		self.searchBtn.configure(bg = "#fff",activebackground="#FFF",activeforeground="#AAA")
		self.entry.grid_configure(row = 0 ,column=0)
		self.searchBtn.grid_configure(row = 0 ,column=1)

	# minimized bar (function)
	def smallViwe(self):
		self.searchFrame.place_configure(relwidth=1,relx=0)
		self.fullViweBtn.place_configure(relwidth=1)
		self.entry.grid_configure(row = 0 ,column=1)
		self.searchBtn.grid_configure(row = 0 ,column=0)

	# serching music
	def searchFunc(self):
		pass

if __name__ == "__main__":
	GroveMusic()
	