from os import path

import pyttsx3  
from threading import Thread

def ThreadTextToAudio(FuntionParam, TextParam:str):
    T1 = Thread(
        target=FuntionParam,
        args=(TextParam,)
    )
    T1.start()

def TextToAudio(Text:str):
    engine = pyttsx3.init()  
    engine.say(Text)
    engine.runAndWait()

def saveAudio(Text, NameFile):
    pathRutSave = path.abspath(f'./OutPutAudio/{NameFile}.mp3')
    engine = pyttsx3.init()  
    engine.save_to_file(Text, pathRutSave)
    engine.runAndWait()
