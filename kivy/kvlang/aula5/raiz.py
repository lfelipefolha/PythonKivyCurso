import kivy
from kivy.app import App
from kivy.uix.boxlayout import  BoxLayout
from kivy.uix.button import Button

def funcSelf(x):
    print("funcself")
Button.funcSelf = funcSelf

class MinhaTela(BoxLayout):

    def funcRoot(self):
        print("funcroot")


class Estudo5App(App):
    def funcApp(self):
        print("funcapp")

janela = Estudo5App()
janela.run()