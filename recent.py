from tkinter import *

class RecentWin():
    def __init__(self,window):
        self.root = window
        self.windows = Frame(self.root,bg="brown")
        self.windows.place(relheight=1,relwidth=1)

