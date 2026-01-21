import random
from tkinter import END
from ttkthemes import ThemedTk
from tkinter import ttk


colours=['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
score = 0

window = ThemedTk(theme = 'breeze')
window.configure(themebg = 'breeze')
window.title('Color_Game Python Project Created by JP')
window.geometry('600x500')
window.resizable(False, False)

restart_ = 0

timeleft = 30

def startGame(event):
    global timeleft,restart_, score
    restart_ = 1
    if timeleft == 30:
        countdown()
    elif timeleft == 0:
        timeleft = 29
        score = 0
        countdown()
    nextColour()


def countdown():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        lbl3.config(text='Time left:' + str(timeleft))
        lbl3.after(1000, countdown)



def nextColour():
    global score
    global timeleft
    if timeleft > 0:
        lbl4.config(foreground=str(colours[1]), text=str(colours[0]))
        if txt.get().lower() == colours[1].lower():
            score += 1
            lbl5.config(text='Score: ' + str(score))
            txt.delete(0,END)
            random.shuffle(colours)
            lbl4.config(foreground=str(colours[1]), text=str(colours[0]))




lbl = ttk.Label(window, text='Type in the colour, and not the word text!', font=('Helvetica', 15))
lbl.pack(pady= 10)
lbl2 = ttk.Label(window, text='Press enter to start',font=('Helvetica', 15))
lbl2.pack(pady= 10)
lbl3 = ttk.Label(window, text='Time left:',font=('Helvetica', 15))
lbl3.pack(pady= 10)
lbl4 = ttk.Label(window, text='', font=('Times', 50))
lbl4.pack(pady= 10)
lbl5 = ttk.Label(window, text='Press enter to start',font=('Helvetica', 15))
lbl5.pack(pady= 10)
txt = ttk.Entry(window,width = 30,font=('Helvetica', 15) )
txt.pack(pady= 10)




window.bind('<Return>',startGame)

window.mainloop()