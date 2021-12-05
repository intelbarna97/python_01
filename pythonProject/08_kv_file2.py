from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

kv_string="""
<MainWindow>:
    Button:
        text:"Button 1 string"
        size_hint:0.3,0.3
        pos_hint:{"top":1, "right":1}
    Button:
        text:"Button 2 string"
        size_hint:0.5,0.5
        pos_hint:{"x":0.2,"y":0.2}

"""
#Builder.load_string(kv_string)
Builder.load_file("kv-files/simple-app.kv")
class MainWindow(FloatLayout):
    pass

class TesztApp(App):
    def build(self):
        main_window = MainWindow()
        return main_window

teszt_app=TesztApp()
teszt_app.run()