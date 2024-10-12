import tkinter as tk
from tkinter import messagebox
import random

liste_innhold = ["", "", ""],\
                ["", "", ""],\
                ["", "", ""]

listen = ["", "", ""],\
         ["", "", ""],\
         ["", "", ""]

mulige_ai_valg = []

tur = "X"

windu = tk.Tk()

windu.title("tic tac toe")
windu.configure(background="black")

def spillet(row, col):
    global tur
    global mulige_ai_valg
    mulige_ai_valg = []

    if liste_innhold[row][col] == "":
        if tur == "O":
            liste_innhold[row][col] = "O"
            tur = "X"
        else:
            liste_innhold[row][col] = "X"
            tur = "O"
        oppdater_knapp(row, col)


        if tur == "O":
            ai_gjetter()



        if sjekk_vinner("X"):
            x_vinner()
        elif sjekk_vinner("O"):
            o_vinner()
        elif sjekk_uavgjort():
            uavgjort()

def ai_gjetter():
    for i in range(len(liste_innhold)):
        for x in range(len(liste_innhold[i])):
            if liste_innhold[i][x] == "":
                mulige_ai_valg.append([i,x])
    ai_guess = random.randrange(1,len(mulige_ai_valg))
    spillet(mulige_ai_valg[ai_guess][0],mulige_ai_valg[ai_guess][1])

    

def sjekk_vinner(spiller):
    for i in range(3):
        if liste_innhold[i][0] == liste_innhold[i][1] == liste_innhold[i][2] == spiller or \
           liste_innhold[0][i] == liste_innhold[1][i] == liste_innhold[2][i] == spiller:
            return True
    if liste_innhold[0][0] == liste_innhold[1][1] == liste_innhold[2][2] == spiller or \
       liste_innhold[0][2] == liste_innhold[1][1] == liste_innhold[2][0] == spiller:
        return True
    return False

def sjekk_uavgjort():
    for row in liste_innhold:
        if "" in row:
            return False
    return True

def x_vinner():
    messagebox.showinfo("VINNER", "Spiller X har vunnet!")
    windu.quit()

def o_vinner():
    messagebox.showinfo("VINNER", "Spiller O har vunnet!")
    windu.quit()

def uavgjort():
    messagebox.showinfo("UAVGJORT", "ingen vant det er uavgjort!")
    windu.quit()

def oppdater_knapp(row, col):
    knapp = listen[row][col]
    knapp.config(font=("Arial", 90), padx=0 , text=liste_innhold[row][col], background="white")

for i in range(len(listen)):
    for x in range(len(listen[i])):
        listen[i][x] = tk.Button(windu, height="1", width="2", background="white", font=("Arial", 90), padx=0 , command=lambda row=i, col=x: spillet(row, col))
        listen[i][x].grid(row=i, column=x)

windu.mainloop()
