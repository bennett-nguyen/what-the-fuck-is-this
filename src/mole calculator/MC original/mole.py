import time

End1 = "\n ==> This program will stop executing. Thanks for using my program.\n"
End2 = "\n ==> This program will stop executing (because you broke it). Thanks for using my program.\n"
Error1 = "\n ==> Invalid input. The number you entered must be a positive number!\n"
Error2 = "\n ==> Invalid input. Check these 3 things if you wished to see what you did wrong.\n1. The input only takes number not text!\n2. “Molar mass” must be an integer (Whole number).\n3. If you’re entering a decimal number, please use “.” instead of “,” (Example: “2.5” not “2,5”).\n"
Error3 = "\n ==> Invalid input. The input only takes number not text!\n"
Error4 = "\n ==> Invalid input. Check these 2 things if you wished to see what you did wrong.\n1. The input only takes number not text!\n2. If you’re entering a decimal number, please use “.” instead of “,” (Example: “2.5” not “2,5”)\n"

def Introduction_1():
    running = True
    def Introduction_2():
        print("\nWelcome to Introduction, you can get some information about this program in here.\n")
        time.sleep(3)
        print("\nWhat would you like to know about?\n1. What is chemistry?\n2. Mole introduction\n3. What can I do with “Calculator”?\n4. What can I do with “Gases’s molar masses comparison”?\n5. Credits\n")
        time.sleep(3)
        Decision6 = input("1/2/3/4/5:  ")
        if Decision6 == "1":
            print("What is Chemistry?\nChemistry, a branch of natural science, this industry studies about composition, structure, properties, and change of matter. Chemistry refers to the elements, compounds, atoms, molecules, and chemical reactions that occur between those components.\nThe importance of Chemistry:\n- Chemical reactions that occur in everyday life such as during cooking, baking or frying in which metamorphosis takes place in a very complex way contribute to the characteristic flavor of the dish. In addition food is broken down into separate ingredients and also converted into energy.\n- The chemical industry is a very important economic sector. The chemical industry produces from basic chemicals such as sulfuric acid or ammonia, often several million tons annually, to fertilizers and plastics and other aspects of industrial life. On the other hand, the chemical industry also produces a lot of complex compounds, especially pharmaceuticals. Without industrially produced chemicals, it would be impossible to manufacture computers or fuels and lubricants for the automotive industry.\n")
            running = True
            time.sleep(15)
        elif Decision6 == "2":
            print("Have you ever wondered how many atoms/molecules in the universe (or at least in a certain object) ? Well scientists wanted to answer that question as well like how do you count something that is small as an atom?\nIn chemistry, there is something that helps you to do that job and it’s called “mole” and a mole is equal to 6x10^23. This idea was came up by Avogadro in 1811, he thought that if he has equal volumes of gases and put it in the environment that has the same temperature and pressure, they would contain the same amount of particles. Since Avogadro was the man who came up with this idea, scientists named this number after his name and now we call it “Avogadro’s Number”. When you go shopping for food, you don’t buy 54 slices of meat, instead you buy your meat by the pound (or kilogram), when you buy your eggs, you buy a dozen eggs. When we hear the word “dozen” we will think of the number 12, a baker’s dozen is 13, a gross is 144, a ream is 500 and a mole act the same way, it’s 6x10^23. Then how big is a mole? Or you can say: “How big is 6x10^23”. Let’s say for example if humanity have 6x10^23 grains of rice. It would take 20 million years for humanity to eat a mole of rice, another example if you were born with 1 mol of pennies and you spend 1 millon dollars per second and die at age 100... well there are still more than 99.99% money left in your bank.\nWhat’s the use of it in chemistry?\nWell mole is the most important part in chemistry, it allows you to calculate mass of a certain substance more easier, use to count atoms/molecules (of course), or even use to calculate the concentration of a solution.\n")
            running = True
            time.sleep(15)
        elif Decision6 == "3":
            print("In “calculator”, you can calculate stuff such as mass, molar mass, volume, mole.\nAlso here is the list that you need to be aware when you enter a value to the calculator:\nMol, Volume, Mass:\n- The following input only take numbers value (not text value)\n- The following input must be a positive number (Neither zero nor negative)\n- If an error occurred when you typed in a decimal number, check the syntax and use “.” not “,” (“2.5” not 2,5”)\nMolar mass:\n- Molar mass’s input only takes whole numbers not a decimal numbers (integer not float)\n- All of things I listed above\n")
            running = True
            time.sleep(7)
        elif Decision6 == "4":
            print("In “Gases’s molar masses comparison”, you can check which gas is heavier than the other one and it’s heavier for how many times by using that gas’s molar mass.")
            running = True
            time.sleep(7)
        elif Decision6 == "5":
            print("Chemistry program (Official Version)\nCreated by Bennett E. Tabasco.\n") # <-- my old name lol
            running = True
            time.sleep(2)
        else:
            print(End2)
            running = False
    while running:
        N = input("Do you want to continue?(y/n): ")
        if N == "y":
            Introduction_2()
            running = True
        elif N == "n":
            N2 = input("Return to the main page?(y/n): ")
            running = False
            if N2 == "y":
                Main_page()
                running = False
            elif N2 == "n":
                print(End1)
                running = False
            else:
                print(End1)
                running = False
        else:
            print(End2)
            running = False

def Calculator():
    def Mol1():
        print("n = m / M")
        try:
            Mass = float(input("Enter mass (g): "))
            Molar_mass = int(input("Enter molar mass (g/mol): "))
            if Mass > 0 and Molar_mass > 0:
                print("n = " + str(Mass) + " / " + str(Molar_mass) + " = " + str(round(Mass / Molar_mass, 3)) + " (mol)")
            else:
                print(Error1)
        except:
            print(Error2)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Mol2():
        print("n = V / 22.4")
        try:
            Volume1 = float(input("Enter volume (l): "))
            if Volume1 > 0:
                print("n = " + str(Volume1) + " / 22.4 " + " = " + str(round(Volume1 / 22.4, 3)) + " (mol)")
            else:
                print(Error1)
        except:
            print(Error4)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Mol3():
        print("n = V / 24 (Normal codition)")
        try:
            Volume2 = float(input("Enter volume (l): "))
            if Volume2 > 0:
                print("n = " + str(Volume2) + " / 24 " + " = " + str(round(Volume2 / 24, 3)) + " (mol)")
            else:
                print(Error1)
        except:
            print(Error4)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Mass():
        print("m = n * M ")
        try:
            Mole1 = float(input("Enter mole (mol): "))
            Molar_mass = int(input("Enter molar mass (g/mol): "))
            if Mole1 > 0 and Molar_mass > 0:
                print("m = " + str(Mole1) + " * " + str(Molar_mass) + " = " + str(round(Mole1 * Molar_mass, 3)) + " (g)\n")
            else:
                print(Error1)
        except:
            print(Error2)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Molar_mass():
        print("M = m / n")
        try:
            Mass = float(input("Enter mass (g): "))
            Mole69 = float(input("Enter mol (mol): "))
            if Mass > 0 and Mole69 > 0:
                print("M = " + str(Mass) + " / " + str(Mole69) + " = " + str(round(Mass / Mole69, 3)) + " (g/mol)")
            else:
                print(Error1)
        except:
            print(Error2)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Volume_Through_Standard():
        print("V = n * 22.4")
        try:
            Mole3 = float(input("Enter mole (mol): "))
            if Mole3 > 0:
                print("V = " + str(Mole3) + " * 22.4 " + " = " + str(round(Mole3 * 22.4, 3)) + " (l)")
            else:
                print(Error1)
        except:
            print(Error4)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Volume_Through_Normal():
        print("V = n * 24")
        try:
            Mole4 = float(input("Enter mole (mol): "))
            if Mole4 > 0:
                print("V = " + str(Mole4) + " * 24 " + " = " + str(round(Mole4 * 24, 3)) + " (l)")
            else:
                print(Error1)
        except:
            print(Error4)
        time.sleep(2)
        Choice = input("Try again?(y/n): ")
        if Choice == "y":
            Decision()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main_page()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End2)

    def Decision():
        print("\nChoose one of these formulas below to begin:\n1. n = m / M (Calculate mole by using mass divide by molar mass)\n2. n = V / 22.4 (Calculate mole in standard condition)\n3. n = V / 24 (Calculate mole in normal condition)\n4. m = n * M (Calculate mass by using mole times molar mass)\n5. M = m / n (Calculate molar mass by using mass divide by mole)\n6. V = n * 22.4 (Calculate gas’s volume in standard condition)\n7. V = n * 24 (Calculate gas’s volume in normal condition)")
        time.sleep(4)
        D = input("1/2/3/4/5/6/7: ")
        if D == "1":
            Mol1()
        elif D == "2":
            Mol2()
        elif D == "3":
            Mol3()
        elif D == "4":
            Mass()
        elif D == "5":
            Molar_mass()
        elif D == "6":
            Volume_Through_Standard()
        elif D == "7":
            Volume_Through_Normal()
        else:
            print(End2)
    print("\nChemistry symbols and their units:\nn: Mole (mol)\nM: Molar mass (g/mol)\nm: Mass (g)\nV: Volume (l)\nN: Avogadro’s number (6.02x10^23)\n")
    time.sleep(3)
    Decision()

def gases_molarmass_comparision():
    print("\n")
    gases_dict = {
        "H2": 2,
        "He": 4,
        "Ne": 20,
        "N2": 28,
        "CO": 28,
        "Air": 29,
        "O2": 32,
        "H2S": 34,
        "HCl": 36.5,
        "F2": 38,
        "Ar": 39.9,
        "CO2": 44,
        "N2O": 44,
        "NO2": 46,
        "SO2": 64,
        "Cl2": 71,
        "Xr": 84,
        "Xe": 131,
        "Br2": 160,
        "Rn": 222,
}
    for gases in gases_dict:
        print(gases)
    print("\n")
    time.sleep(3)
    print("Select 2 gases from the gases list above to compare.")
    Gas1 = str(input("Enter first gas’s name: "))
    Gas2 = str(input("Enter second gas’s name: "))
    try:
        Gas_1 = gases_dict[Gas1]
        Gas_2 = gases_dict[Gas2]
        Result = (Gas_1 / Gas_2)
        Comparison_value = round(Result, 3)
        if Result > 1:
            print(Gas1 + " is " + str(Comparison_value) + " times heavier than " + Gas2)
        elif Result < 1:
            print(Gas1 + " is " + str(Comparison_value) + " times lighter than " + Gas2)
        elif Result == 1:
            print(Gas1 + " has the same molar mass as " + Gas2)
    except:
        print("Please enter a gas’s name.")
    time.sleep(2)
    Ask3 = input("Try again?(y/n): ")
    if Ask3 == "y":
        gases_molarmass_comparision()
    elif Ask3 == "n":
        Ask4 = input("Return to the main page?(y/n): ")
        if Ask4 == "y":
            Main_page()
        else:
            print(End1)

def Main_page():
    print("Choose your destination:\n1. Introduction.\n2. Calculator\n3. Gases’s molar masses comparison\n4. End the program (press any key)")
    D3 = input("1/2/3: ")
    if D3 == "1":
        Introduction_1()
    elif D3 == "2":
        Calculator()
    elif D3 == "3":
        gases_molarmass_comparision()
    else:
        print(End1)

Main_page() #<—- This will activate the code