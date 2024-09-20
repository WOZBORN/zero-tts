class Player:
    def __init__(self, name, voice):
        self.name = name
        self.voice = voice

    def __str__(self):
        return self.name