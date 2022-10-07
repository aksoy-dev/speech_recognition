# -*- coding: utf-8 -*-

import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html

class Komut():
    def __init__(self,gelenses):
        self.ses=gelenses.upper()
        self.sesBloklari=self.ses.split()
        print(self.sesBloklari)
        self.komutlar={"ABONE","CEVİR","NABER","NASILSIN","KAPAT","HAVA"}
        
        
        
        #KOMUT İSİMLERİ
        
    def seslendirme(self,yazi):
        tts=gTTS(text=yazi,lang='tr')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
        
    def kapat(self):
        self.seslendirme("OK Görüşürüz")
        sys.exit()
    
    def HavaDurumu(self):
        r=requests.get("https://www.ntvhava.com/konum/van/7-gunluk-hava-tahmini")
        tree=html.fromstring(r.content)
        
        derece=tree.xpath('//*[id="main"]/selection[3]/div/ul[3]/li[1]/div[2]/div[1]/p[1]/span')
        durum= tree.xpath('//*[id="main"]/selection[3]/div/ul[3]/li[1]/div[2]/div[1]/p[2]')
        uyari=''
        
        if durum[0].text=="Yağmurlu":
            uyari="Şemsiyeni almayı unutma :)"
            
            
        
        yazi=("Fırat,bugün hava {} derece ve {} gözüküyor. {}  ".format(derece[0].text,durum[0].text,uyari))
        self.seslendirme(yazi)
        
    def Sohbet(self):
        sozler="iyi",
        "nasılsın",
        "Genellikle yapay zeka için json dosyaları var sohbet metinleri için kullanılan"
        
        secim=choice(sozler)
        self.seslendirme(secim)
        
    #googleapis.com kısmında youtube apiden anlık olarak veri çekebiliriz
        
        #komut ve islemleri
        
    def KomutBul(self):
        for.komut in self.komutlar:
            if komut in self.sesBloklari:
                self.komutCalistir(komut)
                
    def komutCalistir(self,komut):
        if komut=="KAPAT"
        self.kapat()
        if komut=="NABER" or komut=="NASILSIN":
            self.Sohbet()
        if komut=="HAVA":
            self.HavaDurumu()
            
            
            
        
        
        