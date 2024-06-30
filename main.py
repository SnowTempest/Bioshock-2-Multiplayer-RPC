__author__ = "SnowTempest"
__copyright__ = "Copyright (C) 2024 SnowTempest"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__= "1.0"

import pypresence
from pypresence import DiscordNotFound, DiscordError, InvalidID, PipeClosed
from pymem.exception import ProcessNotFound
from bioshock_2_multiplayer_utils import json, sleep, change_directory, log_normal_error, clear_log, program_close, bioshock_2_is_active
from bioshock_2_multiplayer_rpc import rpc_status

def rpc_id():
    change_directory()
    with open ("rpc_data.json", "r") as json_file:
        json_data = json.load(json_file)

    return json_data.get("APP_ID", "")

def rpc_init():
    try:
        print("Starting RPC Client")
        clear_log()
        CLIENT_ID = rpc_id()

        if CLIENT_ID == "":
            raise DiscordError(code="rpc_init", message="An error has occured trying to retrieve the Application ID in rpc_data.json.")

        RPC = pypresence.Presence(CLIENT_ID, pipe=0)
        RPC.connect()
        return RPC

    except DiscordNotFound:
        log_normal_error("Pypresence Error: DiscordNotFound", "Discord is not open or was not found. Please open Discord before launching the Bioshock 2 Multiplayer RPC.", "Discord was not open during the RPC initialization or the RPC channel was already in use by another program. \nPlease re-open Discord or close any other RPC programs before re-attempting Bioshock 2 Multiplayer RPC connection.")
    except DiscordError:
        log_normal_error("Pypresence Error: DiscordError", "Invalid Discord \"APP_ID\". Please make sure you have the right value stored in rpc_data.json and try again.", "There was an error trying to connect to the User's Discord Developer Application ID. \nPlease verify that your Application ID is valid and fits the format in rpc_data.json. Example Format: \"APP_ID\":123456789098765432")

def rpc_loop():
    RPC = rpc_init()

    print("RPC has been Initialized")
    print("\nYou Can Close the RPC at Any Time Using Ctrl + C.\n")

    try:
        while True:
            if not bioshock_2_is_active():
                program_close("Bioshock 2 Is No Longer Open. Bioshock 2 Multiplayer RPC Will Now Close")
            
            bio2_details, bio2_state, bio2_buttons, bio2_image, bio2_text, bio2_small_image, bio2_small_text = rpc_status()
            RPC.update(buttons=bio2_buttons, state=bio2_state, details=bio2_details, large_text=bio2_text, large_image=bio2_image, small_image=bio2_small_image, small_text=bio2_small_text)
            sleep(1.0)
    except KeyboardInterrupt:
        program_close("\nBioshock 2 Multiplayer RPC Will Now Close.")
    except InvalidID:
        log_normal_error("Pypresence Error : InvalidID", "\nDiscord either closed or crashed. Bioshock 2 Multiplayer RPC will be closed.", "There was an issue during the RPC call trying to contact Discord. Either Discord has crashed or something bad happened with the RPC Program. \nOther causes of this error are currently unknown. Please let the Developer know if this error occurs.")
    except ProcessNotFound:
        log_normal_error("Pymem Error: ProcessNotFound","\nBioshock 2 Multiplayer is not open or crashed. Bioshock 2 Multiplayer RPC will now close.", "Bioshock 2 Multiplayer was not found in the User's list of processes thus it was no longer safe to continue Bioshock 2 Multiplayer RPC connection. \nThis error helps prevent any memory read errors that might occur.")
    except PipeClosed:
        log_normal_error("Pypresence Error: PipeClosed", "\nDiscord either closed or crashed causing the RPC connection to close. Bioshock 2 Multiplayer RPC will be closed.","This issue occurs when Discord itself crashes while the RPC is connected causing the Pipe Connection to be closed. \nSimply restart the Bioshock 2 Multiplayer RPC again after Discord has been re-opened." )


def main():
    banner()
    rpc_loop()

def banner():
    print("*****************************************************************************")
    print(" \nBioshock 2 Multiplayer Discord RPC by SnowTempest (ADTempest on YT/Twitch)\n")
    print("*****************************************************************************")

# Safe Function Calling.
if __name__ == "__main__":
    main()
