
# <img src="https://github.com/user-attachments/assets/9115aa71-ea52-4fb3-b629-b1a1b5833515" width="20" height="20"> TUI - LinkedIn Followers Bot <img src="https://github.com/user-attachments/assets/9115aa71-ea52-4fb3-b629-b1a1b5833515" width="20" height="20">

![GitHub stars](https://img.shields.io/github/stars/capi-nemoo/LinkedIn-Bot-Followers?style=social) ![GitHub forks](https://img.shields.io/github/forks/capi-nemoo/LinkedIn-Bot-Followers?style=social) ![GitHub issues](https://img.shields.io/github/issues/capi-nemoo/LinkedIn-Bot-Followers)

## 🚀 This fork now features full Linux support and a user-friendly Terminal User Interface (TUI) for easier configuration and execution! 🚀

## Overview


Welcome to the **LinkedIn  Bot Follower** project! This tool automates the process of following LinkedIn accounts, helping you grow your professional network with ease. The project includes a Terminal User Interface (TUI) that lets you configure key parameters before launching the appropriate bot script for your operating system.

![2025-02-1805-15-57-ezgif com-resize](https://github.com/user-attachments/assets/7775fdbc-f1ce-4b4c-9011-631319ceed71)

This repository contains:

- **TUI Script (`TUI-bot_Launcher.py`)**: A user-friendly interface to select your OS and enter required configuration values.
- **Bot Scripts**:
  - `botlinkdinW.py` for Windows
  - `botlinkdinL.py` for Linux

## 🔑 Key Features

- **Automated LinkedIn Following**: Follows up to 25 new accounts per run.
- **Weekly Limit Check**: Prevents exceeding a weekly following limit to help avoid detection.
- **Daily Execution Check**: Ensures the bot runs only once per day.
- **Custom Configuration via TUI**: Set your Chrome executable path, profile path, and login status easily.
- **Cross-Platform Compatibility**: Automatically selects the correct bot script based on your OS.

## ⚙️ Requirements

- Python 3.6+
- Chrome or Chromium Browser
- A valid LinkedIn account
- [NoDriver](https://github.com/ultrafunkamsterdam/nodriver) library

Install the required library using:

```bash
pip install nodriver
```


## 🛠 Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/capi-nemoo/LinkedIn-bot-Followers
   cd LinkedIn-bot-Followers
   ```

2. Review and, if needed, modify the default paths in the bot scripts:

   - For Windows: `botlinkdinW.py`
   - For Linux: `botlinkdinL.py`

3. Use the TUI script to configure your settings before running the bot.

## 📜 Usage

Launch the TUI script with:

```bash
python TUI-bot_Launcher.py
```

The TUI will prompt you to:

- **Select Your OS**: Choose between Windows and Linux.
- **Enter Chrome Executable Path**: Provide the full path to your Chrome or Chromium executable.
- **Enter Profile Path**: Specify the directory where your LinkedIn user data should be saved.
- **Set Login State**: Input `1` if you are logged in, or `0` if not.

Based on your selections, the TUI will automatically launch the corresponding bot script with your provided configuration.

### How the Bot Works

1. **Pre-Execution Checks**:
   - The bot reads `AccountLog.txt` to verify if it has already run today or if the weekly follow limit has been reached.
2. **Browser Launch**:
   - It launches Chrome/Chromium with your specified profile.
3. **LinkedIn Interaction**:
   - The bot navigates to your network page, scrolls to find accounts, and follows up to 25 new accounts.
4. **Logging**:
   - The action is logged in `AccountLog.txt` for tracking.

## 🚧 Disclaimer

Automation on LinkedIn can violate its Terms of Service and may lead to account restrictions. Use this bot responsibly and at your own risk. This project is intended for educational purposes only.

## 📧 Contributing

Contributions are welcome! If you have improvements, bug fixes, or new features, feel free to open an issue or submit a pull request.
Specials Thanks to

If you enjoy this project, please consider giving it a star ⭐! Every star helps spread the word and motivates me to keep improving the project. 

A special thanks to [Connor9994](https://github.com/Connor9994/LinkedIn-Follower-Bot), the maintainer of the original project.

```
Enjoy automating your network growth responsibly with the LinkedIn Follower Bot!

```


