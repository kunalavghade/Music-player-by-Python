from tkinter import *

class NowPlaying():
	def __init__(self,window):
		self.window = window
		btn = Button(self.window,text="click Me !", command = self.c)
		btn.pack()
