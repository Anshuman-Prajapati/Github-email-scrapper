# GitHub Commit Email Extractor

![Python](https://img.shields.io/badge/Python-3.x-blue) 
![License](https://img.shields.io/badge/License-MIT-green) 
![GitHub Repo](https://img.shields.io/github/stars/Anshuman-Prajapati/Github-email-scrapper?style=social)

A Python tool to fetch GitHub repository commits and extract **unique emails** from commit patches. Supports **Flash mode** (first commit) and **Detailed mode** (all commits).  

---

## ✨ Features

- List GitHub repositories for any user.
- Identify repository type: Owned or Forked.
- Retrieve commits and extract emails from patches.
- Two modes:
  - **Flash Mode** – Fast, first commit only.
  - **Detailed Mode** – Processes all commits.

---

## 💻 Installation

Clone and run with a single command:

```bash
git clone https://github.com/Anshuman-Prajapati/Github-email-scrapper.git && cd Github-email-scrapper && pip install requests
````
---

## 🏁 Quick Start

```bash
python3 Git-email-scrapper.py
```

1. Enter the GitHub username.
2. Select a repository from the list.
3. Choose a mode (`1` for Flash, `2` for Detailed).
4. View extracted unique emails.

---

## 📌 Example Output
![DEMO](https://github.com/user-attachments/assets/356b5fe5-8e79-4932-a7bf-2db94151b96f)
```
Enter GitHub username: octocat
Repositories for user octocat:
1. Hello-World (Owned)
2. Spoon-Knife (Forked)

Select a repository (1-2): 1
Select mode:
1. Flash mode
2. Detailed mode
Enter choice: 2

Unique emails Found:
From: octocat@github.com
From: someone@example.com
```

---

## ⚡ Dependencies

* Python 3.x
* [requests](https://pypi.org/project/requests/)

---

## 📝 License

This project is licensed under the MIT License. See the ([License](https://github.com/Anshuman-Prajapati/Github-email-scrapper/blob/ebbb1b7cbb3bae7e0d9d3efbbb9c278eb8d78b26/LICENSE)) here.

---

## ⚠️ Disclaimer

This tool is intended for **educational purposes**,and **OSINT research** on publicly available GitHub data only. Unauthorized use against private accounts may be *illegal*. Use responsibly and respect users' privacy.
