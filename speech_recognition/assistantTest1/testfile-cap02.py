# -*- coding: utf-8 -*-

import speech_recognition as sr  #kütüphaneyi çağırıp sr olarak adlandırıyoruz 'Kelimeleri yorumlayarak sese çeviriyor'

import time             #1 sn lik geçikme ayarlayacağız
from komutlar import Komut #☺komutlar.py dosyasını çağırır


r=sr.Recognizer()


while True:    #sonsuz dongu oluşturuyoruz
    with sr.Microphone() as source:  #mikrofondan aldığımız değişkenleri sourceye atar
        print("Nasıl yardımcı oabilirim?")
        audio = r.listen(source)
    data=""
    
    try:
        data=r.recognize_google(audio,language='tr=tr') #yazıya dönüştürür
        print(data)
        komut=Komut(data)
        komut.komutBul()
        time.sleep(1)
        
    except sr.UnkownValueError:
        print("Söylediğinizi anlayamadım")
        
        
    
    