import pygame
from settings.environment import default

class Mixer:
    def __init__(self):
        pygame.mixer.init()
        self.songs = {}
    
    def stop(self, time = 0):
        pygame.mixer.fadeout(time)
        return self

    def pause(self):
        pygame.mixer.pause()
        return self

    def resume(self):
        pygame.mixer.unpause()
        return self

    def __addSound(self, title, song, auto_play = False, loops = 0, volume = 1.0):
        if not song or not title: return

        song = pygame.mixer.Sound(default.song_root + song)
        song.set_volume(volume)
        
        if auto_play:
            song.play(loops=loops)

        self.songs[title] = song
        return song

    def addBackground(self, song, auto_play = False, loops = 0, volume = 1.0):
        if not song: return
        return self.__addSound(song, backgrounds[song], auto_play, loops, volume)
    
    def addEffect(self, song, auto_play = False, loops = 0, volume = 1.0):
        if not song: return
        return self.__addSound(song, effects[song], auto_play, loops, volume)

mixer = Mixer()

backgrounds = {
    "Brasil": "background/brazil.m4a",
    "França": "background/france.mp3",
    "China": "background/china.mp3",
    "Austrália": "background/australia.mp3",
    "África do Sul": "background/south_africa.mp3",

    "menu": "background/menu.mp3"
}

effects = {
    "started": "specials/match_started.ogg",
    "notallowed": "specials/not_allowed.ogg",
    "revealed": "specials/revealed_word.ogg",
    "typing": "specials/typing.ogg",
    "winner": "specials/winner.ogg"
}