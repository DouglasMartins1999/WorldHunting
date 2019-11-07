from random import shuffle, randrange

class Crossword:
    def __init__(self, country, level = 1):
        self.country = country
        self.level = level
        self.wordrange = self.getWords()
        self.words = self.breakIntoLetters()
        self.structure = self.generateStructure()

    def getWords(self):
        level = self.level
        words = []

        if (level == 1):
            words = self.country["categories"]["easy"].copy()

        elif (level == 2):
            easy = self.country["categories"]["easy"].copy()
            medium = self.country["categories"]["medium"].copy()

            shuffle(easy)
            shuffle(medium)

            easy_limit_index = round(len(easy) * 0.6)
            medium_limit_index = round(len(medium) * 0.4)

            words = easy[:easy_limit_index] + medium[:medium_limit_index]

        elif (level == 3):
            words = self.country["categories"]["medium"].copy()

        elif (level == 4):
            medium = self.country["categories"]["medium"].copy()
            hard = self.country["categories"]["hard"].copy()

            shuffle(medium)
            shuffle(hard)

            medium_limit_index = round(len(medium) * 0.6)
            hard_limit_index = round(len(hard) * 0.4)

            words = medium[:medium_limit_index] + hard[:hard_limit_index]

        elif (level == 5):
            words = self.country["categories"]["hard"].copy()

        else:
            words = []

        return sorted(words, key=lambda word: len(word[0]), reverse=True)

    def breakIntoLetters(self):
        words = self.wordrange
        words = list(map(lambda word: [list(map(lambda letter: CrosswordLetter(letter, False), word[0])), word[1]] , words))
        return words

    def generateStructure(self):
        words = self.words.copy()
        sequence = []
        last = None
        shuffle(words)

        try:
            word = words.pop(0)
            sequence.append(CrosswordWord(word[0], True, 0, 0, word[1]))

            while len(words) and last != words[0] and len(sequence) < (self.level * 3):
                last = word = words.pop(0)
                crossed = self.__getCrossed(word, sequence)

                if crossed != None:
                    sequence.append(crossed)
                else:
                    words.append(word)

            addX = min(sequence, key = lambda word: word.posX).posX * -1
            addY = min(sequence, key = lambda word: word.posY).posY * -1

            for seq in sequence:
                seq.posX += addX
                seq.posY += addY

        except IndexError:
            return

        return sequence

    def __getCrossed(self, word, sequence):
        for mainword in sequence:
            for iM, lM in enumerate(mainword.word):
                for iW, lW in enumerate(word[0]):
                    # Possivel união
                    if lM.letter == lW.letter and not lM.isFilled and not lW.isFilled:
                        direction = not mainword.isVertical
                        posX = 0
                        posY = 0

                        if mainword.isVertical:
                            posX = mainword.posX - iW
                            posY = mainword.posY + iM
                        else:
                            posX = mainword.posX + iM
                            posY = mainword.posY - iW

                        if ((posX + len(word)) > 16 or (posY + len(word)) > 15):
                            break

                        lW.isFilled = True
                        lM.isFilled = True
                        
                        return CrosswordWord(word[0], direction, posX, posY, word[1])

        return None

    def getSize(self, block_size = 32):
        vertical = list(filter(lambda word: word.isVertical, self.structure))
        horizontal = list(filter(lambda word: (not word.isVertical), self.structure))

        max_width = max(horizontal, key=lambda word: word.posX + len(word.word))
        max_height = max(vertical, key=lambda word: word.posY + len(word.word))

        width = (max_width.posX + len(max_width.word)) * block_size
        height = (max_height.posY + len(max_height.word)) * block_size

        return (width, height)
                        

class CrosswordLetter:
    def __init__(self, letter = "A", isFilled = False):
        self.letter = letter.upper()
        self.isFilled = isFilled

    def toogleFill(self):
        self.isFilled = not self.isFilled
        return self


class CrosswordWord:
    def __init__(self, word = [CrosswordLetter()], isVertical = True, posX = 0, posY = 0, hint = ""):
        self.word = word
        self.isVertical = isVertical
        self.posX = posX
        self.posY = posY
        self.hint = hint

    def toWord(self):
        letters = list(map(lambda l: l.letter, self.word))
        word = "".join(letters)
        return word

    def addPosX(self, pos = 0):
        self.posX += pos
        return self

    def addPosY(self, pos = 0):
        self.posY += pos
        return self