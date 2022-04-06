from time import sleep
from extensions import *

#-- Extensions
def IntroductionDecisionMaker(f):
    def wrapper():
        f()
        sleep(2)
        Choice = input("\nDo you want to read more?(y/n): ")
        if Choice == "y":
            Introduction()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End1)

    return wrapper

def MolDecisionMaker(f):
    def wrapper():
        f()
        sleep(2)
        Choice = input("\nTry again?(y/n): ")
        if Choice == "y":
            Calculator()
        elif Choice == "n":
            Choice2 = input("Return to the main page?(y/n): ")
            if Choice2 == "y":
                Main()
            elif Choice2 == "n":
                print(End1)
            else:
                print(End1)
        else:
            print(End1)
    return wrapper
#---

def Introduction():

    @IntroductionDecisionMaker 
    def ChemistryIntroduction():
        print("\nThe concept about Chemistry:\n")
        print("Chemistry is the science that deals with the properties, composition, and structure of substances (defined as elements and compounds), the transformations they undergo, and the energy that is released or absorbed during these processes.\n")
        print("Chemistry's Roles:\n")
        print("Chemistry will help us solve many future problems, including sustainable energy and food production, managing our environment, providing safe drinking water and promoting human and environmental health.\n")
        print("Because it is so fundamental to our world, chemistry plays a role in everyone's lives and touches almost every aspect of our existence in some way. Chemistry is essential for meeting our basic needs of food, clothing, shelter, health, energy, and clean air, water, and soil.")
    
    @IntroductionDecisionMaker
    def MoleIntroduction():
        print("\nMole Concept:\n")
        print("In chemistry, the mole is a fundamental (The International System of Units AKA. SI) unit used to measure the amount of substance. This quantity is sometimes referred to as the chemical amount. In Latin, mole means a massive heap of material. It is convenient to think of a chemical mole as such.\n")
        print("\nMole Definition:\n")
        print("The mole is the amount of a substance of a system which contains as many elementary entities as there are atoms in 0.012kg (12 AMU) of Carbon. We symbolize with this 'mol'. When the mole is used, the elementary entities must be specified.\n\n6x10^23 atoms, 6x10^23 molecules, 6x10^23 ions,\n6x10^23 electrons, 6x10^23 particles, or\n6x10^23 specified groups of particles.")

    @IntroductionDecisionMaker
    def CalculatorIntroduction():
        print("\nThe purpose of creating this program is just for fun and, it's a good practice for my Python skills.\n")
        sleep(2)
        print("What can this program do?\n")
        print("1. Mole calculator: The Mole calculator allows you to calculate mol through different chemistry formulas. In addition to only calculate mol, you can also calculate mass, molar mass, and gas volume.\n")
        sleep(2)
        print("2. GMMP: GMMP is an acronym that stands for Gases' Molar Masses Comparison; with this part of the program, you can compare different gases' molar mass with each other and will return back a result either the first gas you chose was heavier than the second gas and vice versa.")

    @IntroductionDecisionMaker
    def Credits():
        print("\nCreated by Bennett Tabasco (AKA Takman)\nMole calculator refactored version.")
    

    TableOfContent = {
        1: ChemistryIntroduction,
        2: MoleIntroduction,
        3: CalculatorIntroduction,
        4: Credits
    }

    print("\nWelcome to Introduction, please select a content to read on this Table of Contents here:\n")
    ChosenContent = int(input("Table Of Contents:\n1. Chemistry Introduction\n2. Mole Introduction\n3. Mole Calculator Introduction\n4. Credits\n\n1/2/3/4: "))

    if ChosenContent:
        try:
            TableOfContent[ChosenContent]()
        except:
            print("Invalid decision.")
            sleep(2)
            Introduction()
    else:
        print("Please choose a content to read.\n")
        sleep(2)
        Introduction()


def Calculator():

    @MolDecisionMaker
    def Mol1():
        print("\nn = m / M")
        try:
            Mass = float(input("Enter mass (g): "))
            Molar_mass = int(input("Enter molar mass (g/mol): "))
            if Mass > 0 and Molar_mass > 0:
                print(f"\nn = {Mass} / {Molar_mass} = {round(Mass / Molar_mass, 3)} (mol)")
            else:
                print(Error1)
        except:
            print(Error2)

    @MolDecisionMaker
    def Mol2():
        print("\nn = V / 22.4")
        try:
            Volume = float(input("Enter volume (l): "))
            if Volume > 0:
                print(f"\nn = {Volume} / 22.4 = {round(Volume / 22.4, 3)} (mol)")
            else:
                print(Error1)
        except:
            print(Error4)

    @MolDecisionMaker
    def Mol3():
        print("\nn = V / 24 (Normal codition)")
        try:
            Volume = float(input("Enter volume (l): "))
            if Volume > 0:
                print(f"\nn = {Volume} / 24 = {round(Volume / 24, 3)} (mol)")
            else:
                print(Error1)
        except:
            print(Error4)

    @MolDecisionMaker
    def Mass():
        print("m = n * M ")
        try:
            Mole = float(input("Enter mole (mol): "))
            Molar_mass = int(input("Enter molar mass (g/mol): "))
            if Mole > 0 and Molar_mass > 0:
                print(f"\nm = {Mole} * {Molar_mass} = {round(Mole * Molar_mass, 3)} (g)")
            else:
                print(Error1)
        except:
            print(Error2)

    @MolDecisionMaker
    def Molar_mass():
        print("M = m / n")
        try:
            Mass = float(input("Enter mass (g): "))
            Mole = float(input("Enter mol (mol): "))
            if Mass > 0 and Mole > 0:
                print(f"\nM = {Mass} / {Mole} = {round(Mass / Mole, 3)} (g/mol)")
            else:
                print(Error1)
        except:
            print(Error2)

    @MolDecisionMaker
    def Volume_Through_Standard():
        print("V = n * 22.4")
        try:
            Mole = float(input("Enter mole (mol): "))
            if Mole > 0:
                print(f"\nV = {Mole} * 22.4 = {round(Mole * 22.4, 3)} (l)")
            else:
                print(Error1)
        except:
            print(Error4)

    @MolDecisionMaker
    def Volume_Through_Normal():
        print("V = n * 24")
        try:
            Mole = float(input("Enter mole (mol): "))
            if Mole > 0:
                print(f"\nV = {Mole} * 24 = {round(Mole * 24, 3)} (l)")
            else:
                print(Error1)
        except:
            print(Error4)

    
    Board = {
        1: Mol1,
        2: Mol2,
        3: Mol3,
        4: Mass,
        5: Molar_mass,
        6: Volume_Through_Standard,
        7: Volume_Through_Normal
    }
    print("\nChoose one of these formulas below to begin:\n1. n = m / M (Calculate mole by using mass divide by molar mass)\n2. n = V / 22.4 (Calculate mole in standard condition using gas's volume)\n3. n = V / 24 (Calculate mole in normal condition using gas's volume)\n4. m = n * M (Calculate mass by using mole times molar mass)\n5. M = m / n (Calculate molar mass by using mass divide by mole)\n6. V = n * 22.4 (Calculate gas’s volume in standard condition)\n7. V = n * 24 (Calculate gas’s volume in normal condition)")
    sleep(2)
    print("\nChemistry symbols and their units:\nn: Mole (mol)\nM: Molar mass (g/mol)\nm: Mass (g)\nV: Volume (l)\nN: Avogadro’s number (6.02x10^23)\n")

    Prompt = int(input("1/2/3/4/5/6/7: "))

    if Prompt:
        try:
            print("\n")
            Board[Prompt]()
        except:
            print("Invalid decision.")
            sleep(2)
            Calculator()
    else:
        print(End1)
        sleep(2)
        Calculator()

def GMC():
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
    sleep(3)
    print("Select 2 gases from the gases list above to compare.")
    Gas1 = str(input("Enter first gas’s name: "))
    Gas2 = str(input("Enter second gas’s name: "))

    try:
        Gas_1 = gases_dict[Gas1]
        Gas_2 = gases_dict[Gas2]
        Result = (Gas_1 / Gas_2)
        Comparison_value = round(Result, 3)
        if Result > 1:
            print(f"\n{Gas1} is {Comparison_value} times heavier than {Gas2}")
        elif Result < 1:
            print(f"\n{Gas1} is {Comparison_value} times lighter than {Gas2}")
        elif Result == 1:
            print(f"\n{Gas1} has the same molar mass as {Gas2}")
    except:
        print("\nAn error occured while running the program.")

    sleep(2)

    Decision = input("\nTry again?(y/n): ")
    if Decision == "y":
        GMC()
    elif Decision == "n":
        Decision2 = input("Return to the main page?(y/n): ")
        if Decision2 == "y":
            Main()
        else:
            print(End1)

def Main():

    Board = {
        1: Introduction,
        2: Calculator,
        3: GMC
    }
    print("\nWelcome to Mole Calculator program, please choose which part of the program you wanted to see:\n\n1. Introduction\n2. Mole Calculator\n3. GMMP")
    try:
        Prompt = int(input("\n1/2/3: "))
        if Prompt:
            Board[Prompt]()
        else:
            print("\nPlease choose something.\n")

    except:
        print("\nInvalid decision.\n")
        sleep(2)
        Main()


Main()