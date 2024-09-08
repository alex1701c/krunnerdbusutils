from typing import List


class Match:
    """
    Object resembling a KRunner match. This must have an id and text.
    By default, all actions provided by the Actions method are associated with the given match
    """
    __slots__ = ["id", "text", "icon", "relevance", "type",
                 "subtext", "category", "actions", "urls", "multiline"]

    def __init__(self, *,
                 id: str = '',
                 text: str = '',
                 icon: str = '',
                 relevance: int = 0,
                 type: int = 100,
                 subtext: str = '',
                 category: str = '',
                 actions: List[str] = None,
                 urls: List[str] = None,
                 multiline: bool = None,
                 ):
        self.id = id
        self.text = text
        self.icon = icon
        self.relevance = relevance
        self.type = type
        self.subtext = subtext
        self.category = category
        self.actions = actions
        self.urls = urls
        self.multiline = multiline
