#!/usr/bin/python3

import gi
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk

gi.require_version('Adap', '1')
from gi.repository import Adap as Adw
from find_icons import find_xsi_icons

# Application ID and variables
app_id = "xyz.agatinos.xsi-icon-browser"
icon_dir = "/usr/share/icons"
search_pattern = "xsi-*"

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

        scroll_control = Gtk.ScrolledWindow()
        scroll_control.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        scroll_control.set_vexpand(True)
        
        content_listbox = Gtk.ListBox()
        content_listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        content_listbox.add_css_class("boxed-list")
        content_listbox.set_margin_top(16)
        content_listbox.set_margin_bottom(16)
        content_listbox.set_margin_start(16)
        content_listbox.set_margin_end(16)

        icon_data = find_xsi_icons(icon_dir, search_pattern, False)

        for item in icon_data:
            item_row = Adw.ActionRow()
            item_row.set_title(item["FileName"])
            item_row.set_subtitle(item["FilePath"])

            item_image = Gtk.Image.new_from_icon_name(item["IconName"])
            item_image.set_pixel_size(64)

            item_row.add_prefix(item_image)
            #item_row.add_suffix(item_image)

            content_listbox.append(item_row)

        scroll_control.set_child(content_listbox)

        # Add widgets to main container
        self.main_content_box.append(app_headerbar)
        self.main_content_box.append(scroll_control)


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
