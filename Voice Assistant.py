import pyttsx3
import datetime
import calendar
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox
import time
import speedtest


root = tk.Tk()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
# default rate/speed = 200
engine.setProperty('rate', 150)


dt = datetime.datetime.now()

var = tk.StringVar()
var1 = tk.StringVar()


def speak(audio):
    global label
    audio1 = audio.split(maxsplit=14)
    if len(audio1) <= 15:
        var.set(audio1[0:14])
    else:
        var.set(audio1[0:14])
        var1.set(audio1[-1])
    root.update()
    engine.say(audio)
    engine.runAndWait()


global user

try:
    file = open('save.txt', 'r')
    if file.read() == '':
        speak('please enter your name in terminal')
        user = input()
        speak('enter your user name of this p c')
        user_name = input()
        file.close()
    else:
        file.close()
        file = open('save.txt', 'r')
        u = file.readline()
        user = u.rstrip('\n')
        user_name = file.readline()
        file.close()
except FileNotFoundError:
    file = open('save.txt', 'w')
    speak('please enter your name in terminal')
    user = input()
    speak('enter your user name of this p c')
    user_name = input()
    file.write(user + '\n')
    file.write(user_name)
    file.close()
a = 'sir'


def wish_me():
    speak('welcome back' + ' ' + a)
    hour = str(dt.hour)
    hour1 = str(dt.strftime('%I'))
    minutes = str(dt.strftime('%M'))
    meridium = str(dt.strftime('%p'))
    day_no = int(dt.weekday())
    day = calendar.day_name[day_no]
    date1 = str(dt.day)
    month_no = int(dt.month)
    year = str(dt.year)
    month = calendar.month_name[month_no]
    if hour1[0][0] == '0':
        hour1 = hour1.replace('0', '')
    else:
        pass
    speak('the current time is')
    speak(hour1 + ' ' + minutes + ' ' + meridium)
    speak('today is')
    speak(month + ' ' + date1 + ' ' + year)
    speak(day)
    hour = int(hour)
    if 6 <= hour < 12:
        speak('good morning! ' + user + ' ' + a)
        speak('I am your assistant')
    elif 12 <= hour < 16:
        speak('good afternoon! ' + user + ' ' + a)
        speak('I am your assistant')
    elif 16 <= hour < 21:
        speak('good evening! ' + user + ' ' + a)
        speak('I am your assistant')
    else:
        speak('good night! ' + user + ' ' + a)
        speak('I am your assistant')


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak('listening...')
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=20)
    try:
        speak('recognizing...')
        query1 = r.recognize_google(audio, language='en-US')
        query2 = query1.lower()
        speak('you said : ' + query2)
    except sr.UnknownValueError:
        message_box('info', 'Can not recognise', 'Please say that again')
        return None

    return query2


def display_time():
    current_time = time.strftime('%I:%M %p')
    clock['text'] = current_time
    root.after(1000, display_time)


def display_date():
    current_date = datetime.datetime.now().date()
    date['text'] = current_date
    hour = datetime.datetime.now().hour
    if hour == 0:
        root.after(0, display_date)
    else:
        pass


def encyclopedia(query1):
    speak('searching wikipedia')
    query1 = query1.replace('wikipedia', '')
    query1 = query1.strip()
    try:
        result = wikipedia.summary(query1, 2)
        speak('according to wikipedia')
        speak(result)
    except Exception as e2:
        speak('sorry, result is not found')
        message_box('error', 'Error', str(e2))
        speak('try saying wikipedia and your query')


def open_chrome(query1):
    exist = os.path.exists('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe')
    if exist:
        chrome = webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s')
        if ('open youtube' or 'youtube') in query1:
            chrome.open('youtube.com')
            speak('opening youtube in chrome')
        elif ('open google' or 'google') in query1:
            chrome.open('google.com')
            speak('opening google in chrome')
        elif ('open gmail' or 'gmail') in query1:
            chrome.open('gmail.com')
            speak('opening g mail in chrome')
        elif ('open bing' or 'bing') in query1:
            chrome.open('bing.com')
            speak('opening bing in chrome')
        elif ('open facebook' or 'face book') in query1:
            chrome.open('facebook.com')
            speak('opening facebook in chrome')
        elif ('open wikipedia' or 'wikipedia') in query1:
            chrome.open('wikipedia.com')
            speak('opening wikipedia in chrome')
        else:
            speak('sorry, please enter u r l')
            url = input('-> ')
            chrome.open(url)
            speak('u r l is opened')
    else:
        speak('sorry chrome does not exist in given location')


def open_firefox(query1):
    exist = os.path.exists('C:/Program Files/Mozilla Firefox/firefox.exe')
    if exist:
        firefox = webbrowser.get('C:/Program Files/Mozilla Firefox/firefox.exe %s')
        if ('open youtube' or 'youtube') in query1:
            firefox.open('youtube.com')
            speak('youtube is opened')
        elif ('open google' or 'google') in query1:
            firefox.open('google.com')
            speak('google is opened')
        elif ('open gmail' or 'gmail') in query1:
            firefox.open('gmail.com')
            speak('g mail is opened')
        elif ('open bing' or 'bing') in query1:
            firefox.open('bing.com')
            speak('bing is opened')
        elif ('open facebook' or 'face book') in query1:
            firefox.open('facebook.com')
            speak('facebook is opened')
        elif ('open wikipedia' or 'wikipedia') in query1:
            firefox.open('wikipedia.com')
            speak('wikipedia is opened')
        else:
            speak('sorry, please enter u r l')
            url = input()
            firefox.open(url)
            speak('u r l is opened')
    else:
        speak('sorry firefox does not exist in given location')


def open_opera(query1):
    exist = os.path.exists('C:/Users/' + user_name + '/AppData/Local/Programs/Opera/launcher.exe')
    if exist:
        opera = webbrowser.get('C:/Users/' + user_name + '/AppData/Local/Programs/Opera/launcher.exe %s')
        if ('open youtube' or 'youtube') in query1:
            opera.open('youtube.com')
            speak('youtube is opened')
        elif ('open google' or 'google') in query1:
            opera.open('google.com')
            speak('google is opened')
        elif ('open gmail' or 'gmail') in query1:
            opera.open('gmail.com')
            speak('g mail is opened')
        elif ('open bing' or 'bing') in query1:
            opera.open('bing.com')
            speak('bing is opened')
        elif ('open facebook' or 'face book') in query1:
            opera.open('facebook.com')
            speak('facebook is opened')
        elif ('open wikipedia' or 'wikipedia') in query1:
            opera.open('wikipedia.com')
            speak('wikipedia is opened')
        else:
            speak('sorry, please enter u r l')
            url = input()
            opera.open(url)
            speak('u r l is opened')
    else:
        speak('sorry opera does not exist in given location')


def send_mail(sender, receiver, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    try:
        server.login(sender, password)
        speak('login success')
    except Exception as e3:
        speak('login unsuccessful')
        message_box('error', 'Login Unsuccessful', str(e3))
        speak('try again')

    try:
        server.sendmail(sender, receiver, message)
        speak('mail sent')
    except Exception as e4:
        speak('mail not sent')
        message_box('error', 'Mail Not Sent', str(e4))


def mail():
    mail_window = tk.Toplevel()
    frame4 = tk.Frame(mail_window, width=400, height=400, bg='black')
    frame4.pack(fill=tk.BOTH, expand=True)
    speak('please enter mail id password message')
    tk.Label(frame4, text='From :', bg='black', fg='SteelBlue4', font=('Arial', 15)).place(x=10, y=40)
    tk.Label(frame4, text='To :', bg='black', fg='SteelBlue4', font=('Arial', 15)).place(x=10, y=100)
    tk.Label(frame4, text='Password :', bg='black', fg='SteelBlue4', font=('Arial', 15)).place(x=10, y=160)
    tk.Label(frame4, text='Message :', bg='black', fg='SteelBlue4', font=('Arial', 15)).place(x=10, y=220)

    entry1 = tk.Entry(frame4, bg='black', fg='SteelBlue4', font=('Arial', 15))
    entry1.place(x=120, y=40)

    entry2 = tk.Entry(frame4, bg='black', fg='SteelBlue4', font=('Arial', 15))
    entry2.place(x=120, y=100)

    entry3 = tk.Entry(frame4, show='*', bg='black', fg='SteelBlue4', font=('Arial', 15))
    entry3.place(x=120, y=160)

    entry4 = tk.Entry(frame4, bg='black', fg='SteelBlue4', font=('Arial', 15))
    entry4.place(x=120, y=220)

    button = tk.Button(frame4, text='submit', bg='black', fg='SteelBlue4', border=0,
                       activebackground='black', activeforeground='SteelBlue4',
                       command=lambda: send_mail(entry1.get(), entry2.get(), entry3.get(), entry4.get()))
    button.place(x=170, y=280)
    mail_window.mainloop()


def open_files(query1):
    if 'paint' in query1:
        os.startfile('C:/WINDOWS/system32/mspaint.exe')
        speak('paint is opened')
    elif 'notepad' in query1:
        os.startfile('C:/WINDOWS/system32/notepad.exe')
        speak('notepad is opened')
    elif 'media player' in query1:
        os.startfile('C:/Program Files (x86)/Windows Media Player/wmplayer.exe')
        speak('windows media player is opened')
    elif ('word pad' or 'wordpad') in query1:
        os.startfile('C:/Program Files/Windows NT/Accessories/wordpad.exe')
        speak('wordpad is opened')
    elif 'registry' in query1:
        os.startfile('C:/WINDOWS/regedit.exe')
        speak('registry is opened')
        speak('be careful while editing registry')
    elif 'magnifier' in query1:
        os.startfile('C:/WINDOWS/system32/Magnify.exe')
        speak('magnifier is opened')
    else:
        speak('sorry')


def message_box(message_type, title, your_message):
    if message_type == 'info':
        tk.messagebox.showinfo(title, your_message)
    elif message_type == 'warning':
        tk.messagebox.showwarning(title, your_message)
    elif message_type == 'yesno':
        tk.messagebox.askyesno(title, your_message)
    elif message_type == 'okcancel':
        tk.messagebox.askokcancel(title, your_message)
    elif message_type == 'yesnocancel':
        tk.messagebox.askyesnocancel(title, your_message)
    elif message_type == 'retrycancel':
        tk.messagebox.askretrycancel(title, your_message)
    elif message_type == 'question':
        tk.messagebox.askquestion(title, your_message)
    elif message_type == 'error':
        tk.messagebox.showerror(title, your_message)
    else:
        tk.messagebox.showinfo(title, your_message)


try:
    import pywhatkit
except Exception as e5:
    message_box('info', 'import error', str(e5))


def main():
    global user
    global user_name
    query = take_command()
    if query is None:
        speak('Sorry, ' + a)
        speak('can you repeat that again')
    elif 'search for' in query:
        query = query.replace('search for', '')
        query = query.strip()
        pywhatkit.search(query)
    elif ('play' and ('in youtube' or 'on youtube')) in query:
        query = query.replace('in youtube', '')
        query = query.replace('play', '')
        query = query.strip()
        pywhatkit.playonyt(query)
    elif ('current time' or 'time now') in query:
        t = str(dt.strftime('%I %M %p'))
        speak(t)
    elif ('current date' or 'date') in query:
        d = str(dt.date())
        speak(d)
    elif ('check internet' or 'speed test' or 'internet speed' or 'speedtest') in query:
        down = str((speedtest.Speedtest().download() / 1024) / 1024)
        up = str((speedtest.Speedtest().upload() / 1024) / 1024)
        i1 = up.find('.')
        i2 = down.find('.')
        speak(up[0][0:i1 + 1] + ' mb per second')
        speak(down[0][0:i2 + 1] + ' mb per second')
    elif ('chrome' or 'in chrome') in query:
        open_chrome(query)
    elif ('mozilla' or 'in mozilla' or 'firefox' or 'in firefox') in query:
        open_firefox(query)
    elif ('opera' or 'in opera') in query:
        open_opera(query)
    elif ('open youtube' or 'youtube') in query:
        webbrowser.open('youtube.com')
        speak('youtube is opened')
    elif ('open google' or 'google') in query:
        webbrowser.open('google.com')
        speak('google is opened')
    elif ('open gmail' or 'gmail') in query:
        webbrowser.open('gmail.com')
        speak('g mail is opened')
    elif ('open bing' or 'bing') in query:
        webbrowser.open('bing.com')
        speak('bing is opened')
    elif ('open facebook' or 'face book') in query:
        webbrowser.open('facebook.com')
        speak('facebook is opened')
    elif 'open wikipedia' in query:
        webbrowser.open('wikipedia.com')
        speak('wikipedia is opened')
    elif 'wikipedia' in query:
        encyclopedia(query)
    elif 'play music' in query:
        speak('enter your user name of this p c')
        user_name = input()
        music_directory = 'C:\\Users\\' + user_name + '\\Music'
        songs = os.listdir(music_directory)
        os.startfile(os.path.join(music_directory, songs[0]))
        speak('music is being played')
    elif ('play video' or 'video') in query:
        video_directory = 'C:\\Users\\' + user_name + '\\Videos'
        os.startfile(os.path.join(video_directory))
        speak('opening videos folder')
    elif ('open photos' or 'photos' or 'open pictures' or 'pictures') in query:
        pictures_directory = 'C:\\Users\\' + user_name + '\\Music'
        photos = os.listdir(pictures_directory)
        os.startfile(os.path.join(pictures_directory, photos[0]))
    elif "what is your name" in query:
        speak("i don't have a name")
    elif 'open' in query:
        open_files(query)
    elif ('change name' or 'change my name') in query:
        file1 = open('save.txt', 'w')
        speak('please enter your name')
        user = input()
        speak('enter your user name of this p c')
        user_name = input()
        file1.write(user + '\n')
        file1.write(user_name)
        file1.close()
    elif ('close' or 'exit' or 'bye') in query:
        speak('see you soon')
        file1 = open('save.txt', 'w')
        file1.write(user + '\n')
        file1.write(user_name)
        file1.close()
        exit()
    else:
        try:
            client = wolframalpha.Client('<api>')
            res = client.query(query)
            output = next(res.results).text
            speak(output)
        except Exception as e6:
            message_box('info', 'info', str(e6))
            webbrowser.open(query)


root.title('GVK Chinmaya Vidyalaya - Voice Assistant')

frame = tk.Frame(root, width=1080, height=720, bg='black')
frame.pack(fill=tk.BOTH, expand=True)


def theme1():
    label21.config(fg='#015a70')
    label22.config(image=image11)
    label4.config(image='', text='HARI OM', font=('Arial', 20), fg='#015a70')
    label4.place(x=480, y=55)
    clock.config(fg='#015a70')
    date.config(fg='#015a70')
    label5.config(fg='#015a70')
    label6.config(fg='#015a70')
    label23.config(font=('Arial', 18), fg='#015a70')
    label24.config(font=('Arial', 20), fg='#015a70')
    label25.config(font=('Arial', 20), fg='#015a70')


def theme2():
    label21.config(fg='SteelBlue4')
    label22.config(image=image10)
    label4.config(text='', image=image7)
    label4.place(x=380, y=40)
    clock.config(fg='SteelBlue4')
    date.config(fg='SteelBlue4')
    label5.config(fg='SteelBlue4')
    label6.config(fg='SteelBlue4')
    label23.config(font=('Colonna MT', 20), fg='SteelBlue2')
    label24.config(font=('Ravie', 15), fg='DeepSkyBlue4')
    label25.config(font=('Ravie', 15), fg='DeepSkyBlue4')


def about_us():

    def theme3():
        label7.config(font=('Arial', 30), fg='#015a70')
        label8.config(font=('Arial', 25), fg='#015a70')
        label9.config(font=('Arial', 25), fg='#015a70')
        label9.place(x=160, y=60)
        label10.config(font=('Arial', 25), fg='#015a70')
        label11.config(font=('Arial', 25), fg='#015a70')
        label11.place(x=160, y=120)
        label12.config(font=('Arial', 25), fg='#015a70')
        label13.config(font=('Arial', 25), fg='#015a70')
        label13.place(x=160, y=200)
        label14.config(font=('Arial', 25), fg='#015a70')
        label15.config(font=('Arial', 25), fg='#015a70')
        label15.place(x=160, y=260)
        label16.config(font=('Arial', 25), fg='#015a70')
        label17.config(font=('Arial', 25), fg='#015a70')
        label17.place(x=170, y=330)
        button4.config(font=('Arial', 25), fg='#015a70')
        label18.config(image=image8)

    def theme4():
        label7.config(font=('Colonna MT', 30), fg='SteelBlue4')
        label8.config(font=('Elephant', 25), fg='SteelBlue4')
        label9.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label9.place(x=180, y=60)
        label10.config(font=('Elephant', 25), fg='SteelBlue4')
        label11.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label11.place(x=180, y=120)
        label12.config(font=('Elephant', 25), fg='SteelBlue4')
        label13.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label13.place(x=180, y=200)
        label14.config(font=('Elephant', 25), fg='SteelBlue4')
        label15.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label15.place(x=180, y=260)
        label16.config(font=('Elephant', 25), fg='SteelBlue4')
        label17.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label17.place(x=190, y=330)
        button4.config(font=('Arial', 25, 'bold'), fg='SteelBlue4')
        label18.config(image=image12)

    def c_m():

        def theme5():
            label19.config(font=('Arial', 30), fg='#015a70')
            label19.place(x=5, y=5)
            label20.config(fg='#015a70')

        def theme6():
            label19.config(font=('Algerian', 30), fg='SteelBlue4')
            label19.place(x=5, y=5)
            label20.config(fg='SteelBlue4')

        window = tk.Tk()
        window.title('Chinmaya Mission')
        file1 = open('chinmaya mission.txt', 'r')
        text = file1.read()
        frame3 = tk.Frame(window, width=810, height=360, bg='black')
        frame3.pack(fill=tk.BOTH, expand=True)

        label19 = tk.Label(frame3, text='The Chinmaya Mission', font=('Arial', 30), fg='SteelBlue4', bg='black')
        label19.place(x=5, y=5)

        label20 = tk.Label(frame3, text=text, font=('Arial', 10), fg='SteelBlue4', bg='black')
        label20.place(x=5, y=60)
        button8 = tk.Button(frame3, text='T1', bg='black', activebackground='black', border=0,
                            fg='#015a70', activeforeground='#015a70', command=theme5)
        button8.place(x=780, y=300)
        button9 = tk.Button(frame3, text='T2', bg='black', activebackground='black', border=0,
                            fg='SteelBlue4', activeforeground='SteelBlue4', command=theme6)
        button9.place(x=780, y=336)
        window.iconbitmap('New folder/logo5.ico')
        window.mainloop()

    about = tk.Toplevel()

    about.title('About Us')

    frame2 = tk.Frame(about, width=1000, height=666, bg='black')
    frame2.pack(fill=tk.BOTH, expand=True)

    label7 = tk.Label(frame2, text='Developed By', font=('Colonna MT', 30), fg='SteelBlue4', bg='black')
    label7.place(x=5, y=5)

    label8 = tk.Label(frame2, text='Name :', font=('Elephant', 25), fg='SteelBlue4', bg='black')
    label8.place(x=50, y=60)

    label9 = tk.Label(frame2, text='SK.Rohith', font=('Arial', 25, 'bold'), fg='SteelBlue4', bg='black')
    label9.place(x=180, y=60)

    label10 = tk.Label(frame2, text='Class :', font=('Elephant', 25), fg='SteelBlue4', bg='black')
    label10.place(x=50, y=120)

    label11 = tk.Label(frame2, text='12', font=('Arial', 25, 'bold'), fg='SteelBlue4', bg='black')
    label11.place(x=180, y=120)

    label12 = tk.Label(frame2, text='Name :', font=('Elephant', 25), fg='SteelBlue4', bg='black')
    label12.place(x=50, y=200)

    label13 = tk.Label(frame2, text='SK.Althaf', font=('Arial', 25, 'bold'), fg='SteelBlue4', bg='black')
    label13.place(x=180, y=200)

    label14 = tk.Label(frame2, text='Class :', font=('Elephant', 25), fg='SteelBlue4', bg='black')
    label14.place(x=50, y=260)

    label15 = tk.Label(frame2, text='12', font=('Arial', 25, 'bold'), fg='SteelBlue4', bg='black')
    label15.place(x=180, y=260)

    label16 = tk.Label(frame2, text='School :', font=('Elephant', 25), fg='SteelBlue4', bg='black')
    label16.place(x=50, y=330)

    label17 = tk.Label(frame2, text='GVK Chinmaya Vidyalaya', font=('Arial', 25, 'bold'), fg='SteelBlue4', bg='black')
    label17.place(x=190, y=330)

    button4 = tk.Button(frame2, text='Chinmaya Mission', border=0, font=('Arial', 25, 'bold'), fg='SteelBlue4',
                        bg='black', activebackground='black', activeforeground='SteelBlue4', command=c_m)
    button4.place(x=340, y=500)

    image8 = ImageTk.PhotoImage(Image.open('New folder/logo4.jpg').resize((230, 392)))
    image12 = ImageTk.PhotoImage(Image.open('New folder/logo2.jpg').resize((230, 392)))
    label18 = tk.Label(frame2, image=image12, width=225, height=387)
    label18.place(x=700, y=25)

    button6 = tk.Button(frame2, text='T1', bg='black', activebackground='black', border=0,
                        fg='#015a70', activeforeground='#015a70', command=theme3)
    button6.place(x=970, y=610)

    button7 = tk.Button(frame2, text='T2', bg='black', activebackground='black', border=0,
                        fg='SteelBlue4', activeforeground='SteelBlue4', command=theme4)
    button7.place(x=970, y=640)

    about.iconbitmap('New folder/logo5.ico')

    about.mainloop()


image1 = ImageTk.PhotoImage(file='New folder/background.jpg')
label1 = tk.Label(frame, image=image1, width=1076, height=716)
label1.place(x=0, y=0)

image2 = ImageTk.PhotoImage(file='New folder/8.jpg')
button1 = tk.Button(frame, image=image2, width=174, height=100, border=0, command=main)
button1.place(x=728, y=194)

image3 = ImageTk.PhotoImage(file='New folder/wish_me.jpg')
button2 = tk.Button(frame, image=image3, width=170, height=100, border=0, command=wish_me)
button2.place(x=728, y=290)

image4 = ImageTk.PhotoImage(file='New folder/10.jpg')
button3 = tk.Button(frame, image=image4, width=172, height=92, border=0, command=root.destroy)
button3.place(x=728, y=400)

image5 = ImageTk.PhotoImage(file='New folder/date.jpg')
label2 = tk.Label(frame, image=image5, width=174, height=76)
label2.place(x=0, y=0)

image6 = ImageTk.PhotoImage(file='New folder/time.jpg')
label3 = tk.Label(frame, image=image6, width=174, height=76)
label3.place(x=893, y=0)

label21 = tk.Label(frame, text='GVK Chinmaya Vidyalaya', font=('Arial', 30), bg='black', fg='SteelBlue4')
label21.place(x=315, y=0)

image10 = ImageTk.PhotoImage(Image.open('New folder/logo2.jpg').resize((60, 100)))
image11 = ImageTk.PhotoImage(Image.open('New folder/logo4.jpg').resize((60, 100)))
label22 = tk.Label(frame, image=image10, width=56, height=96)
label22.place(x=250, y=0)

image13 = ImageTk.PhotoImage(Image.open('New folder/sign1.jpg').resize((80, 80)))
label26 = tk.Label(frame, image=image13, width=76, height=76)
label26.place(x=800, y=5)

image7 = ImageTk.PhotoImage(file='New folder/7.jpg')
label4 = tk.Label(frame, image=image7, bg='black')
label4.place(x=380, y=40)

label5 = tk.Label(root, textvariable=var, fg='SteelBlue4', bg='black')
label5.config(font=("Arial", 13))
label5.place(x=160, y=470)

label6 = tk.Label(root, textvariable=var1, fg='SteelBlue4', bg='black')
label6.config(font=("Arial", 13))
label6.place(x=160, y=500)

clock = tk.Label(frame, font=('Arial', 18), bg='black', fg='SteelBlue4')
clock.place(x=928, y=24)

date = tk.Label(frame, font=('Arial', 16), bg='black', fg='SteelBlue4')
date.place(x=32, y=26)

display_time()
display_date()


def update(ind):
    frame3 = frames[ind % frames1]
    ind += 1
    label.configure(image=frame3)
    root.after(40, update, ind)


frames1 = Image.open('New folder/hud_resize.gif').n_frames
frames = [tk.PhotoImage(file='New folder/hud_resize.gif', format='gif -index %i' % i) for i in range(frames1)]

label = tk.Label(frame, width=226, height=226)
label.place(x=255, y=194)
root.after(0, update, 0)

image9 = ImageTk.PhotoImage(Image.open('New folder/about2.jpg').resize((70, 70)))
button5 = tk.Button(frame, image=image9, border=0, bg='black', width=70, height=70,
                    activebackground='black', command=about_us)
button5.place(x=850, y=625)

button10 = tk.Button(frame, text='T1', bg='black', activebackground='black', border=0,
                     fg='#015a70', activeforeground='#015a70', command=theme1)
button10.place(x=1050, y=660)

button11 = tk.Button(frame, text='T2', bg='black', activebackground='black', border=0,
                     fg='SteelBlue4', activeforeground='SteelBlue4', command=theme2)
button11.place(x=1050, y=690)

label23 = tk.Label(frame, text='Coded by :', font=('Colonna MT', 20), bg='black', fg='SteelBlue2')
label23.place(x=5, y=600)

label24 = tk.Label(frame, text='SK.Rohith', font=('Ravie', 15), bg='black', fg='DeepSkyBlue4')
label24.place(x=5, y=630)

label25 = tk.Label(frame, text='SK.Althaf', font=('Ravie', 15), bg='black', fg='DeepSkyBlue4')
label25.place(x=5, y=660)

root.iconbitmap('New folder/logo5.ico')

root.mainloop()
