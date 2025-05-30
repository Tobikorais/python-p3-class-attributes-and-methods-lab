#!/usr/bin/env python3

from lib.song import Song

Song.count = 0
Song.genre_count = {}
Song.artist_count = {}

class TestSong:
    '''Class "Song" in song.py'''

    def setup_method(self):
        """Reset the Song class attributes before each test."""
        Song.reset()

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        song = Song("99 Problems", "Jay Z", "Rap")
        assert song.name == "99 Problems"
        assert song.artist == "Jay Z"
        assert song.genre == "Rap"

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert Song.count == 2

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert "Rap" in Song.genres
        assert "Pop" in Song.genres

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        assert "Jay Z" in Song.artists
        assert "Beyonce" in Song.artists

    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Crazy in Love", "Beyonce", "Pop")
        assert Song.genre_count["Rap"] == 1
        assert Song.genre_count["Pop"] == 2

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        Song("99 Problems", "Jay Z", "Rap")
        Song("Halo", "Beyonce", "Pop")
        Song("Crazy in Love", "Beyonce", "Pop")
        assert Song.artist_count["Jay Z"] == 1
        assert Song.artist_count["Beyonce"] == 2