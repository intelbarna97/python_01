from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("kv-files/slider-demo.kv")
class MainWindow(FloatLayout):
    pass

class SliderDemoApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

teszt_app=SliderDemoApp()
teszt_app.run()