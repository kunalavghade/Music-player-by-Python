from tkinter import *

class MusicLive():
    def __init__(self,window):
        self.root = window
        self.windows = Frame(self.root,bg="red")
        self.windows.place(relheight=1,relwidth=1)

    def destroys(self):
        self.windows.destroy()