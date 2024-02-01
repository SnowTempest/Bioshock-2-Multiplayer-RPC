#Related Imports
import psutil
import pypresence
from pypresence.exceptions import DiscordNotFound, DiscordError, InvalidID
import os, time, sys
from pymem import *
from pymem.process import *
from pymem.exception import ProcessNotFound
from functools import wraps
from pathlib import Path
import traceback

# Function change_directory()
# Changes the current working directory to be where the executable / Script is located.
# The script directory only matters for my end.
def change_directory():
    if sys.argv[0].endswith('.exe'):
        dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir = os.path.dirname(os.path.abspath(__file__))

    os.chdir(dir)

# Function get_directory()
# Gets the current working directory to be where the executable / Script is located.
# The script directory only matters for my end.
def get_directory():
    if sys.argv[0].endswith('.exe'):
        dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir = os.path.dirname(os.path.abspath(__file__))

    return dir


def log_error(error, error_message, function_name):
    change_directory()
    log_path = Path("log.txt")
    with log_path.open ("w") as log:
        log.write(f"Error: {error} Message: {error_message} Function: {function_name}", )
        log.write(traceback.format_exc())
        log.write("\n\n")


def close(message):
    print(message)
    time.sleep(2)
    exit()

# Public Discord Server Link
MPDISCORD_LINK = "https://discord.gg/4ydTGHfFPQ"
MYDISCORD_LINK = "https://discord.gg/EanaD3sWgh"