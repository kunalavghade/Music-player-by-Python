from tkinter import *

class NowPlaying():
	def __init__(self,window):
		self.window = window
		my_canvas =  Canvas(self.window)
		my_canvas.pack(fill=BOTH,expand=1,side=LEFT)
		my_Scroll = ttk.Scrollbar(self.window,orient=VERTICAL,command = my_canvas.yview)
		my_Scroll.pack(side= RIGHT,fill=Y)
		my_canvas.configure(yscrollcommand=my_Scroll.set)
		my_canvas.bind('<Configure>', lambda e : my_canvas.configure(scrollregion = my_canvas.bbox("all")))
		secondFrame = Frame(my_canvas)
		my_canvas.create_window((0,0),window = secondFrame ,anchor="nw")
		for i in range(100):
		if b ==int(current_time):
