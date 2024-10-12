import tkinter as tk
import random


class hoved():
    def __init__(self):
        self.vindu = tk.Tk()
        self.vindu.title("SNAKE")
        self.vindu.bind("<Key>", self.on_key_press)
        self.vindu.resizable(width=False, height=False)
        self.brettet = tk.Frame(self.vindu, background="black")
        self.brettet.grid(row=1, column=1)
        self.div_box(1, 1)

        self.hoyde = int(20)
        self.bredde = int(20)
        self.brett = []
        self.slange_posisjon = [
            str(f"{int(self.hoyde / 2)}x{int((self.bredde / 2) - 3)}"),
            str(f"{int(self.hoyde / 2)}x{int((self.bredde / 2) - 2)}"),
            str(f"{int(self.hoyde / 2)}x{int((self.bredde / 2) - 1)}"),
            str(f"{int(self.hoyde / 2)}x{int((self.bredde / 2) - 0)}")

        ]
        self.spill_hastighet = 400
        self.current_key = ""
        self.eple_posisjon = ""
        self.sving_husker = []

        self.brettlager()
        self.slange_genererer()
        self.epple_generer()



        self.vindu.mainloop()

    def spill_oppdaterer(self, retning):
        if self.slange_posisjon[-1] == self.eple_posisjon:
            self.slange_posisjon.append(self.eple_posisjon)
            self.slange_genererer()
            self.epple_generer()

        bak_rad = int(self.slange_posisjon[0].split("x")[0])
        bak_kol = int(self.slange_posisjon[0].split("x")[1])
        mid_bak = tk.Label(self.brettet, width=2, height=1, background="black")
        mid_bak.grid(row=bak_rad, column=bak_kol)

        for i in range(len(self.slange_posisjon)):
            if i < len(self.slange_posisjon)-1:
                mid_mid = self.slange_posisjon[i+1].split("x")
                self.slange_posisjon[i] = f"{int(mid_mid[0])}x{int(mid_mid[1])}"
        print(int(self.slange_posisjon[-1].split("x")[0]) == -1 or int(
            self.slange_posisjon[-1].split("x")[1]) == -1 or int(
            self.slange_posisjon[-1].split("x")[0]) == self.hoyde - 1 or int(
            self.slange_posisjon[-1].split("x")[1]) == self.bredde - 1)

        if int(self.slange_posisjon[-1].split("x")[0]) == -1 or int(
                self.slange_posisjon[-1].split("x")[1]) == -1 or int(
                self.slange_posisjon[-1].split("x")[0]) == self.hoyde - 1 or int(
                self.slange_posisjon[-1].split("x")[1]) == self.bredde - 1:
            self.vindu.quit()
            for i in range(25):
                print("")
            print(f"du hadde lengde {len(self.slange_posisjon)}")
            print("")
        else:
            if retning == "opp":
                hode_rad = int(self.slange_posisjon[-1].split("x")[0]) - 1
                hode_kol = int(self.slange_posisjon[-1].split("x")[1])
                self.slange_posisjon[-1] = f"{hode_rad}x{hode_kol}"
            elif retning == "ned":
                hode_rad = int(self.slange_posisjon[-1].split("x")[0]) + 1
                hode_kol = int(self.slange_posisjon[-1].split("x")[1])
                self.slange_posisjon[-1] = f"{hode_rad}x{hode_kol}"
            elif retning == "hoyre":
                hode_rad = int(self.slange_posisjon[-1].split("x")[0])
                hode_kol = int(self.slange_posisjon[-1].split("x")[1]) + 1
                self.slange_posisjon[-1] = f"{hode_rad}x{hode_kol}"
            elif retning == "venstre":
                hode_rad = int(self.slange_posisjon[-1].split("x")[0])
                hode_kol = int(self.slange_posisjon[-1].split("x")[1]) - 1
                self.slange_posisjon[-1] = f"{hode_rad}x{hode_kol}"

            self.slange_genererer()


    def slange_genererer(self):
        for i in self.slange_posisjon:
            mid = tk.Label(self.brettet, width=2, height=1, background="blue")
            mid.grid(row=(i.split("x"))[0], column=(i.split("x"))[1])

    def epple_generer(self):
        eple = tk.Label(self.brettet, width=2, height=1, background="red")
        tilfelig_rad = random.randint(0, self.hoyde-1)
        tilfelig_kol = random.randint(0, self.bredde-1)
        self.eple_posisjon = f"{tilfelig_rad}x{tilfelig_kol}"
        eple.grid(row=tilfelig_rad, column=tilfelig_kol)

    def oppover_piltast(self):
        if self.current_key == "beveg_oppover":
            print("opp")
            self.spill_oppdaterer("opp")
            self.vindu.after(self.spill_hastighet, self.oppover_piltast)

    def nedover_piltast(self):
        if self.current_key == "beveg_nedover":
            print("ned")
            self.spill_oppdaterer("ned")
            self.vindu.after(self.spill_hastighet, self.nedover_piltast)

    def hoyre_piltast(self):
        if self.current_key == "beveg_hoyre":
            print("hoyre")
            self.spill_oppdaterer("hoyre")
            self.vindu.after(self.spill_hastighet, self.hoyre_piltast)

    def venstre_piltast(self):
        if self.current_key == "beveg_venstre":
            print("venstre")
            self.spill_oppdaterer("venstre")
            self.vindu.after(self.spill_hastighet, self.venstre_piltast)




    def on_key_press(self, event):
        if event.keysym == "Up":
            if self.current_key != "beveg_nedover" and self.current_key != "beveg_oppover":
                self.current_key = "beveg_oppover"
                self.oppover_piltast()

        elif event.keysym == "Down":
            if self.current_key != "beveg_oppover" and self.current_key != "beveg_nedover":
                self.current_key = "beveg_nedover"
                self.nedover_piltast()

        elif event.keysym == "Right":
            if self.current_key != "beveg_venstre" and self.current_key != "beveg_hoyre":
                self.current_key = "beveg_hoyre"
                self.hoyre_piltast()

        elif event.keysym == "Left":
            if self.current_key != "beveg_hoyre" and self.current_key != "beveg_venstre":
                self.current_key = "beveg_venstre"
                self.venstre_piltast()




#-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

    def brettlager(self):
        for i in range(self.hoyde):
            for x in range(self.bredde):
                mid = tk.Label(self.brettet, width=2, height=1 ,background="black")
                mid.grid(row=i, column=x)
                self.brett.append(mid)

    def div_box(self, hoyde, bredde):
        for i in range(0, bredde):
            bottom, top = tk.Label(self.vindu, background="white", width=40, height=0), \
                tk.Label(self.vindu, background="white", width=40, height=0)

            bottom.grid(row=(hoyde + 1), column=i + 1, padx=30, pady=30)
            top.grid(row=0, column=i + 1, padx=30, pady=30)

        for i in range(0, hoyde):
            venstre, hoyre = tk.Label(self.vindu, background="white", width=1, height=23), \
                tk.Label(self.vindu, background="white", width=1, height=23)

            venstre.grid(row=i + 1, column=0, padx=30, pady=30)
            hoyre.grid(row=i + 1, column=(bredde + 1), padx=30, pady=30)

        for i in range(4):
            ting = tk.Label(self.vindu, background="white", width=2, height=2)
            if i == 0:
                ting.grid(row=0, column=0, padx=4, pady=4)
            elif i == 1:
                ting.grid(row=0, column=(bredde + 1), padx=4, pady=4)
            elif i == 2:
                ting.grid(row=(hoyde) + 1, column=(bredde + 1), padx=4, pady=4)
            else:
                ting.grid(row=(hoyde + 1), column=0, padx=4, pady=4)


hoved()