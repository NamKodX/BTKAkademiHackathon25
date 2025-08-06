Ferman - Akıllı Asistan
Ferman, Google'ın Gemini Pro modelini kullanarak hızlı ve etkili içerikler üreten, masaüstü tabanlı bir akıllı asistandır. Uygulama, ürün açıklamaları oluşturmanıza ve YouTube videolarını detaylı teknik raporlar halinde özetlemenize yardımcı olur.

Özellikler
Çok Dilli Ürün Açıklaması: Ürün adı ve özelliklerini girerek SEO odaklı, istediğiniz dilde ürün açıklamaları ve pazarlama püf noktaları oluşturabilirsiniz.

İleri Seviye Video Analizi: YouTube video transkriptlerini çekerek, basit bir özetin ötesinde; teknik detaylar, formüller ve ileri seviye bilgiler içeren kapsamlı raporlar elde edebilirsiniz.

Kullanımı Kolay Arayüz: İki ana sekmeden oluşan sade ve anlaşılır bir arayüze sahiptir.

Çıktı Kaydetme: Oluşturulan özetleri tek bir metin dosyasına kolayca kaydedebilirsiniz.

Kurulum
Ferman uygulamasını çalıştırmak için gerekli adımlar aşağıda sıralanmıştır.

1. Gerekli Kütüphaneler

Projeyi çalıştırmadan önce, requirements.txt dosyasındaki kütüphaneleri kurmanız gerekir.

Bash
pip install -r requirements.txt
2. Google Gemini API Anahtarı

Uygulama, içerik üretimi için Google'ın Gemini API'sini kullanır. Bir API anahtarı edinmek için şu adımları izleyin:

Google AI Studio adresine gidin.

"Create API key" butonuna tıklayarak yeni bir anahtar oluşturun.

Projenizin kök dizininde .env adında yeni bir dosya oluşturun.

Oluşturduğunuz anahtarı aşağıdaki gibi .env dosyasına ekleyin:

GOOGLE_API_KEY="AIzaSy...sizin-anahtarınız"
3. ChromeDriver Kurulumu

YouTube transkriptlerini çekmek için Selenium WebDriver ve ChromeDriver gereklidir. Proje, webdriver-manager kütüphanesi sayesinde bu sürücüyü otomatik olarak kurar. Ek bir işlem yapmanıza gerek yoktur.

Kullanım
Kurulumu tamamladıktan sonra, projenin ana dizininde bulunan main.py dosyasını çalıştırın.

Bash
python main.py
Sekme 1: Ürün Açıklaması

Ürün Adı alanına ürününüzün adını girin.

Ana Özellikleri alanına, her satıra bir özellik gelecek şekilde ana özellikleri yazın.

Açıklama Dili menüsünden istediğiniz dili seçin.

Açıklama Oluştur butonuna tıklayarak açıklamayı oluşturun.

Sekme 2: Video Özetleyici

YouTube URL'si alanına özetlemek istediğiniz videonun bağlantısını yapıştırın.

Özet Dili menüsünden özetin hangi dilde oluşturulacağını seçin.

Videoyu Özetle butonuna tıklayarak transkriptin çekilmesini ve analiz edilmesini başlatın.

Oluşturulan özeti beğenirseniz, Sonucu Kaydet butonu ile youtube_ozetleri.txt dosyasına ekleyebilirsiniz.

Dosya Yapısı
Projenin temiz ve modüler bir yapıda olması için dosya yapısı aşağıdaki gibi düzenlenmiştir:

/Ferman
├── gui/
│   └── main_window.py      # Arayüz tasarımını ve bileşenlerini içerir.
├── modules/
│   ├── llm_handler.py      # Gemini API ile iletişim kurarak içerik üretir.
│   └── web_scraper.py      # Selenium ile YouTube transkriptlerini çeker.
├── config/
│   └── settings.py         # Çevre değişkenlerini yönetir.
├── .env                    # Gemini API anahtarını saklar.
├── main.py                 # Ana uygulama mantığı ve GUI'yi çalıştırır.
├── README.md               # Proje tanıtımı ve kullanım kılavuzu.
└── requirements.txt        # Proje için gerekli kütüphaneleri listeler.
