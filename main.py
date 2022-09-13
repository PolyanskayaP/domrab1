from random import randint
from re import L
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
#если работаем более, чем с одним объектом, то надо помещать внутрь слоя:
from kivy.uix.boxlayout import BoxLayout 

from kivy.core.window import Window

Window.size = (350, 300)  
Window.clearcolor = (3/255, 186/255, 255/255, 1) 
#Window.title = "DR1"

class MyApp(App):
    def __init__(self):
        super().__init__() 
        self.cifr = Label(text='')
        self.input_data = TextInput(hint_text='Введите число буквами', multiline=True)
    #    self.input_data.bind(text=self.on_text)


    def btn_pressed(self, *args):    
        data = self.input_data.text
        #алгоритм с data
        self.algor(data)
        

    def algor(self, data):    #data это словами число
        print(data)

        self.cifr.text = str(data)  #вывод должно быть измененной data


    def build(self):
        box = BoxLayout(orientation='vertical') 
        box.add_widget(self.input_data)  #словами
        box.add_widget(self.cifr)       #цифрами 
        btn = Button(text='перевести') 
        btn.bind(on_press=self.btn_pressed)       
        box.add_widget(btn)

        return box 

if __name__ == "__main__":
    MyApp().run()  