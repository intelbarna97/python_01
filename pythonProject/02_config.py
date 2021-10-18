import os

os.environ["KIVY_NO_CONSOLELOG"] = "1"
cwd = os.getcwd()
os.environ["KIVY_HOME"] = cwd + "/conf"

from kivy import Config
from kivy.app import App
from kivy.uix.widget import Widget

Config.set("graphics", "width", "800")
Config.set("graphics", "height", "600")
Config.set("graphics", "resizable", "0")
Config.set("graphics", "borderless", "0")
Config.write()


class TestApp(App):
    def build(self):
        return Widget()


test_app = TestApp()
test_app.run()
