# Program Name:     Asynchronously Transcbe a local audio file 
# Date Created:     18/11/2022
# Purpose:          To transcibe speech files to text 
# Notes:            This code is based off of open source code from online 
#                   https://www.geeksforgeeks.org/python-convert-speech-to-text-and-text-to-speech/

# Python program to translate
# speech to text and text to speech

import speech_recognition as sr
import pyttsx3
import time 

m4a_file = "Hey.m4a"
wav_filename = r"HeyLongTimeNoSee.wav"
from pydub import AudioSegment
track

# Initialize the recognizer
r = sr.Recognizer()

# Initialise speech time 
time_end  = time.time() + 30

# Function to convert text to
# speech
def SpeakText(command):
	
	# Initialize the engine
	engine = pyttsx3.init()
	engine.say(command)
	engine.runAndWait()
	
	
# Loop infinitely for user to
# speak

print("Start of Loop")

while time.time() < time_end:
	
	print("Restart Loop")
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			
			#listens for the user's input
			audio2 = r.listen(source2)
			
			# Using google to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()

			print("Did you say ",MyText)
			SpeakText(MyText)
			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occurred")
