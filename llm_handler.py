# Kütüphaneler
import google.generativeai as genai
from config.settings import GOOGLE_API_KEY

# Gemini API anahtarını yapılandırma
genai.configure(api_key=GOOGLE_API_KEY)

# Gemini modelini oluşturma
model = genai.GenerativeModel('gemini-1.5-flash')

# Ürün açıklama bölümü yapısı
def generate_product_content(product_name, features, target_language):
    """
    Ürün adı ve özelliklerine göre belirtilen dilde SEO odaklı bir açıklama ve pazarlama püf noktaları oluşturur.
    """
    features_list = "\n".join([f"- {f}" for f in features])

    # Prompt yapısına dil bilgisi ekleyip kendi projemize göre uyarlayalım.
    text_prompt = f"""
    Sen, SEO ve pazarlama konularında uzman bir yazarsın. Aşağıdaki ürün adı ve özelliklerine göre, e-ticaret siteleri için SEO odaklı, ikna edici ve madde işaretleri içeren bir ürün açıklaması yaz. Açıklama, müşterinin ürünü satın alması için gerekli tüm bilgileri içermeli. Ayrıca, bu ürünü pazarlarken dikkat edilmesi gereken 5 ten çok adet "püf nokta" ekle.

    Tüm bu metni **{target_language}** dilinde oluştur.

    Ürün Adı: {product_name}
    Ana Özellikleri:
    {features_list}
    """

    print(f"Gemini'den {target_language} dilinde ürün içeriği talep ediliyor...")

    try:
        text_response = model.generate_content(text_prompt)
        return text_response.text
    except Exception as e:
        return f"Hata: Gemini API isteği sırasında bir sorun oluştu: {e}"

# Vİdeo özetleme yapısı
def summarize_transcript(video_title, transcript, target_language):
    """
    Video transkriptini alarak onu istenilen dilde özetleyip detaylandırıyor.
    """
    prompt = f"""
    Sen, karmaşık teknik bilgileri analiz edebilen bir uzmansın. Aşağıdaki video transkriptini inceleyerek ileri seviye bir raporu **{target_language}** dilinde hazırla.

    Raporda şu kısımlar olmalı:

    ### 1. Detaylı Özet ve Ana Fikirler
    - Videoda anlatılan ana konuyu, en önemli 10 maddelik liste halinde özetle.
    - Her maddeyi, videodan edindiğin bilgileri genişleterek ve teknik terimlerle destekleyerek daha somut hale getir.
    - Video eğer çok teknik bir yapıda ise daha teknik şekilde sonuç ver video izlemeden video yapandan daha uzman bilgiye sahip olalım.
    ### 2. Formüller, Denklemler ve Teknik Detaylar
    - Videoda geçen anahtar formülleri, denklemleri veya teknik spesifikasyonları listele.
    - Eğer videoda formül geçmiyorsa, konunun temel prensiplerini açıklayan formülleri kendin ekle.
    - Örneğin, bir fizik videosuysa F=ma, bir finans videosuysa bileşik faiz formülü gibi.

    ### 3. Konunun Derinleştirilmesi ve İleri Seviye Bilgiler
    - Video içeriğini temel alarak, bahsedilen konunun havada kalan veya yüzeysel kalan kısımlarını teknik bilgilerle doldur.
    - Örneğin, "algoritmanın temelini anlattı ama karmaşıklığını ve farklı türlerini yüzeysel geçti." gibi bir durumda, sen bu boşlukları doldur.
    - Bu konunun pratiğe nasıl uygulanabileceğine dair ileri seviye ek bilgiler veya örnekler sun.

    ### 4. Sonuç ve Öneriler
    - Videodaki bilgilerin genel bir değerlendirmesini yap.
    - İzleyicinin bu konuyu daha iyi anlaması için neler yapması gerektiğine dair somut öneriler sun (örneğin, "şu kavramı araştırın", "şu araçları kullanın" gibi).

    Video Başlığı: {video_title}
    Transkript:
    {transcript}
    """

    print(f"Gemini'den {target_language} dilinde teknik analiz talep ediliyor.")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Gemini API isteği sırasında bir hata oluştu: {e}"

if __name__ == '__main__':
    # Test için örnekler
    product_content = generate_product_content(
        product_name="Minimalist Deri Cüzdan",
        features=["Hakiki deri", "6 kart bölmesi", "İnce tasarım"]
    )
    print("--- ÜRÜN İÇERİĞİ ---\n", product_content)

    test_transcript = "bu videoda python programlama dilini öğreneceğiz. python basit bir dil olduğu için yeni başlayanlar için uygundur. ilk olarak değişkenleri ele alacağız..."
    summary = summarize_transcript("Python'a Giriş", test_transcript)
    print("\n--- VİDEO ÖZETİ ---\n", summary)