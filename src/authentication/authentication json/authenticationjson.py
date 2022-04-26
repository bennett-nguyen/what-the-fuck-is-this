import json
import os
from random import randint

isExist = os.path.isfile('./database.json')

# Create new database if it didn't exist in the current directory.
if not isExist:
    with open("database.json", "w") as f:
        pass

inputName = str(input("\nWho are you?: "))
isEnded = False
isEmpty = os.stat("database.json").st_size == 0


def register():

    print("We don't recognize you, please register so you can access this program later.")

    allowedChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"
    keyboardChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`-=[]\;',./~!@#$%^&*()_+{}|:\"<>?"

    while True:

        global new_username
        global new_password

        new_username = str(input("\nEnter Your Username: "))
        new_password = str(input("Enter Your Password: "))

        # Random password generator if the user didn't enter the password
        if not new_password:
            for _ in range(20):
                randomChar = keyboardChar[randint(0, 93)]
                new_password = randomChar + new_password

        # Random name generator if the user didn't enter the username
        if not new_username:
            if not inputName:
                while True:
                    for _ in range(10):
                        randomChar = allowedChar[randint(0, len(allowedChar)-1)]
                        new_username = randomChar + new_username

                    if new_username in existedName:
                        continue
                    else:
                        break
            else:
                new_username = inputName

        # If there's a banned character in the name then remove it
        for nameChar in new_username:
            if nameChar not in allowedChar:
                new_username = new_username.replace(nameChar, "")

        # Username and password preview before submit
        decision = str(input(f"\nYour username is \"{new_username}\" and your password is \"{new_password}\", do you wish to continue? (y/n): "))


        # If the user agreed then write username and password to database
        if decision == "y":

            # If JSON file didn't exist then create a new one and write user's credentials to it. 
            if isEmpty:
                exportData = {}
                exportData["user"] = []

                exportData["user"].append({
                    "username": new_username,
                    "password": new_password
                })
                
                with open("database.json", "w") as database:
                    json.dump(exportData, database, indent=4)
                    print("\nRegistered successfully! Please rerun this program.")

                    
            # Otherwise, write new user's credentials then overwrite the old database.
            else:
                
                data["user"].append({
                    "username": new_username,
                    "password": new_password
                })

                with open("database.json", "w") as database:
                    json.dump(data, database, indent=4)
                    print("\nRegistered successfully! Please rerun this program.")


            break
        
        # Otherwise, re-ask the user for credentials
        else:
            continue



with open("database.json", "r") as database:
    
    # Check if the JSON file is empty
    if isEmpty:
        register()


    # Otherwise, iterate through the database to find informations in which corresponds to the input username
    else:
        data =  json.load(database)
        existedName = []

        for user in data["user"]:

            existedName.append(user["username"])
            # If the username in database corresponed to the input username then ask the user for password but they have 3 tries to enter the correct password.
            if inputName == user["username"] and len(inputName) == len(user["username"]):

                for _ in range(3):
                    inputPass = str(input(f"\nHello {inputName}, please enter your password: "))
                    
                    # If the user entered the correct password then end the iteration of the mother for-loop
                    if inputPass == user["password"] and len(inputPass) == len(user["password"]):
                        print(f"\nWelcome, {inputName}.")