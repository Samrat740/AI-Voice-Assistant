import speech_recognition as sr
import pyttsx3
import time
import webbrowser
import pywhatkit as kit
import pyautogui

# Function to recognize voice commands
def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        if "hello" in text:
            print("Hi! How can I assist you?")
            speak("Hi! How can I assist you?")
        if "tell me about yourself" in text:
            print("Hello, myself Samrat. I am an AI assistant build using advanced python.")
            print("Hope you will like me")
            speak("Hello, myself Samrat. I am an AI assistant build using advanced python. Hope you will like me")
        return text
    except:
        print("Sorry, I didn't catch that.")
        speak("Sorry, I didn't catch that.")
        return ""

# Function to speak a text
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Main function to listen for voice commands and open websites
def main():
    
    while True:
        command = recognize_speech().lower()
        if "samrat" in command:
            if "search" in command:
                print("What do you want me to search?")
                speak("What do you want me to search?")
                query = recognize_speech().lower()
                url = f"https://www.google.com/search?q={query}"
                print("Okay, searching for " + query)
                speak("Okay, searching for " + query)
                webbrowser.open(url)
                time.sleep(5)
                try:
                    result_div = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div/div[1]/a/h3')
                    result = result_div.text
                    speak(result)
                except:
                    print("Here are the search results")
                    speak("Here are the search results")
                    

            if "play music" in command:
                print("What song do you want to listen?")
                speak("What song do you want to listen?")
                song = recognize_speech().lower()
                try:
                    print("Okay, playing on youtube")
                    speak("Okay, playing on youtube")
                    kit.playonyt(song)
                    time.sleep(5)
                    
                except:
                    print("Server busy! Sorry for the inconvenience")
                    speak("Server busy! Sorry for the inconvenience")

                    
                
                
            if "youtube" in command:
                print("Yes, opening YouTube")
                speak("Yes, opening YouTube")
                webbrowser.open("https://www.youtube.com/")

            if "instagram" in command:
                print("Yes, opening Instagram")
                speak("Yes, opening Instagram")
                webbrowser.open("https://www.instagram.com/")
        
            if "facebook" in command:
                print("Yes, opening Facebook")
                speak("Yes, opening Facebook")
                webbrowser.open("https://www.facebook.com/")
            
            if "twitter" in command:
                print("Yes, opening Twitter")
                speak("Yes, opening Twitter")
                webbrowser.open("https://www.twitter.com/")


            elif "exit" in command:
                print("ThankYou! Have A Good Day")
                speak("ThankYou! Have A Good Day")

                break
if __name__ == "__main__":
    main()
