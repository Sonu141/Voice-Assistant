import tkinter as tk
from PIL import Image, ImageTk


def c_m():
    window = tk.Tk()
    window.title('Chinmaya Mission')
    file = open('chinmaya mission.txt', 'r')
    text = file.read()
    frame3 = tk.Frame(window, width=810, height=360, bg='black')
    frame3.pack(fill=tk.BOTH, expand=True)

    label19 = tk.Label(frame3, text='The Chinmaya Mission', font=('Arial', 30), fg='SteelBlue4', bg='black')
    label19.place(x=5, y=5)

    label20 = tk.Label(frame3, text=text, font=('Arial', 10), fg='SteelBlue4', bg='black')
    label20.place(x=5, y=60)
    window.mainloop()


about = tk.Tk()

about.title('About Us')

frame2 = tk.Frame(about, width=1000, height=666, bg='black')
frame2.pack(fill=tk.BOTH, expand=True)

label7 = tk.Label(frame2, text='Developed By', font=('Arial', 30), fg='SteelBlue4', bg='black')
label7.place(x=5, y=5)

label8 = tk.Label(frame2, text='Name :', font=('Arial', 25), fg='SteelBlue4', bg='black')
label8.place(x=50, y=60)

label9 = tk.Label(frame2, text='SK.Rohith', font=('Arial', 25), fg='SteelBlue4', bg='black')
label9.place(x=160, y=60)

label10 = tk.Label(frame2, text='Class :', font=('Arial', 25), fg='SteelBlue4', bg='black')
label10.place(x=50, y=120)

label11 = tk.Label(frame2, text='12', font=('Arial', 25), fg='SteelBlue4', bg='black')
label11.place(x=160, y=120)

label12 = tk.Label(frame2, text='Name :', font=('Arial', 25), fg='SteelBlue4', bg='black')
label12.place(x=50, y=200)

label13 = tk.Label(frame2, text='SK.Althaf', font=('Arial', 25), fg='SteelBlue4', bg='black')
label13.place(x=160, y=200)

label14 = tk.Label(frame2, text='Class :', font=('Arial', 25), fg='SteelBlue4', bg='black')
label14.place(x=50, y=260)

label15 = tk.Label(frame2, text='12', font=('Arial', 25), fg='SteelBlue4', bg='black')
label15.place(x=160, y=260)

label16 = tk.Label(frame2, text='School :', font=('Arial', 25), fg='SteelBlue4', bg='black')
label16.place(x=50, y=330)

label17 = tk.Label(frame2, text='GVK Chinmaya Vidyalaya', font=('Arial', 25), fg='SteelBlue4', bg='black')
label17.place(x=170, y=330)

button4 = tk.Button(frame2, text='Chinmaya Mission', border=0, font=('Arial', 25), fg='SteelBlue4', bg='black',
                    activebackground='black', activeforeground='SteelBlue4', command=c_m)
button4.place(x=340, y=500)

image8 = ImageTk.PhotoImage(file='logo2.jpg')
label18 = tk.Label(frame2, image=image8, width=225, height=387)
label18.place(x=700, y=25)

about.mainloop()
