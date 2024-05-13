class Song:
    name = ""
    genre = ""
    artist = ""
    ID = ""
    url = ""

    def __init__(self, name: str, artist: str, songID: str, url: str):
        self.name = name
        # self.genre = genre
        self.artist = artist
        self.ID = songID
        self.url = url

    def get_name(self):
        return self.name

    # def get_genre(self):
    #     return self.genre

    def get_artist(self):
        return self.artist

    def get_id(self):
        return self.ID

    def get_url(self):
        return self.url

    def set_name(self, value):
        self.name = value

    # def set_genre(self, value):
    #     self.genre = value

    def set_artist(self, value):
        self.artist = value

    def set_ID(self, value):
        self.ID = value

    def set_url(self, value):
        self.url = value
