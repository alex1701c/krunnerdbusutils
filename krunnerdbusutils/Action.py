class Action:
    """
    Object resembling a KRunner action. This must have an id and text.
    Actions are associated with matches based on their id.
    """
    __slots__ = ["id", "text", "icon"]

    def __init__(self, *, id: str = '', text: str = '', icon: str = ''):
        self.id = id
        self.text = text
        self.icon = icon
