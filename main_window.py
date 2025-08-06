# Kütüphaneler
import tkinter as tk
from tkinter import ttk, scrolledtext

# Bu py dosyası genel olarak tasarımla alakalı dosyadır.

# Ana Pencere ve ayarlamalar
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ferman")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True, fill="both")

        # Ürün Açıklaması Sekmesi
        self.description_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.description_frame, text="Ürün Açıklaması")
        self.setup_description_frame()

        # Video Özetleyici Sekmesi
        self.summarizer_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.summarizer_frame, text="Video Özetleyici")
        self.setup_summarizer_frame()

    # ürün Açıklama Sekmesi
    def setup_description_frame(self):
        description_label = ttk.Label(self.description_frame, text="AI Destekli Otomatik Ürün Açıklaması Üretici:")
        description_label.pack(padx=10, pady=(10, 0), anchor="center")

        name_label = ttk.Label(self.description_frame, text="Ürün Adı:")
        name_label.pack(padx=10, pady=(10, 0), anchor="center")
        self.name_entry = ttk.Entry(self.description_frame, width=80)
        self.name_entry.pack(padx=10, pady=(0, 10), fill="x")

        features_label = ttk.Label(self.description_frame, text="Ürünün ana özelliklerini her satıra bir özellik gelecek şekilde belirtiniz:")
        features_label.pack(padx=10, pady=(10, 0), anchor="center")
        self.features_text = scrolledtext.ScrolledText(self.description_frame, wrap=tk.WORD, width=75, height=5)
        self.features_text.pack(padx=10, pady=(0, 10), expand=True, fill="x")

        # Dil Seçeneği Ekleme Bölümü
        lang_label = ttk.Label(self.description_frame, text="Açıklama Dili:")
        lang_label.pack(padx=10, pady=(10, 0), anchor="w")

        self.language_options_desc = ["Türkçe", "English", "Deutsch", "Español", "Français"]
        self.selected_language_desc = tk.StringVar(value=self.language_options_desc[0])

        self.language_menu_desc = ttk.Combobox(self.description_frame,
                                               textvariable=self.selected_language_desc,
                                               values=self.language_options_desc,
                                               state="readonly")
        self.language_menu_desc.pack(padx=10, pady=(0, 10), fill="x")

        self.generate_button = ttk.Button(self.description_frame, text="Açıklama Oluştur")
        self.generate_button.pack(padx=10, pady=5)

        result_label = ttk.Label(self.description_frame, text="AI Tarafından Oluşturulan Açıklama:")
        result_label.pack(padx=10, pady=(10, 0), anchor="center")
        self.description_result_text = scrolledtext.ScrolledText(self.description_frame, wrap=tk.WORD, width=75,
                                                                 height=15)
        self.description_result_text.pack(padx=10, pady=10, expand=True, fill="both")

    # Vİdeo Özetleyici Sekmesi
    def setup_summarizer_frame(self):
        description_label = ttk.Label(self.summarizer_frame, text="AI Destekli Video Anlatım Özetleyici:")
        description_label.pack(padx=10, pady=(10, 0), anchor="center")

        url_label = ttk.Label(self.summarizer_frame, text="YouTube URL'si:")
        url_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.youtube_url_entry = ttk.Entry(self.summarizer_frame, width=80)
        self.youtube_url_entry.pack(padx=10, pady=(0, 10), fill="x")

        # Dil Seçeneği Ekleme
        lang_label = ttk.Label(self.summarizer_frame, text="Özet Dili:")
        lang_label.pack(padx=10, pady=(10, 0), anchor="w")

        self.language_options = ["Türkçe", "English", "Deutsch", "Español", "Français"]
        self.selected_language = tk.StringVar(value=self.language_options[0])

        self.language_menu = ttk.Combobox(self.summarizer_frame,
                                          textvariable=self.selected_language,
                                          values=self.language_options,
                                          state="readonly")
        self.language_menu.pack(padx=10, pady=(0, 10), fill="x")

        self.summarize_button = ttk.Button(self.summarizer_frame, text="Videoyu Özetle")
        self.summarize_button.pack(padx=10, pady=5)

        result_label = ttk.Label(self.summarizer_frame, text="Özet Sonuçları:")
        result_label.pack(padx=10, pady=(10, 0), anchor="center")
        self.summarizer_result_text = scrolledtext.ScrolledText(self.summarizer_frame, wrap=tk.WORD, width=75,
                                                                height=15)
        self.summarizer_result_text.pack(padx=10, pady=10, expand=True, fill="both")

        self.save_button = ttk.Button(self.summarizer_frame, text="Sonucu Kaydet")
        self.save_button.pack(padx=10, pady=5)