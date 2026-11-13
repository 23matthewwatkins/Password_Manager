from vault import PasswordVault

def display_menu():
    #Function displays options for the user to enter, doesn't include input yet
    print("---------------------------")
    print("1: Add Password\n2: View Passwords\n3: Search Passwords\n4: Delete Password\n5: Exit")


display_menu()

#Main function
def main():
    vault = PasswordVault()

    while True: 
        display_menu()

        choice = input("Which option do you choose: ")

        #if user chooses to add password
        if choice == "1":

            print("\n----Add Password----")

            website = input("Enter Website: ")
            username = input("Enter Username: ")
            password = input("Enter Password: ")

            if password == '' or website == '' or username == '':
                print("All fields are required")

            else:
                vault.add_password(website, username, password)

        #if user chooses to view password
        elif choice == "2":
            vault.view_passwords()
        
        #if user chooses to search passwords
        elif choice == "3":
            website = input("Enter website to search: ")
            
            vault.search_password(website)

        #if user chooses to delete passwords
        elif choice == "4":
            website = input("Enter website to delete: ")

            vault.delete_password(website)
        
        #if user chooses to quit the program
        elif choice == "5":
            print("Ending password manager.")
            break

main()