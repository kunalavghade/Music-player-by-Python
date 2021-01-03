import os
import sqlite3
import eyed3
import pygame.mixer as sp
from tkinter import messagebox

class MusicDataBase():
	def __init__(self):
		self.conn = sqlite3.connect("database.db")
		self.cor = self.conn.cursor()
		try:
			self.createDataBase()
		except:
			pass

	def createDataBase(self):
		self.conn.execute('''CREATE TABLE "MusicLIB" (
			"No"	INTEGER PRIMARY KEY AUTOINCREMENT,
			"SongName"	TEXT,
			"Artist"	TEXT,
			"Album"	TEXT, 
			"Path" TEXT,
			"ext" TEXT
		);''')
		self.conn.commit()

	def upDateDataBase(self,query):
		songName = query[0]
		artist = query[1]
		album = query[2]
		path = query[3]
		ext = query[4]
		self.databaseCmd = "insert into 'MusicLIB' (SongName,Artist,Album,Path,ext) values(?,?,?,?,?)"
		self.cor.execute(self.databaseCmd,(songName,artist,album,path,ext))
		self.conn.commit()

	def detection(self,dirPath):
		self.dir = dirPath
		self.song = os.listdir(self.dir)
		for track in self.song:
			song_info = []
			if track.endswith(".mp3") :
				song_info.append(os.path.splitext(track)[0])  
				abs_location = '%s/%s' %(self.dir,track)
				track_info = eyed3.load(abs_location)
				try:
					if track_info.tag.artist == None:
						song_info.append('unknown artist')
					else:
						song_info.append(track_info.tag.artist)					
				except:
					song_info.append('unknown artist')

				try:
					if track_info.tag.album == None:
						song_info.append('unknown album')
					else:
						song_info.append(track_info.tag.album)	
				except:
					song_info.append('unknown album')
				song_info.append(self.dir)
				song_info.append(os.path.splitext(track)[1])
				# print(song_info)
				try:
					self.upDateDataBase(song_info)	
				except:
					pass
		messagebox.showinfo("Success","Songs added successfully !                     ")		

	def selectSection(self,rowid,search):
		query=self.cor.execute(f'''SELECT "_rowid_",* FROM "main"."MusicLIB" WHERE "{rowid}" LIKE"%{search}%"''').fetchall()
		return query
		
	def getPath(self,no):
		query=self.cor.execute(f"select  Path , SongName , ext from 'MusicLIB' where No ='{no}'").fetchall()
		return query

	def getSongName(self,no):
		query=self.conn.execute(f"select SongName ,Artist,Album from 'MusicLIB' where No ='{no}'").fetchall()
		return query

	def playFile(self,path):
		sp.init()
		sp.music.load(path)
		sp.music.play(loops=0)

	def playFileAt(self,path,a):
		sp.init()
		sp.music.load(path)
		sp.music.play(loops=0,start=a)

	def getLength(self):
		query=self.conn.execute('''SELECT COUNT(*) FROM (SELECT "_rowid_",* FROM "main"."MusicLIB");''').fetchall()
		return query

	def stopFile(self):
		sp.music.stop()

	def delete_table(self):
		query=messagebox.askokcancel("Reset", "Reset directory to default empty !")
		if query:
			try:
				self.conn.execute('''DROP TABLE "main"."MusicLIB";''')
				messagebox.showinfo("Success","Songs Reset successfully !                     ")		

			except:
				pass
		else:
			pass

	def pause(self):
		try:
			sp.music.pause()
		except:
			pass

	def unPause(self):
		try:
			sp.music.unpause()
		except:
			pass

	def vol_Val(self,x):
		try:
			sp.music.set_volume(x)
		except :
			pass

	def get_curret_time(self):
		return sp.music.get_pos()

	def stop(self):
		try:
			sp.music.stop()
		except:
			pass
	
	def read_file(self):
		try:
			with open('config.txt', 'r') as f:
				f_content = f.readline()
				if f_content == "Darktheam : false":
					return True
				else:
					return False
		except :
			self.write_file("false")
			return True

	def write_file(self,arg):
		with open('config.txt','w') as wf:
			wf.write(f"Darktheam : {arg}")

	def ger_artist_list(self,arg):
		b=self.cor.execute(f'SELECT {arg} FROM "main"."MusicLIB" WHERE "{arg}" NOT LIKE "unknown {arg}"').fetchall()
		artist_list=[f"unknown {arg}"]
		for i in b:
			artist_list.append(i[0])		
		return artist_list

