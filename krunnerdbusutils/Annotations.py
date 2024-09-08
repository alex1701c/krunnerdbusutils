import dbus
import dbus.service
from functools import wraps
from .Match import Match
from .Action import Action

iface = "org.kde.krunner1"


def match_to_tuple(match: Match) -> ():
    properties = {}
    if match.subtext:
        properties['subtext'] = match.subtext
    if match.category:
        properties['category'] = match.category
    return match.id, match.text, match.icon, match.type, match.relevance, properties


def action_to_tuple(action: Action) -> ():
    return action.id, action.text, action.icon


def krunner_match(method):
    assert method.__name__ == "Match", "Method for DBus-API must be called Match" + \
        str(method)

    @dbus.service.method(iface, in_signature="s", out_signature="a(sssida{sv})")
    @wraps(method)
    def wrapper_function(*args, **kwargs):
        matches = method(*args, **kwargs)
        assert all(isinstance(match, Match)
                   for match in matches), "All items in the list must be Match objects"

        for match in matches:
            if not match.id:
                raise ValueError("Match id cannot be empty or unset")

        return [match_to_tuple(match) for match in matches]
    return wrapper_function


def krunner_actions(method):
    assert method.__name__ == "Actions", "Method for DBus-API must be called Actions" + \
        str(method)

    @dbus.service.method(iface, out_signature="a(sss)")
    @wraps(method)
    def wrapper_function(*args, **kwargs):
        actions = method(*args, **kwargs)
        assert all(isinstance(action, Action)
                   for action in actions), "All items in the list must be Action objects"
        for action in actions:
            if not action.id:
                raise ValueError("Action id cannot be empty or unset")
        return [action_to_tuple(action) for action in actions]
    return wrapper_function


def krunner_run(method):
    assert method.__name__ == "Run", "Method for DBus-API must be called Run" + \
        str(method)

    @dbus.service.method(iface, in_signature="ss")
    @wraps(method)
    def wrapper_function(*args, **kwargs):
        method(*args, **kwargs)
    return wrapper_function
