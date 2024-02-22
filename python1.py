import speech_recognition as sr
import pyttsx3
import datetime

# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech input
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-US')
            print(f"You: {query}")
            return query.lower()
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return ""
        except sr.RequestError:
            print("Sorry, I couldn't reach the recognition service.")
            return ""

# Main function to handle user commands
def main():
    speak("Hello! I'm your voice assistant. How can I assist you today?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How are you today?")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date}")

        elif "exit" in command or "quit" in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()

