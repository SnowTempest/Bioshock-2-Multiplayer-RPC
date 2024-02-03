__author__ = "SnowTempest"
__copyright__ = "Copyright (C) 2022 SnowTempest"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__= "1.0"

from shared import *
from bioshock2 import *

# Function: main()
# Simple main function with banner.
def main():
    print("*****************************************************************************")
    print(" \nBioshock 2 Multiplayer Discord RPC by SnowTempest (ADTempest on YT/Twitch)\n")
    print("*****************************************************************************")

    print("\nYou Can Close the Program at Any Time Using Ctrl + C.\n")
    print("\nWaiting for Multiplayer To Be Open")

    rpc_loop()
    
# Function: rpc_init()
# Initializes the Discord Rich Presence Client Connection.
def rpc_init():
    try:
        CLIENT_ID = rpc_id()
        RPC = pypresence.Presence(CLIENT_ID, pipe = 0)
        RPC.connect()
        return RPC
    except DiscordNotFound:
        close("Discord Is Either Not Open or Not Installed on This System. The Program Will Now Close.")
    except DiscordError:
        close("Invalid APP_ID. Please Make Sure You Have the Right Value and Try Again.")


# Function rpc_id()
# Retrieves the users Discord Application ID from the files.
def rpc_id():
    change_directory()
    file_path = Path("app.txt")

    try:
        with file_path.open("r") as file:
            line = file.readline()
            app_id = line.split('=')[1].strip().strip('"') if 'APP_ID' in line else None
    except FileNotFoundError:
        close("app.txt Not Found. Please Create the File and Put Your Discord App ID Inside.")
    
    if app_id is None:
        close("Invalid Discord ID Found. Did You Follow the Format Correctly?")

    return app_id

# Function: rpc_loop()
# The main rpc loop which will run forever until the user closes Bioshock 2 or close the program manually.
def rpc_loop():
    RPC = rpc_init()
    print("\nRPC has been Activated...")
    print("Press CTRL + C to Quit RPC....\n")

    try:
        while True:
            if not process_active():
                close("Bioshock 2 Is No Longer Open. Bioshock 2 Multiplayer RPC Will Now Close")
            
            bio2_details, bio2_states, bio2_buttons, large_image, large_text = rpc_current_status()
            char_image, char_name = rpc_character_information()

            print("Details: ", bio2_details)
            print("State: ", bio2_states)
            print("\n")

            RPC.update(buttons = bio2_buttons, state=bio2_states, details= bio2_details, large_text=large_text, large_image=large_image, small_image=char_image, small_text=char_name)
            time.sleep(2.0)

    except KeyboardInterrupt:
        close("\nBioshock 2 Multiplayer RPC Will Now Close.")
    except InvalidID:
        close("\nDiscord Either Closed or Crashed. Bioshock 2 Multiplayer RPC Will Now Close.")
    except ProcessNotFound:
        close("\nBioshock 2 Multiplayer Is Not Open. Please Open Before Continuing. Bioshock 2 Multiplayer RPC Will Now Close.")

# Safe Function Calling.
if __name__ == "__main__":
    main()