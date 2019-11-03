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

        self.staticElements()
        self.setBaseRevealedArray()
        self.renderRevealedWords()
        self.renderHint("5. A queda da _______ em 1789 foi fator deterministico para o início da revolução francesa")
        self.renderCrossword()

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
        self.addButton(icons["hint"]["prev"][self.session.level], (477, 500), (27, 27), None, self.base_screen)
        self.addButton(icons["hint"]["next"][self.session.level], (937, 500), (27, 27), None, self.base_screen)

        self.mounted_screen = self.base_screen.copy()

    def renderHint(self, hint):
        hint_text = text(hint, "asap/bold.ttf", 16, "#FFFFFF", (392, 64))
        self.mounted_screen.blit(hint_text, (528, 507))

    def setBaseRevealedArray(self):
        crossword = self.session.crossword.structure

        for word in crossword:
            self.revealed_words.append([])

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

        for n, word in enumerate(crossword.structure):
            for i, letter in enumerate(word.word):
                def textHander():
                    l = n
                    return lambda act: keyboard.setLetterSequence(self.revealed_words[l])

                adiction = (i * box_rect[1])
                posX = word.posX * box_rect[0] + 444 + (crossword_area_size[0] - crossword_size[0]) / 2
                posY = word.posY * box_rect[1] + 51 + (crossword_area_size[1] - crossword_size[1]) / 2

                if(word.isVertical):
                    posY += adiction
                else:
                    posX += adiction

                try:
                    assigned_letter = self.revealed_words[n][i]
                except:
                    assigned_letter = ""

                letter_label = text(assigned_letter, "mclaren/regular.ttf", 20, self.color, (30, 30))

                # print(n, self.revealed_words[n])
                self.addButton(box, (posX, posY), (32, 32), textHander(), self.mounted_screen)
                self.mounted_screen.blit(letter_label, (posX + 8, posY))

    def render(self):
        self.renderCrossword()
        return super().render()
