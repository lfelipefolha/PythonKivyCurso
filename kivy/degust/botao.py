from kivy.app import App
from kivy.uix.button import Button

def Click():
    print("Foi clicado")
def build():
    bt = Button(text ="Clique")
    bt.on_press =Click
    return bt
janela =App()
janela.build =build
janela.run()