import os
import time
import mutagen.mp3
import mutagen.flac
import mutagen.mp3

def verify_extension(file):
    if file.endswith('.mp3'):
        return 'mp3'
    elif file.endswith('.m4a'):
        return 'm4a'
    elif file.endswith('.flac'):
        return 'flac'


audio_length = 0

files = os.listdir("audio_files")

for file in files:
    if verify_extension(file) == 'mp3':
        audio = mutagen.mp3.MP3("audio_files/"+file)
    elif verify_extension(file) == 'm4a':
        audio = mutagen.m4a.M4A("audio_files/"+file)
    elif verify_extension(file) == 'flac':
        audio = mutagen.flac.FLAC("audio_files/"+file)

    audio_length += audio.info.length

minutes = audio_length // 60
hours = minutes // 60


print("Seu tempo de música aproximado em horas, minutos e segundos: ")
print(time.strftime('%H:%M:%S', time.gmtime(audio_length)))









