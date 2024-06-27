import sys
import os
import json
import traceback
import tkinter as tk
from tkinter import messagebox
from time import sleep
from psutil import process_iter

DISCORD_LINK = "https://discord.gg/4ydTGHfFPQ"
APPLICATION_ID = "Bioshock2.exe"

def bioshock_2_is_active():
        directory = None
        for proccess in process_iter(['pid', 'name', 'exe']):
            if proccess.info['name'] == APPLICATION_ID:
                directory = proccess.info['exe']
                break
        
        return directory is not None and "\\MP\\"  in directory

def change_directory():
    if sys.argv[0].endswith('.exe'):
        dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir = os.path.dirname(os.path.abspath(__file__))

    os.chdir(dir)

def log_memory_error(error_message, function_name):
    change_directory()

    log = {
        "Error": error_message,
        "Function": function_name,
        "Traceback": traceback.format_exc().splitlines(),
        "Help": "If you are in need of any assistence with any errors please join the Bioshock 2 Multiplayer Discord and contact either the Admins or the Developer.",
        "Discord": DISCORD_LINK
    }

    log_to_json = json.dumps(log, indent=2)

    with open("error_log.json", "w") as error_log:
        error_log.write(log_to_json)


def log_normal_error(error, error_message, addition_details):
    change_directory()

    log = {
        "Error": error,
        "Error Message": error_message,
        "Additional": addition_details.split("\n"),
        "Help": "If you are in need of any assistence with any errors please join the Bioshock 2 Multiplayer Discord and contact either the Admins or the Developer.",
        "Discord": DISCORD_LINK
    }

    log_to_json = json.dumps(log, indent=2)

    with open("error_log.json", "w") as error_log:
        error_log.write(log_to_json)

    show_error_popup(error, error_message)
    program_close("Program will close in 4 seconds.")

def show_error_popup(error, error_message):
    error_root = tk.Tk()
    error_root.withdraw()
    messagebox.showerror(error, error_message + " Please view error_log.json for more details.")
    error_root.destroy()

def clear_log():
    change_directory()
    with open("error_log.json", "w") as error_log:
        error_log.write("{\n\n}")

def program_close(close_message):
    print(close_message)
    sleep(0.1)
    exit()