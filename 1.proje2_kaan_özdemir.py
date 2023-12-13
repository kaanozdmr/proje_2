# Tir sınıfını tanımlıyoruz. Bu sınıf, TIR'ları temsil eder.
class Tir:
    def __init__(self, gelis_zamani, tir_plakasi, ulke, ton_20_adet, ton_30_adet, yuk_miktari, maliyet):
        # TIR nesnesinin özelliklerini başlatıyoruz.
        self.gelis_zamani = gelis_zamani
        self.tir_plakasi = tir_plakasi
        self.ulke = ulke
        self.ton_20_adet = int(ton_20_adet)
        self.ton_30_adet = int(ton_30_adet)
        self.yuk_miktari = int(yuk_miktari)
        self.maliyet = int(maliyet)

# Gemi sınıfını tanımlıyoruz. Bu sınıf, gemileri temsil eder.
class Gemi:
    def __init__(self, gelis_zamani, gemi_adi, kapasite, gidecek_ulke):
        # Gemi nesnesinin özelliklerini başlatıyoruz.
        self.gelis_zamani = gelis_zamani
        self.gemi_adi = gemi_adi
        self.kapasite = int(kapasite)
        self.gidecek_ulke = gidecek_ulke
        self.yuk_miktari = 0

# Liman sınıfını tanımlıyoruz. Bu sınıf, limanı ve limandaki işlemleri temsil eder.
class Liman:
    def __init__(self):
        # Depolama alanlarını ve kapasite sınırlarını başlatıyoruz.
        self.istif_alani_1 = {"Mordor": 0, "Neverland": 0, "Lilliputa": 0, "Oceania": 0}
        self.istif_alani_2 = {"Mordor": 0, "Neverland": 0, "Lilliputa": 0, "Oceania": 0}
        self.istif_alani_kapasite = 750
        self.doluluk_orani_limit = 100

    def istiflanına_yükle(self, ulke, yuk_miktari):
        # Yük miktarını uygunluk durumuna göre depolama alanına ekliyoruz.
        if sum(self.istif_alani_1.values()) + yuk_miktari <= self.istif_alani_kapasite:
            self.istif_alani_1[ulke] += yuk_miktari
        elif sum(self.istif_alani_2.values()) + yuk_miktari <= self.istif_alani_kapasite:
            self.istif_alani_2[ulke] += yuk_miktari
        else:
            print(f"Her iki istif alanı da dolu! Kalan yük aktarılamıyor: {ulke}")

    def hesaplama_yazdır(self, gelis_zamani, t_anındaki_tırlar, t_anındaki_gemiler):
        # Kamyonlar, gemiler ve depolama alanlarıyla ilgili bilgileri yazdırıyoruz.
        print(f"Geliş Zamanı {gelis_zamani}")

        # Tırları ve gemileri sıralı bir şekilde yazdırıyoruz.
        t_anındaki_tırlar.sort(key=lambda x: x.tir_plakasi)
        t_anındaki_gemiler.sort(key=lambda x: x.gemi_adi)

        # Tırları işliyor ve depolama alanına yüklüyoruz.
        for tir in t_anındaki_tırlar:
            print(f"Gelen TIR: {tir.tir_plakasi} - Gideceği Ülke: {tir.ulke} - Yük Miktarı: {tir.yuk_miktari} ton - Maliyet: {tir.maliyet} TL")
            self.istiflanına_yükle(tir.ulke, tir.yuk_miktari)

        # Gemileri işliyoruz.
        for gemi in t_anındaki_gemiler:
            print(f"Gelen Gemi: {gemi.gemi_adi} - Gideceği Ülke: {gemi.gidecek_ulke} - Kapasite: {gemi.kapasite}")

        # Depolama alanı bilgilerini hesaplayıp yazdırıyoruz.
        doluluk_orani_1 = (sum(self.istif_alani_1.values()) / self.istif_alani_kapasite) * 100
        doluluk_orani_2 = (sum(self.istif_alani_2.values()) / self.istif_alani_kapasite) * 100

        # İlk depolama alanı için bilgileri kontrol edip yazdırıyoruz.
        if doluluk_orani_1 <= self.doluluk_orani_limit:
            print(f"İstif Alanı 1 Bilgileri - Zaman {gelis_zamani} İstif Alanı 1 Doluluk Oranı: {doluluk_orani_1:.2f}% - Yük Miktarı: {sum(self.istif_alani_1.values())}")
        else:
            print(f"İstif Alanı 1 Dolu!")

        # İkinci depolama alanı için bilgileri kontrol edip yazdırıyoruz.
        if doluluk_orani_2 <= self.doluluk_orani_limit:
            print(f"İstif Alanı 2 Bilgileri - Zaman {gelis_zamani} İstif Alanı 2 Doluluk Oranı: {doluluk_orani_2:.2f}% - Yük Miktarı: {sum(self.istif_alani_2.values())}")
        else:
            print(f"İstif Alanı 2 Dolu!")

        # Her ülke için toplam yükü yazdırıyoruz.
        toplam_yukler = {ulke: self.istif_alani_1[ulke] + self.istif_alani_2[ulke] for ulke in self.istif_alani_1}
        print(f"Ülkelere gidecek yüklerin toplam yükler {', '.join([f'{ulke}: {yuk} ton' for ulke, yuk in toplam_yukler.items()])}")
        print("==============")

    def grupla_sırala(self, tir_listesi, gemi_listesi):
        # Tırların ve gemilerin varış zamanlarını gruplayıp sıralı bir şekilde döndürüyoruz.
        gelis_zamani_gruplari = set()

        for tir in tir_listesi:
            gelis_zamani_gruplari.add(tir.gelis_zamani)
        for gemi in gemi_listesi:
            gelis_zamani_gruplari.add(gemi.gelis_zamani)

        return sorted(gelis_zamani_gruplari, key=lambda x: int(x))

    def t_anındaki_veriler(self, gelis_zamani, tir_listesi, gemi_listesi):
        # Belirli bir zamandaki TIR'ları ve gemileri getiriyoruz.
        t_anındaki_tırlar = [t for t in tir_listesi if t.gelis_zamani == gelis_zamani]
        t_anındaki_gemiler = [g for g in gemi_listesi if g.gelis_zamani == gelis_zamani]

        return t_anındaki_tırlar, t_anındaki_gemiler

    def liman_simulasyon(self, gemiler_dosya, olaylar_dosya):
        # Gemi ve TIR verilerini içeren dosyalardan veri okuyarak liman faaliyetlerini simüle ediyoruz.
        tir_listesi = []  # TIR nesnelerini saklamak için boş bir liste oluşturulur.
        gemi_listesi = []  # Gemi nesnelerini saklamak için boş bir liste oluşturulur.

        # Olaylar dosyasından TIR verilerini okuyoruz ve TIR nesnelerini oluşturuyoruz.
        olay_verileri = self.dosya_veri_oku(olaylar_dosya)
        for gelis_zamani, (tir_plakasi, ulke, ton_20_adet, ton_30_adet, yuk_miktari, maliyet) in olay_verileri:
            tir = Tir(gelis_zamani, tir_plakasi, ulke, ton_20_adet, ton_30_adet, yuk_miktari, maliyet)
            tir_listesi.append(tir)  # Oluşturulan TIR nesnesi listeye eklenir.

        # Gemiler dosyasından gemi verilerini okuyoruz ve gemi nesnelerini oluşturuyoruz.
        gemi_verileri = self.dosya_veri_oku(gemiler_dosya)
        for gelis_zamani, (gemi_adi, kapasite, gidecek_ulke) in gemi_verileri:
            gemi = Gemi(gelis_zamani, gemi_adi, kapasite, gidecek_ulke)
            gemi_listesi.append(gemi)  # Oluşturulan gemi nesnesi listeye eklenir.

        # TIR ve gemilerin varış zamanlarını gruplayarak sıralıyoruz.
        sirali_gelis_zamanlari = self.grupla_sırala(tir_listesi, gemi_listesi)

        # Her bir zaman grubu için liman faaliyetlerini simüle ediyoruz.
        for gelis_zamani in sirali_gelis_zamanlari:
            t_anındaki_tırlar, t_anındaki_gemiler = self.t_anındaki_veriler(gelis_zamani, tir_listesi, gemi_listesi)
            # Eğer belirli bir zaman diliminde TIR veya gemi varsa, ilgili hesaplamaları yapıyoruz.
            if t_anındaki_tırlar or t_anındaki_gemiler:
                self.hesaplama_yazdır(gelis_zamani, t_anındaki_tırlar, t_anındaki_gemiler)

    def dosya_veri_oku(self, dosya_adi):
        # Dosya adı verilen dosyadan verileri okur ve bir demet listesi olarak döndürür.
        veri_listesi = []  # Verileri saklamak için boş bir liste oluşturulur.
        with open(dosya_adi, 'r', encoding='windows-1254') as dosya:  # Dosya, belirtilen kodlama ile açılır.
            satirlar = dosya.readlines()  # Dosyanın tüm satırları okunur.
            for satir in satirlar[1:]:  # İlk satır (genellikle başlık) hariç her satır için döngü yapılır.
                satir = satir.strip().split(',')  # Her satır virgülle ayrılır ve boşluklar temizlenir.
                gelis_zamani = satir[0]  # İlk öğe zaman damgası olarak alınır.
                veri = tuple(satir[1:])  # Kalan öğeler bir demet olarak alınır.
                if veri:  # Eğer demet boş değilse,
                    veri_listesi.append((gelis_zamani, veri))  # Zaman damgası ve veri demeti listeye eklenir.
        return veri_listesi  # Oluşturulan demet listesi döndürülür.


# Liman faaliyetlerini simüle et
liman = Liman()
liman.liman_simulasyon("gemiler.csv", "olaylar.csv")
