
class Tır:
    def __init__(self):
        # CSV dosyasının adı
        self.dosya = "olaylar.csv"
        # Tır verilerini içeren sözlük
        self.tırSozlugu = {} 
        # Tır plakalarını içeren liste
        self.tırPlakaListesi = [] 
        # Tır yük miktarlarını içeren liste
        self.tırYukListesi = [] 
        # Tır geliş zamanlarını içeren liste
        self.tırZamanListesi = [] 
        # Tır ülkelerini içeren liste
        self.tırUlkeListesi = [] 
        # Tır verilerini oku ve listeleri oluştur
        self.tır_sozlugu()         
        self.tır_plaka_listesi()
        self.tır_yuk_listesi()   
        self.tır_zaman_listesi()
        self.tırUlkeListesiOlustur()

    def tır_sozlugu(self):
        self.tırSozlugu = []  # Sözlüğü liste olarak oluşturalım

        # CSV dosyasını aç ve verileri oku
        with open(self.dosya, "r") as dosya:
            satirlar = dosya.readlines()
            
            # İlk satır başlıkları içeriyorsa, başlıkları atla
            if satirlar:
                basliklar = satirlar[0].strip().split(",")
                satirlar = satirlar[1:]

                for satir in satirlar:
                    satir = satir.strip().split(",")
                    tır_verisi = dict(zip(basliklar, satir))
                    self.tırSozlugu.append(tır_verisi)

                # Verileri geliş zamanına göre sırala
                self.tırSozlugu = sorted(self.tırSozlugu, key=lambda x: x['geliş_zamanı'])

    def tır_yuk_listesi(self):  
        # Tır verilerinden yük miktarlarını çıkar ve listeye ekle
        for i in self.tırSozlugu:
            self.tırYukListesi.append(int(i["yük_miktarı"]))

    def tırUlkeListesiOlustur(self): 
        # Tır verilerinden ülkeleri çıkar ve listeye ekle
        for i in self.tırSozlugu:
            self.tırUlkeListesi.append(i["ülke"])

    def tır_plaka_listesi(self): 
        # Tır verilerinden plakaları çıkar ve son 3 karakterini listeye ekle
        for i in self.tırSozlugu:
            plaka = i["tır_plakası"]
            plakaNumarası = plaka[-3:]
            self.tırPlakaListesi.append(plakaNumarası)
    
    def tır_zaman_listesi(self):  
        # Tır verilerinden geliş zamanlarını çıkar ve sırala
        for i in self.tırSozlugu:
            self.tırZamanListesi.append(int(i["geliş_zamanı"]))
        self.tırZamanListesi.sort()

class Gemi:
    def __init__(self):
        # CSV dosyasının adı
        self.dosya = "gemiler.csv"
        # Gemi verilerini içeren sözlük
        self.sıralıSozluk = {} 
        # Gemi adlarını içeren liste
        self.gemiAdıListesi = [] 
        # Gemi kapasitelerini içeren liste
        self.gemiKapasiteListesi = [] 
        # Gemi yük miktarlarını içeren liste
        self.gemiYukListesi = [] 
        # Gemi verilerini oku ve listeleri oluştur
        self.gemi_adı_listesi() 
        self.gemi_sozlugu()
        self.gemi_kapasite_listesi()
        self.gemiDurumu()

    def gemi_sozlugu(self):     
        # CSV dosyasını aç ve verileri bir sözlüğe dönüştür
        self.sıralıSozluk = [] 

        with open(self.dosya, "r") as dosya:
            satirlar = dosya.readlines()

            # İlk satır başlıkları içeriyorsa, başlıkları atla
            if satirlar:
                basliklar = satirlar[0].strip().split(",")
                satirlar = satirlar[1:]

                for satir in satirlar:
                    satir = satir.strip().split(",")
                    gemi_verisi = dict(zip(basliklar, satir))
                    self.sıralıSozluk.append(gemi_verisi)

                self.sıralıSozluk = sorted(self.sıralıSozluk, key=lambda x: x['gemi_adı'])


    def gemi_kapasite_listesi(self):  
        # Gemi verilerinden kapasiteleri çıkar ve listeye ekle
        for i in self.sıralıSozluk:
            self.gemiKapasiteListesi.append(int(i["kapasite"]))
         
    def gemi_adı_listesi(self):      
        # 1'den 450'ye kadar olan gemi adlarını oluştur
        for i in range(1, 451):
            self.gemiAdıListesi.append(str(i))
        
        # Gemi adlarını 3 karakterli hale getir
        for index, value in enumerate(self.gemiAdıListesi):
            if len(value) == 1:
                self.gemiAdıListesi[index] = f"00{value}"
            elif len(value) == 2:
                self.gemiAdıListesi[index] = f"0{value}"

    def gemiYukListesiAl(self, ad):   
        # Belirli bir geminin yük kapasitesini al
        for i in self.sıralıSozluk:
            if ad == i["gemi_adı"]:
                return int(int(i["kapasite"]) * 95 / 100)

    def gemiKapasiteAl(self, ad):    
        # Belirli bir geminin kapasitesini al
        for i in self.sıralıSozluk:
            if ad == i["gemi_adı"]:
                return int(i["kapasite"])
    
    def gemiZamanAl(self, ad):    
        # Belirli bir geminin geliş zamanını al
        for i in self.sıralıSozluk:
            if ad == i["gemi_adı"]:
                return int(i["geliş_zamanı"])

    def gemiUlkeAl(self, ad): 
        # Belirli bir geminin gideceği ülkeyi al
        for i in self.sıralıSozluk:
            if ad == i["gemi_adı"]:
                return i["gidecek_ülke"]
    
    def gemiDurumu(self):  
        # Gemi kapasitelerinin %95'ini al ve liste oluştur
        for i in self.gemiKapasiteListesi:
            self.gemiYukListesi.append(int(i) * 95 / 100)
        return self.gemiYukListesi

class Stack:
    def __init__(self):
        # Yığın elemanlarını içeren liste
        self._elemanlar = list() 

    def bosmu(self):  
        # Yığın boş mu kontrolü
        return len(self) == 0

    def __len__(self):  
        # Yığın eleman sayısı
        return len(self._elemanlar)

    def enust(self): 
        # Yığının en üstündeki elemanı alma
        assert not self.bosmu(), "Boş."
        return self._elemanlar[-1]

    def cikar(self):  
        # Yığından eleman çıkarma
        assert not self.bosmu(), "Boş"
        return self._elemanlar.pop()

    def ekle(self, eleman): 
        # Yığına eleman ekleme
        self._elemanlar.append(eleman)

    def __str__(self):  
        # Yığını string olarak temsil etme
        return str(self._elemanlar)
     
class Liman:    
    def __init__(self):
        # Gemi ve Tır sınıflarını içeren nesneler
        self.gemi = Gemi()  
        self.tır = Tır()    
        # Limandaki istif alanlarını içeren yığınlar
        self.istifAlani = Stack()   
        self.istifAlani2 = Stack()  

    def indirYukle(self): 
        # Gemi ve Tır verilerini kullanarak yükleme ve boşaltma işlemlerini simüle et
        for indeksGemi, gemiAdı in enumerate(self.gemi.gemiAdıListesi): 
            gemiYuk = 0  # Başlangıçta geminin yük miktarını sıfırla
            for indeksTır, tırPlaka in enumerate(self.tır.tırPlakaListesi):
                # Eğer geminin zamanı tırdan daha azsa ve gemi ile tır aynı ülkeden ise
                if self.gemi.gemiZamanAl(gemiAdı) < self.tır.tırZamanListesi[indeksTır]: 
                    if self.gemi.gemiUlkeAl(gemiAdı) == self.tır.tırUlkeListesi[indeksTır]: 
                        gemiYuk += self.tır.tırYukListesi[indeksTır]  # Tırın yükünü gemiye ekle
                        # Eğer gemi yükü, geminin kapasitesine yaklaşıyorsa
                        if gemiYuk > self.gemi.gemiYukListesi[indeksGemi] - 10: 
                            # Gemi tam yüklendiğinde bilgi mesajı yazdır ve döngüden çık
                            print(f"{self.gemi.gemiZamanAl(gemiAdı)} zamanında gelen {gemiAdı} gemisi {gemiYuk} yükü ile {self.gemi.gemiUlkeAl(gemiAdı)} ülkesine yola çıkmıştır.")
                            break
                    else:
                        # Eğer gemi ve tır farklı ülkelerden ise ve istif alanı dolu değilse
                        if len(self.istifAlani) < 22: 
                            # Tırı ilk istif alanına ekle
                            self.istifAlani.ekle((tırPlaka, self.tır.tırUlkeListesi[indeksTır], self.tır.tırYukListesi[indeksTır])) 
                        else:
                            # Eğer ilk istif alanı doluysa ve üstteki tır gemiyle aynı ülkeden değilse
                            while not self.istifAlani.bosmu() and self.istifAlani.enust()[1] != self.gemi.gemiUlkeAl(gemiAdı):
                                # Tırları ikinci istif alanına aktar
                                self.istifAlani2.ekle(self.istifAlani.cikar()) 
                                # Eğer ikinci istif alanında gemi ülkesine uygun tır varsa
                                if not self.istifAlani.bosmu() and self.istifAlani.enust()[1] == self.gemi.gemiUlkeAl(gemiAdı):
                                    # Gemi ülkesine uygun tırın yükünü gemiye ekle
                                    gemiYuk += self.istifAlani.cikar()[2]

# Liman nesnesi oluştur ve yükleme işlemini başlat
liman = Liman()
liman.indirYukle()
