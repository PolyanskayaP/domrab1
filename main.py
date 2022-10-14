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
        self.input_data = TextInput(hint_text='Введите число буквами', multiline=True)

    def btn_pressed(self, *args):    
        data = self.input_data.text
        #алгоритм с data
        self.algor(data)
        

    def algor(self, data):    #data это словами число
        lev_str = '   >'
        pra_str = '<   '

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
        elif slova[2] != '':
            if (slova[0] not in des_ar.values() and slova[0] not in onl_ar.values() and slova[0] not in ed_ar.values() and slova[0] not in sot_ar.values()):
                osh.append('первое слово ('+slova[0]+') написано неправильно')
                self.input_data.text = " "+ lev_str + slova[0] + pra_str +" "+slova[1]+" "+ slova[2]     
            elif (slova[1] not in des_ar.values() and slova[1] not in onl_ar.values() and slova[1] not in ed_ar.values() and slova[1] not in sot_ar.values() and slova[1]!=''):
                self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]     
                osh.append('второе слово ('+slova[1]+') написано неправильно')
            elif (slova[1] in sot_ar.values()):
                osh.append('второе слово ('+slova[1]+') не должно быть сотней')
                self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]     

            elif (slova[2] not in ed_ar.values() and slova[2] not in des_ar.values() and slova[2] not in onl_ar.values() and slova[2] not in sot_ar.values() and slova[2]!=''):
                osh.append('третье слово  ('+slova[2]+') написано неправильно')
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
            elif (slova[2] in sot_ar.values()):
                osh.append('третье слово  ('+slova[2]+') не должно быть сотней')
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
           
            elif (slova[1] in ed_ar.values()) and (slova[2] in ed_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя два слова подряд ('+slova[1]+' '+slova[2]+') единичного формата')
            elif (slova[1] in des_ar.values()) and (slova[2] in des_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя писать два слова ('+slova[1]+' '+slova[2]+') подряд десятичного формата ')
            elif (slova[1] in onl_ar.values()) and (slova[2] in onl_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя писать два слова ('+slova[1]+' '+slova[2]+') подряд формата 10-19')
            elif (slova[1] in des_ar.values()) and (slova[2] in onl_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя сначала писать десятки('+slova[1]+'), потом число формата 10-19('+slova[2]+')')
            elif (slova[1] in ed_ar.values()) and (slova[2] in des_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом десятки('+slova[2]+')')
            elif (slova[1] in ed_ar.values()) and (slova[2] in onl_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом слово формата 10-19('+slova[2]+')')
            elif (slova[1] in ed_ar.values()) and (slova[2] in sot_ar.values()):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом сотни('+slova[2]+')')
            elif (slova[1] in onl_ar.values()) and not(slova[2] == ''):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя после слова форматом 10-19('+slova[1]+') писать еще слово('+slova[2]+')')          
            elif (slova[1] in ed_ar.values()) and not(slova[2] == ''):
                self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                osh.append('нельзя после слова единичного формата('+slova[1]+') писать еще слово('+slova[2]+')')                      

        if osh:
            #self.cifr.text = ";\n".join(osh)
            self.cifr.text = '>error<' 
        else:
            rev_sot = {v:k for k, v in sot_ar.items()}
            rev_des = {v:k for k, v in des_ar.items()}
            rev_ed = {v:k for k, v in ed_ar.items()}
            rev_onl = {v:k for k, v in onl_ar.items()}
            
            if slova[0] not in sot_ar.values():
                fir, sec = '', ''
                osh1 = [] 
                #if slova[2] != '':
                 #   er.append('-') 

                if (slova[0] not in des_ar.values() and slova[0] not in onl_ar.values() and slova[0] not in ed_ar.values() and slova[0] not in sot_ar.values() and slova[0]!=''):
                    self.input_data.text = lev_str + slova[0] + pra_str +" "+ slova[1] +" "+ slova[2]     
                    osh1.append('второе слово ('+slova[1]+') написано неправильно')
                elif (slova[0] in sot_ar.values()):
                    osh1.append('второе слово ('+slova[1]+') не должно быть сотней')
                    self.input_data.text = lev_str + slova[0] + pra_str +" "+ slova[1] +" "+ slova[2]     

                elif (slova[1] not in ed_ar.values() and slova[1] not in des_ar.values() and slova[1] not in onl_ar.values() and slova[1] not in sot_ar.values() and slova[1]!=''):
                    osh1.append('третье слово  ('+slova[2]+') написано неправильно')
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                elif (slova[1] in sot_ar.values()):
                    osh1.append('третье слово  ('+slova[2]+') не должно быть сотней')
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  

                elif (slova[0] in ed_ar.values()) and (slova[1] in ed_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя два слова подряд ('+slova[1]+' '+slova[2]+') единичного формата')
                elif (slova[0] in des_ar.values()) and (slova[1] in des_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя писать два слова ('+slova[1]+' '+slova[2]+') подряд десятичного формата ')
                elif (slova[0] in onl_ar.values()) and (slova[1] in onl_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя писать два слова ('+slova[1]+' '+slova[2]+') подряд формата 10-19')
                elif (slova[0] in des_ar.values()) and (slova[1] in onl_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя сначала писать десятки('+slova[1]+'), потом число формата 10-19('+slova[2]+')')
                elif (slova[0] in ed_ar.values()) and (slova[1] in des_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом десятки('+slova[2]+')')
                elif (slova[0] in ed_ar.values()) and (slova[1] in onl_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом слово формата 10-19('+slova[2]+')')
                elif (slova[0] in ed_ar.values()) and (slova[1] in sot_ar.values()):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя сначала писать слово единичного формата('+slova[1]+'), потом сотни('+slova[2]+')')
                elif (slova[0] in onl_ar.values()) and not(slova[1] == ''):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]   
                    osh1.append('нельзя после слова форматом 10-19('+slova[1]+') писать еще слово('+slova[2]+')')          
                elif (slova[0] in ed_ar.values()) and not(slova[1] == ''):
                    self.input_data.text = slova[0] +" "+ lev_str + slova[1] + pra_str +" "+ slova[2]  
                    osh1.append('нельзя после слова единичного формата('+slova[1]+') писать еще слово('+slova[2]+')')                      
                elif slova[2]!='':
                    self.input_data.text = slova[0]+" "+ slova[1] +" "+ lev_str + slova[2] + pra_str 
                    osh1.append('третье')
####
                if osh1:
                    self.cifr.text = '>error<'
                else:
                    if slova[0]=='десять' and slova[1]=='' and slova[2]=='': 
                        fir = '10'
                    elif (slova[0] in ed_ar.values()):
                        fir = str(rev_ed[slova[0]])
                    elif (slova[0] in des_ar.values() and slova[1] in ed_ar.values()):
                        fir = str(rev_des[slova[0]])
                        sec = str(rev_ed[slova[1]])
                    elif (slova[0] in des_ar.values() and slova[1]==''):
                        fir = str(rev_des[slova[0]])
                        sec = '0'               
                    elif (slova[0] in onl_ar.values()):
                        fir = str(rev_onl[slova[0]])
                    else:
                        fir = 'ошибка'
                    #if (slova[0] in sot_ar.values()):
                    #   fir = str(rev_sot[slova[0]])

                    
                    self.cifr.text = fir + sec 
            else:
                s = str(rev_sot[slova[0]])

                if (slova[1] in onl_ar.values()):   #сто тринадцать
                    q = str(rev_onl[slova[1]])
                    qqq = s + q
                    #self.cifr.text = s + q 
                    self.cifr.text = qqq 
                    ###self.input_data.foreground_color = (9,9,9,1)
                    #self.cifr.font_size = 78
                    #self.cifr.text = '[color=FFFF00]+self.cifr.text[0]+[/color]'+self.cifr.text[1:]    # "[color=3333ff]proud[/color]"
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

