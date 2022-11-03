#I hate how this reads

import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import randint
from PIL import Image, ImageTk
c_score=0
p_score=0
p_choice = 0
c_choice = 0
choice_images = ['rock.png','paper.png','scissors.png','cpu_rock.png','cpu_paper.png','cpu_scissors.png','','','']

root = tk.Tk()
root.geometry("320x180")
root.title('Rock Paper Scissors')
root.resizable(1, 1)
player_image = PhotoImage(file=choice_images[p_choice])
comp_image = PhotoImage(file=choice_images[c_choice+3])

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)



def rock_paper_scissors(player,cpu_choice):
    global c_score
    global p_score
    global c_choice
    global p_choice
    p_choice = player
    c_choice = cpu_choice
    
    if player == 0:
        if cpu_choice == 0:
            print("TIE")
        if cpu_choice == 1:
            print("LOSE")
            c_score = c_score + 1
        if cpu_choice == 2:
            print("WIN")
            p_score = p_score + 1
        print(cpu_choice)
    if player == 1:
        if cpu_choice == 0:
            print("WIN")
            p_score = p_score + 1
        if cpu_choice == 1:
            print("TIE")
        if cpu_choice == 2:
            print("LOSE")
            c_score = c_score + 1
    if player == 2:
        if cpu_choice == 0:
            print("LOSE")
            c_score = c_score + 1
        if cpu_choice == 1:
            print("WIN")
            p_score = p_score + 1
        if cpu_choice == 2:
            print("TIE")
    
    scoreboard = ttk.Label(root, text=(str(p_score)+" | "+str(c_score)))
    scoreboard.grid(column=1, row=0, sticky=tk.N)

    player_image = ImageTk.PhotoImage(Image.open(choice_images[p_choice]))
    comp_image = ImageTk.PhotoImage(Image.open(choice_images[c_choice+3]))
    comp_go.configure(image=comp_image)
    comp_go.image=comp_image
    player_go.configure(image=player_image)
    player_go.image=player_image
    
#Inits Scoreboard
scoreboard = ttk.Label(root, text=(str(p_score)+" | "+str(c_score)))
scoreboard.grid(column=1, row=0, sticky=tk.N)

# Option buttons
rock_button = ttk.Button(root, text="Rock", command=lambda:rock_paper_scissors(0,randint(0,2)))
rock_button.grid(column=1, row=3, sticky=tk.NS, pady=5)

paper_button= ttk.Button(root, text="Paper", command=lambda:rock_paper_scissors(1,randint(0,2)))
paper_button.grid(column=0, row=3, sticky=tk.E, pady=5)

scissors_button = ttk.Button(root, text="Scissors", command=lambda:rock_paper_scissors(2,randint(0,2)))
scissors_button.grid(column=2, row=3, sticky=tk.W, pady=5)



player_go = tk.Label(root,image=player_image)
player_go.grid(column=0,row=1, sticky=tk.W)
comp_go = tk.Label(root,image=comp_image)
comp_go.grid(column=2,row=1, sticky=tk.E)
root.update()

root.mainloop()
