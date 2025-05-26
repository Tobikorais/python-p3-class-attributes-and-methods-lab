#!/usr/bin/env python3

from song import Song

Song.count = 0
Song.genre_count = {}
Song.artist_count = {}

class TestSong:
    '''Class "Song" in song.py'''

    def setup_method(self):
        """Reset the Song class attributes before each test."""
        Song.reset()

    Song("99 Problems", "Jay Z", "Rap")
    Song("Halo", "Beyonce", "Pop")
    Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 4)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.genres)
        assert("Pop" in Song.genres)
        assert("Rock" in Song.genres)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Jay Z" in Song.artists)
        assert("Beyonce" in Song.artists)
        assert("Hall and Oates" in Song.artists)
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 3)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count["Jay Z"] == 1)
        assert(Song.artist_count["Beyonce"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count["Hall and Oates"] == 2)

    def test_counts_total_songs(self):
        """Test that total_songs is updated correctly."""
        Song("Song 1", "Artist 1", "Genre 1")
        Song("Song 2", "Artist 2", "Genre 2")
        assert Song.total_songs == 2

    def test_tracks_genres(self):
        """Test that genres are tracked correctly."""
        Song("Song 1", "Artist 1", "Rap")
        Song("Song 2", "Artist 2", "Pop")
        assert "Rap" in Song.genres
        assert "Pop" in Song.genres

    def test_tracks_artists(self):
        """Test that artists are tracked correctly."""
        Song("Song 1", "Jay Z", "Rap")
        Song("Song 2", "Artist 2", "Pop")
        assert "Jay Z" in Song.artists
        assert "Artist 2" in Song.artists

    def test_counts_songs_by_genre(self):
        """Test that genre_count is updated correctly."""
        Song("Song 1", "Artist 1", "Rap")
        Song("Song 2", "Artist 2", "Rap")
        Song("Song 3", "Artist 3", "Pop")
        assert Song.genre_count["Rap"] == 2
        assert Song.genre_count["Pop"] == 1

    def test_counts_songs_by_artist(self):
        """Test that artist_count is updated correctly."""
        Song("Song 1", "Jay Z", "Rap")
        Song("Song 2", "Jay Z", "Pop")
        assert Song.artist_count["Jay Z"] == 2