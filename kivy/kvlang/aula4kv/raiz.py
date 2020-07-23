import kivy
from kivy.app import App
from kivy.uix.boxlayout import  BoxLayout

class MinhaTela(BoxLayout):

    def click(self):
        print("oi")
        self.ids.lb1.text= "hey"
        self.ids.lb2.text = "oi"

class Estudo4App(App):
    pass

janela = Estudo4App()
janela.run()