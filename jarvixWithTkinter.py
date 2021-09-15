from tkinter import *
from tkinter.ttk import Style
from tkinter.messagebox import *
import random
root = Tk()
root.title("jarvis")
root.geometry("598x560+100+00")
root.configure(background = "dark blue")

topFrame = Frame(root,bg="light blue")
topFrame.pack()
# ss = 'Jarvis'
# count = 0
# text = ''
# SliderLabel = Label(root,text=ss,font=('Times new roman',20,'italic bold'),relief=RIDGE,borderwidth=0,width=17,bg='light blue')
# SliderLabel = Label(root,text=ss,font=('Times new roman',20,'italic bold'),relief=RIDGE,borderwidth=4,width=18,bg='linen')
# SliderLabel.place(x=272,y=20)
# IntroLabelTick()
# IntroLabelColorTick()

bottomFrame = Frame(root)
bottomFrame.pack(side =BOTTOM)
photo = PhotoImage(file = "jarvis.png")
Label(topFrame ,image = photo).grid(row=2 ,column = 1 ,sticky = W)
# label = Label(topFrame, text="CRIMINAL \n RECORD \n DATABASE ",fg="black",bg="light blue",font=(None, 25)).grid(row=1,column = 3,sticky= E)


# Label(topFrame, text="Enter Password",fg="black",bg="light blue",font=(None, 15)).grid(row=4,column=3)
# textentry = Entry(topFrame , width =30 ,fg="black" ,bg="white",show = "*")
# textentry.grid(row=5, column = 3,sticky=W)
# Button(topFrame ,text="Submit",width=10 ,command = click).grid(row=6,column=3,sticky=W)

# pass_label=Label(root,text="Enter Password",font=('Times new roman',15,'italic bold'),relief=RIDGE,borderwidth=0,width=30,bg='light blue')
# pass_label.place(x=100,y=230)

#Official log in
# SliderLabel = Label(root,text=ss,font=('Times new roman',20,'italic bold'),relief=RIDGE,borderwidth=0,width=17,bg='light blue')

# Label(topFrame, text="OFFICIAL LOG IN",bg="light blue",font=('Times new roman',15,'bold')).grid(row=4,column=1,sticky=NW)
# Label(topFrame, text="OFFICIAL LOG IN",fg="black",bg="light blue",font=(,font=('Times new roman',15,'italic bold')).grid(row=4,column=1,sticky=NW)
# Label(topFrame, text="Enter Password",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=1,sticky=SW)
# textentry = Entry(topFrame , width =15 ,fg="black" ,bg="white",show = "*")
# textentry.grid(row=6, column = 1,sticky=W)
# Button(topFrame ,text="Log In",width=10 ,command = click).grid(row=7,column=1,sticky=W)

#Public log in
# Label(topFrame, text="                  PUBLIC LOG IN",bg="light blue",font=('Times new roman',15,'bold')).grid(row=4,column=2,sticky=NE)
# Label(topFrame, text="                  Enter Name",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=2,sticky=S)
# Label(topFrame, text="                  Click below to log in publicly",bg="light blue",font=('Times new roman',11,'italic')).grid(row=5,column=2,sticky=SE)
# textentry_public = Entry(topFrame , width =18 ,fg="black" ,bg="white")
# textentry_public.grid(row=6, column = 2,sticky=E)

# Button(topFrame ,text="Log In",width=10,command = complain_management).grid(row=7,column=2,sticky=E)


def runVirtualAssistant():
    import pyttsx3 #pip install pyttsx3
    import  speech_recognition as sr #pip install speechRecognition
    import datetime
    import  wikipedia #pip install wikipedia
    import  webbrowser
    import  os
    import  smtplib
    
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    # print(voices[1].id)
    engine.setProperty('voice', voices[0].id)
    
    
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    
    
    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Jaiiii Shreeeee Raam!")
    
        elif hour>=12 and hour<18:
            speak("Jaiiii Shreeeee Raam!")   
    
        else:
            speak("Jaiiii Shreeeee Raam!")  
    
        speak("I am Jarvis Sir. Please tell me how may I help you")       
    
    def takeCommand():
        #It takes microphone input from the user and returns string output
    
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    
        try:
            print("Recognizing...")    
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
    
        except Exception as e:
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
        server.close()
    
    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()
    
            # Logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
    
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
    
            elif 'open google' in query:
                webbrowser.open("google.com")
    
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")   
    
    
            elif 'play music' in query:
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))
    
            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")
    
            elif 'open code' in query:
                codePath = "C:\\Users\\Shiva\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
    
            elif 'email to harry' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "skDemo@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend kumar bhai. I am not able to send this email")    
       


                    
    

    # exit()
# Label(topFrame, text="Please speak ...How may I help you..",
    #   fg="blue", bg="white", font=(None, 25)).grid(row=0, column=1, sticky=N)
Button(topFrame, text="Click Here To Speak", bg="pink", font=(None, 27),width=20, command=runVirtualAssistant).grid(row=0, column=1, sticky=N)
Button(topFrame, text="Quit", bg="light gray", font=(None, 24),width=20, command=quit).grid(row=1, column=1, sticky=N)


# def on_stop():
#     """Stop the animation"""
#     start_button.configure(state="normal")
#     # stop_button.configure(state="disabled")
#     running = False

# stop_button=Button(topFrame, text="Click Here To Speak", bg="pink", font=(None, 20),width=20, command=on_stop).grid(row=2, column=1, sticky=N)

root.mainloop()
