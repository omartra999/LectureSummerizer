from whisper import load_model
from transformers import MarianMTModel, MarianTokenizer, pipeline
import torch
class TextManager:

    def __init__(self):
        """
        Initialize models for transcription, and summarization
        """
        print("initializing....")
        print("initializing transcription model...")
        self.transcription_model = load_model("medium").to("cuda" if torch.cuda.is_available() else "cpu")
        print("transcription model initialized....")
        print("initializing translation model...")
        self.translation_model_name = "Helsinki-NLP/opus-mt-de-en"
        self.translation_model = MarianMTModel.from_pretrained(self.translation_model_name)
        print("translation model initialized....")
        print("initializing translation tokenizer model...")
        self.translation_tokenizer = MarianTokenizer.from_pretrained(self.translation_model_name)
        print("translation tokenizer initialized....")
        print("initializing pipeline...")
        self.summarizer = pipeline("summarization")
        print("summarizer initialized ......")

    def transcribe_audio(self,audio_path):
        """
        Transcribe an audio into german text

        """
        print(f"transcribing {audio_path}")
        try:
            result = self.transcription_model.transcribe(audio_path,language="de", verbose= False)
        except Exception as e:
            print(f"Error during transcription: {e}")
        return result["text"]

    def translate_text(self, german_text):
        """
        Translates German Text into English

        :param german_text:
        :return:
        """
        print("startet translating.....")
        tokens = self.translation_tokenizer(german_text, return_tensors="pt", truncation=True,max_length=512)
        print("tokens generated....")
        translated_tokens = self.translation_model.generate(**tokens)
        print("tokens translated....")
        english_text = self.translation_tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        print("text translated to english.....")
        return english_text

    def summarize_text(self,text):
        """
        Summarizes the given English text
        :param text:
        :return:
        """
        print("startet summarizing....")
        summary = self.summarizer(text)
        print("text summarized successfully....")
        return summary[0]["summary_text"]

    def save_to_notepad(self, text, file_name):
        """
          Save summarized text to a notepad file.

          :param text: The text to save.
          :param file_name: The name of the output file (default: "summary.txt").
          """
        try:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(text)
            print(f"Summary saved to {file_name}")
        except Exception as e:
            print(f"An error occurred: {e}")
