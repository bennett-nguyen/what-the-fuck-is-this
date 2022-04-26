import os


inputName = str(input("\nWhat's your name?: "))


bannedCharacters = ['!', '@', '#', '$', '%', '^', '&', '*','-', '+', '=', '~', '>', '<', '.', ',', '(', ')', '[', ']', '{', '}', '?', '\\', '`', '|', '/', ':', "\"", "\'", ";"]

# Check if the database was empty
isEmpty = os.stat("users.txt").st_size == 0

# Check if the mother for loop was ended
isEnded = False



def signUp():
    print("We don't recognize you, please sign up so you can access this program later.\n")

    while True:

        global new_username
        global new_password

        new_username = str(input("\nEnter Your Username: "))
        new_password = str(input("Enter Your Password: "))


        # If there's a banned character in the name then remove it
        for nameChar in new_username:
            if nameChar in bannedCharacters:
                new_username = new_username.replace(nameChar, "")

        # Username and password preview before submit
        decision = str(input(f"\nYour username is \"{new_username}\" and your password is \"{new_password}\", do you wish to continue? (y/n): "))


        # If the user agreed then write username and password to database
        # Else re-ask the user for credentials
        if decision == "y":
            database.write(f"\n{new_username} {new_password}")
            print("\nSigned up, please rerun this program")
            break
        else:
            continue




with open("users.txt", "r+") as database:

    # This one is similar to the signUp() function but it won't write an extra line in the database which prevents error from occuring
    if isEmpty:
        print("We don't recognize you, please sign up so you can access this program later.\n")

        while True:
            global new_username
            global new_password

            new_username = str(input("\nEnter Your Username: "))
            new_password = str(input("Enter Your Password: "))

            for nameChar in new_username:
                if nameChar in bannedCharacters:
                    new_username = new_username.replace(nameChar, "")

            decision = str(input(f"\nYour username is \"{new_username}\" and your password is \"{new_password}\", do you wish to continue? (y/n): "))

            if decision == "y":
                database.write(f"{new_username} {new_password}")
                print("\nSigned up, please rerun this program")
                break
            else:
                continue


    else:
        # Log In


        # Scan through the database (mother for loop btw)

        # If there were no usernames in the database which corresponded to the input username then ask for the user to sign up
        # Else check the else block of the mother for loop
        for data in database:
            
            # Data will be displayed in a list like this: ["username", "password"]
            data = data.split()

            username = data[0]
            password = data[1]

            # If the username in the database corresponded to the input username then ask for password
            if inputName == username:
                

                for tries in range(3):
                    inputPass = str(input(f"\nHello {inputName}, please enter your password: "))

                    if inputPass == password and len(inputPass) == len(password):
                        print(f"\nLogged in successfully!\n\nWelcome, {inputName}")

                        # Mark that the mother for loop has ended
                        isEnded = True
                        break

                else:
                    print("\nAmount of tries exceeded.")
                    isEnded = True

        else:
            # If the mother for loop ended with a mark then don't ask the user to sign up
            if isEnded:
                pass
            else:
                signUp()