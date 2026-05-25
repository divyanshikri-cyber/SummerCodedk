import pyttsx3
import pyautogui
import os
import speech_recognition as sr
import time
from time import sleep
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def input_query():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        speak_va('speak')
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(voice).lower()
            print('this is the query that was made....', query)
            return query
        except Exception as ex:
            print('An exception occurred', ex)
            speak_va("Try again")
def speak_va(transcribed_query):
    engine.say(transcribed_query)
    engine.runAndWait()

def message():
    speak_va('whom do you wanna call')
recognizer = sr.Recognizer()
with sr.Microphone() as source:
        print('Listening....')
        speak_va("Whom do you wanna message")
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            input_callcommand = recognizer.recognize_google(voice).lower()
            print('messaging...',input_callcommand)
            
        except Exception as ex:
            print('Unable to recognise', ex)
            speak_va("Try again")

        sleep(7)
        pyautogui.click(x=1774,y=17)
        os.startfile(r'C:\Users\jaypa\OneDrive\Desktop\WhatsApp.lnk')
        
        pyautogui.click(x=141,y=128,duration=2)
        pyautogui.typewrite(input_callcommand)
        pyautogui.press('enter')
        pyautogui.click(x=776, y=1000)
recognizer = sr.Recognizer()
with sr.Microphone() as source:
        print('Listening....')
        speak_va("What is the message")
        recognizer.pause_threshold = 0.7
        voice = recognizer.listen(source)
        try:
            input_msg = recognizer.recognize_google(voice).lower()
            print('messaging...',input_callcommand)
            
        except Exception as ex:
            print('Unable to recognise', ex)
            speak_va("Try again")
        pyautogui.typewrite(input_msg)
        pyautogui.press('enter')
        speak_va("Message delivered sir")
        
        
