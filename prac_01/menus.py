'''

get name
show menu
get menu choice
if choose H:
    print hello and name
if choose G:
    print goodbye and name
if choose Q:
    print finished
end

'''
name = str(input("Enter name: "))
print ("(H)ello \n(G)oodbye \n(Q)uit")
menu_choice = (input(">>> ")).upper()
while menu_choice !="Q":
    if menu_choice == "H":
        print("Hello {}".format(name))
    elif menu_choice == "G":
        print("Goodbye {}".format(name))
    else:
        print("Invalid message")
    print("(H)ello \n(G)oodbye \n(Q)uit")
    menu_choice =(input(">>> ")).upper()
print("Finished.")