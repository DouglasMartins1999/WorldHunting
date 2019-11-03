from pygame import *

class Action:
    def __init__(self, rect, handler):
        self.rect = rect
        self.handler = handler

class Listener:
    def __init__(self):
        self.actions = []

    def addListener(self, action):
        self.actions.append(action)
        return self

    def removeListener(self, action):
        self.actions = list(filter(lambda listener: listener != action, self.actions))
        return self

    def replaceListener(self, old_action, new_action):
        self.removeListener(old_action)
        self.addListener(new_action)
        print("Add aqui")
        return self

    def clearListeners(self):
        actions = self.actions
        self.actions = []
        return actions

    def callListeners(self, evt = (0, 0)):
        for action in self.actions:
            if(action.rect.collidepoint(evt)):
                action.handler(action)

class KeyHandler:
    def __init__(self):
        self.possible_keys = {
            K_SPACE: " ",
            K_0: "0",
            K_1: "1",
            K_2: "2",
            K_3: "3",
            K_4: "4",
            K_5: "5",
            K_6: "6",
            K_7: "7",
            K_8: "8",
            K_9: "9",
            K_a: "A",
            K_b: "B",
            K_c: "C",
            K_d: "D",
            K_e: "E",
            K_f: "F",
            K_g: "G",
            K_h: "H",
            K_i: "I",
            K_j: "J",
            K_k: "K",
            K_l: "L",
            K_m: "M",
            K_n: "N",
            K_o: "O",
            K_p: "P",
            K_q: "Q",
            K_r: "R",
            K_s: "S",
            K_t: "T",
            K_u: "U",
            K_v: "V",
            K_w: "W",
            K_x: "X",
            K_y: "Y",
            K_z: "Z",
        }
        self.letterSequence = []

    def checkLetter(self, event):
        letter = None

        try:
            letter = self.possible_keys[event]
        except KeyError:
            letter = None

        return letter

    def printLetters(self, event):
        letter = self.checkLetter(event)

        if letter != None:
            self.letterSequence.append(letter)

        if (event == K_BACKSPACE):
            try:
                self.letterSequence.pop()
            except:
                print()

        print(self.letterSequence)

    def setLetterSequence(self, sequence):
        print("Changing", self.letterSequence, sequence)
        self.letterSequence = sequence


events = Listener()
keyboard = KeyHandler()