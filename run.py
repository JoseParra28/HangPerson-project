username = input("Welcome to HangPerson! \nPlease insert your name\n")
while len(username) < 1 or username.isalpha() is False:
    print('Please insert letters only \n')