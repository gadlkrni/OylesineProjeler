# -*- coding: utf-8 -*-

from tkinter import *
from gemilerListeModul import *

print(gemilerNeredeTamListesi)

toplamHak = 16
oyunPuani = 0
bulununca = 20
bulunanGe = 0

def tiklaFunc(gelenVeri):

    global toplamHak
    global oyunPuani
    global bulunanGe

    if ( toplamHak != 0 ):
        toplamHak = toplamHak - 1
        tiklaAyikla = int(gelenVeri[6:])
        varMi = 0

        for gemiListeSabit in gemilerNeredeTamListesi:
            if ( tiklaAyikla == gemiListeSabit ):
                varMi = 1
                break

        if ( varMi == 1 ):
            metin.config(text='Tebrikler gemiyi buldunuz!', bg='#f1c40f')
            oyunPuani = oyunPuani + bulununca
            puan.config(text='Puan: ' + str(oyunPuani))
            bulunanGe = bulunanGe + 1
            bulunan.config(text='Bulunan: ' + str(bulunanGe) + ' / 12')
            exec('gemiKutu_' + str(tiklaAyikla) + '.' + 'config(state="disabled", bg="#f1c40f", text="✓")')
        elif ( varMi == 0 ):
            metin.config(text='Maalesef bir şey bulamadınız.', bg='#e74c3c')
            exec('gemiKutu_' + str(tiklaAyikla) + '.' + 'config(state="disabled", bg="#e5e5e5", text="", fg="#fff")')

    else:
        metin.config(text='Oyuna devam edebilmek için yeterince hakkınız kalmadı!', bg='#e74c3c')

    # ---> IF komutu bitti <--- #

    toplamHakMetin = 'Kalan Hak: ' + str(toplamHak)
    hak.config(text=toplamHakMetin)

    # ---> DEF komutu bitti <--- #

pencere = Tk()
pencere.title('İlk Uygulamam')
pencere.geometry('399x384+50+50')
pencere.resizable(False, False) # boyut değişimini engelle

metin = Label(pencere)
metin.config(text='Hoşgeldin dostum oyunuma, her satırda 2 adet gemi var!', bg='#2ecc71', fg='#fff', height=2, width=54)
metin.pack(padx=10, pady=(10, 5))

satir_Puan = Frame(pencere)
satir_Puan.pack(side=TOP)

hak = Label(satir_Puan)
hak.config(text='Kalan Hak: 16', bg='#3498db', fg='#fff', height=2, width=14)
hak.pack(padx=(10, 0), pady=5, side=LEFT)

bulunan = Label(satir_Puan)
bulunan.config(text='Bulunan: 0 / 12', bg='#2980b9', fg='#fff', height=2, width=18)
bulunan.pack(padx=2, pady=5, side=LEFT)

puan = Label(satir_Puan)
puan.config(text='Puan: 0', bg='#f39c12', fg='#fff', height=2, width=19)
puan.pack(padx=(0, 10), pady=5, side=LEFT)

satir_0 = Frame(pencere)
satir_0.pack(side=TOP, padx=5)

satir_6 = Frame(pencere)
satir_6.pack(side=TOP, padx=5)

satir_12 = Frame(pencere)
satir_12.pack(side=TOP, padx=5)

satir_18 = Frame(pencere)
satir_18.pack(side=TOP, padx=5)

satir_24 = Frame(pencere)
satir_24.pack(side=TOP, padx=5)

satir_30 = Frame(pencere)
satir_30.pack(side=TOP, padx=5)

for gemiler in range(1,37,1):
    if ( gemiler > 30 ):
        hangiSatir = satir_30
    elif ( gemiler > 24 ):
        hangiSatir = satir_24
    elif ( gemiler > 18 ):
        hangiSatir = satir_18
    elif ( gemiler > 12 ):
        hangiSatir = satir_12
    elif ( gemiler > 6 ):
        hangiSatir = satir_6
    elif ( gemiler > 0 ):
        hangiSatir = satir_0

    gidecekVerimiz = 'tonID_' + str(gemiler)

    # ---> exec adamdır! :) exec ile anlaşılıyor işte. :) <--- #

    exec('gemiKutu_' + str(gemiler) + '=' + 'Button(hangiSatir)')
    exec('gemiKutu_' + str(gemiler) + '.' + "config(text = 'SEÇ', command = lambda gidecekVerimiz=gidecekVerimiz :tiklaFunc(gidecekVerimiz), bg='#95a5a6', fg='#fff', width=7, border=0, height=2, cursor='pirate', activebackground='#7f8c8d', activeforeground='#f1c40f')")
    exec('gemiKutu_' + str(gemiler) + '.' + 'pack(padx=5, pady=5, side=LEFT)')

mainloop()