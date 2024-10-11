import json
import traceback
from sys import exit
from tkinter import Tk, messagebox

DISCORD_LINK = "https://discord.gg/4ydTGHfFPQ"
STORE_LINK = "https://store.steampowered.com/app/8850/BioShock_2/"

class BioMPLogger():
    def __init__ (self, LOG_FILE="error_log.json"):
        self.LOG_FILE = LOG_FILE
        self.log_clear()
    
    def log_write(self, log):
        log_to_json = json.dumps(log, indent=2)

        try:
            with open(self.LOG_FILE, "w") as log:
                log.write(log_to_json + "\n")
        except Exception as e:
            print(f'There was an error writing to log. Error Code: {e}')
            print(f'Included Log: {log_to_json}')

    def log_error(self, error, error_message, error_type="GENERAL", function_name=None, additional_details=None):
        log = {
            "Error": error,
            "Error Message": error_message,
            "Function": function_name if error_type == "MEMORY" else "N/A",
            "Additional": additional_details.split("\n") if error_type == "GENERAL" else "N/A",
            "Traceback": traceback.format_exc().splitlines() if error_type == "GENERAL" else "N/A",
            "Help": "If you are in need of any assistence with any errors please join the Bioshock 2 Multiplayer Discord and contact either the Admins or the Developer.",
            "Discord": DISCORD_LINK
        }

        self.log_write(log)

        if error_type == "GENERAL":
            self.log_display_error(error, error_message)
            exit()

    def log_clear(self):
        open(self.LOG_FILE, 'w').close()
    
    def log_display_error(self, error, error_message):
        root = Tk()
        root.withdraw()
        messagebox.showerror(error, error_message + " Please look at error_log.json in the program's directory for more details.")
        root.destroy()
    
    def log_test_logger(self):
        log = {
            "Error": "Log Tester", 
            "Error Message": "Testing the logging environment."
        }

        self.log_write(log)
