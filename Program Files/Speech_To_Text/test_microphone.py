#!/usr/bin/env python3

# Program Name:     Microphone Speech to Text Recognition 
# Date Created:     18/11/2022
# Purpose:          To transcibe live speech to text 
# Notes:            This code is based off of open source code from online 
#                   https://medium.com/analytics-vidhya/offline-speech-recognition-made-easy-with-vosk-c61f7b720215

# Importing required files 
import argparse
import queue
import sys
import sounddevice as sd
import json

from vosk import Model, KaldiRecognizer

q = queue.Queue()

# Usage of text string which is the final compilation of text
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError: 
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
args = parser.parse_args(remaining)

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])

    model = Model(lang="en-us")

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device,
            dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                print("This is the end of a phrase.")
                #text_file = open(r'output.txt', 'w')
                #text_file.write(json.loads(rec.Result())['text'])
                #text_file.close()
                print("The text file has now been created")
                json_object = json.loads(rec.Result())
                print(json.loads(rec.Result())['text'])
            else:
                #print(json.loads(rec.PartialResult())['partial'])
                pass
            if dump_fn is not None:
                dump_fn.write(data)

except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))
