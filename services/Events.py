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

events = Listener()