"""
utility library for KRunner
"""

__version__ = "1.0.0"

import dbus
from dbus.service import BusName
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
from typing import Type
from .Match import Match
from .Action import Action
from .Annotations import krunner_actions, krunner_match, krunner_run


class AbstractRunner(dbus.service.Object):
    """
    Abstract class to be registered for KRunner DBus API. The subclass should utilize the
    krunner_actions, krunner_match and krunner_run method annotations
    """

    def __init__(self, servicename, objpath):
        """
        the servicename should correspond to the X-Plasma-DBusRunner-Service value
        objpath should be the same as the X-Plasma-DBusRunner-Path metadata value
        """
        busname = BusName(servicename, dbus.SessionBus(), do_not_queue=True)
        dbus.service.Object.__init__(self, busname, objpath)


def run_event_loop(runner_class: Type):
    """
    Instantiates the given class and runs a main event loop
    This is just an utility and can be done manually
    """
    DBusGMainLoop(set_as_default=True)
    runner_class()
    loop = GLib.MainLoop()
    loop.run()
