from moviepy import  VideoFileClip
import os

def extract_audio(input):

    # getting filename
    file_name = os.path.basename(input).split(".")[0]

    # getting the audios folder path
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"../audios"))
    os.makedirs(output_dir, exist_ok= True)

    # making an output file
    output = os.path.join(output_dir,f"{file_name}_audio.wav")

    video = VideoFileClip(input)
    audio = video.audio
    audio.write_audiofile(output)

    print(f"audio from {input} saved to {output}")