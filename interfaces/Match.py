from interfaces.BaseScreen import BaseScreen
from components.Images import backgrounds, icons
from components.Fonts import text
from components.Color import level_colors
from services.Session import LevelSession
from services.Events import keyboard
from settings.environment import level_names

class Match(BaseScreen):
    def __init__(self, level_session):
        super().__init__(backgrounds[level_session.country["name"]])
        self.session = level_session
        self.color = level_colors[self.session.level]
        self.revealed_words = []
        self.hint = 0

        self.staticElements()
        self.setBaseRevealedArray()
        self.renderRevealedWords()

    def staticElements(self):
        level = text("Nível {}: ".format(self.session.level), "asap/bold.ttf", 16, self.color, (60, 25))
        level_name = text(level_names[self.session.level], "asap/regular.ttf", 16, "#000000", (120, 25))

        self.base_screen.blit(level, (74, 45))
        self.base_screen.blit(level_name, (133, 45))
        self.base_screen.blit(icons["hints_label"], (528, 477))

        # Action Buttons
        self.addButton(icons["cancel"], (74, 508), (36, 36), None, self.base_screen)
        self.addButton(icons["disable_sound"], (114, 508), (36, 36), None, self.base_screen)
        self.addButton(icons["reveal_letter"], (155, 508), (36, 36), None, self.base_screen)

        # Hint Buttons
        self.addButton(icons["hint"]["prev"][self.session.level], (477, 500), (27, 27), self.removeFromHint, self.base_screen)
        self.addButton(icons["hint"]["next"][self.session.level], (937, 500), (27, 27), self.addToHint, self.base_screen)

        self.mounted_screen = self.base_screen.copy()

    def renderHint(self):
        hint = self.hint
        hint_text = str(hint + 1) + ". " + self.session.crossword.structure[hint].hint
        hint_label = text(hint_text, "asap/bold.ttf", 16, "#FFFFFF", (392, 64))

        self.mounted_screen = self.base_screen.copy()
        self.mounted_screen.blit(hint_label, (528, 507))

    def renderRevealedWords(self):
        posX = (100, 235)
        posY = 100

        for i, word in enumerate(self.revealed_words):
            word_label = text("".join(word).capitalize(), "asap/regular.ttf", 16, "#FFFFFF", (125, 25))
            self.mounted_screen.blit(word_label, (posX[i % 2], posY))
            if (i % 2 == 1): 
                posY += 30

    def renderCrossword(self):
        crossword = self.session.crossword
        box = icons["letter_box"]
        box_rect = (30, 30)
        crossword_area_size = (544, 416)
        crossword_size = crossword.getSize()

        def textHander():
            word = self.revealed_words[n]
            max_letters = len(crossword.structure[n].word)
            return lambda act: keyboard.setLetterSequence(word, max_letters)

        for n, word in enumerate(crossword.structure):
            for i, letter in enumerate(word.word):
                assigned_letter = self.revealed_words[n][i] if len(self.revealed_words[n]) > i else ""
                posX = word.posX * box_rect[0] + 444 + (crossword_area_size[0] - crossword_size[0]) / 2
                posY = word.posY * box_rect[1] + 51 + (crossword_area_size[1] - crossword_size[1]) / 2
                adiction = (i * box_rect[1])

                if word.isVertical:
                    posY += adiction
                else:
                    posX += adiction

                letter_label = text(assigned_letter, "mclaren/regular.ttf", 20, self.color, (30, 30))

                self.addButton(box, (posX, posY), box_rect, textHander(), self.mounted_screen)
                self.mounted_screen.blit(letter_label, (posX + 8, posY))

    def render(self):
        self.renderHint()
        self.renderCrossword()
        return super().render()




    def setBaseRevealedArray(self):
        crossword = self.session.crossword.structure

        for word in crossword:
            self.revealed_words.append([])

    def addToHint(self, act):
        if self.hint < (len(self.session.crossword.structure) - 1):
            self.hint += 1

    def removeFromHint(self, act):
        if self.hint > 0:
            self.hint -= 1
