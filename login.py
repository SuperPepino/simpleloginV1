setupused = False
from hashlib import sha256
from colorama import Fore, Back, Style
import os
import time

logged_in = False
active = False
message_shown = False
User_found = False
user_incorrect_block = True

bannedusers = open("bannedusers.txt", "a")
bannedusers.close()
bannedusers = open("bannedusers.txt", "r")
banneduserlist = bannedusers.read()
bannedusers = banneduserlist.split(",")
users = open("users.txt", "a")
users.close()
users = open("users.txt", "r")
Userslist = users.read()
users.close()
Extracted_Data = Userslist.split(",")
Listed_users = Extracted_Data[0::2]
Listed_passwords = Extracted_Data[1::2]


Options = input("log in or sign up? : ").strip().lower()
if Options == "log in":
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
        else:
            user_incorrect_block = False

if logged_in == True:
    adddefaultperms = open(f"user_{ActiveUser}.txt", "a")
    adddefaultperms.close()
    with open (f"user_{ActiveUser}.txt", "r") as adddefaultperms:
        defaultpermscheck = adddefaultperms.read()
        if defaultpermscheck == "":
            with open(f"user_{ActiveUser}.txt", "w") as adddefaultperms:
                adddefaultperms.write("canmessage,canread")
    if username == "setup":
        print(Fore.RED + "!Do not forget to delete your setup user!" + Fore.RESET)
    user_incorrect_block = True
    active = True

while active == True:
    message_shown = False
    if {username} != "setup":
        with open(f"mailbox_{username}.txt", "a+") as mailbox:
            mailbox.seek(0)
            maillen = mailbox.read()
            if maillen != "":
                print(Fore.CYAN + "You have new mail!" + Fore.RESET)
    activity = input(Fore.BLUE + f"What do you want to do today? [help for a list of commands] " + Fore.RESET)

    if activity == "promote":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canpromote" in checkpermissions:
            target = input("Enter username of promotion target: ")
            for i in range(len(Listed_users)):
                if target == Listed_users[i]:
                    promotiontarget = i+1
                    promotion_level = input("Enter targets new access level [1-5]: ")
                    promotion_level = int(promotion_level)
                    if promotion_level == 1:
                        promotionnewaccesslevel = "canread"
                    if promotion_level == 2:
                        promotionnewaccesslevel = "canmessage,canread"
                    if promotion_level == 3:
                        promotionnewaccesslevel = "canmessage,canread,canbanusername"
                    if promotion_level == 4:
                        promotionnewaccesslevel = "canmessage,canread,canunbanusername,canbanusername,canban"
                    if promotion_level == 5:
                        promotionnewaccesslevel = "canmessage,canread,canunbanusername,canbanusername,canban,canpromote"
                    confirmation = input(f"Are you sure you want to promote {target} to level {promotion_level}? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]")
                    if confirmation.upper() == "Y":
                        with open(f"user_{promotiontarget}.txt", "w+") as promotion:
                            promotion.write(f"{promotionnewaccesslevel}")
                    print(Fore.GREEN + "Success, " + Fore.RESET + f"{target} has been promoted to access level {promotion_level}")

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
                user_incorrect_block = True
                break
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
                    user_incorrect_block = True
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
                    print(Fore.GREEN + "Message sent" + Fore.RESET)
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
        Commands = open("Commands.txt", "r")
        Commandread = Commands.read
        print(Fore.CYAN + Commandread + Fore.RESET)
    
    elif activity == "quit":
        active = False

    elif activity == "ban":
        with open(f"user_{ActiveUser}.txt", "r") as f:
            checkpermissions = f.read()
        if "canban" in checkpermissions:
            banrecipient = input("Put username you want to ban here: ")
            if banrecipient in bannedusers:
                print("User already banned...")
            elif banrecipient not in bannedusers:
                if banrecipient in Listed_users:
                    banwrite =  open("bannedusers.txt", "a")
                    banwrite.write(f"{banrecipient},")
                    for i in range(len(Listed_users)):
                        bannednumber = i
                        hashedbannedpassword = Listed_passwords[i]
                        if banrecipient == Listed_users[i]:
                            os.remove(f"user_{i+1}.txt")
                            open(f"mailbox_{banrecipient}.txt", "a").close
                            os.remove(f"mailbox_{banrecipient}.txt")
                            newuserslist = Userslist.replace(f"{banrecipient},{hashedbannedpassword},", "")
                            with open("users.txt", "w") as edituserslist:
                                edituserslist.write(f"{newuserslist}")
                                print(Fore.RED + f"User {banrecipient} banned" + Fore.RESET)
                            for j in range(i+1, len(Listed_users)):
                                old = f"user_{j+1}.txt"
                                new = f"user_{j}.txt"
                                if os.path.exists(old):
                                    os.rename(old, new)
                else:
                    print("User not found")

    elif activity == "banusername":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canbanusername" in checkpermissions:
            banrecipient = input("Put username you want to ban here: ")
            if banrecipient in bannedusers:
                print("User already banned...")
            elif banrecipient not in bannedusers:
                banwrite =  open("bannedusers.txt", "a")
                banwrite.write(f"{banrecipient},")
            else:
                print("User not found")

    elif activity == "unbanusername":
        checkpermissions = open(f"user_{ActiveUser}.txt", "r")
        checkpermissions = checkpermissions.read()
        if "canunbanusername" in checkpermissions:
            unbanrecipient = input("Put username you want to unban here: ")
            if unbanrecipient in bannedusers:
                newbannedusers = banneduserlist.replace(f"{unbanrecipient}, ", "")
                with open("bannedusers.txt", "w") as edituserslist:
                    edituserslist.write(newbannedusers)
                print(Fore.GREEN + f"Username {unbanrecipient} has been unbanned" + Fore.RESET)
            elif unbanrecipient not in bannedusers:
                print("Username is not banned")

    

if Options == "sign up":
    newusername = input("Enter new username: ")
    if newusername in Listed_users:
        print("This username is already taken, please try again and choose a different one")
    if newusername in banneduserlist:
        print("This username is banned, please try a different one")
    elif newusername not in Listed_users and newusername not in banneduserlist:
        newpassword = input("Enter new password: ")
        h = sha256()
        h.update(f'{newpassword}'.encode('utf-8'))
        hashed_newpassword = h.hexdigest()
        newaccount = (f"{newusername},{hashed_newpassword}")
        users = open("users.txt", "r")
        if users == "":
            users.close()
            print("Program not set up yet, use setup command first")
        elif users != "":
            users.close()
            users = open("users.txt", "a")
            users.write(f",{newaccount}")
            users.close
            print(f"You have created an account, {newusername}!")



if Options == "setup":
        if "" not in Listed_users:
            print("Login already set up, you cannot use it again...")
            user_incorrect_block = True
        elif "" in Listed_users:
            print(Fore.RED + "Setup procedure...")
            time.sleep(2)
            print("Writing files for setup")
            time.sleep(4)
            with open("Commands.txt", "w") as writehelp:
                writehelp.write(
                    "message = Send a message to a different user\n"
                    "readmail = Read the mail other people have sent to you\n"
                    "changelog = Shows the changelog\n"
                    "promote = promote a different user to give them more clearance\n"
                    "banusername = Bans a username from an account being created with it\n"
                    "unbanusername = Unbans a username from an account being created with it\n"
                    "ban = Bans a username from an account being created with it and deletes current user with that name\n"
                    "deleteaccount = delete your account\n"
                    "quit = Close the application"
                )
            time.sleep(1)
            user_incorrect_block = True
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
            time.sleep(2)
            print("User for setup added with username setup and password setup!")
            print("! Dont forget to delete setup user so you to avoid security risks !")

if user_incorrect_block is False:
    print("Username or password incorrect! Try again...")