from random import randint
from re import L
from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button 
#если работаем более, чем с одним объектом, то надо помещать внутрь слоя:
from kivy.uix.boxlayout import BoxLayout 

from kivy.core.window import Window

Window.size = (600, 400)  
Window.clearcolor = (3/255, 186/255, 255/255, 1) 
#Window.title = "DR1"

class MyApp(App):
    def __init__(self):
        super().__init__() 
        self.cifr = Label(text='')
        self.input_data = TextInput(hint_text='Введите число буквами', multiline=True)

    def btn_pressed(self, *args):    
        data = self.input_data.text
        #алгоритм с data
        self.algor(data)
        

    def algor(self, data):    #data это словами число
        sot_ar = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
        des_ar = {  2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
        ed_ar =  {  1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

        onl_ar = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

        data = " ".join(data.split())
        slova = data.split(' ', 2) 
        skolko = len(slova)
        if (skolko == 2):
            slova.append('')
        if (skolko == 1):
            slova.append('')
            slova.append('')
        if (skolko == 0):
            slova.append('')
            slova.append('')
            slova.append('')
        skolko = len(slova)

        osh = []
        if (slova[0]=='') and (slova[1]=='') and (slova[2]==''):
            osh.append('вы ничего не написали :(')
        else:
            if (slova[0] not in des_ar.values() and slova[0] not in onl_ar.values() and slova[0] not in ed_ar.values() and slova[0] not in sot_ar.values()):
                osh.append('первое слово написано неправильно')
            elif (slova[0] in ed_ar.values()):
                osh.append('первое слово не должно быть единицами')
            elif (slova[0] in des_ar.values()):
                osh.append('первое слово не должно быть десятками')
            elif (slova[0] in onl_ar.values()):
                osh.append('первое слово не должно быть формата 10-19')

            if (slova[1] not in des_ar.values() and slova[1] not in onl_ar.values() and slova[1] not in ed_ar.values() and slova[1] not in sot_ar.values() and slova[1]!=''):
                osh.append('второе слово написано неправильно')
            elif (slova[1] in sot_ar.values()):
                osh.append('второе слово не должно быть сотней')

            if (slova[2] not in ed_ar.values() and slova[2] not in des_ar.values() and slova[2] not in onl_ar.values() and slova[2] not in sot_ar.values() and slova[2]!=''):
                osh.append('третье слово написано неправильно')
            elif (slova[2] in sot_ar.values()):
                osh.append('третье слово не должно быть сотней')
           
            if (slova[1] in ed_ar.values()) and (slova[2] in ed_ar.values()):
                osh.append('нельзя два слова единичного формата')
            elif (slova[1] in des_ar.values()) and (slova[2] in des_ar.values()):
                osh.append('нельзя два слова десятичного формата')
            elif (slova[1] in onl_ar.values()) and (slova[2] in onl_ar.values()):
                osh.append('нельзя два слова формата 10-19')
            elif (slova[1] in des_ar.values()) and (slova[2] in onl_ar.values()):
                osh.append('нельзя сначала писать десятки, потом число формата 10-19')
            elif (slova[1] in ed_ar.values()) and (slova[2] in des_ar.values()):
                osh.append('нельзя сначала писать слово единичного формата, потом десятки')
            elif (slova[1] in ed_ar.values()) and (slova[2] in onl_ar.values()):
                osh.append('нельзя сначала писать слово единичного формата, потом слово формата 10-19')
            elif (slova[1] in ed_ar.values()) and (slova[2] in sot_ar.values()):
                osh.append('нельзя сначала писать слово единичного формата, потом сотни')
            elif (slova[1] in onl_ar.values()) and not(slova[2] == ''):
                osh.append('нельзя после слова форматом 10-19 писать еще слово')          
            elif (slova[1] in ed_ar.values()) and not(slova[2] == ''):
                osh.append('нельзя после слова единичного формата писать еще слово')                      

        if osh:
            self.cifr.text = ";\n".join(osh) 
        else:
            rev_sot = {v:k for k, v in sot_ar.items()}
            rev_des = {v:k for k, v in des_ar.items()}
            rev_ed = {v:k for k, v in ed_ar.items()}
            rev_onl = {v:k for k, v in onl_ar.items()}
            s = str(rev_sot[slova[0]])

            if (slova[1] in onl_ar.values()):
                q = str(rev_onl[slova[1]])
                self.cifr.text = s + q 
            elif (slova[1] in ed_ar.values()):
                q = '0' + str(rev_ed[slova[1]])
                self.cifr.text = s + q 
            elif (slova[1] in des_ar.values()) and (slova[2] in ed_ar.values()):
                d = str(rev_des[slova[1]])
                e = str(rev_ed[slova[2]])
                self.cifr.text = s + d + e 
            elif (slova[1] in des_ar.values()) and (slova[2] == ''):
                d = str(rev_des[slova[1]])
                e = '0'
                self.cifr.text = s + d + e 
            elif (slova[1] == '') and (slova[2] == ''):
                d = '0'
                e = '0'
                self.cifr.text = s + d + e 
        osh = []

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

