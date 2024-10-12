import tkinter as tk
import time


class battle_ship():
        def __init__(self):
                self.hoved = tk.Tk()
                self.hoved.title("battle ship")
                self.hoved.configure(background="grey")
                self.hoved.resizable(width=False, height=False)
                self.boot_plasering = [[1, 1], [1, 2], [1, 3]]
                self.teller = 0
                self.brett = []

                self.ramme_brett = tk.Frame(self.hoved, background="blue")
                self.ramme_brett.grid(row=1, column=1)

                self.div_box(1,1)
                self.brett_box(7,7)


# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        def brett_box(self, hoyde, bredde):
                for i in range(hoyde):
                    colonner = []
                    for x in range(bredde):
                        mid = tk.Label(self.ramme_brett, width=4, height=2, background="light grey")
                        mid.grid(row=i, column=x, padx=3, pady=5)
                        mid.bind("<Button-1>", lambda event, i=i, x=x: self.trykking(i, x))
                        colonner.append(mid)
                    self.brett.append(colonner)


                self.hoved.mainloop()

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        def div_box(self, hoyde, bredde):
                for i in range(0, bredde):
                    bottom, top = tk.Label(self.hoved, background="white", width=40, height=0), \
                        tk.Label(self.hoved, background="white", width=40, height=0)

                    bottom.grid(row=(hoyde + 1), column=i + 1, padx=30, pady=30)
                    top.grid(row=0, column=i + 1, padx=30, pady=30)

                for i in range(0, hoyde):
                    venstre, hoyre = tk.Label(self.hoved, background="white", width=1, height=23), \
                        tk.Label(self.hoved, background="white", width=1, height=23)

                    venstre.grid(row=i + 1, column=0, padx=30, pady=30)
                    hoyre.grid(row=i + 1, column=(bredde + 1), padx=30, pady=30)

                for i in range(4):
                    ting = tk.Label(self.hoved, background="white", width=2, height=2)
                    if i == 0:
                        ting.grid(row=0, column=0, padx=4, pady=4)
                    elif i == 1:
                        ting.grid(row=0, column=(bredde + 1), padx=4, pady=4)
                    elif i == 2:
                        ting.grid(row=(hoyde) + 1, column=(bredde + 1), padx=4, pady=4)
                    else:
                        ting.grid(row=(hoyde + 1), column=0, padx=4, pady=4)

# _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        def trykking(self, i, x):
                guess = [int(i)+1, int(x)+1]
                riktig_treff = False

                for i in self.boot_plasering:
                    if guess == i:
                        self.boot_plasering.remove(i)

                        if self.boot_plasering == []:
                            if self.teller > 15:
                                print (f"-_-_-_-_WOW ER DU DUM, {self.teller} ANTALL TREKK_-_-_-_-")
                            elif self.teller <= 15:
                                print(f"-_-_-_-_GRATULERER, {self.teller} ANTALL TREKK_-_-_-_-")

                            time.sleep(4)
                            self.hoved.destroy()

                        riktig_treff = True

                if riktig_treff:
                    self.teller += 1
                    self.brett[guess[0]-1][guess[1]-1] = tk.Label(self.ramme_brett, width=4, height=2, background="red")
                    self.brett[guess[0]-1][guess[1]-1].grid(row=guess[0]-1, column=guess[1]-1)
                    print(f"-_-_-_-_-_DU TRAFF trekk nr.{self.teller}_-_-_-_-_-")
                else:
                    self.teller += 1
                    self.brett[guess[0]-1][guess[1]-1] = tk.Label(self.ramme_brett, width=4, height=2, background="blue")
                    self.brett[guess[0]-1][guess[1]-1].grid(row=guess[0]-1, column=guess[1]-1)
                    print(f"-_-_-_-_-_DU BOMMA trekk nr.{self.teller}_-_-_-_-_-")


battle_ship()

