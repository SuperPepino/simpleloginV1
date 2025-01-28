from hashlib import sha256

users = open(r"users.txt", "a")
users.close()
users = open("users.txt", "r")
extracted_data = users.readline(x)
extracted_data = extracted_data.split(",")
listed_users = extracted_data[0::2]
listed_passwords = extracted_data[1::2]
logged_in = False

Options = input("log in or sign up? : ")

if Options.lower() == "log in":
    username = input("Enter your username: ")
    password = input("Enter password: ")
    users.close()
    h = sha256()
    h.update(f'{password}'.encode('utf-8'))
    hashedpassword = h.hexdigest()
    for i in range(len(listed_passwords)):
        if username in listed_users[i] and hashedpassword in listed_passwords[i]:
            print ("login complete")

if Options.lower() == "sign up":
    newusername = input("Enter new username: ")
    if newusername in listed_users:
        print("This username is already taken, please try again and choose a different one")
        quit
    elif newusername not in listed_users:
        newpassword = input("Enter new password: ")
        h = sha256()
        h.update(f'{newpassword}'.encode('utf-8'))
        hashed_newpassword = h.hexdigest()
        newaccount = (f"{newusername}, {hashed_newpassword}")
        users = open("users.txt", "a")
        users.write(f"{newaccount}\n")