<img src="https://placehold.co/1200x300/0f172a/ffffff?text=Python+Login+System&font=montserrat" />


<p align="center">
  <b>Simple authentication system with basic messaging functionality and a moderation system.</b>
</p>

<p align="center">
  <a href="https://pepinoportfolio.vercel.app/Projects/PythonLogin">Documentation</a> •
  <a href="https://github.com/SuperPepino/simpleloginV1/issues">Report Bug</a> •
  <a href="https://discord.com/channels/@me/938003608132272138">Request Feature</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-Completed-green" height="25">
  <img src="https://img.shields.io/badge/python-blue" height="25">
  <img src="https://img.shields.io/badge/hackatime-12h%2005m-blue" height="25">
</p>

---

## Why use This Login System?

- Simple to use
- Includes useful features like messaging, permissions, banning, etc.
- Lightweight (No database required)

## ✨ Features ✨

- Account system
- Password hashing
- Between user messaging  
- Mailbox system
- Permission system with 5 access levels
- Banning system 
- Blacklisting offensive usernames
- Initial setup mode for first time setup


## Data Storage

- `users.txt` → Stores usernames and hashed passwords
- `bannedusers.txt` → Stores list of banned usernames
- `user_(id).txt` → Stores users permissions and data
- `mailbox_(username).txt` → Stores users inbox

## 🚀 Quick-Start Guide

download the program by running:
```bash
pip install simple-login-system==0.{version}
```

Run it by typing

```bash
python -m simplelogin.login
```

To setup type:

```bash
setup
```
<h1 align="center">
  <b>!DISCLAIMER!</b>
  <p>Setup user can only be used for promoting and some default features</p>
  <p>Make a different user and promote it using setup to acecess more features</p>
</h1>


Setup will:

- Create a default admin account  
- Grant promotion permissions to this account

**Log in to setup account using:**

- Username: `setup`  
- Password: `setup`  

<h1 align="center">
 **Important:** Delete this account after creating your own admin account and giving it perms using setup account.
</h1>

## Command list

| Command         | Description                          |
| --------------- | -------------------------------------|
| `help`          | Show all commands                    |
| `date`          | Shows the current date and time      |
| `message`       | Send a message to a user             |
| `readmail`      | Read your mailbox                    |
| `promote`       | Promote a user (requires permission) |
| `ban`           | Ban a user                           |
| `blacklist`     | Blacklists a username from use for a new account |
| `deleteaccount` | Delete your account                  |
| `changelog`     | View changes                         |
| `quit`          | Exit the program                     |

## Contributing to the project

-  Found a bug? Open an issue  
-  Have an idea? Suggest a feature  
-  Want to improve the code? Submit a Pull Request

All contributions are welcome and highly encouraged.

## AI declaration

Used copilot for deployment to PyPi and chatgpt for simple bug fixes early on.

## Optimization

- I made the program as optimized as possible by using defines to make it run smooth, I also dont use any databases or external programs that might make it take more memory or cpu capability.
- I made it run fast and smooth with not too much random bulk that would be in the way of users access to the program, but still tried to make it look good

---
<br>
<p align="center">
  If you like it, consider ⭐ the repo!
</p>
<h3 align="center" ><strong>
**I will try to update this program once in a while so I will post devlogs on my <span><a href="pepinoportfolio.vercel.app">website</a></span>. with updates**
</strong></h3>