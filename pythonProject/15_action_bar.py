from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_file("kv-files/action-bar-demo.kv")

class MainWindow(FloatLayout):
    pass

class TestApp(App):
    def build(self):
        return MainWindow()

TestApp().run()