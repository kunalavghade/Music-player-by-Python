from tkinter import *

class SearchWin():
    def __init__(self,window):
        self.root = window
        self.windows = Frame(self.root,bg="blue")
        self.windows.place(relheight=1,relwidth=1)

