# -*- coding: utf-8 -*-

from tkinter import *

def enaslambulFunc():

    kutuContent = girisYapilan.get()

    if ( kutuContent == '' ):
        girisYapilan.insert(END, 'boşluk')
        kutuContent = 'boşluk'

    gelendenTRayikla = list(kutuContent)

    # ---> TR harf var ise EN harf çevir <--- #

    TRler = ['ç','ı','ü','ğ','ö','ş','İ','Ğ','Ü','Ö','Ş','Ç',' ']
    ENler = ['c','i','u','g','o','s','I','G','U','O','S','C','-']

    bizimSonKelimemiz = ''

    for karakterlerTekTek in gelendenTRayikla:
        if ( karakterlerTekTek in TRler ):
            kacinciSirada = TRler.index(karakterlerTekTek) # TR'deki sırasını buldum.
            karakterlerTekTek = ENler[kacinciSirada] # EN'de yukarıdaki sırayı yazdım.

        bizimSonKelimemiz = bizimSonKelimemiz + karakterlerTekTek

    # ---> TR harf var ise EN harf çevir <--- #

    import urllib.request # bağlanmak için
    import re # ayıklamak için

    esanlamFade = 'http://www.es-anlam.com/kelime/' + bizimSonKelimemiz
    esanlamPage = urllib.request.urlopen(esanlamFade).read().decode("utf-8")

    ayiklamaRegex = '<h2 style="font-size:24px" id="esanlamlar"><i>.*?</i> kelimesinin eş anlamlı sözcükleri :  <strong>(.*?)</strong></h2>'

    arananFade = re.compile(ayiklamaRegex)
    ciktimizDi = re.findall(arananFade, esanlamPage)

    ciktiAyikla = ciktimizDi[0].split(',')

    sonuclarYazan.delete(1.0, END) # text yerini temizliyoruz.
    sonuclarYazan.config(state='normal') # text yerini disabled'ten kurtarıyoruz.

    if ( ciktiAyikla[0] == 'BULUNAMADI !' ):

        sonuclarYazan.insert(END, 'Herhangi bir sonuç bulunamadı.')

    else:

        kacTane = 0

        for ciktilarTek in ciktiAyikla:
            kacTane = kacTane + 1
            ciktilarTek = ciktilarTek.strip() # strip() PHP'deki trim işlemini görür.
            ciktilarTek = str(kacTane) + '. ' + ciktilarTek + '\n'
            sonuclarYazan.insert(END, ciktilarTek)

    # ---> DEF komutu bitti <--- #

pencere = Tk()
pencere.title('Eş Anlamlı Kelimeler')
pencere.geometry('399x384+50+50')
pencere.resizable(False, False) # boyut değişimini engelle

girisCumlesi = Label(pencere)
girisCumlesi.config(text='Eş anlamını bulmak istediğiniz kelimeyi yazın.', bg='#2ecc71', fg='#fff', height=2, width=60)
girisCumlesi.pack(padx=10, pady=(10, 5))

girisYapilan = Entry(pencere)
girisYapilan.config(bg='#e5e5e5', border=0, justify='center', width=100, font = "arial 22 normal", fg='#f39c12')
girisYapilan.insert(END, 'bulmak')
girisYapilan.pack(padx=10, pady=(5, 10))

submitButon = Button(pencere)
submitButon.config(text='KELİMENİN EŞ ANLAMINI BUL', command=enaslambulFunc, bg='#3498db', fg='#fff', width=60, border=0, height=2, cursor='cross', activebackground='#2980b9', activeforeground='#f1c40f')
submitButon.pack(padx=10, pady=(0,10))

sonuclarYazan = Text(pencere)
sonuclarYazan.config(bg='#dbdbdb', border=0, width=100, font = "arial 16 normal", fg='#34495e', state='disabled')
sonuclarYazan.pack(padx=10, pady=(0,10))

mainloop()