
brett = ["1a","2a","3a","4a","5a","6a","7a","8a"],\
        ["1b","2b","3b","4b","5b","6b","7b","8b"],\
        ["1c","2c","3c","4c","5c","6c","7c","8c"],\
        ["1d","2d","3d","4d","5d","6d","7d","8d"],\
        ["1e","2e","3e","4e","5e","6e","7e","8e"],\
        ["1f","2f","3f","4f","5f","6f","7f","8f"],\
        ["1g","2g","3g","4g","5g","6g","7g","8g"],\
        ["1h","2h","3h","4h","5h","6h","7h","8h"],



spill = True

baater = ["1a", "2a", "1b", "8h"]

hitt_info = ""

#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
while spill == True:
        for rad in brett:
                raden = "| "
                for felt in rad:
                    raden += felt + " | "
                print(raden)
                print("-----------------------------------------")



        print("")

        if hitt_info == False:
               print("DU BOMMA----DU BOMMA")
        elif hitt_info == True:
               print("DU TRAFF----DU TRAFF")
               
        print("")

        guess = input("hvilket felt ligger det en båt i: ")

        print("")


        hitt = False 
        for i in baater:
                if i == guess:
                    baater.remove(i)
                    hitt = True

        if hitt == True:
                hitt_info = True
                for i in range(len(brett)):
                        for x in range(len(brett[i])):
                                if brett[i][x] == guess:
                                        brett[i][x] = "XX"

        if hitt == False:
                hitt_info = False
                for i in range(len(brett)):
                        for x in range(len(brett[i])):
                                if brett[i][x] == guess:
                                        brett[i][x] = "OO"
                            
        if baater == []:
                for i in range(4):
                        print("------DU VANT------DU VANT------DU VANT------")
                spill = False
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------
