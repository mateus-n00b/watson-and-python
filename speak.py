from gtts import gTTS
from playsound import playsound
import os
def speak(text):
 audio_file = 'audios/audio.mp3'
 tts = gTTS(text,lang='pt-br')
 #Salva o arquivo de audio
 tts.save(audio_file)
 print("Processando...")
 #Da play ao audio
 playsound(audio_file)
