# Kütüphaneler
import sys
import os
import threading
import tkinter as tk
from tkinter import messagebox
from gui.main_window import MainWindow
from modules.llm_handler import generate_product_content, summarize_transcript
from modules.web_scraper import get_youtube_transcript

# Proje kök dizin ekleme
project_root = os.path.dirname(os.path.abspath(__file__))
if project_root not in sys.path:
    sys.path.append(project_root)

class FermanApp:
    def __init__(self):
        self.app = MainWindow()

        # Ürün Açıklaması sekmesi için komutları atama
        self.app.generate_button.config(command=self.start_content_generation_thread)

        # Video Özetleyici sekmesi için komutları atama
        self.app.summarize_button.config(command=self.start_summarize_thread)
        self.app.save_button.config(command=self.save_summary)

    def run(self):
        self.app.mainloop()

    #  Ürün açıklama kısmı
    def start_content_generation_thread(self):
        product_name = self.app.name_entry.get().strip()
        features_text = self.app.features_text.get("1.0", tk.END).strip()
        features = [f.strip() for f in features_text.split('\n') if f.strip()]

        if not product_name or not features:
            messagebox.showwarning("Uyarı", "Lütfen ürün adı ve en az bir özellik girin.")
            return

        thread = threading.Thread(target=self.run_content_generation, args=(product_name, features))
        thread.start()


    def run_content_generation(self, product_name, features):
        self.app.description_result_text.delete("1.0", tk.END)
        self.app.description_result_text.insert(tk.END, "İçerik oluşturuluyor.\nLütfen bekleyin.")
        self.app.description_result_text.config(state=tk.DISABLED)
        self.app.generate_button.config(state=tk.DISABLED)

        try:
            # Arayüzden seçilen dili al
            target_language = self.app.selected_language_desc.get()

            # Gemini ile içerik oluşturma
            description_result = generate_product_content(product_name, features, target_language)

            # Arayüzü güncelleme
            self.app.description_result_text.config(state=tk.NORMAL)
            self.app.description_result_text.delete("1.0", tk.END)
            self.app.description_result_text.insert(tk.END, description_result)
            self.app.description_result_text.config(state=tk.DISABLED)

        except Exception as e:
            messagebox.showerror("Hata", f"İçerik oluşturulurken bir hata oluştu: {e}")

        finally:
            self.app.description_result_text.config(state=tk.NORMAL)
            self.app.generate_button.config(state=tk.NORMAL)


    # Video özetleme kısmı
    def start_summarize_thread(self):
        youtube_url = self.app.youtube_url_entry.get().strip()
        if not youtube_url:
            messagebox.showwarning("Uyarı", "Lütfen bir YouTube URL'si girin.")
            return

        thread = threading.Thread(target=self.run_summarize, args=(youtube_url,))
        thread.start()

    def run_summarize(self, youtube_url):
        self.app.summarize_button.config(state=tk.DISABLED)
        self.app.save_button.config(state=tk.DISABLED)
        self.app.summarizer_result_text.delete("1.0", tk.END)
        self.app.summarizer_result_text.insert(tk.END, "Transkript çekiliyor ve özetleniyor.\nLütfen bekleyin.")

        try:
            # Arayüzden seçilen dili al
            target_language = self.app.selected_language.get()

            transcript_data = get_youtube_transcript(youtube_url)
            if not transcript_data["transcript"]:
                raise Exception("Transkript çekilemedi.")

            # Seçilen dili summarize_transcript fonksiyonuna gönder
            summary = summarize_transcript(transcript_data["title"], transcript_data["transcript"], target_language)

            self.app.summarizer_result_text.config(state=tk.NORMAL)
            self.app.summarizer_result_text.delete("1.0", tk.END)
            self.app.summarizer_result_text.insert(tk.END, summary)

        except Exception as e:
            messagebox.showerror("Hata", f"Video özeti oluşturulurken bir hata oluştu: {e}")
            self.app.summarizer_result_text.delete("1.0", tk.END)

        finally:
            self.app.summarize_button.config(state=tk.NORMAL)
            self.app.save_button.config(state=tk.NORMAL)

    # Özeti kaydetme işlevi
    def save_summary(self):
        summary_text = self.app.summarizer_result_text.get("1.0", tk.END).strip()
        if not summary_text:
            messagebox.showwarning("Uyarı", "Kaydedilecek bir özet bulunamadı.")
            return

        try:
            filename = "youtube_ozetleri.txt"
            with open(filename, "a", encoding="utf-8") as f:
                f.write(summary_text)
                f.write("\n\n---\n\n")
            messagebox.showinfo("Başarılı", f"Özet başarıyla '{filename}' dosyasına kaydedildi.")
        except Exception as e:
            messagebox.showerror("Hata", f"Dosya kaydedilirken bir hata oluştu: {e}")


if __name__ == "__main__":
    app_instance = FermanApp()
    app_instance.run()