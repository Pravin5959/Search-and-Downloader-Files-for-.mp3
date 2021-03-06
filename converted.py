import numpy as np 
import pandas as pd
from pydub import AudioSegment
import os

rock_path = r"C:\Users\pravi\Desktop\music4all\Rock_names_FLOP.csv"

rock_csv = pd.read_csv(rock_path)
# print(rock_csv['id'])

mp3 = ".mp3"

mp3_list = []

for i in rock_csv['id']:
    k = i + mp3
    mp3_list.append(k)

audio_path = r"C:\Users\pravi\Desktop\music4all\audios"

audio_path_list = os.listdir(audio_path)

rock_save_path = r"C:\Users\pravi\Desktop\music4all\rock_music"

for p in audio_path_list:
    if p in mp3_list:
        print("Processing.. ", p)
        rock = AudioSegment.from_file(audio_path + "/" + p, "mp3")
        if p.endswith(mp3):
            res = p[:-len(mp3)]
        rock.export(rock_save_path + "/" + res + ".wav", format= "wav")
