from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from PIL import ImageTk,Image
from string import ascii_lowercase
import random
from tkinter.font import Font

root=Tk()
root.title("Wordle")
root.iconbitmap(r'images\iconimage.ico')
window_width = 760
window_height = 717
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
xcord = (screen_width / 2) - (window_width / 2)
ycord = (screen_height / 2) - (window_height / 2)
root.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
root.config(bg = "white")

entry = Entry(root, width = 35, borderwidth=1, relief = "solid", bg = "#d3d3d3")
entry.grid(row=6, column=2, columnspan=3, ipady = 17, padx=5, pady=8, ipadx = 4)
cnt = 0
   

def play():
    play = Toplevel()
    play.title("Wordle")
    play.iconbitmap(r"images\iconimage.ico")
    window_width = 800
    window_height = 717
    screen_width = play.winfo_screenwidth()
    screen_height = play.winfo_screenheight()
    xcord = (screen_width / 2) - (window_width / 2)
    ycord = (screen_height / 2) - (window_height / 2)
    play.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
    exitbutton = Button(play, text = "PLAY", bg = "#6baa64" , fg = "white", relief = "solid", borderwidth = 1, activebackground = "#6baa64", activeforeground = "white", font= ('Helvetica 30 bold'), command = play.destroy)
    exitbutton.place(relx=.5, rely=0.8,anchor= CENTER)
    my_img1 = ImageTk.PhotoImage(Image.open("images\WordleTitleScreen.png"))
    my_label = Label(play, image=my_img1)
    my_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    my_label.image = my_img1

play()

def notwordprompt():
    top = Toplevel()
    top.title("Wordle")
    top.geometry("100x90")
    window_width = 500
    window_height = 350
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    xcord = (screen_width / 2) - (window_width / 2)
    ycord = (screen_height / 2) - (window_height / 2)
    top.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
    top.iconbitmap(r"images\iconimage.ico")
    my_img1 = ImageTk.PhotoImage(Image.open("images\wordleincorrect.png"))
    my_label = Label(top, image=my_img1)
    my_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    my_label.image = my_img1
    my_font = Font(family="Segoe UI", size=26)
    lbl = Label(top, text = "This is not a word!", font = ("Bahnschrift 25 bold"), fg = "red")
    lbl.place(relx=0.5, rely=0.9, anchor=CENTER)

def congratulations():
    global top
    top = Toplevel()
    top.title("Congratulations!")
    window_width = 520
    window_height = 530
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    xcord = (screen_width / 2) - (window_width / 2)
    ycord = (screen_height / 2) - (window_height / 2)
    top.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
    top.iconbitmap(r"images\iconimage.ico")
    my_img1 = ImageTk.PhotoImage(Image.open("images\wordletrophy.png"))
    my_label = Label(top, image=my_img1)
    my_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    my_label.image = my_img1
    lbl = Label(top, text = "\U0001F389 You guessed the word! \U0001F389\n You Win!", font = ("Bahnschrift 25 bold"), fg = "#6baa64")
    lbl.place(relx=0.5, rely=0.7, anchor=CENTER)
    redo = Button(top, text = "Play Again", relief = "solid", borderwidth = 1, font = ("Bahnschrift 25 bold"), bg = "#6baa64", fg = "white", activebackground = "#6baa64", activeforeground = "white", command = playagain)
    redo.place(relx=0.5, rely=0.88, anchor=CENTER)

def loser():
    global top
    top = Toplevel()
    top.title("Game Over!")
    window_width = 500
    window_height = 500
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    xcord = (screen_width / 2) - (window_width / 2)
    ycord = (screen_height / 2) - (window_height / 2)
    top.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
    top.iconbitmap(r"images\iconimage.ico")
    my_img1 = ImageTk.PhotoImage(Image.open("images\wordleincorrect.png"))
    my_label = Label(top, image=my_img1)
    my_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    my_label.image = my_img1
    lbl = Label(top, text = "You Lose!\n The word was: " + goal, font = ("Bahnschrift 25 bold"), fg = "red")
    lbl.place(relx=0.5, rely=0.7, anchor=CENTER)
    redo = Button(top, text = "Play Again", font = ("Bahnschrift 18 bold"), relief = "solid", borderwidth = 1, bg = "red", fg = "white", activebackground = "red", activeforeground = "white", command = playagain)
    redo.place(relx=0.5, rely=0.85, anchor=CENTER)

def notwordlength():
    top = Toplevel()
    top.title("Error!")
    window_width = 500
    window_height = 350
    screen_width = top.winfo_screenwidth()
    screen_height = top.winfo_screenheight()
    xcord = (screen_width / 2) - (window_width / 2)
    ycord = (screen_height / 2) - (window_height / 2)
    top.geometry(f'{window_width}x{window_height}+{int(xcord)}+{int(ycord)}')
    top.iconbitmap(r"images\iconimage.ico")
    my_img1 = ImageTk.PhotoImage(Image.open("images\wordleincorrect.png"))
    my_label = Label(top, image=my_img1)
    my_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    my_label.image = my_img1
    lbl = Label(top, text = "Word should be 5 letters long!", font = ("Bahnschrift 25 bold"), fg = "red")
    lbl.place(relx=0.5, rely=0.9, anchor=CENTER)

def generateword():
    with open('wordledictionary.txt') as file:
        lines = file.readlines()
        word = lines[random.randrange(0, len(lines))]
    return word
    file.close()

global goal
goal = generateword()
w = []
n= []

def dupCheck():
    global goal
    global w
    global n
    letters = []
    for i in range(5):
        letters.append(goal[i])

    word = list(set(letters))
    nums = [0 for i in range(len(word))]
    for i in range (5):
        nums[word.index(goal[i])] += 1
   
    w = word
    n = nums
    return nums

dupCheck()
   
def submit():
    global cnt
    global goal
    global buttons
    global keyboard
    global w
    global n
    nums = []
    nums = n
    win = 0
    flag = False
    guess = entry.get()
    if len(guess) != 5:
        flag = False
        entry.delete(0, END)
        notwordlength()
    else:
        with open('wordledictionary.txt') as file:
            lines = file.readlines()
            for i in range(len(lines)):
                if guess == lines[i]:
                    flag = True
                    break
                elif (guess + "\n")== lines[i]:
                    flag = True
                    break
                else:
                    entry.delete(0, END)
            if flag != True:
                notwordprompt()
    if flag:
        nums = dupCheck()
        for i in range(5):
            if guess[i] == goal[i] and n[w.index(goal[i])] != 0:
                buttons[cnt][i].config(text=guess[i].upper(), bg="#6baa64", fg = "white")
                buttons[cnt][i].config(font=("Bahnschrift 10 bold"), height = 2, width = 3)
                nums[w.index(guess[i])] -= 1
                for k in range(26):
                    if guess[i] == qwerty[k].lower():
                        keyboard[k].config(bg = "#6baa64", fg = "white")
                        keyboard[k].config(font=("Bahnschrift 10 bold"))
                win += 1
       
        for i in range(5):
            if goal.find(guess[i]) != -1 and nums[w.index(guess[i])] != 0 and buttons[cnt][i]["bg"] != "#6baa64":
                for j in range(5):
                    if guess[i] == goal[j]:
                        buttons[cnt][i].config(text=guess[i].upper(), bg="#C2B76A", fg = "white")
                        buttons[cnt][i].config(font=("Bahnschrift 10 bold"))
                        nums[w.index(guess[i])] -= 1
                        for k in range(26):
                            if guess[i] == qwerty[k].lower() and keyboard[k]["bg"] != "#6baa64":
                                keyboard[k].config(bg = "#C2B76A", fg = "white")
                                keyboard[k].config(font=("Bahnschrift 10 bold"))
                       
        for i in range(5):
            if buttons[cnt][i]["bg"] != "#6baa64" and buttons[cnt][i]["bg"] != "#C2B76A":
                buttons[cnt][i].config(text=guess[i].upper(), bg="gray", fg = "white")
                buttons[cnt][i].config(font=("Bahnschrift 10 bold"))
                for k in range(26):
                    if guess[i] == qwerty[k].lower() and keyboard[k]["bg"] != "#6baa64" and keyboard[k]["bg"] != "#C2B76A":
                        keyboard[k].config(bg = "gray", fg = "white")
                        keyboard[k].config(font=("Bahnschrift 10 bold"))
           
        if win == 5:
            congratulations()
            submit.config(state = DISABLED)
           
        entry.delete(0, END)
        cnt += 1

        if cnt == 6 and win !=5:
            loser()
            submit.config(state = DISABLED)
           
#user interface
buttons = [[0 for i in range(5)] for j in range(6)]
button = [[0 for i in range(5)] for j in range(6)]
for x in range(6):
    for y in range(5):
        buttons[x][y] = Label(root, text="", borderwidth = 1, bg = "white", relief = "solid", height = 2, width = 3)
        buttons[x][y].grid(row=x, column=y + 2, ipadx=20, ipady=15, padx=3, pady=2)

submit = Button(root, text="Enter", relief = "solid", borderwidth = 1, bg = "#d3d3d3", command=submit)
submit.grid(row=6, column=5, columnspan=2, ipady=15, ipadx=50, padx=10, pady=8)

keyboard = [0 for i in range(26)]
qwerty = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
          'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
          'Z', 'X', 'C', 'V', 'B', 'N', 'M']

for i in range(10):
    keyboard[i] = Label(root, text=qwerty[i], bd = 1, relief = "solid", bg = "#d3d3d3", font=("Bahnschrift 10 bold"))
    keyboard[i].grid(row=7, column=i, ipadx=25, ipady=5, padx=5, pady=5)

for i in range(10, 19, 1):
    keyboard[i] = Label(root, text=qwerty[i], bd = 1, relief = "solid", bg = "#d3d3d3", font=("Bahnschrift 10 bold"))
    keyboard[i].grid(row=8, column=i - 10, ipadx=25, ipady=5, padx=5, pady=5)
   
for i in range(19, 26, 1):
    keyboard[i] = Label(root, text=qwerty[i], bd = 1, relief = "solid", bg = "#d3d3d3", font=("Bahnschrift 10 bold"))
    keyboard[i].grid(row=9, column=i - 18, ipadx=25, ipady=5, padx=5, pady=5)

def playagain():
    top.destroy()
    global cnt
    global goal
    goal = generateword()
    cnt = 0
    for x in range(6):
        for y in range(5):
            buttons[x][y].config(bg = "white", text = "")
    for i in range(10):
        keyboard[i].config(bg = "#d3d3d3", fg = "black", font=("Bahnschrift 10 bold"))

    for i in range(10, 19, 1):
        keyboard[i].config(bg = "#d3d3d3", fg = "black")
       
    for i in range(19, 26, 1):
        keyboard[i].config(bg = "#d3d3d3", fg = "black")
   
    submit.config(state = NORMAL)

root.mainloop()
