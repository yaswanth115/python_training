class Playlist:
    def __init__(self,name):
        self.name = name
        self.songs = []
    def add_song(self,song):
        self.songs.append(song)
        print(f"suncefully added the song {song}")
    def remove_song(self,song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"successfully removed the song {song}")
        else:
            print(f"song {song} not found in the playlist")  

    def display_show(self):  
        for song in self.songs: 
            print(song)       
s1= Playlist("myfav")
s1.add_song("chuttamalle")         
s1.add_song("samajavaragamana")
s1.add_song("kundanalu") 
s1.remove_song("chuttamalle")
s1.remove_song("ramulo")
s1.display_show()
