#!/usr/bin/python3

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

gi.require_version('Adap', '1')
from gi.repository import Adap as Adw

# Application ID
app_id = "xyz.agatinos.xsi-icon-browser"

class MainWindow(Adw.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window general information and optional icon
        self.set_title("XSI Icon Browser")
        self.set_default_size(800, 620)
        self.set_icon_name("xsi-apps-symbolic")

        # Main container for the controls required
        self.main_content_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=12)
        self.set_content(self.main_content_box)

        # Create HeaderBar along with the required title
        app_headerbar = Adw.HeaderBar()
        app_headerbar.set_show_title(True)

        # Add widgets to main container
        self.main_content_box.append(app_headerbar)


class MyApp(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()

def main():
    app = MyApp(application_id=app_id)
    app.run(None)

if __name__ == "__main__":
    main()
