from tkinter import *

class MusicLive():
    def __init__(self,window):
        self.root = window
        print("self gotted")
        self.button =Button(self.root, text = "click me")
        self.button.place(relx=0.5,rely=.05)
