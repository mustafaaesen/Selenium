# Selenium Çalışmaları – Ekşi Sözlük Otomasyon Örnekleri

Bu repo, Python **Selenium WebDriver** kullanılarak web tarayıcı otomasyonu öğrenme ve pratik yapma sürecinde geliştirilen çalışmaları içermektedir. Çalışmalar, dinamik içerik barındıran gerçek bir web sitesi üzerinde otomasyon ve veri toplama mantığını anlamaya yöneliktir.

---

## Proje Amacı

Bu çalışmanın amacı:
- Selenium WebDriver kullanarak tarayıcıyı programatik olarak kontrol etmek
- Dinamik web sayfalarında element bulma ve veri çekme işlemlerini öğrenmek
- Gerçek bir site üzerinde otomasyon akışı kurmak
- Random bekleme, sayfa gezme ve veri toplama senaryolarını uygulamaktır

Çalışmalar **Ekşi Sözlük** sitesi üzerinde gerçekleştirilmiştir.

---

## Repo Yapısı

Repo içerisinde üç temel Selenium örneği bulunmaktadır:
```
Selenium/
│
├── eksisozluk-1.py
├── eksisozluk-2.py
├── eksisozluk-3.py
└── entry.txt
```

---

## Dosya Açıklamaları

### 1. eksisozluk-1.py  
Bu dosya Selenium ile yapılan ilk deneme çalışmasını içerir.

- Chrome WebDriver başlatılır
- Belirli bir Ekşi Sözlük başlığı tarayıcıda açılır
- Sayfanın yüklenmesi beklenir
- Sayfadaki entry içerikleri CSS Selector kullanılarak alınır
- Entry metinleri terminale yazdırılır

Bu aşamada Selenium’un temel kullanım mantığı, element seçimi ve sayfa etkileşimi öğrenilmiştir.

---

### 2. eksisozluk-2.py  
Bu dosyada otomasyon süreci daha ileri bir seviyeye taşınmıştır.

- Başlığa ait sayfalar rastgele seçilir
- Random sayfa numarası üretilerek farklı sayfalara gidilir
- Her sayfadaki entry içerikleri toplanır
- Toplanan entry’ler bir Python listesinde saklanır
- Süreç belirli bir sayfa sayısına ulaşana kadar devam eder

Bu çalışma ile:
- Random pagination
- Döngü kontrollü veri toplama
- Dinamik içerik üzerinde Selenium kullanımı
pratik edilmiştir.

---

### 3. eksisozluk-3.py  
Bu dosya Selenium otomasyonunun en kapsamlı halidir.

- Tarayıcı tamamen otomatik şekilde yönetilir
- Rastgele sayfalara gidilerek entry’ler toplanır
- Toplamda belirlenen sayıda (örneğin 100 entry) veri elde edilir
- Toplanan tüm entry’ler `entry.txt` dosyasına yazılır
- Süreç sonunda tarayıcı kapatılır

Bu aşamada uçtan uca bir Selenium otomasyon akışı kurulmuştur.

---

## Kullanılan Teknikler

- Selenium WebDriver
- CSS Selector ile element bulma
- Dinamik sayfa bekleme (`time.sleep`)
- Random sayı üretimi
- Döngü kontrollü otomasyon
- TXT dosyasına veri kaydetme

---

## Instagram ve Twitter (X) Denemeleri Hakkında

Aynı Selenium yöntemleri Instagram ve Twitter (X) platformları üzerinde de denenmiştir. Bu denemelerde:

- Bekleme süreleri randomize edilmiştir
- Kullanıcı davranışı insansı şekilde taklit edilmeye çalışılmıştır
- Karakterler tek tek ve farklı süre aralıklarıyla girilmiştir
- Doğrudan link açmak yerine Google üzerinden arama yapılarak siteye girme yöntemi uygulanmıştır

Ancak bu platformlarda uygulanan **agresif login ve bot tespit politikaları** nedeniyle, bu yöntemler yeterince etkili olamamıştır. Özellikle davranışsal analiz ve otomasyon tespit mekanizmaları Selenium tabanlı girişleri engellemiştir.

Bu nedenle çalışmalar, otomasyon açısından daha erişilebilir ve eğitim amaçlı uygun olan Ekşi Sözlük sitesi üzerinde sürdürülmüştür.

---

## Not

Bu repo, Selenium WebDriver kullanımı konusunda pratik kazanmak ve tarayıcı otomasyonunun sınırlarını deneyimlemek amacıyla oluşturulmuştur. Eğitim ve öğrenme odaklıdır.
