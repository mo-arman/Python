import pyttsx3

# Initialize the speech engine
engine = pyttsx3.init()

# Set the speaking rate (optional, to slow down or speed up)
engine.setProperty('rate', 150)  # Adjust the rate if needed

# Define a longer text to reach 1 minute
speech_text = """
Hello, world! Today, let's explore what artificial intelligence can achieve.
Artificial intelligence, or AI, is transforming the world around us, from virtual assistants
to complex problem-solving in fields like healthcare, finance, and more. AI enables us to 
analyze vast amounts of data quickly, learn from it, and make decisions with incredible accuracy.
In the future, AI might help us in ways we can't even imagine today, making life more convenient 
and productive for everyone. The journey of AI has just begun, and it's a thrilling one.
"""

# Say the text
engine.say(speech_text)

# Run the speech
engine.runAndWait()
