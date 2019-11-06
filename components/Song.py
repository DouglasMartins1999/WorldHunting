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

    def addBackground(self, title, auto_play = False, loops = 0, volume = 1.0):
        pygame.mixer.music.load(default.song_root + backgrounds[title])
        pygame.mixer.music.set_volume(volume)
        
        if auto_play: 
            pygame.mixer.music.play(loops = loops)
        
        return self
    
    def addEffect(self, title, auto_play = False, loops = 0, volume = 1.0):
        song = pygame.mixer.Sound(default.song_root + backgrounds[title])
        song.set_volume(volume)
        
        if auto_play: 
            song.play(loops = loops)

        self.songs[title] = song
        return song

mixer = Mixer()

backgrounds = {
    "Brasil": "background/brazil.ogg",
    "França": "background/france.ogg",
    "China": "background/china.ogg",
    "Austrália": "background/australia.ogg",
    "África do Sul": "background/south_africa.ogg",

    "menu": "background/menu.ogg"
}

effects = {
    "started": "specials/match_started.ogg",
    "notallowed": "specials/not_allowed.ogg",
    "revealed": "specials/revealed_word.ogg",
    "typing": "specials/typing.ogg",
    "winner": "specials/winner.ogg"
}