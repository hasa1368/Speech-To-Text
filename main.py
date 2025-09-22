import speech_recognition as sr

def main():
    recognizer = sr.Recognizer()

    # Use default microphone
    with sr.Microphone() as source:
        print("🎤 لطفاً صحبت کنید ...")
        recognizer.adjust_for_ambient_noise(source)  # reduce background noise
        audio = recognizer.listen(source)

    try:
        # Use Google API with Farsi language (Persian/Iran)
        text = recognizer.recognize_google(audio, language="fa-IR")
        print("✅ متن شما: " + text)

        # Save result to a text file
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)

    except sr.UnknownValueError:
        print("❌ متوجه صحبت شما نشدم.")
    except sr.RequestError as e:
        print(" خطا در ارتباط با سرویس گوگل؛ جزئیات:", e)

if __name__ == "__main__":
    main()
