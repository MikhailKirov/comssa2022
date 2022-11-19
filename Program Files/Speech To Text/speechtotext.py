# Program Name:     Asynchronously Transcbe a local audio file 
# Date Created:     18/11/2022
# Purpose:          To transcibe speech files to text 
# Notes:            This code is based off of open source code from
#                   google collab https://cloud.google.com/speech-to-text/docs/samples/speech-transcribe-async#speech_transcribe_async-python

import os 
import sys


from pydub import AudioSegment
audio = AudioSegment.from_file('Hey.m4a')

def transcribe_file(speech_file):
    """Transcribe the given audio file asynchronously."""
    from google.cloud import speech

    client = speech.SpeechClient()

    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()

    """
     Note that transcription is limited to a 60 seconds audio file.
     Use a GCS file for audio longer than 1 minute.
    """
    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )


    operation = client.long_running_recognize(config=config, audio=audio)

    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)

    # Each result is for a consecutive portion of the audio. Iterate through
    # them to get the transcripts for the entire audio file.
    for result in response.results:
        # The first alternative is the most likely one for this portion.
        print(u"Transcript: {}".format(result.alternatives[0].transcript))
        print("Confidence: {}".format(result.alternatives[0].confidence))

    print("Hello")


transcribe_file(audio)
