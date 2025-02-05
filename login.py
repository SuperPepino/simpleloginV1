setupused = False
from hashlib import sha256
from colorama import Fore, Back, Style
import os

logged_in = False
active = False
message_shown = False
User_found = False

users = open(r"users.txt", "a")
users.close()
users = open(r"users.txt", "r")
Userslist = users.read()
users.close()
Extracted_Data = Userslist.split(",")
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
            ActiveUser = (i+1)
            print(f"Welcome {username}!")

if logged_in == True:
    with open(f"user_{ActiveUser}.txt", "r") as adddefaultperms:
        defaultpermscheck = adddefaultperms.read()
        if defaultpermscheck == "":
            with open(f"user_{ActiveUser}.txt", "w") as adddefaultperms:
                adddefaultperms.write("canmessage,canread")
    if username == "setup":
        print(Fore.RED + "!Do not forget to delete your setup user!" + Fore.RESET)
    active = True

while active == True:
    message_shown = False
    if {username} != "setup":
        with  open(f"mailbox_{username}.txt", "a+") as mailcheck:
            mailbox = mailcheck.read()
            if len(mailbox) > 0:
                print(Fore.CYAN + "You have new mail!" + Fore.RESET)
    activity = input(f"What do you want to do today? [help for a list of commands] ")
    if activity == "promote":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canpromote" in checkpermissions:
            target = input("Enter username of promotion target: ")
            for i in range(len(Listed_users)):
                if target == Listed_users[i]:
                    promotiontarget = i+1
                    promotion_level = input("Enter targets new access level: ")
                    promotion_level = int(promotion_level)
                    if promotion_level == 1:
                        promotionnewaccesslevel = "canmessage,canread"
                    if promotion_level == 10:
                        promotionnewaccesslevel = "canmessage,canread,canpromote"
                    confirmation = input(f"Are you sure you want to promote {target} to level {promotion_level}? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]")
                    if confirmation.upper() == "Y":
                        with open(f"user_{promotiontarget}.txt", "w+") as promotion:
                            promotion.write(f"{promotionnewaccesslevel}")
    elif activity.lower() == "deleteaccount":
        if username == "setup":
            os.remove("user_1.txt")
            for i in range(len(Listed_passwords)):
                        if ActiveUser < i+1:
                          os.rename(f"user_{i+1}.txt", f"user_{i}.txt")
            os.remove("mailbox_setup.txt")
            newuserslist = Userslist.replace(f"{username},{hashedpassword},", "")
            with open("users.txt", "w") as edituserslist:
                edituserslist.write(newuserslist)
                print("Setup user deleted")
        else:
            confirmation = input("Are you sure you want to delete your account? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]")
            if confirmation.upper() == "Y":
                print("You will not be able to sign in to this account again, your mailbox will be cleared and all user data will be deleted.")
                confirmation = input("This is your last warning. Are you sure you want to delete your account? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]")
                if confirmation.upper() == "Y":
                    os.remove(f"user_{ActiveUser}.txt")
                    os.remove(f"mailbox_{username}.txt")
                    newuserslist = Userslist.replace(f"{username},{hashedpassword},", "")
                    with open("users.txt", "w") as edituserslist:
                        edituserslist.write(newuserslist)
                    print(f"User {username} deleted")
                    for i in range(len(Listed_passwords)):
                        if ActiveUser < i+1:
                          os.rename(f"user_{i+1}.txt", f"user_{i}.txt")
                if confirmation.upper() == "N":
                    print("account deletion cancelled")
            if confirmation.upper() == "N":
                print("account deletion cancelled")
            break
    elif activity.lower() == "message":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canmessage" in checkpermissions:
            recipient = input("Enter username of message recipient: ")
            for i in range(len(Listed_users)):
                if recipient == Listed_users[i]:
                    message = input("Enter message: ")
                    messagesending = open(f"mailbox_{recipient}.txt", "a")
                    messagesending.write(f"{message}\n")
                    messagesending.close
                if recipient not in Listed_users and message_shown == False:
                    message_shown = True
                    print("User does not exist")
    elif activity == "readmail":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canread" in checkpermissions:
            with  open(f"mailbox_{username}.txt", "r") as mailbox:
                printmail = mailbox.read()
                print(Fore.YELLOW + f"{printmail}" + Fore.RESET)
                maildeletion = input(f"Would you like to empty your mailbox? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]")
                if maildeletion.upper() == "Y":
                    with open(f"mailbox_{username}.txt", "w") as mailbox:
                        print(Fore.RED + "Mail deleted" + Fore.RESET)
                        mailbox.write("")
                if maildeletion.upper() == "N":
                    print("mail kept")
    elif activity == "changelog":
        Changelogopen = open("Changelog.md", "r")
        Changelogread = Changelogopen.read
        print(Changelogread)
    elif activity == "help":
        print(Fore.CYAN + "message = Send a message to a different user\nreadmail = Read the mail other people have sent to you\npromote = promote a different user to give them more clearance\ndeleteaccount = delete your account\nquit = Close the application" + Fore.RESET)
    elif activity == "quit":
        break
    

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
        users.write(f",{newaccount}")
        users.close
        print(f"You have created an account, {newusername}!")



if Options.lower() == "setup":
        if "" not in Listed_users:
            print("Login already set up, you cannot use it again...")
        elif "" in Listed_users:
            print(Fore.RED + "Setup procedure...")
            print("User for setup added with username setup and password setup!")
            print("! Dont forget to delete setup user so you to avoid security risks !")
            newusername = "setup"
            newpassword = "setup"
            h = sha256()
            h.update(f'{newpassword}'.encode('utf-8'))
            hashed_newpassword = h.hexdigest()
            newaccount = (f"{newusername},{hashed_newpassword}")
            users = open("users.txt", "a")
            users.write(f"{newaccount}")
            users.close
            with open(f"user_1.txt", "a+") as addsetupperms:
                if addsetupperms.read().strip() == "":
                    with open(f"user_1.txt", "w") as addsetupperms:
                        addsetupperms.write("canpromote")

else:
    print("Username or password incorrect! Try again...")