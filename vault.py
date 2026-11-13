class PasswordVault:
    
    def __init__(self):
        self.credentials = []


    #function for adding a new account to the vault
    def add_password(self, website, username, password):

        #a dictionary for the new account
        account = {
            "website": website,
            "username": username,
            "password": password
        }

        #adds the account to the list
        self.credentials.append(account)

        print("\nAccount successfully added!")


    #display all accounts in the vault
    def view_passwords(self):

        #checks if vault is empty
        if len(self.credentials) == 0:

            print("\nYour vault is empty.")
            return

        print("\n===== SAVED ACCOUNTS =====")

        for account in self.credentials:

            print("-------------------------")
            print("Website:", account["website"])
            print("Username:", account["username"])
            print("Password: ********")


    #search for an account using the website
    def search_password(self, website):
        for account in self.credentials:
            if account["website"].lower() == website.lower():

                print("\n===== ACCOUNT FOUND =====")
                print("Website:", account["website"])
                print("Username:", account["username"])
                print("Password:", account["password"])

                return
        print("\nAccount not found.")


    #delete an account using its website
    def delete_password(self, website):
        for account in self.credentials:
            if account["website"].lower() == website.lower():
                self.credentials.remove(account)
                print("\nAccount successfully deleted!")

                return

        print("\nAccount not found.")
