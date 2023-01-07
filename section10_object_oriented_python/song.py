class Song:
    """class to represent a song
    
    Attributes:
        title (str): The title of the song
        artist (Artist): An artist object representing the song creator
        duration (int): The duration of the song in seconds. May be zero
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """class to represent an Album using it's track list

    Attributes:
        name (str): the name of the album.
        year (int): the year the album was released.
        artist: (Artist): the artist responsible for the album. If not specified,
        the artist will default to an artist with the name "Various Artist".
        tracks (list[Song]): A list of the songs on the album.

        Methods:
            add_song: Used to add a new song to the album's track list.
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artist")
        else:
            self.artist = artist

        self.tracks = []


    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): a song to add.
            position (optional[int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary.
                Otherwise the song will be added to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


class Artist:
    """Basic class to store artist details.

    Attributes:
        name (str): name of the artist.
        album (list[Album]): A list of albums by this artist.
            The list includes only those albums that in this collection,
            it is not an exhaustive list of the artist's published albums.

    Methods:
        add_album: Use to add a new album to the artist album list.
    """

    def __init__(self, name):
        self.name = name
        self.albums = []


    def add_album(self, album):
        """Add a new album to the list.

            Args:
                album (Album): Album object to add to the list.
                    If the album is already present, it will not be added again (although this is yet to be implemented)
        """
        self.albums.append(album)


def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            # data rows should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print("{}:{}:{}:{}".format(artist_field, album_field, year_field, song_field))

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist != artist_field:
                # we've just read details for a new artist
                # store the current album in the current artist collection then create a new artist object
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist (artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                # we've just read a new album for the current artist
                # store the current album in the artist's collection then create a new album object
                new_artist.add_album(new_album)
                new_album = Album("{}:{}:{}:".format(artist_field, album_field, year_field, song_field))

                if new_artist is None:
                    new_artist = Artist(artist_field)
                elif new_artist.name != artist_field:
                    # we've just read details for a new artist
                    # store the current album in the currents artists collection then create a new artist object
                    new_artist.add_album(new_album)
                    artist_list.append(new_artist)
                    new_artist = Artist(artist_field)
                    new_album = None

                if new_album is None:
                    new_album = Album(album_field, year_field, new_artist)
                elif new_album.name != album_field:
                    # we've just read a new album for the current artist
                    # store the current album in the artist's collection then create a new album object
                    new_artist.add_album(new_album)
                    new_album = Album(album_field, year_field, new_artist)

                #create a new song object and add it to the current album's collection
                new_song = Song(song_field, new_artist)
                new_album.add_song(new_song)

        # After read the last line of the text file, we will have an artist that havent been
        # stored - process them now
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)



    return artist_list



if __name__ == '__main__':
    artists = load_data()
    print("There are {} artists".format(len(artists)))












