from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget


class MainWindow(FloatLayout):
    def __init__(self):
        super().__init__()

        self.btn1= Button(
            text="Hello",
           size = (200,100), #1.szélesség, 2.magasság
            #width=200,
            #height=300,
            size_hint=(None, None), #default size_hint=(1, 1)
            pos_hint={"center_y":0.5}
        )
        self.btn1.bind(on_press=self.push)

        self.btn2=Button(
            text="Center",
            size_hint=(.2,.4),
            pos_hint={"center" : (0.5, 0.5)} #center_x center_y
        )
        self.btn2.bind(on_press=App.get_running_app().stop)

        self.btn3 = Button(
            text="Top/Right",
            size_hint=(.2, 0.4),
            pos_hint = {"top": 0.5, "right": 0.5}
        )
        self.btn3.bind(state=self.callback)
        self.btn4 = Button(
            text="x, y",
            size_hint=(.2, 0.4),
            pos_hint={"x": 0.5, "y": 0.5}
        )
        self.add_widget(self.btn1)
        self.add_widget(self.btn2)
        self.add_widget(self.btn3)
        self.add_widget(self.btn4)
    def push(self,instance): #instance a példányneve lesz
        print("Megnyomtad gombot")
    def callback(self, instance, value):
        print("My button <%s> state is <%s>" % (instance, value))


class TestApp(App):
    def build(self):
        return MainWindow()

TestApp().run()