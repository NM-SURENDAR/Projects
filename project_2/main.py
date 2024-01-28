import tkinter as tk
import speech_recognition as sr

def record_audio():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        text_entry.insert(tk.END, text + '\n')
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

def save_to_file():
    text_content = text_entry.get("1.0", tk.END)
    with open("output.txt", "w") as file:
        file.write(text_content)

# Create the main window
app = tk.Tk()
app.title("NLP Virtual Assistant")

# Create widgets
text_entry = tk.Text(app, wrap="word", height=10, width=40)
record_button = tk.Button(app, text="Record", command=record_audio)
save_button = tk.Button(app, text="Save to File", command=save_to_file)

# Place widgets in the window
text_entry.pack(padx=10, pady=10)
record_button.pack(pady=5)
save_button.pack(pady=5)

# Start the GUI event loop
app.mainloop()
