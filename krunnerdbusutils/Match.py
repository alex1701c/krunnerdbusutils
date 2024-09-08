class Match:
    """
    Object resembling a KRunner match. This must have an id and text
    """
    __slots__ = ["id", "text", "icon",
                 "relevance", "type", "subtext", "category"]

    def __init__(self, *,
                 id: str = '',
                 text: str = '',
                 icon: str = '',
                 relevance: int = 0,
                 type: int = 100,
                 subtext: str = '',
                 category: str = ''):
        self.id = id
        self.text = text
        self.icon = icon
        self.relevance = relevance
        self.type = type
        self.subtext = subtext
        self.category = category
