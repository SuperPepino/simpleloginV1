from hashlib import sha256
from colorama import Fore, Style
import os
import time
from datetime import datetime


class SimpleLoginSystem:
    def __init__(self):
        self.logged_in = False
        self.active = False
        self.user_incorrect_block = True
        self.LoginCheck = False
        self.ActiveUser = None
        self.username = None
        self.password = None
        self.hashedpassword = None
        self.Options = None
        self.Listed_users = []
        self.Listed_passwords = []
        self.banneduserlist = []

    def ensure_root_dir(self):
        os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    def load_users(self):
        if not os.path.exists("users.txt"):
            return [], []
        with open("users.txt", "r") as users:
            data = users.read().strip()
        if not data:
            return [], []
        extracted = [item for item in data.split(",") if item]
        return extracted[0::2], extracted[1::2]

    def load_banned(self):
        if not os.path.exists("bannedusers.txt"):
            return []
        with open("bannedusers.txt", "r") as banned:
            data = banned.read().strip()
        if not data:
            return []
        return [item for item in data.split(",") if item]

    def save_users(self):
        with open("users.txt", "w") as users:
            if self.Listed_users:
                users.write(",".join(f"{name},{password}" for name, password in zip(self.Listed_users, self.Listed_passwords)) + ",")
            else:
                users.write("")

    def save_banned(self):
        with open("bannedusers.txt", "w") as banned:
            if self.banneduserlist:
                banned.write(",".join(self.banneduserlist) + ",")
            else:
                banned.write("")

    def main(self):
        self.ensure_root_dir()
        self.Listed_users, self.Listed_passwords = self.load_users()
        self.banneduserlist = self.load_banned()

        if not self.Listed_users:
            print(Fore.RED + "Program not set up yet. Set program up before use" + Fore.RESET)
            Dosetup = input("Do you want to set up the program now? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
            if Dosetup == "Y":
                self.setup()
            else:
                print(Fore.RED + "Setup cancelled, you will not be able to use the program until you set it up" + Fore.RESET)
                self.main()
        else:
            self.login_prompt()

    def login_prompt(self):
        self.Listed_users, self.Listed_passwords = self.load_users()
        self.banneduserlist = self.load_banned()
        self.Options = input("log in or sign up? : ").strip().lower()

        if self.Options in ("log in", "login"):
            self.login()
        elif self.Options in ("sign up", "signup"):
            self.sign_up()
        elif self.Options in ("setup", "set up"):
            self.setup()
        else:
            print(Fore.RED + "Unknown option. Please choose 'log in', 'sign up', or 'setup'." + Fore.RESET)
            self.login_prompt()

    def login(self):
        self.username = input("Enter your username: ").strip()
        self.password = input("Enter password: ").strip()
        h = sha256()
        h.update(self.password.encode("utf-8"))
        self.hashedpassword = h.hexdigest()
        self.Listed_users, self.Listed_passwords = self.load_users()
        if self.username in self.banneduserlist:
            print("This user is banned.")
            return self.login_prompt()

        for index, listed_password in enumerate(self.Listed_passwords):
            if self.username == self.Listed_users[index] and self.hashedpassword == listed_password:
                self.logged_in = True
                self.LoginCheck = True
                self.ActiveUser = index + 1
                self.user_incorrect_block = True
                print(f"Welcome {self.username}!")
                self.after_login()
                self.active_loop()
                return

        print("Username or password incorrect! Try again...")
        self.login_prompt()

    def after_login(self):
        os.makedirs(".", exist_ok=True)
        with open(f"user_{self.ActiveUser}.txt", "a+") as adddefaultperms:
            adddefaultperms.seek(0)
            defaultpermscheck = adddefaultperms.read().strip()
            if not defaultpermscheck:
                adddefaultperms.write("canmessage,canread")

        if self.username == "setup":
            print(Fore.RED + "!Do not forget to delete your setup user!" + Fore.RESET)
        else:
            with open(f"mailbox_{self.username}.txt", "a+") as mailbox:
                mailbox.seek(0)
                maillen = mailbox.read()
                if maillen:
                    print(Fore.CYAN + "You have new mail!" + Fore.RESET)

        self.LoginCheck = False
        self.user_incorrect_block = True
        self.active = True

    def active_loop(self):
        self.Listed_users, self.Listed_passwords = self.load_users()
        self.banneduserlist = self.load_banned()

        while self.active:
            activity = input(Fore.BLUE + "What do you want to do today? [help for a list of commands] " + Fore.RESET).strip().lower()
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            if activity in ("time", "date"):
                print(f"The current time is {current_time}")

            elif activity == "promote":
                self.command_promote()

            elif activity == "deleteaccount":
                self.command_deleteaccount()

            elif activity == "message":
                self.command_message(current_time)

            elif activity == "readmail":
                self.command_readmail()

            elif activity == "changelog":
                self.command_changelog()

            elif activity == "help":
                self.command_help()

            elif activity in ("logout", "log out"):
                self.logged_in = False
                self.active = False
                print(Fore.YELLOW + "Logged out." + Fore.RESET)

            elif activity == "shutdown":
                self.command_shutdown()

            elif activity == "ban":
                self.command_ban()

            elif activity == "blacklist":
                self.command_blacklist()

            elif activity == "pardon":
                self.command_pardon()

            elif activity == "quit":
                checkpermissions = self.read_permissions()
                if "canclose" not in checkpermissions:
                    print("You do not have permission to use this command")
                    continue
                self.active = False
                print(Fore.YELLOW + "Exiting application." + Fore.RESET)

            else:
                print(Fore.RED + "Unknown command. Type 'help' for a list of commands." + Fore.RESET)

    def command_promote(self):
        checkpermissions = self.read_permissions()
        if "canpromote" not in checkpermissions:
            print("You do not have permission to use this command")
            return

        target = input("Enter username of promotion target: ").strip()
        if target not in self.Listed_users:
            print("User not found")
            return

        promotiontarget = self.Listed_users.index(target) + 1
        promotion_level = int(input("Enter targets new access level [1-5]: ").strip())
        promotionnewaccesslevel = {
            1: "canread",
            2: "canmessage,canread",
            3: "canmessage,canread,canbanusername",
            4: "canmessage,canread,canunbanusername,canbanusername,canban",
            5: "canmessage,canread,canunbanusername,canbanusername,canban,canpromote,canclose",
        }.get(promotion_level)

        if not promotionnewaccesslevel:
            print("Invalid promotion level")
            return

        with open(f"user_{promotiontarget}.txt", "w") as promotion:
            promotion.write(promotionnewaccesslevel)

        print(Fore.GREEN + "Success, " + Fore.RESET + f"{target} has been promoted to access level {promotion_level}")

    def command_deleteaccount(self):
        if self.username == "setup":
            self.delete_user_files(self.ActiveUser)
            self.Listed_users.pop(0)
            self.Listed_passwords.pop(0)
            self.save_users()
            self.reindex_user_files(self.ActiveUser)
            print("Setup user deleted")
            self.active = False
            return

        confirmation = input("Are you sure you want to delete your account? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
        if confirmation != "Y":
            print("Account deletion cancelled")
            return

        confirmation = input("This is your last warning. Are you sure you want to delete your account? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
        if confirmation != "Y":
            print("Account deletion cancelled")
            return

        self.delete_user_files(self.ActiveUser)
        self.delete_mailbox(self.username)
        self.Listed_users.pop(self.ActiveUser - 1)
        self.Listed_passwords.pop(self.ActiveUser - 1)
        self.save_users()
        self.reindex_user_files(self.ActiveUser)
        print(Fore.GREEN + f"User {self.username} deleted" + Fore.RESET)
        self.active = False

    def command_message(self, current_time):
        checkpermissions = self.read_permissions()
        if "canmessage" not in checkpermissions:
            print("You do not have permission to send a message")
            return

        recipient = input("Enter username of message recipient: ").strip()
        if recipient not in self.Listed_users:
            print("User does not exist")
            return

        message = input("Enter message: ").strip()
        with open(f"mailbox_{recipient}.txt", "a") as messagesending:
            messagesending.write(f"{self.username} [{current_time}] {message}\n")
        print(Fore.GREEN + "Message sent" + Fore.RESET)

    def command_readmail(self):
        checkpermissions = self.read_permissions()
        if "canread" not in checkpermissions:
            print("You do not have permission to read mail")
            return

        with open(f"mailbox_{self.username}.txt", "a+") as mailbox:
            mailbox.seek(0)
            printmail = mailbox.read()
        print(Fore.YELLOW + f"{printmail}" + Fore.RESET)

        maildeletion = input("Would you like to empty your mailbox? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
        if maildeletion == "Y":
            with open(f"mailbox_{self.username}.txt", "w") as mailbox:
                mailbox.write("")
            print(Fore.RED + "Mail deleted" + Fore.RESET)
        else:
            print("Mail retained")

    def command_changelog(self):
        with open("Changelog.md", "r") as changelogread:
            Changelogread = changelogread.read()
            START = Changelogread.find("#")
            END = Changelogread.find("#", START + 1)
            print(Fore.LIGHTMAGENTA_EX + Changelogread[START:END] + Fore.RESET)

    def command_help(self):
        with open("Commands.txt", "r") as Commands:
            Commandread = Commands.read()
            print(Fore.CYAN + Commandread + Fore.RESET)

    def command_shutdown(self):
        checkpermissions = self.read_permissions()
        if "canclose" not in checkpermissions:
            print("You do not have permission to shutdown the application")
            return

        confirmation = input("Are you sure you want to shutdown the application? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
        if confirmation == "Y":
            print(Fore.RED + "Shutdown initiated..." + Fore.RESET)
            time.sleep(2)
            print(Fore.BLUE + "Goodbye!" + Fore.RESET)
            exit()
        print(Fore.GREEN + "Shutdown cancelled" + Fore.RESET)

    def command_ban(self):
        checkpermissions = self.read_permissions()
        if "canban" not in checkpermissions:
            print("You do not have permission to use this command")
            return

        banrecipient = input("Put username you want to ban here: ").strip()
        if banrecipient in self.banneduserlist:
            print("User already banned...")
            return

        if banrecipient not in self.Listed_users:
            print("User not found")
            return

        if banrecipient == "setup":
            print("You cannot ban the setup user, log in as it and deleteaccount instead")
            return

        self.banneduserlist.append(banrecipient)
        self.save_banned()

        user_index = self.Listed_users.index(banrecipient)
        self.delete_user_files(user_index + 1)
        self.delete_mailbox(banrecipient)
        self.Listed_users.pop(user_index)
        self.Listed_passwords.pop(user_index)
        self.save_users()
        self.reindex_user_files(user_index + 1)

        print(Fore.RED + f"User {banrecipient} banned" + Fore.RESET)

    def command_blacklist(self):
        checkpermissions = self.read_permissions()
        if "canbanusername" not in checkpermissions:
            print("You do not have permission to use this command")
            return

        banrecipient = input("Put username you want to ban here: ").strip()
        if banrecipient in self.banneduserlist:
            print("User already banned...")
            return

        self.banneduserlist.append(banrecipient)
        self.save_banned()
        print(Fore.GREEN + f"Username {banrecipient} blacklisted" + Fore.RESET)

    def command_pardon(self):
        checkpermissions = self.read_permissions()
        if "canunbanusername" not in checkpermissions:
            print("You do not have permission to use this command")
            return

        unbanrecipient = input("Put username you want to unban here: ").strip()
        if unbanrecipient not in self.banneduserlist:
            print("Username is not banned")
            return

        self.banneduserlist.remove(unbanrecipient)
        self.save_banned()
        print(Fore.GREEN + f"Username {unbanrecipient} has been unbanned" + Fore.RESET)

    def sign_up(self):
        self.Listed_users, self.Listed_passwords = self.load_users()
        self.banneduserlist = self.load_banned()

        newusername = input("Enter new username: ").strip()
        if newusername in self.Listed_users:
            print("This username is already taken, please try again and choose a different one")
            return self.login_prompt()

        if newusername in self.banneduserlist:
            print("This username is banned, please try a different one")
            return self.login_prompt()

        newpassword = input("Enter new password: ").strip()
        h = sha256()
        h.update(newpassword.encode("utf-8"))
        hashed_newpassword = h.hexdigest()
        self.Listed_users.append(newusername)
        self.Listed_passwords.append(hashed_newpassword)
        self.save_users()
        print(f"You have created an account, {newusername}!")
        self.login_prompt()

    def setup(self):
        self.ensure_root_dir()
        self.Listed_users, self.Listed_passwords = self.load_users()
        if self.Listed_users:
            print(Fore.RED + "Program already set up, you cannot use it again..." + Fore.RESET)
            return

        setupquestion = input("Program not set up yet. Do you want to initiate setup? [" + Fore.GREEN + "Y" + Fore.RESET + "/" + Fore.RED + "N" + Fore.RESET + "]").strip().upper()
        if setupquestion != "Y":
            print(Fore.RED + "Setup cancelled, you will not be able to use the program until you set it up" + Fore.RESET)
            return self.main()

        with open("Commands.txt", "w") as writehelp:
            writehelp.write(
                "time/date = Shows the current date and time\n"
                "message = Send a message to a different user\n"
                "readmail = Read the mail other people have sent to you\n"
                "changelog = Shows the changelog\n"
                "promote = promote a different user to give them more clearance\n"
                "blacklist = Bans a username from an account being created with it\n"
                "pardon = Unbans a username from an account being created with it\n"
                "ban = Bans a username from an account being created with it and deletes current user with that name\n"
                "deleteaccount = delete your account\n"
                "quit = Close the application\n"
            )

        with open("bannedusers.txt", "w") as f:
            f.write("setup,")

        newusername = "setup"
        newpassword = "setup"
        h = sha256()
        h.update(newpassword.encode("utf-8"))
        hashed_newpassword = h.hexdigest()
        self.Listed_users = [newusername]
        self.Listed_passwords = [hashed_newpassword]
        self.save_users()

        with open("user_1.txt", "w") as addsetupperms:
            addsetupperms.write("canpromote")

        print("User for setup added with username setup and password setup!")
        print(Fore.RED + "! Dont forget to delete setup user so you to avoid security risks !" + Fore.RESET)
        self.main()

    def read_permissions(self):
        if not self.ActiveUser:
            return ""
        path = f"user_{self.ActiveUser}.txt"
        if not os.path.exists(path):
            return ""
        with open(path, "r") as permissions_file:
            return permissions_file.read()

    def delete_user_files(self, user_index):
        path = f"user_{user_index}.txt"
        if os.path.exists(path):
            os.remove(path)

    def delete_mailbox(self, username):
        path = f"mailbox_{username}.txt"
        if os.path.exists(path):
            os.remove(path)

    def reindex_user_files(self, start_index):
        current_users = len(self.Listed_users) + 1
        for i in range(start_index + 1, current_users + 1):
            old = f"user_{i}.txt"
            new = f"user_{i - 1}.txt"
            if os.path.exists(old):
                os.rename(old, new)


if __name__ == "__main__":
    SimpleLoginSystem().main()
