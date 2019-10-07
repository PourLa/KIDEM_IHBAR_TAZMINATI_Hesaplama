import datetime
import time
from os import system

class Tahsılat:

    def tahsılat(Net_ucret):
        #Burada işe başlama ve işten çıkış arasındaki gün sayısını belirliyoruz.Yani Kaç yıl çalıştığını buluyoruz.
        ıse_baslama = datetime.datetime(2019,8,8)
        ısten_ayrılma = datetime.datetime(2021,6,27)

        Toplam_gun = ısten_ayrılma -  ıse_baslama
        net_gun = Net_ucret/365
        Net_Kıdem = Toplam_gun.days * net_gun
        Damga_vergısı = 0.00948
        Kıdem_Tazmınat = Net_Kıdem - (Net_Kıdem*Damga_vergısı)

        print("Kıdem Tazminatınızın Tutarı :",Kıdem_Tazmınat)
        input ("ENTER'a basınız!")

    def Ihbar_Tazmınat(Net_ucret):



        while True:

            ıse_baslama = datetime.datetime (2019,8,8)
            ısten_ayrılma = datetime.datetime (2021,6,27)
            Toplam_gun = ısten_ayrılma - ıse_baslama
            yıl = Toplam_gun.days / 365
            zaman = round (yıl)
            gunluk_ucret = Net_ucret / 30
            haftalık_ucret = gunluk_ucret * 7
            Gelır_vergısı = 0.15 * Net_ucret
            Damga_vergısı = 0.00948 * Net_ucret

            if zaman < 0.5:
                #6 aydan az ise ihbar 2 hafta
                ıhbar_tazmınat = 2 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat - (Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                input("ENTER'a basınız!")
                break

            elif  0.5<zaman<1:
                #6 aydan fazka 1,5 aydan az 4 hafta
                ıhbar_tazmınat = 4 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat - (Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                input("ENTER'a basınız!")
                break

            elif 1.5<zaman<3:
                #1,5 ile 3 yıl arasında ise 6 hafta
                ıhbar_tazmınat = 6 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat-(Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                input("ENTER'a basınız!")
                break

            elif 3<zaman:
                #3 yıldan fazla çalışan 8 hafta
                ıhbar_tazmınat = 8 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat-(Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                input("ENTER'a basınız!")
                break

            else:
                print("Yanlış birşey oldu!")


    def kıd_ıhbar(Net_ucret):

        ıse_baslama = datetime.datetime (2019, 8, 8)
        ısten_ayrılma = datetime.datetime (2021, 6, 27)

        Toplam_gun = ısten_ayrılma - ıse_baslama
        net_gun = Net_ucret / 365
        Net_Kıdem = Toplam_gun.days * net_gun
        Damga_vergısı = 0.00948
        Kıdem_Tazmınat = Net_Kıdem - (Net_Kıdem * Damga_vergısı)

        print ("Kıdem Tazminatınızın Tutarı :", Kıdem_Tazmınat)


        while True:

            ıse_baslama = datetime.datetime (2019,8,8)
            ısten_ayrılma = datetime.datetime (2021,6,27)
            Toplam_gun = ısten_ayrılma - ıse_baslama
            yıl = Toplam_gun.days / 365
            zaman = round (yıl)
            gunluk_ucret = Net_ucret / 30
            haftalık_ucret = gunluk_ucret * 7
            Gelır_vergısı = 0.15 * Net_ucret
            Damga_vergısı = 0.00948 * Net_ucret

            if zaman < 0.5:
                #6 aydan az ise ihbar 2 hafta
                ıhbar_tazmınat = 2 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat - (Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                break

            elif  0.5<zaman<1:
                #6 aydan fazka 1,5 aydan az 4 hafta
                ıhbar_tazmınat = 4 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat - (Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                break

            elif 1.5<zaman<3:
                #1,5 ile 3 yıl arasında ise 6 hafta
                ıhbar_tazmınat = 6 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat-(Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                break

            elif 3<zaman:
                #3 yıldan fazla çalışan 8 hafta
                ıhbar_tazmınat = 8 * haftalık_ucret
                Net_ıhbar_tazmınat = ıhbar_tazmınat-(Gelır_vergısı+Damga_vergısı)
                print("İhbar Tazminatı Tutarı :",Net_ıhbar_tazmınat)
                break

            else:
                print("Yanlış birşey oldu!")

        Toplam = Kıdem_Tazmınat + Net_ıhbar_tazmınat
        print("Toplam eline geçicek para :",Toplam)
        input ("ENTER'a basınız!")


print ("""        

 /$$   /$$ /$$$$$$ /$$$$$$$  /$$$$$$$$ /$$      /$$                       /$$$$$$ /$$   /$$ /$$$$$$$   /$$$$$$  /$$$$$$$ 
| $$  /$$/|_  $$_/| $$__  $$| $$_____/| $$$    /$$$          /$$         |_  $$_/| $$  | $$| $$__  $$ /$$__  $$| $$__  $$
| $$ /$$/   | $$  | $$  \ $$| $$      | $$$$  /$$$$         | $$           | $$  | $$  | $$| $$  \ $$| $$  \ $$| $$  \ $$
| $$$$$/    | $$  | $$  | $$| $$$$$   | $$ $$/$$ $$       /$$$$$$$$        | $$  | $$$$$$$$| $$$$$$$ | $$$$$$$$| $$$$$$$/
| $$  $$    | $$  | $$  | $$| $$__/   | $$  $$$| $$      |__  $$__/        | $$  | $$__  $$| $$__  $$| $$__  $$| $$__  $$
| $$\  $$   | $$  | $$  | $$| $$      | $$\  $ | $$         | $$           | $$  | $$  | $$| $$  \ $$| $$  | $$| $$  \ $$
| $$ \  $$ /$$$$$$| $$$$$$$/| $$$$$$$$| $$ \/  | $$         |__/          /$$$$$$| $$  | $$| $$$$$$$/| $$  | $$| $$  | $$
|__/  \__/|______/|_______/ |________/|__/     |__/                      |______/|__/  |__/|_______/ |__/  |__/|__/  |__/
                                                                                                                                                                                                                                        
             /$$$$$$$$ /$$$$$$  /$$$$$$$$ /$$      /$$ /$$$$$$ /$$   /$$  /$$$$$$  /$$$$$$$$ /$$$$$$                     
            |__  $$__//$$__  $$|_____ $$ | $$$    /$$$|_  $$_/| $$$ | $$ /$$__  $$|__  $$__/|_  $$_/                     
               | $$  | $$  \ $$     /$$/ | $$$$  /$$$$  | $$  | $$$$| $$| $$  \ $$   | $$     | $$                       
               | $$  | $$$$$$$$    /$$/  | $$ $$/$$ $$  | $$  | $$ $$ $$| $$$$$$$$   | $$     | $$                       
               | $$  | $$__  $$   /$$/   | $$  $$$| $$  | $$  | $$  $$$$| $$__  $$   | $$     | $$                       
               | $$  | $$  | $$  /$$/    | $$\  $ | $$  | $$  | $$\  $$$| $$  | $$   | $$     | $$                       
               | $$  | $$  | $$ /$$$$$$$$| $$ \/  | $$ /$$$$$$| $$ \  $$| $$  | $$   | $$    /$$$$$$                     
               |__/  |__/  |__/|________/|__/     |__/|______/|__/  \__/|__/  |__/   |__/   |______/                     
                                                                                                                         
                                       EREN ÖZTÜRK TARAFINDAN KODLANMIŞTIR!                                                                        
                                                                                                                                                                                                  

        """)

input ("ENTER'a basınız!")
system ('cls')

time.sleep (2)

giris = '-'*30 + """

╔═╗╔═╗╔═╗╔═╗╔╗╔╔═╗╦╔═╦  ╔═╗╦═╗
╚═╗║╣ ║  ║╣ ║║║║╣ ╠╩╗║  ║╣ ╠╦╝
╚═╝╚═╝╚═╝╚═╝╝╚╝╚═╝╩ ╩╩═╝╚═╝╩╚═                                                                                       
                                                                                                                 
1-KIDEM TAZMİNATI HESAPLAMA
2-İHBAR TAZMİNATI HESAPLAMA
3-KIDEM + İHBAR TAZMİNATI TOPLAMI
4-ÇIKIŞ

""" + '-'*30

print(giris)


while True:
    secenek = input ("İşleminizi seçiniz:")
    print ('--------------------------')

    if secenek =="4":
        print ("Çıkış yapılıyor...\n"
               + '--------------------------')
        break


    elif secenek == "1":
        Tahsılat.tahsılat(float(input("Net ücretİ Giriniz:")))
        print ('--------------------------')
        system ('cls')
        print ("Aşağıdaki seçeneklerden birini giriniz:\n", giris)

    elif secenek == "2":
        Tahsılat.Ihbar_Tazmınat(float(input("Net ücretİ Giriniz:")))
        print ('--------------------------')
        system ('cls')
        print ("Aşağıdaki seçeneklerden birini giriniz:\n", giris)

    elif secenek == "3":
        Tahsılat.kıd_ıhbar(float(input("Net ücretİ Giriniz:")))
        print ('--------------------------')
        system ('cls')
        print ("Aşağıdaki seçeneklerden birini giriniz:\n", giris)


    else:
        print ("Yanlış bir işlem yaptınız!")
        time.sleep (1)
        print ('--------------------------')
        print ("Aşağıdaki seçeneklerden birini giriniz:\n", giris)

