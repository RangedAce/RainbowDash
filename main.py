if __name__ == "__main__":

    import os

    lowercase = False
    uppercase = False
    numbers = False

    lowercase_tab = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    uppercase_tab = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    numbers_tab = ['1','2','3','4','5','6','7','8','9','0']

    os.system("cls")

    def menu_principal():
        choix = None
        print("  ________________________________________")
        print(" / _____________________________________  \\")
        print(" | |                                    | |")
        print(" | | ________                .__        | |")
        print(" | | \______ \ _____    _____|  |__     | |")
        print(" | |  |    |  \\\\__  \  /  ___/  |  \    | |")
        print(" | |  |    `   \/ __ \_\___ \|   Y  \   | |")
        print(" | | /_______  (____  /____  >___|  /   | |")
        print(" | |         \/     \/     \/     \/    | |")
        print(" | |                                    | |")
        print(" | |____________________________________| |")
        print(" \________________________________________/\n")

        print("\n 1. Lancer la création d'une Rainbow table")
        print("___________________________________________\n")
        print(" 0. Quitter\n")
        
        choix = eval(input("Votre choix : "))

        if choix == 1:
            os.system("cls")
            creation_rainbow_table(lowercase, uppercase, numbers)
        if choix == 0:
            quit()
        else:
            os.system("cls")
            menu_principal()
        


    def creation_rainbow_table(lowercase, uppercase, numbers):

        temp = []
        result = ""

        print("  ________________________________________")
        print(" / _____________________________________  \\")
        print(" | |                                    | |")
        print(" | | ________                .__        | |")
        print(" | | \______ \ _____    _____|  |__     | |")
        print(" | |  |    |  \\\\__  \  /  ___/  |  \    | |")
        print(" | |  |    `   \/ __ \_\___ \|   Y  \   | |")
        print(" | | /_______  (____  /____  >___|  /   | |")
        print(" | |         \/     \/     \/     \/    | |")
        print(" | |                                    | |")
        print(" | |____________________________________| |")
        print(" \________________________________________/\n")

        if lowercase == False:
            print(" [ ] 1. Inclure les minuscules")
        if lowercase == True:
            print(" [X] 1. Inclure les minuscules")
        if uppercase == False:
            print(" [ ] 2. Inclure les majuscules")
        if uppercase == True:
            print(" [X] 2. Inclure les majuscules")
        if numbers == False:
            print(" [ ] 3. Inclure les chiffres\n")
        if numbers == True:
            print(" [X] 3. Inclure les chiffres\n")

        print(" 9. Étape suivante")
        print("___________________________________________\n")
        print(" 0. Quitter\n")
        
        choix = eval(input("Votre choix : "))

        if choix == 1:
            lowercase = not lowercase
            os.system("cls")
            creation_rainbow_table(lowercase, uppercase, numbers)
        elif choix == 2:
            uppercase = not uppercase
            os.system("cls")
            creation_rainbow_table(lowercase, uppercase, numbers)
        elif choix == 3:
            numbers = not numbers
            os.system("cls")
            creation_rainbow_table(lowercase, uppercase, numbers)
        elif choix == 0:
            quit()
        elif choix == 9:
            if lowercase == False and uppercase == False and numbers == False:
                print("\n\n\n\n\n\n\nERREUR : Vous devez choisir au moins une catégorie\n\n")
                os.system("cls")
                creation_rainbow_table(lowercase, uppercase, numbers)
            else:
                if lowercase == True:
                    temp += lowercase_tab
                if uppercase == True:
                    temp += uppercase_tab
                if numbers == True:
                    temp += numbers_tab
                
                nb_caracteres = eval(input("\nCombien voulez-vous de caractères ? "))
                print("Création de la rainbow table en cours...")

                if nb_caracteres == 1:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        rainbow_table = open("rainbow_table.txt", "a")
                        rainbow_table.write(result1 + "\n")


                elif nb_caracteres == 2:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            rainbow_table = open("rainbow_table.txt", "a")
                            rainbow_table.write(result2 + "\n")

                elif nb_caracteres == 3:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            for k in range(len(temp)):
                                result3 = result2 + temp[k]
                                rainbow_table = open("rainbow_table.txt", "a")
                                rainbow_table.write(result3 + "\n")

                elif nb_caracteres == 4:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            for k in range(len(temp)):
                                result3 = result2 + temp[k]
                                for l in range(len(temp)):
                                    result4 = result3 + temp[l]
                                    rainbow_table = open("rainbow_table.txt", "a")
                                    rainbow_table.write(result4 + "\n")

                elif nb_caracteres == 5:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            for k in range(len(temp)):
                                result3 = result2 + temp[k]
                                for l in range(len(temp)):
                                    result4 = result3 + temp[l]
                                    for m in range(len(temp)):
                                        result5 = result4 + temp[m]
                                        rainbow_table = open("rainbow_table.txt", "a")
                                        rainbow_table.write(result5 + "\n")
                
                elif nb_caracteres == 6:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            for k in range(len(temp)):
                                result3 = result2 + temp[k]
                                for l in range(len(temp)):
                                    result4 = result3 + temp[l]
                                    for m in range(len(temp)):
                                        result5 = result4 + temp[m]
                                        for n in range(len(temp)):
                                            result6 = result5 + temp[n]
                                            rainbow_table = open("rainbow_table.txt", "a")
                                            rainbow_table.write(result6 + "\n")

                elif nb_caracteres == 7:
                    for i in range(len(temp)):
                        result1 = temp[i]
                        for j in range(len(temp)):
                            result2 = result1 + temp[j]
                            for k in range(len(temp)):
                                result3 = result2 + temp[k]
                                for l in range(len(temp)):
                                    result4 = result3 + temp[l]
                                    for m in range(len(temp)):
                                        result5 = result4 + temp[m]
                                        for n in range(len(temp)):
                                            result6 = result5 + temp[n]
                                            for n in range(len(temp)):
                                                result7 = result6 + temp[n]
                                                rainbow_table = open("rainbow_table.txt", "a")
                                                rainbow_table.write(result7 + "\n")
                
                rainbow_table.close()
        else:
            os.system("cls")
            creation_rainbow_table(lowercase, uppercase, numbers)

        






















menu_principal()