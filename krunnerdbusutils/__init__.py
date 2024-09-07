"""
utility library for KRunner
"""

__version__ = "1.0.0"

import dbus
from dbus.service import BusName
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from .Match import Match
from .Action import Action
from .Annotations import krunner_actions, krunner_match, krunner_run


class AbstractRunner(dbus.service.Object):
    def __init__(self, busname, objpath):
        busname = BusName(busname, dbus.SessionBus(), do_not_queue=True)
        dbus.service.Object.__init__(self, busname, objpath)


def run_event_loop():
    DBusGMainLoop(set_as_default=True)
    loop = GLib.MainLoop()
    loop.run()
