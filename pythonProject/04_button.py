from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainWindow(Widget):
    def __init__(self):
        super().__init__()
        self.button = Button(
            text = "Button1",
            pos=(100,100)
        )
        self.add_widget(self.button)

class TestApp(App):
    def build(self):
        return MainWindow()

TestApp().run()