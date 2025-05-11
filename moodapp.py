from tkinter import *
from tkinter import font

gui = Tk()
gui.geometry("600x700")
gui.title("Mood App")
gui.config(background="gray99")
print(font.families())

moods = ["Happy", "Sad", "Relaxed", "Energetic", "Angry"]

songs = {
    "Happy":[
        ("U Cant Touch This", "https://www.youtube.com/watch?v=otCpCn0l4Wo"),
        ("Happy","https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    ],

    "Sad":[
        ("U Cant Touch This", "https://www.youtube.com/watch?v=otCpCn0l4Wo"),
        ("Happy","https://www.youtube.com/watch?v=ZbZSe6N_BXs")
    ]
    
 
 
 
    
}

label1 = Label(gui,text = "How are you feeling today?", bg = "gray99", fg = "gray0", font=("Songti TC",24))
label1.place(x= 190, y=25)

rc = Label(gui,text = "", bg = "gray99", fg = "gray0", font=("Songti TC",24))
rc.place(x=200 ,y=190)

mood_var = StringVar(value="Happy")

r1 = Radiobutton(gui,bg="gray99",text= "Happy", variable= mood_var, value= "Happy")
r2 = Radiobutton(gui,bg="gray99",text= "Sad", variable= mood_var, value= "Sad")
r3 = Radiobutton(gui,bg="gray99",text= "Relaxed", variable= mood_var, value= "Relaxed")
r4 = Radiobutton(gui,bg="gray99",text= "Energetic", variable= mood_var, value= "Energetic")
r5= Radiobutton(gui,bg="gray99",text= "Angry", variable= mood_var, value= "Angry")
r1.place(x=70,y=45)
r2.place(x=70,y=75)
r3.place(x=70,y=105)
r4.place(x=70,y=135)
r5.place(x=70,y=165)

rec = Button(gui,highlightbackground="gray99",fg="gray0",text = "Recommended 🎧",font=("Arial Unicode MS",20))
rec.place(x=200 ,y=170)

prev = Button(gui,highlightbackground="gray99",fg="gray0",text = "Play ▶️",font=("Arial Unicode MS",20))
prev.place(x=230 ,y=270)

gui.mainloop()