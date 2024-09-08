class Action:
    """
    Object resembling a KRunner match. This must have an id and text
    """
    __slots__ = ["id", "text", "icon"]

    def __init__(self, *, id: str = '', text: str = '', icon: str = ''):
        self.id = id
        self.text = text
        self.icon = icon
