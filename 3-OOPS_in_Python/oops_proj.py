class ChatBook:

    __user_id = 0  #class variable to keep track of user ids
    def __init__(self):
        self.id = ChatBook.__user_id # unique user id for each object
        ChatBook.__user_id += 1
        self.__name = "Default User" #hidden attribute
        #self.userid = 0
        #self.userid += 1
        self.username = ""
        self.password = ""
        self.loggedin = False 
        #self.menu()
    @staticmethod
    def get_id():
        return ChatBook.__user_id
    @staticmethod
    def set_id(val):
        ChatBook.__user_id = val

    def get_name(self):
        return self.__name 
    
    def set_name(self, value):
        self.__name = value
    
    def menu(self):
        user_input = input(""" Welcome to ChatBook ! How would you like to proceed ?
                           1. Press 1 to SignUp
                           2. Press 2 to SignIn
                           3. Press 3 to Write a Post
                           4. Press 4 to message a friend
                           5. Press any other key to Exit
                           
                           -> """)
        if user_input == '1':
            self.SignUp() 
        elif user_input == '2':
            self.SignIn()
        elif user_input == '3':
            self.my_post()
        elif user_input == '4':
            self.message_friend()
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

    def my_post(self):
        if self.loggedin == True:
            post = input("Write your post here : ")
            print(f"Your post '{post} hass been published successfully !")
        else:
            print("Please SignIn to write a post.")
        print("\n")
        self.menu()
    def message_friend(self):
        if self.loggedin == True:
            friend = input("Enter your friend's username : ")
            message = input("Enter your message : ")
            print(f"Your message '{message}' has been sent to {friend} successfully !")
        else:
            print("Please SignIn to message a friend.")
        print("\n")
        self.menu()

user1 = ChatBook()