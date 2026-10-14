class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)
            print(song, "added to playlist.")
        else:
            print(song, "already exists in playlist.")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(song, "removed from playlist.")
        else:
            print(song, "not found in playlist.")

    def display_songs(self):
        print("Playlist:", self.name)
        if self.songs:
            for song in self.songs:
                print(song)
        else:
            print("Playlist is empty.")

    def song_count(self):
        return len(self.songs)

playlist = Playlist("My Favorites")

playlist.add_song("Chuttamalle")
playlist.add_song("Samajavaragamana")
playlist.add_song("Chuttamalle")  

playlist.display_songs()
print("Total songs:", playlist.song_count())

playlist.remove_song("Chuttamalle")
playlist.remove_song("RRR Song") 

playlist.display_songs()