import speech_recognition as sr
import speak
from time import ctime
import time
import sys
r = sr.Recognizer()
lang = 'en'
data = ''
nameCalled = 0
# Enable Microphone and use for audio input

# Speech recognition using Google Speech Recognition

def spk(text, lang):
    speak.tts(text, lang)

def audioRecord():
    try:
        with sr.Microphone() as source:
                #r.energy_threshold = 500
                # Increase for less sensitivity, decrease for more
                print('Listening...')
                audio = r.listen(source)
                #r.adjust_for_ambient_noise(source)
                data = r.recognize_google(audio)
                print('You said ' + data)
                return data
            
    except sr.UnknownValueError:
        print('Google could not understand audio!')
    except sr.RequestError as e:
       print('Could not request results for GSR')

              
def brain(data):
    global nameCalled
    #^^Keep track to see if amber was called^^
    global lang

    #If amber was said, than the next command heard can be executed
    if nameCalled == 0:

        if 'Amber' in data:
            nameCalled = 1
            spk('Yes?', lang)
        elif 'nothing' in data:
            spk('Okay', lang)
            sys.exit()     
        else:
            return 'null'
        #Once we hear amber, the next command spoken can be executed,
        # if something goes wrong, just set the nameCalled variable to 0
        #and restart the process
    elif nameCalled == 1:
        if 'what time is it' in data:
            spk(ctime(), lang)
        if 'nothing' in data:
            spk('Okay', lang)
            sys.exit()
        nameCalled = 0
    else:
        nameCalled = 0

    
  


# initialization
spk('hello nick, what can I do for you today', lang)
while 1:
    data = audioRecord()
    brain(data)

    
