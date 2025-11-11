class ChatBook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False 
        self.menu()
    
    def menu(self):
        user_input = input(""" Welcome to ChatBook ! How would you like to proceed ?
                           1. Press 1 to SignUp
                           2. Press 2 to SignIn
                           3. Press 3 to Write a Post
                           4. Press 4 to message a friend
                           5. Press any other key to Exit""")
        if user_input == '1':
            self.SignUp() 
        elif user_input == '2':
            self.SignIn()
        elif user_input == '3':
            pass
        elif user_input == '4':
            pass
        else:
            exit()

    def SignUp(self):
        email = input("Enter your email id : ")
        pwd = input("Set your password : ")
        self.username = email
        self.password = pwd
        print("SignUp Successful ! Please SignIn to continue.")
        print("\n")
        self.menu()

    def SignIn(self):
        if self.username == '' and self.password == '':
            print("No user found ! Please SignUp first by pressing 1 in the main menu.")
        else:
            uname = input("Enter your email/username : ")
            pwd = input("Enter your password :")
            if self.username == uname and self.password == pwd:
                print("SignIn Successful !")
                self.loggedin = True
            else:
                print("Invalid Credentials ! Please try again.")
        print("\n")
        self.menu()

obj = ChatBook()