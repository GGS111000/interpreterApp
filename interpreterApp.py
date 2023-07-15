import speech_recognition as sr
from googletrans import Translator
from tkinter import Tk, Button, Text, END, messagebox


def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # messagebox.showinfo("Info", "Start speaking...")
        audio = r.record(source, duration=5)  # Listening for 5 seconds
        # messagebox.showinfo(
        #     "Info", "Speech recognition is completed. Translating now..."
        # )

    try:
        text_en = r.recognize_google(audio, language="en")
        text_zh = r.recognize_google(audio, language="zh-CN")

        translator = Translator()
        detected_lang = translator.detect(
            text_en if len(text_en) > len(text_zh) else text_zh
        ).lang
        text = text_en if detected_lang == "en" else text_zh

        translated = translator.translate(
            text, "zh-cn" if detected_lang == "en" else "en"
        )

        text_box.insert(END, f"Original: {text}\n")
        text_box.insert(END, f"Translated: {translated.text}\n\n")
    except Exception as e:
        print(e)


root = Tk()
root.geometry("400x600")

btn = Button(root, text="Speak", command=recognize_speech)
btn.pack()

text_box = Text(root)
text_box.pack()

root.mainloop()
