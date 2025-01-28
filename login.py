from hashlib import sha256

logged_in = False

users = open(r"users.txt", "a")
users.close()
users = open(r"users.txt", "r")
Extracted_Data = users.read()
users.close()
Extracted_Data = Extracted_Data.split(",")
Listed_users = Extracted_Data[0::2]
Listed_passwords = Extracted_Data[1::2]

Options = input("log in or sign up? : ")
if Options.lower() == "log in":
    username = input("Enter your username: ")
    password = input("Enter password: ")
    users.close()
    h = sha256()
    h.update(f'{password}'.encode('utf-8'))
    hashedpassword = h.hexdigest()
    for i in range(len(Listed_passwords)):
        if username == Listed_users[i] and hashedpassword == Listed_passwords[i]:
            logged_in = True
            print(f"Welcome {username}!")
        else:
            print("Username or password incorrect! Try again...")

if logged_in == True:
    Current_user = open(f"user_{i+1}", "a")
    Current_user_data = Current_user.read
    Current_user_data.split(", ")
    Current_user.close

if Options.lower() == "sign up":
    newusername = input("Enter new username: ")
    if newusername in Listed_users:
        print("This username is already taken, please try again and choose a different one")
        quit
    elif newusername not in Listed_users:
        newpassword = input("Enter new password: ")
        h = sha256()
        h.update(f'{newpassword}'.encode('utf-8'))
        hashed_newpassword = h.hexdigest()
        newaccount = (f"{newusername},{hashed_newpassword}")
        users = open("users.txt", "a")
        users.write(f"{newaccount},")
        print(f"You have created an account, {newusername}!")