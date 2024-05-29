#!/usr/bin/env python3

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from MainWindow import MainWindow

class ExampleApplication(Gtk.Application):

    def __init__(self):
        super().__init__(application_id="com.example.application")
        self.connect('activate', self.on_activate)
        self.main_window = None

    def on_activate(self, app):
        if not self.main_window:
            self.main_window = MainWindow()
            self.main_window.set_application(self)
            self.main_window.present()


if __name__ == '__main__':
    app = ExampleApplication()
    app.run(None)

