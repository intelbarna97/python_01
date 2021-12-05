from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

Builder.load_file("kv-files/screen-demo.kv")

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    def kiir(self):
        print("I am from the python file!")

class Manager(ScreenManager):
    pass

class TestApp(App):
    def build(self):
        self.title="vad"
        return Manager()

TestApp().run()