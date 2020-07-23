from kivy. app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
class Meuprogram(App):
    def click(self):
        print(ed.text)

    def build(self):
        layout = FloatLayout()
        global ed
        ed = TextInput(text="Digite o texto")

        ed.size_hint = None, None
        ed.height = 200
        ed.width = 200
        ed.x = 100
        ed.y = 250

        bt = Button(text = ed.text)
        bt.size_hint = None, None
        bt.width = 100
        bt.height = 60
        bt.y = 150
        bt.x = 150

        bt.on_press = self.click

        layout.add_widget(ed)
        layout.add_widget(bt)
        return layout


    from kivy.core.window import Window
    Window.size = 400, 600
Meuprogram().run()