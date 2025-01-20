from modules.audio_manager import AudioManager

lecture = input("enter the path of the desired lecture:")
extracted_audio = AudioManager.extract_audio(lecture)

if not AudioManager.allowed_audio_size(extracted_audio):
   audio_parts =  AudioManager.break_up_audio(extracted_audio)
else :
    audio_parts = [extracted_audio]

for audio in audio_parts:
    text_part = TextManager.convert_to_text(audio)

#TODO:
# for each part of the audio:
# transcribe it into german text
# translate to english
# Summerize it