from tkinter import *
from tkinter import font
from tkinter import PhotoImage
from PIL import Image, ImageTk
import random, webbrowser


gui = Tk()
image = Image.open("musicimage.jpeg")
image = image.resize((600,320))
image = ImageTk.PhotoImage(image)
gui.geometry("600x320")
gui.title("Mood App")
#gui.config(background="gray99")
imagelabel = Label(gui,image=image)
imagelabel.place(relwidth=1,relheight=1)
print(font.families())

moods = ["Happy", "Sad", "Relaxed", "Energetic", "Workout"]

songs = {
    "Happy":[
        ("U Cant Touch This", "https://www.youtube.com/watch?v=otCpCn0l4Wo"),
        ("Happy","https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    ],

    "Sad":[
        ("Lucid Dreams", "https://www.youtube.com/watch?v=mzB1VGEGcSU"),
        ("Trauma","https://www.youtube.com/watch?v=rlhspn3EhII")
    ],

    "Relaxed":[
        ("Death Bed","https://www.youtube.com/watch?v=4N-WFXpBjpc"),
        ("Candyland", "https://www.youtube.com/watch?v=IhchfhxvPKI")
    ],

    "Energetic":[
        ("Believer","https://www.youtube.com/watch?v=7wtfhZwyrcc"),
        ("Ice Ice Baby","https://www.youtube.com/watch?v=rog8ou-ZepE")
    ],

    "Workout":[
        ("In Da Club","https://www.youtube.com/watch?v=5qm8PH4xAss")
    ]
 
    
}

song= ""
link= ""

def recommend_songs():
    global song, link
    mood = mood_var.get()
    song,link = random.choice(songs[mood])
    rc.config(text=song)

def play_songs():
    global link
    webbrowser.open(link)

label1 = Label(gui,text = "How are you feeling today?", bg = "gray99", fg = "gray0", font=("Songti TC",24))
label1.place(x= 190, y=25)

rc = Label(gui,text = "", bg = "gray99", fg = "gray0", font=("Songti TC",24))
rc.place(x=210 ,y=210)

mood_var = StringVar(value="Happy")

r1 = Radiobutton(gui,bg="gray99",text= "Happy", variable= mood_var, value= "Happy")
r2 = Radiobutton(gui,bg="gray99",text= "Sad", variable= mood_var, value= "Sad")
r3 = Radiobutton(gui,bg="gray99",text= "Relaxed", variable= mood_var, value= "Relaxed")
r4 = Radiobutton(gui,bg="gray99",text= "Energetic", variable= mood_var, value= "Energetic")
r5= Radiobutton(gui,bg="gray99",text= "Workout", variable= mood_var, value= "Workout")
r1.place(x=70,y=45)
r2.place(x=70,y=75)
r3.place(x=70,y=105)
r4.place(x=70,y=135)
r5.place(x=70,y=165)

rec = Button(gui,highlightbackground="gray99",fg="gray0",text = "Recommended 🎧",font=("Arial Unicode MS",20),command=recommend_songs)
rec.place(x=200 ,y=170)

play = Button(gui,highlightbackground="gray99",fg="gray0",text = "Play ▶️",font=("Arial Unicode MS",20),command=play_songs)
play.place(x=230 ,y=270)

gui.mainloop()
