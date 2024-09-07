class Action:
    def __init__(self, *, id: str = '', text: str = '', icon: str = ''):
        self.id = id
        self.text = text
        self.icon = icon

    def to_tuple(self) -> ():
        return self.id, self.text, self.icon
