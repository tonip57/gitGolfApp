from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem
from kivy.uix.label import Label
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivy.metrics import dp
from kivymd.uix.toolbar import MDToolbar
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from functools import partial
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
from kivymd.uix.datatables import MDDataTable
from kivy.network.urlrequest import UrlRequest

store = JsonStore('tallennettukierros.json')

import imp
import sys

class ImportBlocker(object):

    def __init__(self, *args):
        self.black_list = args

    def find_module(self, name, path=None):
        if name in self.black_list:
            return self

        return None

    def load_module(self, name):
        module = imp.new_module(name)
        module.__all__ = [] # Necessary because of how bs4 inspects the module

        return module

sys.meta_path = [ImportBlocker('bs4.builder._htmlparser')]
from bs4 import BeautifulSoup
            

class KierrosScreen(Screen):
    
    def on_pre_enter(self):
        v = 1
        s = 0
        lista = ["","","","","","","","","","","","","","","","","",""]
        for i in range(18):
            x = 'v' + str(v)
            luku = store.get("kierros1")[str(x)]
            v = v + 1
            lista[s] = luku
            s = s + 1
            
        self.ids.v1.text = lista[0]
        self.ids.v2.text = lista[1]
        self.ids.v3.text = lista[2]
        self.ids.v4.text = lista[3]
        self.ids.v5.text = lista[4]
        self.ids.v6.text = lista[5]
        self.ids.v7.text = lista[6]
        self.ids.v8.text = lista[7]
        self.ids.v9.text = lista[8]
        self.ids.v10.text = lista[9]
        self.ids.v11.text = lista[10]
        self.ids.v12.text = lista[11]
        self.ids.v13.text = lista[12]
        self.ids.v14.text = lista[13]
        self.ids.v15.text = lista[14]
        self.ids.v16.text = lista[15]
        self.ids.v17.text = lista[16]
        self.ids.v18.text = lista[17] 
            
        
    def tyhjenna(self):
        store.put("kierros1", 
        v1 = "",
        v2 = "",
        v3 = "",
        v4 = "",
        v5 = "",
        v6 = "",
        v7 = "",
        v8 = "",
        v9 = "",
        v10 = "",
        v11 = "",
        v12 = "",
        v13 = "",
        v14 = "",
        v15 = "",
        v16 = "",
        v17 = "",
        v18 = "") 
        self.on_pre_enter()
    
        
    pass


class MenuScreen(Screen):
    pass




class SaaScreen(Screen):    
    
    def on_pre_enter(self):
        self.haku()
    
    def haku(self, *args):
        url = "https://www.supersaa.fi/suomi/siikajoki/"
        
        self.page = UrlRequest(url, on_success=partial(self.nayta_saa))
        
    
    def nayta_saa(self, *args):
               

        page = self.page.result
        
        page_soup = soup(page, "html.parser")
        containers = page_soup.findAll("span", {"class":"supers-forecast-temperature"})
        kellonajat = page_soup.findAll("div", {"class":"supers-forecast-item supers-day-marker"})
        sateentodnak = page_soup.findAll("span", {"class":"supers-forecast-rain-probability"})
        tuulennopeus = page_soup.findAll("span", {"class":"supers-windspeed"})
        sateenmaara = page_soup.findAll("span", {"class":"supers-forecast-rain-amount"})
        
        
        
        #TÄMÄN HETKINEN SÄÄ
        
        
        thlampo = page_soup.findAll("span", {"class":"supers-current-temperature"})
        thlampo = thlampo[0].text
        
        thtuntuukuin = page_soup.findAll("span", {"class":"supers-value"})
        thtuntuukuin = thtuntuukuin[0].text
        
        thsadetod = page_soup.findAll("span", {"class":"supers-value"})
        thsadetod = thsadetod[1].text
        
        thsademaara = page_soup.findAll("span", {"class":"supers-value"})
        thsademaara = thsademaara[2].text
        
        thlampo2 = page_soup.findAll("span", {"class":"supers-current-temperature"})
        thlampo2 = thlampo2[1].text
        
        thtuntuukuin2 = page_soup.findAll("span", {"class":"supers-value"})
        thtuntuukuin2 = thtuntuukuin2[3].text
        
        thsadetod2 = page_soup.findAll("span", {"class":"supers-value"})
        thsadetod2 = thsadetod2[4].text
        
        thsademaara2 = page_soup.findAll("span", {"class":"supers-value"})
        thsademaara2 = thsademaara2[5].text
        
        thtuuli1 = page_soup.findAll("span", {"class":"supers-windspeed"})
        thtuuli1 = thtuuli1[0].text
        
        thtuuli2 = page_soup.findAll("span", {"class":"supers-windspeed"})
        thtuuli2 = thtuuli2[1].text
        
        thtuuli1 = int(thtuuli1)
        thtuuli2 = int(thtuuli2)
        thtuuliKA = (thtuuli1 + thtuuli2) / 2
        
        
        thtuntuukuin = thtuntuukuin.replace('°', '') 
        thtuntuukuin2 = thtuntuukuin2.replace('°', '')
        thtuntuukuin = int(thtuntuukuin)
        thtuntuukuin2 = int(thtuntuukuin2)
        thtuntuukuinKA = (thtuntuukuin + thtuntuukuin2) / 2
        
            
        thsademaara = thsademaara.replace('mm', '') 
        thsademaara2 = thsademaara2.replace('mm', '')
        thsademaara = int(thsademaara)
        thsademaara2 = int(thsademaara2)
        thsademaaraKA = (thsademaara + thsademaara2) / 2
        
        
        thlampo = thlampo.replace('°', '') 
        thlampo2 = thlampo2.replace('°', '')
        thlampo = int(thlampo)
        thlampo2 = int(thlampo2)
        thlampoKA = (thlampo + thlampo2) / 2
        
        thsadetod = thsadetod.replace('%', '') 
        thsadetod2 = thsadetod2.replace('%', '')
        thsadetod = int(thsadetod)
        thsadetod2 = int(thsadetod2)
        thsadetodKA = (thsadetod + thsadetod2) / 2
        
        thkello = page_soup.select('h2')[0].text.strip()
        
        
        self.ids.thsaa.text = str(thkello) + " | " + str(thlampoKA)
        self.ids.thsaa.secondary_text = "Tuntuu: " + str(thtuntuukuinKA) + " | Tuuli: " + str(thtuuliKA) + " m/s"
        self.ids.thsaa.tertiary_text = "Sade: " + str(thsadetodKA) + " % | " + str(thsademaaraKA) + " mm "
        
        
        
        left = 0
        right = 1
        x = 0
        
        lista = []

        while x < 5:
            sadetod1 = sateentodnak[left].text
            sadetod2 = sateentodnak[right].text
            sadetod1 = sadetod1.replace('%', '') 
            sadetod2 = sadetod2.replace('%', '')
            sadetod1 = int(sadetod1)
            sadetod2 = int(sadetod2)
            sadetodKA = (sadetod1 + sadetod2) / 2
        
            sademaara1 = sateenmaara[left].text
            sademaara2 = sateenmaara[right].text
            sademaara1 = sademaara1.replace('mm', '') 
            sademaara2 = sademaara2.replace('mm', '')
            sademaara1 = float(sademaara1)
            sademaara2 = float(sademaara2)
            sademaaraKA = (sademaara1 + sademaara2) / 2
        
            lampotila1 = containers[left].text
            lampotila2 = containers[right].text
            lampotila1 = lampotila1.replace('°', '') 
            lampotila2 = lampotila2.replace('°', '')
            lampotila1 = int(lampotila1)
            lampotila2 = int(lampotila2)
            lampotilaKA = (lampotila1 + lampotila2) / 2
        
            tuuli1 = tuulennopeus[left+3].text
            tuuli2 = tuulennopeus[right+3].text
            tuuli1 = int(tuuli1)
            tuuli2 = int(tuuli2)
            tuuliKA = (tuuli1 + tuuli2) / 2
        
            kellonaika = int(kellonajat[x].text)
        
            left = left + 2
            right = right + 2
            x = x + 1
            
            lista.append([str(kellonaika), str(lampotilaKA), str(sadetodKA), str(sademaaraKA), str(tuuliKA)])
        
        
        self.ids.k1.text = str(lista[0][0])
        self.ids.l1.text = str(lista[0][1])
        self.ids.st1.text = str(lista[0][2])
        self.ids.sm1.text = str(lista[0][3])
        self.ids.t1.text = str(lista[0][4])
        
        self.ids.k2.text = str(lista[1][0])
        self.ids.l2.text = str(lista[1][1])
        self.ids.st2.text = str(lista[1][2])
        self.ids.sm2.text = str(lista[1][3])
        self.ids.t2.text = str(lista[1][4])
        
        self.ids.k3.text = str(lista[2][0])
        self.ids.l3.text = str(lista[2][1])
        self.ids.st3.text = str(lista[2][2])
        self.ids.sm3.text = str(lista[2][3])
        self.ids.t3.text = str(lista[2][4])
        
        self.ids.k4.text = str(lista[3][0])
        self.ids.l4.text = str(lista[3][1])
        self.ids.st4.text = str(lista[3][2])
        self.ids.sm4.text = str(lista[3][3])
        self.ids.t4.text = str(lista[3][4])
        
        self.ids.k5.text = str(lista[4][0])
        self.ids.l5.text = str(lista[4][1])
        self.ids.st5.text = str(lista[4][2])
        self.ids.sm5.text = str(lista[4][3])
        self.ids.t5.text = str(lista[4][4])


   

    
class SecondScreen(Screen):
    piilotettu = False
    
    def on_pre_enter(self):
        self.nayta_viime_kierros()
    
    def piilota_lyontimaara(self):   
        if self.piilotettu == False:
            self.piilotettu = True
            self.ids.lyontiMaara.text = ""
            
        else: 
            self.piilotettu = False
            self.laske_lyonnit()
    
        
    
    def lyonnit(self, lyontimaara):
        v1par = 4
        v2par = 4
        v3par = 4
        v4par = 3
        v5par = 4
        v6par = 4
        v7par = 5
        v8par = 3
        v9par = 5
        v10par = 4
        v11par = 4
        v12par = 5
        v13par = 3
        v14par = 4
        v15par = 3
        v16par = 4
        v17par = 4
        v18par = 5
        
        vihrea = (0, 1, 0.3, 1)
        punainen = (1, 0, 0, 1)
        violetti = (1, 0, 1, 0.8)
        musta = (0, 0, 0, 0.9)
        
        
        
        
        if self.ids.vaylaNumero.text == "1":
            self.ids.v1.text = str(v1par + lyontimaara)
            if int(self.ids.v1.text) == v1par:
                self.ids.v1.color = vihrea
            elif int(self.ids.v1.text) == v1par - 1:
                self.ids.v1.color = punainen
            elif int(self.ids.v1.text) == v1par + 1:
                self.ids.v1.color = violetti
            else:
                self.ids.v1.color = musta
        
        elif self.ids.vaylaNumero.text == "2": 
            self.ids.v2.text = str(v2par + lyontimaara)
            if int(self.ids.v2.text) == v2par:
                self.ids.v2.color = vihrea
            elif int(self.ids.v2.text) == v2par - 1:
                self.ids.v2.color = punainen
            elif int(self.ids.v2.text) == v2par + 1:
                self.ids.v2.color = violetti
            else:
                self.ids.v2.color = musta
        
        elif self.ids.vaylaNumero.text == "3":
            self.ids.v3.text = str(v3par + lyontimaara)
            if int(self.ids.v3.text) == v3par:
                self.ids.v3.color = vihrea
            elif int(self.ids.v3.text) == v3par - 1:
                self.ids.v3.color = punainen
            elif int(self.ids.v3.text) == v3par + 1:
                self.ids.v3.color = violetti
            else:
                self.ids.v3.color = musta
        
        elif self.ids.vaylaNumero.text == "4":
            self.ids.v4.text = str(v4par + lyontimaara)
            if int(self.ids.v4.text) == v4par:
                self.ids.v4.color = vihrea
            elif int(self.ids.v4.text) == v4par - 1:
                self.ids.v4.color = punainen
            elif int(self.ids.v4.text) == v4par + 1:
                self.ids.v4.color = violetti
            else:
                self.ids.v4.color = musta
        
        elif self.ids.vaylaNumero.text == "5":
            self.ids.v5.text = str(v5par + lyontimaara)
            if int(self.ids.v5.text) == v5par:
                self.ids.v5.color = vihrea
            elif int(self.ids.v5.text) == v5par - 1:
                self.ids.v5.color = punainen
            elif int(self.ids.v5.text) == v5par + 1:
                self.ids.v5.color = violetti
            else:
                self.ids.v5.color = musta
        
        elif self.ids.vaylaNumero.text == "6":
            self.ids.v6.text = str(v6par + lyontimaara)
            if int(self.ids.v6.text) == v6par:
                self.ids.v6.color = vihrea
            elif int(self.ids.v6.text) == v6par - 1:
                self.ids.v6.color = punainen
            elif int(self.ids.v6.text) == v6par + 1:
                self.ids.v6.color = violetti
            else:
                self.ids.v6.color = musta
        
        elif self.ids.vaylaNumero.text == "7":
            self.ids.v7.text = str(v7par + lyontimaara)
            if int(self.ids.v7.text) == v7par:
                self.ids.v7.color = vihrea
            elif int(self.ids.v7.text) == v7par - 1:
                self.ids.v7.color = punainen
            elif int(self.ids.v7.text) == v7par + 1:
                self.ids.v7.color = violetti
            else:
                self.ids.v7.color = musta
        
        elif self.ids.vaylaNumero.text == "8":
            self.ids.v8.text = str(v8par + lyontimaara)
            if int(self.ids.v8.text) == v8par:
                self.ids.v8.color = vihrea
            elif int(self.ids.v8.text) == v8par - 1:
                self.ids.v8.color = punainen
            elif int(self.ids.v8.text) == v8par + 1:
                self.ids.v8.color = violetti
            else:
                self.ids.v8.color = musta
        
        elif self.ids.vaylaNumero.text == "9":
            self.ids.v9.text = str(v9par + lyontimaara)
            if int(self.ids.v9.text) == v9par:
                self.ids.v9.color = vihrea
            elif int(self.ids.v9.text) == v9par - 1:
                self.ids.v9.color = punainen
            elif int(self.ids.v9.text) == v9par + 1:
                self.ids.v9.color = violetti
            else:
                self.ids.v9.color = musta
        
        elif self.ids.vaylaNumero.text == "10":
            self.ids.v10.text = str(v10par + lyontimaara)
            if int(self.ids.v10.text) == v10par:
                self.ids.v10.color = vihrea
            elif int(self.ids.v10.text) == v10par - 1:
                self.ids.v10.color = punainen
            elif int(self.ids.v10.text) == v10par + 1:
                self.ids.v10.color = violetti
            else:
                self.ids.v10.color = musta
        
        elif self.ids.vaylaNumero.text == "11":
            self.ids.v11.text = str(v11par + lyontimaara)
            if int(self.ids.v11.text) == v11par:
                self.ids.v11.color = vihrea
            elif int(self.ids.v11.text) == v11par - 1:
                self.ids.v11.color = punainen
            elif int(self.ids.v11.text) == v11par + 1:
                self.ids.v11.color = violetti
            else:
                self.ids.v11.color = musta
        
        elif self.ids.vaylaNumero.text == "12":
            self.ids.v12.text = str(v12par + lyontimaara)
            if int(self.ids.v12.text) == v12par:
                self.ids.v12.color = vihrea
            elif int(self.ids.v12.text) == v12par - 1:
                self.ids.v12.color = punainen
            elif int(self.ids.v12.text) == v12par + 1:
                self.ids.v12.color = violetti
            else:
                self.ids.v12.color = musta
        
        elif self.ids.vaylaNumero.text == "13":
            self.ids.v13.text = str(v13par + lyontimaara)
            if int(self.ids.v13.text) == v13par:
                self.ids.v13.color = vihrea
            elif int(self.ids.v13.text) == v13par - 1:
                self.ids.v13.color = punainen
            elif int(self.ids.v13.text) == v13par + 1:
                self.ids.v13.color = violetti
            else:
                self.ids.v13.color = musta
        
        elif self.ids.vaylaNumero.text == "14":
            self.ids.v14.text = str(v14par + lyontimaara)
            if int(self.ids.v14.text) == v14par:
                self.ids.v14.color = vihrea
            elif int(self.ids.v14.text) == v14par - 1:
                self.ids.v14.color = punainen
            elif int(self.ids.v14.text) == v14par + 1:
                self.ids.v14.color = violetti
            else:
                self.ids.v14.color = musta
        
        elif self.ids.vaylaNumero.text == "15":
            self.ids.v15.text = str(v15par + lyontimaara)
            if int(self.ids.v15.text) == v15par:
                self.ids.v15.color = vihrea
            elif int(self.ids.v15.text) == v15par - 1:
                self.ids.v15.color = punainen
            elif int(self.ids.v15.text) == v15par + 1:
                self.ids.v15.color = violetti
            else:
                self.ids.v15.color = musta
        
        elif self.ids.vaylaNumero.text == "16":
            self.ids.v16.text = str(v16par + lyontimaara)
            if int(self.ids.v16.text) == v16par:
                self.ids.v16.color = vihrea
            elif int(self.ids.v16.text) == v16par - 1:
                self.ids.v16.color = punainen
            elif int(self.ids.v16.text) == v16par + 1:
                self.ids.v16.color = violetti
            else:
                self.ids.v16.color = musta
        
        elif self.ids.vaylaNumero.text == "17":
            self.ids.v17.text = str(v17par + lyontimaara)
            if int(self.ids.v17.text) == v17par:
                self.ids.v17.color = vihrea
            elif int(self.ids.v17.text) == v17par - 1:
                self.ids.v17.color = punainen
            elif int(self.ids.v17.text) == v17par + 1:
                self.ids.v17.color = violetti
            else:
                self.ids.v17.color = musta
        
        elif self.ids.vaylaNumero.text == "18":
            self.ids.v18.text = str(v18par + lyontimaara)
            if int(self.ids.v18.text) == v18par:
                self.ids.v18.color = vihrea
            elif int(self.ids.v18.text) == v18par - 1:
                self.ids.v18.color = punainen
            elif int(self.ids.v18.text) == v18par + 1:
                self.ids.v18.color = violetti
            else:
                self.ids.v18.color = musta
        
        self.laske_lyonnit()
        self.tallenna_kierros()
    
    
    def laske_lyonnit(self):
        lyonnit = 0
        if self.ids.v1.text != "":
            lyonnit = lyonnit + int(self.ids.v1.text)
        if self.ids.v2.text != "":
            lyonnit = lyonnit + int(self.ids.v2.text)
        if self.ids.v3.text != "":
            lyonnit = lyonnit + int(self.ids.v3.text)
        if self.ids.v4.text != "":
            lyonnit = lyonnit + int(self.ids.v4.text)
        if self.ids.v5.text != "":
            lyonnit = lyonnit + int(self.ids.v5.text)
        if self.ids.v6.text != "":
            lyonnit = lyonnit + int(self.ids.v6.text)
        if self.ids.v7.text != "":
            lyonnit = lyonnit + int(self.ids.v7.text)
        if self.ids.v8.text != "":
            lyonnit = lyonnit + int(self.ids.v8.text)
        if self.ids.v9.text != "":
            lyonnit = lyonnit + int(self.ids.v9.text)
            
        if self.ids.v10.text != "":
            lyonnit = lyonnit + int(self.ids.v10.text)
        if self.ids.v11.text != "":
            lyonnit = lyonnit + int(self.ids.v11.text)
        if self.ids.v12.text != "":
            lyonnit = lyonnit + int(self.ids.v12.text)
        if self.ids.v13.text != "":
            lyonnit = lyonnit + int(self.ids.v13.text)
        if self.ids.v14.text != "":
            lyonnit = lyonnit + int(self.ids.v14.text)
        if self.ids.v15.text != "":
            lyonnit = lyonnit + int(self.ids.v15.text)
        if self.ids.v16.text != "":
            lyonnit = lyonnit + int(self.ids.v16.text)
        if self.ids.v17.text != "":
            lyonnit = lyonnit + int(self.ids.v17.text)
        if self.ids.v18.text != "":
            lyonnit = lyonnit + int(self.ids.v18.text)
        
        if self.piilotettu == False:  
            self.ids.lyontiMaara.text = str(lyonnit)
            
        
    
    def taakse(self):       
       
        if self.ids.vaylaNumero.text != "1":
            numero = int(self.ids.vaylaNumero.text)
            numero = numero - 1
            self.ids.vaylaNumero.text = str(numero)
        
        
    def eteen(self):
        if self.ids.vaylaNumero.text != "18":
            numero = int(self.ids.vaylaNumero.text)
            numero = numero + 1
            self.ids.vaylaNumero.text = str(numero)
                
    def nayta_viime_kierros(self):
        if str(self.ids.v1.text) == "":
            self.ids.v1.text = store.get("kierros1")['v1']
        if str(self.ids.v2.text) == "":
            self.ids.v2.text = store.get("kierros1")['v2']
        if str(self.ids.v3.text) == "":
            self.ids.v3.text = store.get("kierros1")['v3']
        if str(self.ids.v4.text) == "":
            self.ids.v4.text = store.get("kierros1")['v4']
        if str(self.ids.v5.text) == "":
            self.ids.v5.text = store.get("kierros1")['v5']
        if str(self.ids.v6.text) == "":
            self.ids.v6.text = store.get("kierros1")['v6']
        if str(self.ids.v7.text) == "":
            self.ids.v7.text = store.get("kierros1")['v7']
        if str(self.ids.v8.text) == "":
            self.ids.v8.text = store.get("kierros1")['v8']
        if str(self.ids.v9.text) == "":
            self.ids.v9.text = store.get("kierros1")['v9']
        if str(self.ids.v10.text) == "":
            self.ids.v10.text = store.get("kierros1")['v10']
        if str(self.ids.v11.text) == "":
            self.ids.v11.text = store.get("kierros1")['v11']
        if str(self.ids.v12.text) == "":
            self.ids.v12.text = store.get("kierros1")['v12']
        if str(self.ids.v13.text) == "":
            self.ids.v13.text = store.get("kierros1")['v13']
        if str(self.ids.v14.text) == "":
            self.ids.v14.text = store.get("kierros1")['v14']
        if str(self.ids.v15.text) == "":
            self.ids.v15.text = store.get("kierros1")['v15']
        if str(self.ids.v16.text) == "":
            self.ids.v16.text = store.get("kierros1")['v16']
        if str(self.ids.v17.text) == "":
            self.ids.v17.text = store.get("kierros1")['v17']
        if str(self.ids.v18.text) == "":
            self.ids.v18.text = store.get("kierros1")['v18']
        
    def tallenna_kierros(self):
        
             
        store.put("kierros1", 
        v1 = str(self.ids.v1.text),
        v2 = str(self.ids.v2.text),
        v3 = str(self.ids.v3.text),
        v4 = str(self.ids.v4.text),
        v5 = str(self.ids.v5.text),
        v6 = str(self.ids.v6.text),
        v7 = str(self.ids.v7.text),
        v8 = str(self.ids.v8.text),
        v9 = str(self.ids.v9.text),
        v10 = str(self.ids.v10.text),
        v11 = str(self.ids.v11.text),
        v12 = str(self.ids.v12.text),
        v13 = str(self.ids.v13.text),
        v14 = str(self.ids.v14.text),
        v15 = str(self.ids.v15.text),
        v16 = str(self.ids.v16.text),
        v17 = str(self.ids.v17.text),
        v18 = str(self.ids.v18.text))         
        

    pass
    
    
    



class MainApp(MDApp):
            
    def builf(self):

        kv = Builder.load_file("main.kv")
        return kv

    
    def stop(self, *largs):
        # Open the popup you want to open and declare callback if user pressed `Yes`
        popup = ExitPopup(title="Haluatko varmasti poistua?")
        popup.bind(on_confirm=partial(self.close_app, *largs))
        b = popup.open()
        

    def close_app(self, *largs):   
        super(MainApp, self).stop(*largs)
     
    pass


class ExitPopup(Popup):

    def __init__(self, **kwargs):
        super(ExitPopup, self).__init__(**kwargs)
        self.register_event_type('on_confirm')
    
    def close_popup(self):
        self.dismiss()

    def on_confirm(self):
        pass

    def on_button_yes(self):
        self.dispatch('on_confirm')


if __name__ == "__main__":            
    sm = ScreenManager()
    sm.add_widget(MenuScreen())
    sm.add_widget(SaaScreen())
    sm.add_widget(SecondScreen())
    MainApp().run()
    