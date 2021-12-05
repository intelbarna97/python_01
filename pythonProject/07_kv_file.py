from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


class MainWindow(FloatLayout):
    pass

class TesztApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

teszt_app=TesztApp()
teszt_app.run()