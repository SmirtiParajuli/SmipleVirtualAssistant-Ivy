import datetime
import os
import platform
import subprocess
import webbrowser
import pyttsx3
import requests
import speech_recognition as sr
import openai


# Function that play audio
def say(text):
    """
      Convert the given text to speech and play it.

      Parameters:
      - text (str): The text to be converted to speech.
      """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# todo: This  is the function to make the weather forcast but the api does not work.
# todo : And need to add this comand to the main function

def get_weather(city):
    """
     Get weather information for a given city.

     Parameters:
     - city (str): The city for which weather information is requested.

     Returns:
     - str: Weather information for the city.
     """
    api_key = "Please provide your weatherai API key here"

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # You can change to "imperial" for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    print(response.json())  # Check if this is printed
    weather_data = response.json()

    if response.status_code != 200:
        return f"Error: {weather_data['message']}"

    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]
    return f"The weather in {city} is {description} with a temperature of {temperature} degrees Celsius."



def ai(prompt):
    """
       Generate a response using OpenAI's GPT-3.5 Turbo model and save it to a file called OpenAi.

       Parameters:
       - prompt (str): The prompt for generating the AI response.
       """
    openai.api_key = "Please  put your open Ai API here "
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    # Append the generated text to the prepared text
    text += response["choices"][0]["text"]
    # Create a directory for storing OpenAI responses if it doesn't exist
    if not os.path.exists("Openai"):
        os.mkdir("Openai")
    # Save the response to a file with a specific format
    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)
        # Notify the user that the response is available
    say("Your response is now available.")

def take_command():
    # Create a Recognizer object for speech recognition
    r = sr.Recognizer()
    # Set up the microphone and other necessary configurations
    with sr.Microphone() as source:
        print("Listening...")
        # Adjust the pause threshold and ambient noise for better recognition
        r.pause_threshold = 0.6
        r.adjust_for_ambient_noise(source, duration=1)
        # Listen to the audio from the microphone
        audio = r.listen(source)

# Default comments for the try-except block
    try:
        print("Recognizing...")
        # Use Google Speech Recognition to convert audio to text
        command = r.recognize_google(audio, language="en-au")
        print(f"User said: {command}")
        return command
    except sr.UnknownValueError:
        # Handle the case where speech recognition couldn't understand the audio
        print("Sorry, I couldn't understand that.")
        return ""
    except sr.RequestError as e:
        # Handle the case where there is an issue with the Google Speech Recognition service
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

if __name__ == '__main__':
    introduction = "Hello, I am Ivy, your virtual assistant."
    print(introduction)
    say(introduction)


    # List of the web pages that Ivy opens on command
    sites = [
        ("YouTube", "https://youtube.com"),
        ("GitHub", "https://github.com"),
        ("LinkedIn", "https://linkedin.com"),
        ("TorrentBlackboard", "https://torrens.blackboard.com"),
        ("Notion", "https://notion.so"),
        ("Google", "https://google.com")
    ]

    while True:
        user_input = take_command()

        if "hello" in user_input:
            response = "Hi there!"
            say(response)
        elif "stop" in user_input.lower():
            say("Goodbye! Have a good one!")
            break
        else:
            # Function to open the web page
            # todo: add more sites to open automatic
            for site in sites:
                if f"open {site[0]}".lower() in user_input.lower():
                    webbrowser.open(site[1])
                    say(f"Opening {site[0]}")
# todo: Add the specific song play
            # Project file opening system
            if "open image" in user_input.lower():
                image_path = r"IMG_4577.webp"
                try:
                    # Using different commands based on the operating system
                    if platform.system() == "Windows":
                        os.startfile(image_path)
                    else:
                        subprocess.Popen(["open", image_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception as e:
                    print(f"Error opening image: {e}")

            # Check for opening folders or navigate through the file
            if "open folder" in user_input.lower():
                folder_path = r"Pictures"  # Change the folder path as needed
                try:
                    # Using different commands based on the operating system
                    if platform.system() == "Windows":
                        os.startfile(folder_path)
                    else:
                        subprocess.Popen(["open", folder_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception as e:
                    print(f"Error opening folder: {e}")
# This is the function to  open internal app through the voice command. need to change the file plath( use the file path that your
# app in store and it will be able to apen the file) for multiple file need to change the code according to the sites (the above code)
            if "open app" in user_input.lower():
                folder_path = r"Pictures"  # Change the folder path as needed
                try:
                    # Using different commands based on the operating system
                    if platform.system() == "Windows":
                        os.startfile(folder_path)
                    else:
                        subprocess.Popen(["open", folder_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                except Exception as e:
                    print(f"Error opening folder: {e}")

# Condition for the date and time for the time or date
            if "time" in user_input.lower():
                current_datetime = datetime.datetime.now().strftime("%I:%M %p")
                response = f"The current time is {current_datetime}"
                say(response)
                print(response)  # for debug purpose
            elif "date" in user_input.lower():
                current_datetime = datetime.datetime.now()
                formatted_date = current_datetime.strftime("%A, %B %d, %Y")
                response = f"Today's date is {formatted_date}"
                say(response)
                print(response) # for debug purpose

            # else:
            #     print("Condition not met. User input:", user_input.lower())
            elif "Using artificial intelligence".lower() in user_input.lower():
                ai(prompt=user_input)

#todo: make a AWS toolkit working and make a Ivy chat with you


