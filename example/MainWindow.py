#!/usr/bin/env python3

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

try:
    import locale
    from locale import gettext as _

    # Translation Constants:
    APPNAME = "example"
    TRANSLATIONS_PATH = "/usr/share/locale"
    locale.bindtextdomain(APPNAME, TRANSLATIONS_PATH)
    locale.textdomain(APPNAME)
except:
    # locale load fallback
    def _(msg):
        return msg


class MainWindow:
    def __init__(self, application):
        self.builder = Gtk.Builder()

        # Import UI file:
        glade_file = (
            os.path.dirname(os.path.abspath(__file__)) + "/ui/MainWindow.ui"
        )

        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        self.ui_window_main.set_application(application)

        # show main window
        self.ui_window_main.show()

        # do some stuff
        print(_("Hello World"))

    def __getattr__(self, name):
        # return object if exists
        if self.builder.get_object(name):
            return self.builder.get_object(name)
