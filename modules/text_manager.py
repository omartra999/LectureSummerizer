from whisper import load_model
from transformers import MarianMTModel, MarianTokenizer, pipeline

class TextManager:

    def __init__(self):
        """
        Initialize models for transcription, and summarization
        """
        self.transcription_model = load_model("medium")
        self.translation_model_name = "Helsinki-NLP/opus-mt-de-en"
        self.translation_model = MarianMTModel.from_pretrained(self.translation_model_name)
        self.translation_tokenizer = MarianTokenizer.from_pretrained(self.translation_model_name)
        self.summarizer = pipeline("summarization")

    def transcribe_audio(self,audio_path):
        """
        Transcribe an audio into german text

        """
        result = self.transcription_model.transcribe(audio_path,language="de")
        return result["text"]

    def translate_text(self, german_text):
        """
        Translates German Text into English

        :param german_text:
        :return:
        """
        tokens = self.translation_tokenizer(german_text, return_tensors="pt", truncation=True,max_length=512)
        translated_tokens = self.translation_model.generate(**tokens)
        english_text = self.translation_tokenizer.decode(translated_tokens[0], skip_special_tokens=True)
        return english_text

    def summarize_text(self,text):
        """
        Summarizes the given English text
        :param text:
        :return:
        """
        summary = self.summarizer(text)
        return summary[0]["summary_text"]