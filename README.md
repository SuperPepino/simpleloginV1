<p align="center">
  <img src="https://placehold.co/1200x300/0f172a/ffffff?text=Python+Login+System&font=montserrat" />
</p>

<p align="center">
  <b>Simple file-based authentication system with messaging, permissions, and moderation.</b>
</p>

<p align="center">
  <a href="#">Documentation</a> •
  <a href="#">Report Bug</a> •
  <a href="#">Request Feature</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-WIP-orange" height="25">
  <img src="https://img.shields.io/badge/python-3.x-blue" height="25">
</p>

---

## 🌟 Why This Project?

- Fully customizable and easy to extend  
- Includes real-world features (messaging, permissions, banning, etc.)  
- Lightweight — no database required  

---

## ✨ Features

- 🔑 User authentication (login & signup)  
- 🔒 Password hashing using SHA-256  
- 📬 User-to-user messaging  
- 📥 Mailbox system (read, send, clear)  
- 🛡️ Permission system (tiers 1–5)  
- ⬆️ User promotion system  
- 🚫 User banning system  
- ❌ Account deletion  
- 🛠️ Initial setup mode  

---

## 🔐 System Overview

This system uses **plain text files** as a simple, lightweight database.

### 📁 Data Storage

- `users.txt` → Stores usernames and hashed passwords  
- `bannedusers.txt` → Stores banned usernames  
- `user_(id).txt` → Stores user permissions  
- `mailbox_(username).txt` → Stores user messages  

---

## 🛠️ First-Time Setup

Run the program and type:

```bash
setup
```

This will:

- Create a default admin account  
- Grant admin permissions  

**Default credentials:**

- Username: `setup`  
- Password: `setup`  

⚠️ **Important:** Delete this account after creating your own admin account.

---

## 🧑‍💻 Usage

At startup, choose:

- `log in`  
- `sign up`  
- `setup`  

---

## 📜 Commands

| Command         | Description                          |
| --------------- | ------------------------------------ |
| `help`          | Show all commands                    |
| `date/time`     | Shows the current date and time      |
| `message`       | Send a message to a user             |
| `readmail`      | Read your mailbox                    |
| `promote`       | Promote a user (requires permission) |
| `ban`           | Ban a user                           |
| `banusername`   | Ban a username from use for a new account |
| `deleteaccount` | Delete your account                  |
| `changelog`     | View changes                         |
| `quit`          | Exit the program                     |

---

## 🚫 Banning System

- Stored in `bannedusers.txt`  

When a user is banned:

- Their account is removed  
- Their mailbox is deleted  
- Their username cannot be reused  

---

## 🔮 Planned Features

- Improved security (salted hashing, validation)  
- Better error handling  
- Cleaner code structure  
- Database support (SQLite)  
- Logging system  
- Admin tools / interface  

---

## 🤝 Contributing

- 🐛 Found a bug? Open an issue  
- 💡 Have an idea? Suggest a feature  
- 🔧 Want to improve the code? Submit a PR  

All contributions are welcome.

---
## 🤖 AI declaration

Used copilot for deployment to PyPi and chatgpt for simple bug fixes early on

---

## 📄 License

This project is free to use for **educational purposes**.

---

<p align="center">
  Made with learning in mind.<br>
  If you like it, consider ⭐ starring the repo!
</p>
I will try to update this program once in a while so I have a changelog aswel.
