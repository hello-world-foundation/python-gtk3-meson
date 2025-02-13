#!/usr/bin/env python3

import gi
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MainWindow:
    def __init__(self, application):
        self.builder = Gtk.Builder()

        # Import UI file:
        glade_file = (
            os.path.dirname(os.path.abspath(__file__)) + "/ui/MainWindow.ui"
        )

        self.builder.add_from_file(glade_file)
        self.builder.connect_signals(self)

        # define components
        self.window = self.builder.get_object("ui_window_main")

        self.window.set_application(application)

        # show main window
        self.window.show()