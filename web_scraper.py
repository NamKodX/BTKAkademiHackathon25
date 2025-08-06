# Kütüphaneler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Videodaki metnin transkripti adına youtube apisini kullanamama sebebim her videoda işe yaramaması oldu.
# Bunun adına en uygun çözüm olarak seleniumdaki tecrübeme dayanarak buna uygun özetleme sitesi buldum ve bu noktada selenium yapısını ve gücü ile
# beraber sitedeki oluşturulan özeti canlı botlar ile beraber alıp bunu çeşitli dillerle özetleyip detaylandırabildim.
def get_youtube_transcript(youtube_url):

    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Transkript çekme için site
    transcribe_site_url = "https://youtubetotranscript.com/"

    print(f"{transcribe_site_url} sitesine bağlanılıyor...")
    driver.get(transcribe_site_url)

    try:
        # YouTube URL giriş kutusu xpath üzerinden bağlantı
        url_input_xpath = '//*[@id="hero"]/div/div/form/input'
        url_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, url_input_xpath))
        )
        # Enter tuşuna basarak butonu aktif etme
        url_input.send_keys(youtube_url)
        url_input.send_keys(Keys.ENTER)

        # Transkriptin hazır olması biraz uzun sürdüğünden burada bekleme yarattım.
        title_xpath = '//*[@id="app"]/article/div/div/h1'
        video_title_element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, title_xpath))
        )
        video_title = video_title_element.text

        # Yine video başlığını siteden çektim.
        print(f"Video başlığı bulundu: {video_title}")

        # Transkript metninin bulunduğu elementin xpathini referans aldım
        transcript_container_xpath = '//*[@id="transcript"]'
        transcript_container = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, transcript_container_xpath))
        )

        # Transkriptin içerisindeki tüm p etiketlerini bulup metinlerini birleştirme işlemi yaptım.
        transcript_elements = transcript_container.find_elements(By.TAG_NAME, "p")
        transcript = " ".join([p.text for p in transcript_elements])

        # Bulunmama durumlarında hata yönetimi yapılarıyla daha güvenli kod oluşturdum.
        if not transcript:
            raise Exception("Transkript metni bulunamadı.")

        print("Transkript başarıyla çekildi.")

        return {"title": video_title, "transcript": transcript}

    except Exception as e:
        print(f"Transkript çekme sırasında bir hata oluştu: {e}")
        return {"title": None, "transcript": None}

    finally:
        driver.quit()