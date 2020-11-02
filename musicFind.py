import os
import sqlite3
import eyed3

class MusicDataBase():
	"""docstring for MusicDataBase"""
	def __init__(self,a):
		self.dir = "C:\\Programming\\Pythone\\Python Project\\music"
		self.song = os.listdir(self.dir)
		self.conn = sqlite3.connect("database.db")
		self.cor = self.conn.cursor()
		# self.createDataBase()
		# self.detection()
		self.getPath(a)

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

	def detection(self):
		for track in self.song:
			song_info = []
			if track.endswith(".mp3") or track.endswith(".m4a"):
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
						song_info.append('unknown artist')
					else:
						song_info.append(track_info.tag.album)	
				except:
					song_info.append('unknown artist')
				song_info.append(self.dir)
				song_info.append(os.path.splitext(track)[1])
			self.upDateDataBase(song_info)			

	def selectSection(self,rowid,search):
		query=self.cor.execute(f'''SELECT "_rowid_",* FROM "main"."MusicLIB" WHERE "{rowid}" LIKE"%{search}%"''').fetchall()
		print(query)


	def getPath(self,no):
		query=self.cor.execute(f"select  Path , SongName , ext from 'MusicLIB' where No ='{no}'").fetchall()
		print(query)


a=input("enter row name : ")

MusicDataBase(a)