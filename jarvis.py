import pyttsx3
import datetime
import os
import cv2
import sys
import pywhatkit
import webbrowser
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # speak('praduman meethaa auur chakkkaa hai')
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    try:
        print('wait...')
        query = r.recognize_google(audio,language='en-IN')
        print(f'user said : {query}')
    except Exception as e:
        speak('say hii Tanuj try again ')
        return 'none'
    speak(query)
    return query
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <=12:
        speak('hii , good morning sagar bhai: ')
    elif hour>=12 or hour <=18:
        speak('hii good afternoon  tanuj  bhai : ')
    else:
        speak('hii good evening sagar bhai : ')
    speak('tell me')
    speak(' hii doctor vimlesh bhai')

if __name__ == '__main__':
    wish()
    # speak('hey my name is tanuj')
    # take()
    while True:
        query = take().lower()
        if 'open notepad' in query:
            npath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(npath)
        elif 'praduman' in query:
            speak('praduman meethaa auur chakkkaa hai')
        elif 'open camera' in query:
            video_capture = cv2.VideoCapture(0)
            cv2.namedWindow("Window")

            while True:
                ret, frame = video_capture.read()
                cv2.imshow("Window", frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            video_capture.release()
            cv2.destroyAllWindows()
        elif 'open google' in query:
            speak('what search on gooogle : ')
            cm = take().lower()
            webbrowser.open(f'{cm}')

        elif 'send message' in query:
            try:

                # sending message to reciever
                # using pywhatkit
                pywhatkit.sendwhatmsg("+919794154351",
                                      "Hello from GeeksforGeeks",
                                      14, 32)
                print("Successfully Sent!")

            except:

                # handling exception
                # and printing error message
                print("An Unexpected Error!")
        elif 'play song on youtube' in query:
            pywhatkit.playonyt('tum hi aana')
        elif 'jab tak song' in query:
            t='C:\\Users\\Tanuj\OneDrive\\Desktop\\videos and movies\\movies\\ki jab tak jiyu.mp4'
            os.startfile(t)
        else:
            sys.exit()

