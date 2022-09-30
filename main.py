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
    sot_ar = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
    des_ar = {0: '', 2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
    ed_ar =  {0: '', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

    onl_ar = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

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
        sot_ar = {1: 'сто', 2: 'двести', 3: 'триста', 4: 'четыреста', 5: 'пятьсот', 6: 'шестьсот', 7: 'семьсот', 8: 'восемьсот', 9: 'девятьсот'}
        des_ar = {  2: 'двадцать', 3: 'тридцать', 4: 'сорок', 5: 'пятьдесят', 6: 'шестьдесят', 7: 'семьдесят', 8: 'восемьдесят', 9: 'девяносто'}
        ed_ar =  {  1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

        onl_ar = {10: 'десять', 11: 'одиннадцать', 12: 'двенадцать', 13: 'тринадцать', 14: 'четырнадцать', 15: 'пятнадцать', 16: 'шестнадцать', 17: 'семнадцать', 18: 'восемнадцать', 19: 'девятнадцать'}

        #print(data)
        if (data[-1:] == ' '):
            data = data[:-1]
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
            if (slova[0] not in sot_ar.values()):
                osh.append('первое число должно быть сотней')
            if (slova[1] in sot_ar.values()):
                osh.append('второе число не должно быть сотней')
            if (slova[2] in sot_ar.values()):
                osh.append('третье число не должно быть сотней')
            if (slova[1] in ed_ar) and (slova[2] in ed_ar):
                osh.append('нельзя два числа единичного формата')
            if (slova[1] in des_ar) and (slova[2] in des_ar):
                osh.append('нельзя два числа десятичного формата')
            if (slova[1] in onl_ar) and (slova[2] in onl_ar):
                osh.append('нельзя два числа формата 10-19')
            if (slova[1] in des_ar) and (slova[2] in onl_ar):
                osh.append('нельзя сначала писать десятки, потом число формата 10-19')
            if (slova[1] in ed_ar) and (slova[2] in des_ar):
                osh.append('нельзя сначала писать число единичного формата, потом десятки')
            if (slova[1] in ed_ar) and (slova[2] in onl_ar):
                osh.append('нельзя сначала писать число единичного формата, потом число формата 10-19')
            if (slova[1] in onl_ar) and not(slova[2] == ''):
                osh.append('нельзя после числа форматом 10-19 писать еще число')

        if osh:
            self.cifr.text = "; ".join(osh) 
        else:
            rev_sot = {v:k for k, v in sot_ar.items()}
            rev_des = {v:k for k, v in des_ar.items()}
            rev_ed = {v:k for k, v in ed_ar.items()}
            rev_onl = {v:k for k, v in onl_ar.items()}
            s = str(rev_sot[slova[0]])

            if (slova[1] in onl_ar):
                q = rev_onl[slova[1]]
                self.cifr.text = s + q 
            elif (slova[1] in ed_ar):
                q = '0' + rev_ed[slova[1]]
                self.cifr.text = s + q 
            elif (slova[1] in des_ar) and (slova[2] in ed_ar):
                d = rev_des[slova[1]]
                e = rev_ed[slova[2]]
                self.cifr.text = s + d + e 
            elif (slova[1] in des_ar) and (slova[2] == ''):
                d = rev_des[slova[1]]
                e = '0'
                self.cifr.text = s + d + e 
            elif (slova[1] == '') and (slova[2] == ''):
                d = '0'
                e = '0'
                self.cifr.text = s + d + e 

             
             
            #data = rev_sot[slova[0]] + 


        #вывод ошибок предусмотреть
    #    self.cifr.text = str(data)  #вывод должно быть измененной data
        osh = []
        #ширину экрана исправь и т д 


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

##and (slova[1] in des_ar.values() or slova[1] in onl_ar.values() or slova[1] in ed_ar.values() or slova[1]=='') \
