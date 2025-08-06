# Kütüphane Yükleme
import os
from dotenv import load_dotenv

# settings.py dizini
current_dir = os.path.dirname(os.path.abspath(__file__))

# Üst dizine gitme
project_root = os.path.join(current_dir, "..")

# .env dosyasının yolunu oluşturarak oradan api key yapısını almak
dotenv_path = os.path.join(project_root, '.env')

# .env dosyasını tam yolu ile yükle
load_dotenv(dotenv_path)

# Ortam değişkenini okuyup içeri alma işlemi.
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Eğer key none dönerse uyarı yapısı
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY bulunamadı. Lütfen .env dosyasını kontrol edin.")