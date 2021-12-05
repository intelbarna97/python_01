from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("kv-files/spinner-demo.kv")
class MainWindow(FloatLayout):
    values_list = ["Home", "Work", "Other", "Custom"]

class SpinnerDemoApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

teszt_app=SpinnerDemoApp()
teszt_app.run()