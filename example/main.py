#!/usr/bin/python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gio, Gtk

from MainWindow import MainWindow

class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id="org.example.application",
                         flags=Gio.ApplicationFlags.FLAGS_NONE, **kwargs
        )
        self.window = None
        GLib.set_prgname("org.example.application")

    def do_activate(self):
        if not self.window:
            self.window = MainWindow(self)
        else:
            self.window.present()


app = Application()
app.run(sys.argv)
