# Import Required Modules
import requests
import os

# Establish Constant Variables
url = "https://forum.plutonium.pw/user/"
current_username = None
taken = None

# Define Menu
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        '''
        =============
        = Main Menu =
        =============\n
        '''
    )
    print("1. Check for names from wordlist")
    print("2. Check for names manually")
    menu_choice = input(" >>  ")
    if menu_choice == '1':
        wordlist()
    elif menu_choice == '2':
        check_manually(current_username, taken, url)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("No valid option was selected... Press enter")
        input()
        menu()

# Check For Usernames From Word List
def wordlist():
    url = "https://forum.plutonium.pw/user/"
    os.system('cls' if os.name == 'nt' else 'clear')
    outputfile = open("untaken_names.txt", "w")
    with open('wlist.txt', 'r') as file:
        for line in file:
            response = requests.get(url + line.rstrip("\n"))
            if (response.status_code == 404):
                print(f"The username, ", line.rstrip("\n"), f", is NOT TAKEN.")
                outputfile.write(line.rstrip("\n") + "\n")
            elif (response.status_code == 200):
                print(f"The username, ", line.rstrip("\n"), f", is TAKEN.")
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Invalid response, press enter to retry")
                print(response.status_code)
                input()
    outputfile.close

# Check for usernames manually
def check_manually(current_username, taken, url):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(
        f'''
        = Username: {current_username}
        = Taken: {taken}
        '''
    )
    check_username = input("Enter the desired username: ")
    current_username = check_username
    response = requests.get(url + current_username)
    if (response.status_code == 404):
        taken = False
        check_manually(current_username, taken, url)
    elif (response.status_code == 200):
        taken = True
        check_manually(current_username, taken, url)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Invalid response, press enter to retry")
        print(response.status_code)
        input()
        check_manually(current_username, taken, url)

menu()