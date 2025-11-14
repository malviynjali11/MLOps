# # lst = [1, 2, 3]
# # my_str = "MLOps Playlist"
# # my_int = 150 

# # print(type(lst))
# # print(type(my_str))
# # print(type(my_int))

from oops_proj import ChatBook

# # function v/s method 
# lst = [1, 2, 3, 4, 5]
# # function 
# a1 = len(lst)
# print(f"Length of the list using function len() is : {a1}")
# # method
# user1 = ChatBook()
# user1.message_friend()

# Encapsulation Example 
user1 = ChatBook()
#print(user1._ChatBook__name)  # Accessing the hidden attribute using name mangling

# Getter and Setter methods
# print(user1.get_name()) # Accessing hidden attribute using getter method
# user1.set_name("Anjali") # Modifying hidden attribute using setter method
# print(user1.get_name())

# print(user1.id)  # Accessing userid 

# user2 = ChatBook()
# print(user2.id)  # Accessing userid attribute for new object

# user3 = ChatBook()
# print(user3.id)  # Accessing userid attribute for new object

print(user1.id)

ChatBook.set_id(10)  # Modifying class variable using setter method
user2 = ChatBook()
print(user2.id)  # Accessing userid attribute for new object