from kivy.app import App
from kivy.uix.widget import Widget


class TestApp(App):
    def build(self):
        return Widget()

test_app = TestApp()
test_app.run()