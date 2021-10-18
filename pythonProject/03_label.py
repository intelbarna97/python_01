from kivy.app import App
from kivy.uix.label import Label


class TestApp(App):
    def build(self):
        return Label(
            #text = "Hello World",
            font_size = 60,
            italic = True,
            bold = True,
            underline = True,
            color = (1, 0.5, 0), #RGB #RGBA(1, 0.5, 1, 0)
            font_name = "fonts/Amsterdam_Laviera.ttf",
            text = "[color=ff0000]Hello[/color][color=ffffff]____[/color][color=00ff00]World[/color]",
            markup = True
        )


test_app = TestApp()
test_app.run()
