from typing import final

from moviepy import  VideoFileClip
from pydub import AudioSegment
from pydub.utils import which
import os


class AudioManager():

    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../audios"))
    AudioSegment.converter = which("ffmpeg")

    @staticmethod
    def extract_audio(input, output_dir=output_dir):
        """

        :param input: input video file
        :param output_dir: audio files directory

        extracts audio from a video file and saves it in a .mp3

        """
        # getting filename
        file_name = os.path.basename(input).split(".")[0]

        # getting the audios folder path
        os.makedirs(output_dir, exist_ok= True)

        # making an output file
        output = os.path.join(output_dir,f"{file_name}_audio.mp3")

        video = VideoFileClip(input)
        audio = video.audio
        audio.write_audiofile(output)

        print(f"audio from {input} saved to {output}")
        return f"audios/{file_name}_audio.mp3"
    
    @staticmethod
    def allowed_audio_size(input, max_size_mb=25):
        """

        :param input: input mp3 file
        :return: True if mp3 < 25 mb
        """
        try:
            file_size = os.path.getsize(input)
            file_size_in_mb = file_size / (1024 * 1024)
            print("size bigger than allowed proceed to chunk the audio up")
            return file_size_in_mb < max_size_mb
        except FileNotFoundError:
            print(f"the file {input} does not exist in this directory")


    @staticmethod
    def break_up_audio(input_path, max_size_mb = 25, output_dir = output_dir):
        """

        :param input_path: mp3 audio file bigger than 25 mb
        :param max_size_mb:
        :param output_dir:
        :return: audio file splits to chunks smaller than 25mbs

        """
        print(input_path)
        try:

            # File info
            audio = AudioSegment.from_file(file= input_path)
            print("cuting the audio to parts")
            file_name = os.path.basename(input_path).split(".")[0]
            file_size = os.path.getsize(input_path)
            file_size_mb = file_size / (1024 * 1024)


            # Calculations
            duration_ms = len(audio)
            num_parts = int(file_size_mb // max_size_mb) + 1
            part_duration = duration_ms // num_parts

            # Split and save parts
            os.makedirs(output_dir, exist_ok=True)
            parts = []
            for i in range(num_parts):
                print(f"working on part {i}")
                start_time = i * part_duration
                end_time = min((i + 1) * part_duration, duration_ms)
                part = audio[start_time:end_time]

                part_name = os.path.join(output_dir,f"{file_name}_part{i + 1}.mp3")
                part.export(part_name, format = "mp3")
                parts.append(part_name)

                print(f"saved part {i + 1} to {part_name}")
            return parts
        except FileNotFoundError as e:
            print(f"FileNotFoundError : {e}")
            return []
        except Exception as e:
            print(f"An error occured: {e}")
            return []

