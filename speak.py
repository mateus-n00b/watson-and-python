from gtts import gTTS
from playsound import playsound
import os
def speak(text):
 audio_file = 'audios/audio.mp3'
 error_file = "audios/error.mp3"
 try:
     tts = gTTS(text,lang='en-us')
     #Salva o arquivo de audio
     tts.save(audio_file)
     print("Processando...")
     #Da play ao audio
     playsound(audio_file)
 except Exception as e:
     print(e)
     playsound(error_file)
