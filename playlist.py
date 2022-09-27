
class Playlist():
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.songs = []
    
    def add_song(self, song):
        self.songs.append(song)

    def get_ids(self):
        ids = []
        for song in self.songs:
            ids.append(song.id)

        return ids