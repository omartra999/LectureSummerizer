from modules.audio_manager import AudioManager
from modules.text_manager import TextManager
print("Finished Importing")

text_manager = TextManager()
lecture = input("enter the path of the desired lecture:")
print("extracting audio....")
extracted_audio = AudioManager.extract_audio(lecture)

if not AudioManager.allowed_audio_size(extracted_audio):
   audio_parts =  AudioManager.break_up_audio(extracted_audio)
else :
    audio_parts = [extracted_audio]

text = ""
for audio in audio_parts:
    print(f"processsing {audio}")

    german_text = text_manager.transcribe_audio(audio)
    print(f"German Transcription: {german_text}")

    english_text = text_manager.translate_text(german_text)
    print(f"English translation: {english_text}")

    text += english_text

summarized_text = text_manager.summarize_text(text)
print(f"Summary: {summarized_text}")

text_manager.save_to_notepad(summarized_text, "summary_V5.txt")