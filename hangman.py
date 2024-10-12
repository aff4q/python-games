ordet = "bergen"

antall_liv = 5
liv = []
null_liv = []
liv_nedteller = 0
for i in range(antall_liv):
    liv.append("0 ")

for i in range(antall_liv):
    null_liv.append("X ")

ordet_liste = []
for i in ordet:
    ordet_liste.append(i)

brett_liste = []
for i in ordet:
    brett_liste.append("_ ")

gjettete_bokstaver = []

brett = brett_liste

bokstaver = "abcdefghijklmnopqrstuvwxyzæøå"
bokstaver_liste = []

for i in bokstaver:
    bokstaver_liste.append(i)

#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------

spill = False
while spill == False:

    liv_viser = ""
    for i in liv:
        liv_viser += i
    print(liv_viser)

    liste = ""
    for i in brett_liste:
        liste += str(i)

    print(liste)

    gjildigSvar = False

    while gjildigSvar == False:

        guess = input("gjett en bokstav: ")

        for i in bokstaver_liste:
            if i == guess:
                gjildigSvar = True
                break
        if gjildigSvar == False:
            print("ugyldig svar prøv på nytt")

    if gjildigSvar == True:

        gjett_riktig = False
        gjettet_samme = False

        for x in brett_liste:
            if guess == x:
                print("dette har du allerede gjettet")
                gjett_riktig = True
                gjettet_samme = True
                break
                        
        for z in gjettete_bokstaver:
            if z == guess:
                print("dette har du allerede gjettet")
                gjettet_samme = True
                break
        
        gjettete_bokstaver.append(guess)

        riktig = False

        for i in range(len(ordet_liste)):
            if guess == ordet_liste[i]:
                brett_liste[i] = ordet_liste[i]
                ordet_liste[i]
                riktig = True

        if riktig == True:
            print("riktig---riktig---riktig")

        if riktig == False and gjettet_samme == False:
            liv[liv_nedteller] = "X "
            liv_nedteller = liv_nedteller + 1



    print("")

    if ordet_liste == brett:
        spill = True 
        liste = ""
        for i in brett_liste:
            liste += str(i)
        print(liste)
        for i in range(3):
            print("------DU VANT------DU VANT------DU VANT------")
    
    if liv == null_liv:
        spill = True 
        null_liv_viser = ""
        for i in null_liv:
            null_liv_viser += i
        print(null_liv_viser)
        for i in range(3):
            print("------DU TAPTE------DU TAPTE------DU TAPTE------")



#------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------
