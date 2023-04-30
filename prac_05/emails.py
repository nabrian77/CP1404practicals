user_emails={}
def main():
    email = input("Email:")
    while email !="":
        EmailName = name_from_mail(email)
        check=input("Is your name {}? (Y/N)".format(EmailName))
        if check.upper() !="Y" and check !="":
            EmailName = input("Name:")
        user_emails[email] = EmailName
        email = input("Email:")

    for email, EmailName in user_emails.items():
        print("{} ({})".format(EmailName, email))
def name_from_mail(email):
    first=email.split('@')[0]
    parts = first.split('.')
    name = " ".join(parts).title()
    return name

main()