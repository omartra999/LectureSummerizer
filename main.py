from modules.audio_manager import AudioManager

# lecture = input("enter the path of the desired lecture:")
# extracted_audio = AudioManager.extract_audio(lecture)
#
# if not AudioManager.allowed_audio_size(extracted_audio):
#     AudioManager.break_up_audio(extracted_audio)

AudioManager.allowed_audio_size("audios/RN_WS24_V5_audio.mp3")
AudioManager.break_up_audio("audios/RN_WS24_V5_audio.mp3")

