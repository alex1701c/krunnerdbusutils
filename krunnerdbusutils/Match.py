from typing import List


class Match:
    """
    Object resembling a KRunner match. This must have an id and text.
    Attributes:
        id: ID of this match. The "Run" method of the DBus interface should use this to determine the action that should be triggered
        text: Primary text describing the action
        icon: icon name for this match
        type: Used for comparing categories
        relevance: double number to indicate the relevance of the match. This should be between 0 and 100. This is primarely used to compare matches of the same category.
        subtext: Text providing additonal context
        category: Category used for grouping matches. By default, the plugin's name is used
        actions: IDs of actions that are associated with the match. If unset, all actions are used
        urls: URLs associated with this match. Useful for drag/drop
        multiline: Boolean, if this match has a multiline text. This also allows the text to use Qt's styles text
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
