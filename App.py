from ast import main
from tkinter.tix import MAIN
import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    
    def build(self):
        return Label(text='Hello')

if __name__ == '__main__':
    MyApp().run()