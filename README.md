# 🎤 Speech-to-Text Project (Farsi / Online)

This project is a simple **Python Speech-to-Text** application that captures audio from your microphone and converts it into **Persian text**.  
It uses the online **Google Speech Recognition API**, so an internet connection is required.

---

## 📂 Project Structure
SpeechToText/
├── main.py # Main Python program
├── requirements.txt # Required libraries
└── output.txt # Output file where recognized text is saved

yaml
Copy code

---

## 🚀 Installation and Running

### 1. Install Python
- Recommended: **Python 3.10 or higher**  
- Verify installation:
```bash
python --version
pip --version
2. Install Dependencies
In PyCharm Terminal or CMD:

bash
Copy code
pip install SpeechRecognition
pip install pyaudio
⚠️ If pyaudio fails on Windows:

Download the appropriate .whl from PyAudio wheels

Install manually:

bash
Copy code
pip install PyAudio-0.2.11-cp311-cp311-win_amd64.whl
3. Run the Program
bash
Copy code
python main.py
The program activates your microphone

Speak in Farsi → the recognized text will appear in the console

The text is also saved automatically in output.txt

✨ Features
Converts Farsi speech to text

Uses Google Speech API (online)

Automatically saves recognized text to a file

Easy to extend and add more features

👨‍💻 Developer
Hamed Sadeghi Firouzja
