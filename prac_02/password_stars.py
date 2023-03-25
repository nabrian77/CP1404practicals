user_password = input("Enter your password: ")
while user_password == "":
    print("Please enter your password")
    user_password = input("Enter your password: ")
password_length = len(user_password)
for i in range(password_length):
    print("*", end= '')
