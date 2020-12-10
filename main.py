import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    print(text)
    tts = gTTS(text=text, lang="pt-br")
    filename = "user_audio.mp3"

    tts.save(filename)
    playsound.playsound(filename)
    os.remove('user_audio.mp3')


def listen():
    mic = sr.Recognizer()
    with sr.Microphone() as source:

        mic.adjust_for_ambient_noise(source)
        
        speak('Fale agora.')
        
        audio = mic.listen(source)

        try:
            speech = mic.recognize_google(audio,language='pt-BR')
            
            speak("Você disse: " + speech)
            return speech
        
        except UnboundLocalError:
            speak('Oxi...')

        except sr.UnknownValueError:
            speak("Oxi... Não entendi")



listen()

