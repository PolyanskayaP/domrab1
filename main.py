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
Window.clearcolor = (3/255, 6/255, 5/255, 1) 
#Window.title = "DR1"

class MyApp(App):
    def __init__(self):
        super().__init__() 
        self.cifr = Label(text='')
        self.input_data = TextInput(hint_text='Введите число прописью', multiline=True)

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

        rev_sot = {v:k for k, v in sot_ar.items()}
        rev_des = {v:k for k, v in des_ar.items()}
        rev_ed = {v:k for k, v in ed_ar.items()}
        rev_onl = {v:k for k, v in onl_ar.items()}

        cif = ''
        if (slova[0]=='') and (slova[1]=='') and (slova[2]==''):
            self.cifr.text = 'вы ничего не написали :('
        else:
            if (slova[0] in sot_ar.values()):
                cif = cif + str(rev_sot[slova[0]]) 
                if (slova[1] == ''):
                    cif = cif + '00'
                    self.cifr.text = cif 
                else:
                    if (slova[1] in des_ar.values()):
                        cif = cif + str(rev_des[slova[1]]) 
                        if (slova[2]==''):
                            cif = cif + '0'
                            self.cifr.text = cif  
                        elif (slova[2] in ed_ar.values()):
                            cif = cif + str(rev_ed[slova[2]])                      
                            self.cifr.text = cif
                        else:
                            ks = slova[2].split(' ', 1)  
                            if ks[0] not in ed_ar.values():
                                self.cifr.text = 'неправильное слово - '+ ks[0] +'. \n'+'Нельзя после слова десятичного формата ('+slova[1]+') \nписать ничего другого, кроме единиц'
                            else:
                                #cif = cif + str(rev_ed[ks[0]])                      
                                #self.cifr.text = cif
                                self.cifr.text = 'неправильное слово - '+ ks[1] +'. \n'+'Нельзя после слова единичного формата ('+ks[0]+') \nписать ничего другого, кроме единиц'
                    elif (slova[1] in onl_ar.values()):
                        cif = cif + str(rev_onl[slova[1]]) 
                        if (slova[2] == ''):
                            self.cifr.text = cif
                        else:
                            ks = slova[2].split(' ', 1) 
                            self.cifr.text =  'неправильное слово - '+ ks[0] +'. \n'+'Нельзя после слова формата 10-19 ('+slova[1]+') \nписать никакое другое слово '
                    elif (slova[1] in ed_ar.values()):
                        cif = cif + '0' + str(rev_ed[slova[1]]) 
                        if (slova[2] == ''):
                            self.cifr.text = cif
                        else:
                            ks = slova[2].split(' ', 1) 
                            self.cifr.text =  'неправильное слово - '+ ks[0] +'. \n'+'Нельзя после слова единичного формата ('+slova[1]+') \nписать другое слово '
                    else:
                        self.cifr.text =  'неправильное слово - '+ slova[1] + '\nнельзя после сотен ('+slova[0]+') писать что-либо ('+slova[1]+'), кроме десятков, единиц\nи слов формата 10-19'                  
            else:
                if (slova[0] in des_ar.values()):
                    cif = cif + str(rev_des[slova[0]]) 
                    if (slova[1]==''):
                        cif = cif + '0'
                        self.cifr.text = cif  
                    elif (slova[1] in ed_ar.values()):
                        cif = cif + str(rev_ed[slova[1]]) 
                        if (slova[2]==''):
                            self.cifr.text = cif
                        else:
                            ks = slova[2].split(' ', 1) 
                            self.cifr.text = 'неправильное слово - '+ ks[0] +'. \n'+'Нельзя после слова единичного формата ('+slova[1]+') \nписать другое слово ('+slova[2]+')'
                    else:
                        self.cifr.text = 'неправильное слово - '+ slova[1] +'. \n'+'Нельзя после слова десятичного формата ('+slova[0]+') \nписать ничего другого, кроме единиц'
                elif (slova[0] in onl_ar.values()):
                    cif = cif + str(rev_onl[slova[0]]) 
                    if (slova[1] == ''):
                        self.cifr.text = cif
                    else:
                        self.cifr.text =  'неправильное слово - '+ slova[1] +'. \n'+'Нельзя после слова формата 10-19 ('+slova[0]+') \nписать другое слово ('+slova[1]+')'
                elif (slova[0] in ed_ar.values()):
                    cif = cif + str(rev_ed[slova[0]]) 
                    if (slova[1] == ''):
                        self.cifr.text = cif
                    else:
                        self.cifr.text =  'неправильное слово - '+ slova[1] +'. \n'+'Нельзя после слова единичного формата ('+slova[0]+') \nписать никакое другое слово '
                else:
                    self.cifr.text =  'неправильное слово - '+ slova[0] 

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
