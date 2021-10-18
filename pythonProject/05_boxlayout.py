from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MainWindow(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation="horizontal"
        self.padding=20
        self.spacing=50

        btn1= Button(
            text="Hello",
           #size = (200,100), 1.szélesség, 2.magasság
            #width=200,
            #height=300,
            size_hint=(None, None), #default size_hint=(1, 1)
            pos_hint={"y":0.5}
        )
        btn2=Button(
            text="Kivy",
            size_hint=(.5,1)
        )
        btn3 = Button(
            text="World",
            size_hint=(.5, 1)
        )
        self.add_widget(btn1)
        self.add_widget(btn2)
        self.add_widget(btn3)


class TestApp(App):
    def build(self):
        return MainWindow()

TestApp().run()