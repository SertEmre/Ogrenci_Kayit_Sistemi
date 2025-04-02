#args ve kwargs ile derste yapılan sözlük uygulamasını input ile geliştir
def ögrenci_ekle(**kwargs):
    numara = kwargs.get("ögrenci_numara")
    if numara in ögrenci_bilgileri:
        print("Bu numaraya ait bir ögrenci var")
        return
    
    ögrenci_bilgileri[numara] = kwargs

ögrenci_bilgileri = {}

while True:
    isim = input("Ögrenci Adi:")
    soyisim = input("Ögrenci Soyadi: ")
    numara = input("Ögrenci no: ")
    bölüm = input("Ögrenci Bölümü: ")

    ögrenci_ekle(ad = isim,soyad= soyisim,ögrenci_numara = numara,ögrenci_bölüm = bölüm)
    ekle= input("Yeni öğrenci eklemek ister misiniz?(Evet:E,Hayır:H):").lower()
    if ekle == "h":
        break

print(50*"-")
for numara,bilgiler in ögrenci_bilgileri.items():
    print(f"Okul no:{numara}:{bilgiler['ad']}{bilgiler["soyad"]}")
