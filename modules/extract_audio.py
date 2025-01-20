from moviepy import  VideoFileClip

def extract_audio(input, output):
    video = VideoFileClip(input)
    audio = video.audio
    audio.write_audiofile(output)

    print(f"audio from {input} saved to {output}")