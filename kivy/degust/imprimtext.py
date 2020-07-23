from kivy.app import App
from kivy.uix.label import Label

def build():
    '''return Label(text ="CUrso de python e kivy", italic =True, font_size = 30)
'''
    lb = Label ()
    lb.text = "CUUUUUU"
    lb.font_size = 30
    lb.italic = True
    return lb
app = App()
app.build = build
app.run()