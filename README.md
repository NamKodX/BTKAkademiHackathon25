# Ferman - Akıllı Asistan

**Ferman**, Google'ın **Gemini Pro** modelini kullanarak hızlı ve etkili içerikler üreten masaüstü tabanlı bir akıllı asistandır.
Bu uygulama, ürün açıklamaları oluşturmanıza ve YouTube videolarını teknik raporlar şeklinde özetlemenize yardımcı olur.

---

## Özellikler

### Çok Dilli Ürün Açıklaması

* Ürün adı ve temel özellikleri girerek, SEO odaklı ve çok dilli ürün açıklamaları oluşturabilirsiniz.
* Pazarlama için özel dil kalıpları ve ipuçları içerir.

### İleri Seviye Video Analizi

* YouTube video transkriptlerini çeker.
* Basit özetin ötesinde, teknik detaylar, formüller ve ileri düzey bilgiler içeren kapsamlı analizler sunar.

### Kullanımı Kolay Arayüz

* Sade, anlaşılır, iki ana sekmeden oluşan bir kullanıcı arayüzüne sahiptir.

### Çıktı Kaydetme

* Üretilen açıklama veya özetler `.txt` dosyasına kolayca kaydedilebilir.

---

## ⚙️ Kurulum

### 1. Gerekli Kütüphaneler

```bash
pip install -r requirements.txt
```

### 2. Google Gemini API Anahtarı

1. [Google AI Studio](https://makersuite.google.com/app) adresine gidin.
2. “Create API key” butonuna tıklayın.
3. Proje klasörünüzün kök dizininde `.env` adlı bir dosya oluşturun.
4. Aşağıdaki satırı ekleyin:

```env
GOOGLE_API_KEY="AIzaSy...sizin-anahtarınız"
```

### 3. ChromeDriver ve Selenium

YouTube transkriptlerini çekmek için **Selenium** ve **ChromeDriver** kullanılır.

---

## 💻 Kullanım

### 🔸 Uygulamayı Başlatmak

```bash
python main.py
```

### 📟️ Sekme 1: Ürün Açıklaması

1. **Ürün Adı** alanına ürününüzün adını girin.
2. **Ana Özellikler** kısmına her satıra bir özellik yazın.
3. **Açıklama Dili** listesinden dil seçin.
4. “Açıklama Oluştur” butonuna basın.

### 🎮 Sekme 2: YouTube Video Özetleyici

1. **YouTube URL** alanına videonun bağlantısını girin.
2. **Özet Dili** listesinden dil seçin.
3. “Videoyu Özetle” butonuna tıklayın.
4. Oluşturulan özet beğenildiyse, “Sonucu Kaydet” butonu ile `youtube_ozetleri.txt` dosyasına ekleyebilirsiniz.

---

## 🗂️ Dosya Yapısı

```bash
/Ferman
├── gui/
│   └── main_window.py      # Arayüz tasarımını ve bileşenlerini içerir.
├── modules/
│   ├── llm_handler.py      # Gemini API ile içerik üretimini yönetir.
│   └── web_scraper.py      # YouTube transkriptlerini çeken Selenium yapısı.
├── config/
│   └── settings.py         # API anahtarlarını ve ortam değişkenlerini yönetir.
├── .env                    # Google Gemini API anahtarınızı içerir.
├── main.py                 # Uygulamanın giriş noktası.
├── README.md               # Proje tanıtımı ve kullanım kılavuzu.
└── requirements.txt        # Gerekli tüm kütüphaneler listelenir.
```
---

## 📌 Lisans

Bu proje Apache2.0 Lisansı ile lisanslanmıştır.

---

**Fermân ile üretkenliğinizi artırın, içeriklerinizi zeka ile güçlendirin.**
💬 Sorularınız için: namik.can@hotmail.com
