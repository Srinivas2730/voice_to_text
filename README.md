                                        🧠 Streamlit Project
                                      📄 Voice-to-Text Converter

📌 Project Overview

This app converts your speech into text! It supports multiple languages and accents, and also allows you to type text directly if you prefer. Built with Python + Streamlit + SpeechRecognition, this beginner-friendly project is perfect for demonstrating audio AI workflows.

🚀 How I Built & Ran the App (Step-by-Step)

1️⃣ Created a project folder: VoiceToTextProject

2️⃣ Inside the folder, added the main Python file:

project1_voice_to_text.py → Streamlit frontend for recording and converting speech

3️⃣ Created a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate  # Windows

4️⃣ Installed dependencies:

pip install SpeechRecognition pyaudio streamlit

5️⃣ Ran the app:

streamlit run project1_voice_to_text.py

6️⃣ Opened the app in the browser:
🌍 http://localhost:8501

🔁 GitHub Upload Steps

1️⃣ Created a new repository on GitHub
2️⃣ Opened terminal in the project folder
3️⃣ Initialized Git:

git init

4️⃣ Added all files:

git add .

5️⃣ Committed changes:

git commit -m "Add Voice-to-Text Converter project"

6️⃣ Linked to GitHub repo:

git remote add origin https://github.com/your-username/your-repo-name.git

7️⃣ Pushed the code:

git push -u origin main
📁 Project Folder Structure

📦 VoiceToTextProject
┣ 📄 project1_voice_to_text.py → Streamlit app for audio-to-text
┣ 📁 .venv → Virtual environment (not tracked)
┣ 📄 README.md → This file
┗ 📄 LICENSE → MIT License

💡 What the App Can Do

✔ Record audio and convert to text
✔ Supports multiple accents/languages: English (US/UK/India), Spanish, French, Telugu
✔ Option to type text instead of speaking
✔ Streamlit interface with live results

✨ Tech Stack Used
Python — programming language
Streamlit — interactive front-end
SpeechRecognition — convert audio to text
PyAudio — microphone access

👩‍💻 Created By

Ushmitha Annapaneni

Feel free to ⭐ star or fork the project!

📄 License

MIT License — Free to use, modify, and share