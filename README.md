# 🤖 AI Chat Bot – Automated Chat Responder

A Python bot that reads chat history and uses **OpenAI GPT** to generate witty, roast-style replies in real-time. It pastes and sends responses automatically, fully hands-free. Built with **PyAutoGUI** and **Pyperclip**, it can target specific users or threads, showcasing AI-powered, automated, and interactive chat tools that are both fun and practical.

---

## ✨ Features
- **Automated Chat Reader** – Copies chat text directly from the screen  
- **AI-Powered Replies** – Generates witty or roast-style responses  
- **Hands-Free Automation** – Pastes and sends replies automatically  
- **Custom Targeting** – Responds to specific users or chat threads  

---

## 🛠 Tech Stack
- **Python**  
- **OpenAI API**  
- **PyAutoGUI** (automation)  
- **Pyperclip** (clipboard handling)  

---

## 🚀 How It Works
1. Selects and copies chat history  
2. Checks if the last message is from a target sender  
3. Sends the chat to GPT for response generation  
4. Pastes the reply and sends it automatically  

---

## 🔧 Setup & Usage
```bash
# Clone the repository
git clone https://github.com/<your-username>/<repo-name>.git

# Install dependencies
pip install pyautogui pyperclip openai

# Add your OpenAI API key in the script
python main.py
