import speech_recognition as sr

r=sr.Recognizer()

with r as source :
    print("Say something")
    audio=r.listen(source)

def new_func(r, audio):
    return "Google speech recog. thinks you said " + r.recognize_google(audio)

try:
    print(new_func(r, audio))

    
except sr.UnknownValueError:

    print("couldn't identify what was said")

except sr.RequestError as e:
    print("Could not process please try again, {0}".format(e))