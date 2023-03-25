def main():
    user_password = get_password()
    while user_password == "":
        print("Please enter your password")
        user_password = get_password()
    password_length = len(user_password)
    print_stars(password_length)


def print_stars(password_length):
    for i in range(password_length):
        print("*", end='')


def get_password():
    user_password = input("Enter your password: ")
    return user_password

main()
