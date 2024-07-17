                                                        Ivy - Your Virtual Assistant

Description:

    Ivy is a Python-based virtual assistant that uses speech recognition and synthesis to interact with users. It performs various tasks such as 
    retrieving weather information, opening websites, executing system commands, and generating responses using openAI like ChatGPT.

Setup Instructions:

Python Version:

        Make sure you have Python 3.x installed on your system.
        and other important dependencies.

Dependencies:

Install the required Python libraries using pip:

    pip install pyttsx3 requests SpeechRecognition openai


API Keys:

      Obtain the necessary API keys:
      OpenWeatherMap API key for weather information.
      OpenAI API key for AI response generation.
      Operating System Compatibility:

The script supports Windows and Unix-based systems (Linux, macOS).

Functionalities:

Speech Recognition and Synthesis:

    Converts speech to text using Google's Speech Recognition.
    Converts text to speech using pyttsx3.
    
Web Interaction:

    Opens predefined websites (e.g., YouTube, GitHub) based on user commands.
    
System Commands:

Opens specific files (image_path, folder_path) based on user commands.

Retrieves current date and time:

AI Interaction:

    Uses OpenAI's GPT-3.5 Turbo model to generate responses based on user prompts.
Voice Commands:

Recognizes voice commands for various operations like opening apps, checking time/date, and interacting with AI.

Usage:
Running the Script:

        Execute VirtualAssistant.py in a Python environment.

Voice Commands:

      Speak clearly into the microphone to interact with Ivy.

Commands:

    Say "Hello" to start a conversation with Ivy.
    Ask for the "time" or "date" to get current time or date information.
    Ask Ivy to "open" a specific website, image, folder, or app.
    Use the phrase "Using artificial intelligence" to prompt Ivy to generate an AI response based on your input.
    
Notes:

        Ensure microphone access is granted for speech recognition to function correctly.
        Modify image_path, folder_path, and add more websites/apps as needed in the script.
        
Troubleshooting:

      If encountering issues with speech recognition or API calls, check internet connectivity and API key validity.
      Review console outputs for error messages and debug information.
      
Author:
Smirti Parajuli
