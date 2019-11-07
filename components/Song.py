import pygame
from settings.environment import default
 
class Effect:
    def __init__(self, sound):
        self.sound = sound

    def play(self):
        self.sound.play()
        return self

    def stop(self, fade = 0):
        self.fadeout(fade)
        return self

    @property
    def volume(self):
        return self.sound.get_volume()

    @volume.setter
    def volume(self, volume):
        return self.sound.set_volume(volume)

    def setVolume(self, volume):
        self.sound.set_volume(volume)
        return self

class Music:
    def __init__(self, mixer):
        self.mixer = mixer

    def stop(self, time = 0):
        pygame.mixer.music.fadeout(time)
        return self

    def pause(self):
        pygame.mixer.music.pause()
        return self

    def resume(self):
        pygame.mixer.music.unpause()
        return self

    @property
    def volume(self):
        return pygame.mixer.music.get_volume()

    @volume.setter
    def volume(self, volume):
        return pygame.mixer.music.set_volume(volume)

    def setVolume(self, volume = 1):
        pygame.mixer.music.set_volume(volume)
        return self

class Mixer:
    def __init__(self):
        pygame.mixer.init()
        self.music = Music(self)
    
    def stop(self, time = 0):
        pygame.mixer.fadeout(time)
        return self

    def pause(self):
        pygame.mixer.pause()
        return self

    def resume(self):
        pygame.mixer.unpause()
        return self

    def addBackground(self, title, auto_play = True):
        pygame.mixer.music.load(default.song_root + backgrounds[title])
        
        if auto_play: 
            pygame.mixer.music.play()
        
        return self
    
    def addEffect(self, title, auto_play = True):
        song = pygame.mixer.Sound(default.song_root + effects[title])
        
        if auto_play: 
            song.play()

        return Effect(song)

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