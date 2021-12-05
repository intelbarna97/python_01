from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


Builder.load_file("kv-files/if-else-demo.kv")
class MainWindow(FloatLayout):
    def kiir(self):
        print("This giraffe is tall!")

class CheckDemoApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

teszt_app=CheckDemoApp()
teszt_app.run()