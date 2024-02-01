from shared import *
from bioshock2_memory import *

# Function process_active()
# This function checks if the Bioshock 2 process is Active.
# Also checks if the Process is located in the Multiplayer Directory and not the Singleplayer Direcotry.
def process_active():
    directory = None
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['name'] == APPLICATION_ID:
            directory = proc.info['exe']
            break
    
    return directory is not None and "\\MP\\" in directory

if process_active():
    MEM = Pymem(APPLICATION_ID)
    BASE_ADDRESS = module_from_name(MEM.process_handle, APPLICATION_ID).lpBaseOfDll
    BASE_POINTER = BASE_ADDRESS + INITIAL_OFFSET
else:
    close("\nBioshock 2 Multiplayer is not Open. Please open before continuing. Bioshock 2 Multiplayer RPC will safely close.")

# Class Bioshock2
class Bioshock2Multiplayer:
    CHARACTERS = {
        0: "Mlle Blanche de Glace",
        1: "Naledi Atkins",
        2: "Jacob Norris",
        3: "Barbara Johnson",
        4: "Buck Raleigh",
        5: "Zigo d'Acosta",
        6: "Danny Wilkins",
        7: "Oscar Calraca",
        8: "Suresh Sheti",
        9: "Louie McGraff"
    }

    MELEE_WEAPONS = {
        "Default Melee": ["Wrench", "Candle Stick","Pipe","Machete","Rolling Pin","Mallet","Barbed Wire","Crowbar","Flashlight","Hatchet"],
        "Blanche Unique": "Knife",
        "Naledi Unique": "Pipe Wrench",
        "Jacob Unique": "Torch",
        "Barbara Unique": "Frying Pan",
        "Buck Unique": "Golf Club",
        "Zigo Unique": "Fisherman Club",
        "Danny Unique": "Football Trophy",
        "Oscar Unique": "Cricket Bat",
        "Suresh Unique": "Cane",
        "Louie Unique": "Shank"
    }

    MAPS = {
        0:  "Arcadia",
        1:  "Farmer's Market",
        2:  "Fort Frolic",
        3:  "Hephaestus",
        4:  "Home For The Poor",
        5:  "Kashmir Restaurant",
        6:  "Medical Pavilion",
        7:  "Mercury Suites",
        8:  "Neptune's Bounty",
        9:  "Point Prometheus",
        10: "Fontaine Fisheries",
        11: "Pauper's Drop",
        12: "Smuggler's Hideout",
        13: "Fighting McDonagh's",
        14: "Dionysus Park",
        15: "Siren Alley",
        16: "Test Box",
    }

    MAP_URLS = {
        "DE_Arcadia": "Arcadia",
        "DE_Market": "Farmer's Market",
        "DE_FortFrolic": "Fort Frolic",
        "DE_Hephaestus": "Hephaestus",
        "DE_HomeforthePoor": "Home For The Poor",
        "DE_Kashmir": "Kashmir Restaurant",
        "DE_Medical": "Medical Pavilion",
        "DE_MercurySuites": "Mercury Suites",
        "DE_Fisheries": "Neptune's Bounty",
        "DE_Museum": "Point Prometheus",
        "DE_Freezers": "Fontaine Fisheries",
        "DE_Ghetto": "Pauper's Drop",
        "DE_Subbay": "Smuggler's Hideout",
        "DE_Tavern": "Fighting McDonagh's",
        "DE_Gallery": "Dionysus Park",
        "DE_RedLightAlley": "Siren Alley",
        "DE_Testbox": "Testbox",
        "DE_ApartmentLobby" : "Apartment Lobby",
        "Entry": "Main Menu"
    }


    GAMEMODES ={
        0: "Survival of the Fittest",
        1: "Civil War",
        3: "Capture The Sister",
        4: "Team Adam Grab",
        5: "Turf War",
        6: "Kill 'Em Kindly",
        8: "Adam Grab",
        9: "Last Splicer Standing"
    }

    PLASMIDS = {
        "Electro Bolt",
        "Telekinesis",
        "Aero Dash",
        "Insect Swarm",
        "Geyser Trap", 
        "Houdini",
        "Poison Quills",
        "Incinerate", 
        "Winter Blast",
        "Proximity Mine",
        "Stomp"
    }

    WEAPONS = {
        "Pistol",
        "Shotgun",
        "Crossbow",
        "Grenade Launcher",
        "Machine Gun",
        "Nail Gun",
        "Elephant Gun",
        "Rivet Gun",
        "Wrench"
    }

    UPGRADES = {
        "Ammo Capacity",
        "Automatic Firing",
        "Damage Increase",
        "Automatic Reload",
        "Rate of Fire",
        "Sawed-Off Barrel",
        "Magazine Size",
        "Kickback Reduction",
        "Firing Boost",
        "Piercing Bolt",
        "Velocity Boost",
        "Homing Grenades",
        "Slug Capacity",
        "Sniper Scope",
        "Burst Firing"
    }

    SCREENS = {
        "MatchMakingPortal.swf": "Lobby",
        "ConfigureLoadout.swf": "Loadout",
        "CustomizeCharacter.swf": "Customize Character",
        "CharacterSelect.swf": "Select Character",
        "ViewProfile.swf": "Personal Statistics",
        "Trials.swf": "Trials",
        "MainMenu.swf": "MainMenu",
        "Credits.swf": "Credits",
        "Options.swf": "Options",
        "AttractVideoContainer.swf": "Intro Video",
        "Apartment": "Apartment",
        "Apartment Lobby": "Apartment Lobby",
        "Apartment Intro": "Prologue",
        "Apartment Outro": "Epilogue",
        "HUDMultiplayer.swf": "In-Game",
        "PlasmidVideoContainer.swf": "Plasmid Video",
        "End Game": "Match Ended",
        "Scoreboard": "Scoreboard",
        "Match Results": "Match Results",
        "Loading": "Loading"
    }

class Bioshock2MultiplayerRichPresence:
    MAP_IMAGES ={
        "Arcadia":              "https://i.imgur.com/8k1fkKb.png",
        "Farmer's Market":      "https://i.imgur.com/0Fj2jiA.png",
        "Fort Frolic":          "https://i.imgur.com/OYMhqZl.png",
        "Hephaestus":           "https://i.imgur.com/adRcoOj.png",
        "Home For The Poor":    "https://i.imgur.com/jw0sdrt.png",
        "Kashmir Restaurant":   "https://i.imgur.com/4ks1As2.png", 
        "Medical Pavilion":     "https://i.imgur.com/I8jWFOC.png",
        "Mercury Suites":       "https://i.imgur.com/UXnGnxx.png",
        "Neptune's Bounty":     "https://i.imgur.com/SqI15fL.png",
        "Point Prometheus":     "https://i.imgur.com/dgRqebN.png",
        "Fontaine Fisheries":   "https://i.imgur.com/vhpse05.png",
        "Pauper's Drop":        "https://i.imgur.com/jNiTUT7.png",
        "Smuggler's Hideout":   "https://i.imgur.com/eV8kOFK.png",
        "Fighting McDonagh's":  "https://i.imgur.com/MG3zPQo.png",
        "Dionysus Park":        "https://i.imgur.com/ylscKK9.png",
        "Siren Alley":          "https://i.imgur.com/I0jTeQB.pngb",
        "Testbox":              "https://i.imgur.com/cG9yNAi.png",
        "Apartment":            "https://i.imgur.com/h9TrCSL.png",
        "Main Menu":            "https://i.imgur.com/zJRrotE.png",
        "DLC":                  "https://i.imgur.com/LHnNhqC.png"
    }

    CHARACTER_IMAGES = {
        "Mlle Blanche de Glace": "https://i.imgur.com/8urkDmq.png",
        "Naledi Atkins":         "https://i.imgur.com/qaRMFRm.png",
        "Jacob Norris":          "https://i.imgur.com/WbqxwU2.png",
        "Barbara Johnson":       "https://i.imgur.com/GVmIHLg.png",
        "Buck Raleigh":          "https://i.imgur.com/UNCjf49.png",
        "Zigo d'Acosta":         "https://i.imgur.com/JspBIN5.png",
        "Danny Wilkins":         "https://i.imgur.com/e0vCXv3.png",
        "Oscar Calraca":         "https://i.imgur.com/MIFGDa5.png",
        "Suresh Sheti":          "https://i.imgur.com/xckcZav.png",
        "Louie McGraff":         "https://i.imgur.com/ADpFeUt.png"
    }
    
    GAME_INFORMATION = {
        "MainMenu": {"Details": "Main Menu", "States": "At the Title Screen"},
        "Options": {"Details": "Options", "States": "At the Options Menu"},
        "Loadout": {"Details": "Customize Loadout", "States": "Customizing their Loadout"},
        "Select Character": {"Details": "Character Selection", "States": "Choosing their Character"},
        "Customize Character": {"Details": "Customize Character", "States": "Choosing their Mask and Melee"},
        "Personal Statistics": {"Details": "Personal Statistics", "States": "Looking at their Lifetime Stats"},
        "Trials": {"Details": "Trials", "States": "Looking at their list of Trials"},
        "Intro Video": {"Details": "Promotional Video", "States": "Watching the Promotional Video"},
        "Credits": {"Details": "Credits", "States": "Watching the Credits"},
        "Plasmid Video": {"Details": "Plasmid Promotional Video", "States": "Watching a Plasmid Video"},
        "Lobby": {"Details": "Lobby", "States": "Main Menu"},
        "Apartment": {"Details": "Apartment", "States": "Wandering in their Apartment"},
        "Prologue": {"Details": "Prologue", "States": "Watching the Apartment Prologue"},
        "Epilogue": {"Details": "Epilogue", "States": "Watching the Apartment Epilogue"},
        "Apartment Lobby": {"Details": "Apartment Lobby", "States": "Main Menu"},
        "In-Game": {"Details": "In-Game", "States": "In-Game"},
        "Match Ended": {"Details": "End-Match", "States": "Match Has Ended"},
        "Scoreboard": {"Details": "Scoreboard", "States": "Viewing End-Match Scoreboard"},
        "Match Results": {"Details": "Match Results", "States": "Viewing Match Results"},
        "Loading": {"Details": "Loading", "States": "Player is currently loading..."}
    }

def pointer_address(base, offsets):
    addr = MEM.read_int(base)
    for i, offset in enumerate(offsets):
        if i != len(offsets) - 1:
            addr = MEM.read_int(addr + offset)
    addr = addr + offsets[-1]
    return addr

# Function wait_for_load_and_retry()
# Wrapper function which checks if the game is currently loading and waits until the game is loaded.
# The function also catches the MemoryReadError Exception and retries the function 3 times.
# If no result is found after 3 retries the value forces the function to return None as its value,
def wait_for_load_and_retry(max_retries=3, retry_delay=1):
    def decorator(func):
        @wraps(func)

        def wrapper(*args, **kwargs):

            try:
                loading_flag_address = pointer_address(BASE_POINTER, OFFSETS["Loading Flag"])

                while not MEM.read_bool(loading_flag_address):
                    time.sleep(2)
            except:
                close("Bioshock 2 either closed or has crashed. If this isn't the case. Please let the Developer Know in the Discord.")
            
            retries = 0

            while retries < max_retries:
                try:
                    result = func(*args, **kwargs)
                    return result
                except pymem.exception.MemoryReadError as mre:
                    retries += 1
                    log_error(mre, "Memory Read Error", func.__name__)
                    time.sleep(retry_delay)
            
            return None
        
        return wrapper
    return decorator


def sanitize_string(string):
    return string.replace(b'\x00', b'').decode("ascii", errors="ignore")

@wait_for_load_and_retry()
def loading():
    return MEM.read_bool(pointer_address(BASE_POINTER, OFFSETS["Loading Flag"]))

@wait_for_load_and_retry()
def screen_id():
    if in_apartment():
        return apartment_screen()
    
    if not loading():
        return Bioshock2Multiplayer.SCREENS["Loading"]

    if pre_game() or in_game() or end_game():
        hud_movie_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["HUD Movie Size"]))
        movie = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["HUD Movie"]), hud_movie_size * 2)
    else:
        bink_movie_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Background Bink Movie Size"]))
        movie = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Background Bink Movie"]), bink_movie_size * 2)

    movie_no_spaces = sanitize_string(movie)
    screen_id = movie_no_spaces.split('\\')[2]
    return Bioshock2Multiplayer.SCREENS[screen_id]

@wait_for_load_and_retry()
def in_lobby():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby GameSettings Class"])) > 0 and lobby_num_players() > 0

@wait_for_load_and_retry()
def lobby_num_players():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby NumPlayers"]))

@wait_for_load_and_retry()
def public_connections():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Public Connections"]))

@wait_for_load_and_retry()
def private_connections():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Private Connections"]))

@wait_for_load_and_retry()
def in_public_lobby():
    return in_lobby() and public_connections() > 0

@wait_for_load_and_retry()
def in_private_lobby():
    return in_lobby() and private_connections() > 0

@wait_for_load_and_retry()
def lobby_map():
    lobby_information_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array"]))
    lobby_information_count = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array Count"]))
    lobby_information_max = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array Max Size"]))

    if lobby_information_address == 0:
        return "Lobby Not Initialized"
    
    if lobby_information_max == 0x21 and lobby_information_count == 0x3:
        lobby_section = "A"
    elif lobby_information_max == 0x21 and lobby_information_count == 0x7:
        lobby_section = "B"
    elif lobby_information_max == 0x29:
        lobby_section = "C"
    
    lobby_map = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Map " + lobby_section]))
    return Bioshock2Multiplayer.MAPS[lobby_map]
    
@wait_for_load_and_retry()
def lobby_gamemode():
    lobby_information_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array"]))
    lobby_information_count = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array Count"]))
    lobby_information_max = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Information Address Array Max Size"]))

    if lobby_information_address == 0:
        return "Lobby Not Initialized"

    if lobby_information_max == 0x21 and lobby_information_count == 0x3:
        lobby_section = "A"
    elif lobby_information_max == 0x21 and lobby_information_count == 0x7:
        lobby_section = "B"
    elif lobby_information_max == 0x29:
        lobby_section = "C"

    lobby_gamemode = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby GameMode " + lobby_section]))
    lobby_hardcore_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Hardcore Flag " + lobby_section]))
    lobby_hardcore_flag = (lobby_hardcore_address & (1 << 0)) != 0
    return Bioshock2Multiplayer.GAMEMODES[9] if lobby_gamemode == 1 and lobby_hardcore_flag else Bioshock2Multiplayer.GAMEMODES[lobby_gamemode]


@wait_for_load_and_retry()
def lobby_status():
    lobby_status_size =  MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Lobby Status Message Size"]))
    lobby_status_message = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Lobby Status Message"]), lobby_status_size * 2)
    lobby_status = sanitize_string(lobby_status_message)

    if len(lobby_status) > 30:
        return lobby_status[:30]
    else:
        return lobby_status

@wait_for_load_and_retry()
def in_game_gamemode():
    game_mode = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["In-Game GameMode"]))
    hardcore_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["In-Game Hardcore Flag"]))
    hardcore_flag = (hardcore_address & (1 << 1)) != 0

    return Bioshock2Multiplayer.GAMEMODES[9] if game_mode == 1 and hardcore_flag else Bioshock2Multiplayer.GAMEMODES[game_mode]

@wait_for_load_and_retry()
def in_game_map():
    last_url_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Last URL Size"]))
    last_url = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Last URL"]), last_url_size * 2)
    map = sanitize_string(last_url)

    return Bioshock2Multiplayer.MAP_URLS[map]

@wait_for_load_and_retry()
def pre_game():
    shock_mp_game_replication_info_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["ShockMPGameReplicationInfo Class"]))

    if shock_mp_game_replication_info_address != 0:
        waiting_player_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Waiting Player Flag"]))
        game_ready_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Game Ready Flag"]))
        waiting_player_flag = (waiting_player_address & (1 << 1)) != 0
        game_ready_flag = (game_ready_address & (1 << 0)) != 0
        return (waiting_player_flag or loadout_selected()) and not in_apartment() and game_ready_flag and not in_game()
    
    return False

# Function in_game()
# Checks if the Player is In-Game.
@wait_for_load_and_retry()
def in_game():
    shock_mp_game_replication_info_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["ShockMPGameReplicationInfo Class"]))

    if shock_mp_game_replication_info_address != 0:
        game_ready_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Game Ready Flag"]))
        game_ready_flag = (game_ready_address & (1 << 0)) == 0
        return game_ready_flag and MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["In-Game Flag"])) == 1
        
    return False

@wait_for_load_and_retry()
def end_game():
    shock_mp_game_replication_info_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["ShockMPGameReplicationInfo Class"]))

    if shock_mp_game_replication_info_address != 0:
        game_ended_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Game Ended Flag"]))
        game_ended_flag = (game_ended_address & (1 << 0)) != 0
        return game_ended_flag
    
    return False

@wait_for_load_and_retry()
def display_scoreboard():
    scoreboard_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Scoreboard Shown Flag"]))
    scoreboard_flag = (scoreboard_address & (1 << 0)) != 0
    return scoreboard_flag

@wait_for_load_and_retry()
def display_match_results():
    match_result_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Match Results Flag"]))
    match_result_flag = (match_result_address & (1 << 0)) != 0
    return match_result_flag

@wait_for_load_and_retry()
def end_game_screen():
    if display_match_results():
        return Bioshock2Multiplayer.SCREENS["Match Results"]
    elif display_scoreboard():
        return Bioshock2Multiplayer.SCREENS["Scoreboard"]
    else:
        return Bioshock2Multiplayer.SCREENS["End Game"]

@wait_for_load_and_retry()
def current_character():
    return Bioshock2Multiplayer.CHARACTERS[MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Character"]))]

@wait_for_load_and_retry()
def current_weapon():
    weapon_name_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Weapon Name Size"]))
    weapon = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Weapon Name"]), weapon_name_size * 2)
    weapon = sanitize_string(weapon)
    return weapon if weapon in Bioshock2Multiplayer.WEAPONS else "No Weapon"

@wait_for_load_and_retry()
def current_upgrade():
    upgrade_class_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Upgrade Class"]))

    if upgrade_class_address != 0:
        upgrade_name_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Upgrade Name Size"]))
        upgrade = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Upgrade Name"]), upgrade_name_size * 2)
        upgrade = sanitize_string(upgrade)
        return upgrade if upgrade in Bioshock2Multiplayer.UPGRADES else "No Upgrade"
    else:
        return "No Upgrade"
    
@wait_for_load_and_retry()
def current_plasmid():
    plasmid_name_size = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Plasmid Name Size"]))
    plasmid = MEM.read_bytes(pointer_address(BASE_POINTER, OFFSETS["Plasmid Name"]), plasmid_name_size * 2)
    plasmid = sanitize_string(plasmid)
    return plasmid if plasmid in Bioshock2Multiplayer.PLASMIDS else "No Plasmid"

@wait_for_load_and_retry()
def current_melee():
    character = current_character()
    melee_id = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Melee"]))

    if character == "Mlle Blanche de Glace":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Blanche Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]
    elif character == "Naledi Atkins":
        if melee_id == 1:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Naledi Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]
    elif character == "Jacob Norris":
        if melee_id == 1:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Jacob Unique"]
        elif melee_id in range(20, 30):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 20]
    elif character == "Barbara Johnson":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Barbara Unique"]
        elif melee_id in range(17, 27):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 17]
    elif character == "Buck Raleigh":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Buck Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]
    elif character == "Zigo d'Acosta":
        if melee_id == 1:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Zigo Unique"]
        elif melee_id in range(19, 29):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 19]
    elif character == "Danny Wilkins":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Danny Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]
    elif character == "Oscar Calraca":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Oscar Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]
    elif character == "Suresh Sheti":
        if melee_id == 1:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Suresh Unique"]
        elif melee_id in range(19, 29):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 19]
    elif character == "Louie McGraff":
        if melee_id == 0:
            return Bioshock2Multiplayer.MELEE_WEAPONS["Louie Unique"]
        elif melee_id in range(18, 28):
            return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][melee_id - 18]

@wait_for_load_and_retry()
def current_kills():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Kills"]))

@wait_for_load_and_retry()
def current_assists():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Assists"]))

@wait_for_load_and_retry()
def current_deaths():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Deaths"]))

@wait_for_load_and_retry()
def current_num_players():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Game NumPlayers"]))

@wait_for_load_and_retry()
def current_timer():
    time = MEM.read_float(pointer_address(BASE_POINTER, OFFSETS["Main Timer"]))
    minutes, seconds = divmod(time, 60)
    return f"{int(minutes):2d}:{int(seconds):02d}"

@wait_for_load_and_retry()
def current_round():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Current Round"]))

@wait_for_load_and_retry()
def player_dead():
    dead_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Death Flag"]))
    death_flag = (dead_address & (1 << 4)) != 0
    return death_flag

@wait_for_load_and_retry()
def player_melee():
    return MEM.read_bool(pointer_address(BASE_POINTER, OFFSETS["Melee Flag"]))

@wait_for_load_and_retry()
def player_bigdaddy():
    return current_weapon() == "Rivet Gun" and (current_plasmid() == "Proximity Mine" or current_plasmid() == "Stomp")

@wait_for_load_and_retry()
def apartment_screen():
    if in_apartment_lobby():
        return Bioshock2Multiplayer.SCREENS['Apartment Lobby']
    elif in_apartment_intro():
        return Bioshock2Multiplayer.SCREENS['Apartment Intro']
    elif in_apartment_outro():
        return Bioshock2Multiplayer.SCREENS['Apartment Outro']
    else:
        return Bioshock2Multiplayer.SCREENS['Apartment']

# Function in_apartment()
# Due to lack of being able to find this function I will need to hack myself a version that works using Loadouts.
@wait_for_load_and_retry()
def in_apartment():
    return in_game_map() == "Apartment Lobby" and not in_game()

@wait_for_load_and_retry()
def in_apartment_lobby():
    apartment_lobby_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Bathysphere Lobby Flag"]))
    apartment_lobby_flag = (apartment_lobby_address & (1 << 3)) != 0

    return apartment_lobby_flag

@wait_for_load_and_retry()
def in_apartment_intro():
    video_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Apartment Videos Flag"]))
    intro_flag = (video_address & (1 << 0)) != 0

    return intro_flag

@wait_for_load_and_retry()
def in_apartment_outro():
    video_address = MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Apartment Videos Flag"]))
    outro_flag = (video_address & (1 << 1)) != 0

    return outro_flag

@wait_for_load_and_retry()
def loadout_start_time():
    return MEM.read_float(pointer_address(BASE_POINTER, OFFSETS["Loadout Start Time"]))

@wait_for_load_and_retry()
def loadout_selected():
    return MEM.read_int(pointer_address(BASE_POINTER, OFFSETS["Loadout Selected Flag"])) >= 0


def rpc_current_status():
    bio2_details, bio2_states = rpc_current_screen()
    bio2_buttons = [{"label": "Not Currently in a Lobby", "url": MPDISCORD_LINK}]
    menu_image, menu_text = Bioshock2MultiplayerRichPresence.MAP_IMAGES["DLC"], bio2_details
    
    if bio2_details in ["Main Menu", "Credits", "Promotional Video"]:
        menu_image, menu_text = Bioshock2MultiplayerRichPresence.MAP_IMAGES["Main Menu"], bio2_details
    elif bio2_details in ["Apartment", "Prologue", "Epilogue"]:
        menu_image, menu_text = Bioshock2MultiplayerRichPresence.MAP_IMAGES["Apartment"], bio2_details
    elif bio2_details in ["Lobby", "Apartment Lobby"]:
        bio2_details, bio2_states, bio2_buttons = rpc_lobby_information()
        menu_image, menu_text = rpc_lobby_map()
    elif in_lobby() and bio2_details not in ["Lobby", "Apartment Lobby", "In-Game"]:
        bio2_buttons = rpc_lobby_button()
        menu_image, menu_text = rpc_lobby_map()
    elif bio2_details == "In-Game":
        bio2_details, bio2_states, bio2_buttons = rpc_game_information()
        menu_image, menu_text = rpc_game_map()
    
    return bio2_details, bio2_states, bio2_buttons, menu_image, menu_text


def rpc_current_screen():
    screen = screen_id()
    if screen is not None:
        details, states = Bioshock2MultiplayerRichPresence.GAME_INFORMATION[screen]["Details"], Bioshock2MultiplayerRichPresence.GAME_INFORMATION[screen]["States"]
    else:
        details, states = "Loading...", "Player is Loading....."
    return details, states

def rpc_character_information():
    return Bioshock2MultiplayerRichPresence.CHARACTER_IMAGES[current_character()], "Playing as : " + current_character()

def rpc_lobby_map():
    map = lobby_map()

    if map == "Lobby Not Initialized":
        return Bioshock2MultiplayerRichPresence.MAP_IMAGES["DLC"], "Waiting to Join Lobby"

    return Bioshock2MultiplayerRichPresence.MAP_IMAGES[map], map

def rpc_game_map():
    map = in_game_map()
    return Bioshock2MultiplayerRichPresence.MAP_IMAGES[map], map

def rpc_lobby_information():
    if in_public_lobby():
        return lobby_gamemode(), lobby_map(), rpc_lobby_button()
    elif in_private_lobby():
        return lobby_gamemode(), lobby_map(), rpc_lobby_button()
    else:
        return "Lobby", "Main Menu", [{"label": "Not Currently in a Lobby", "url": MYDISCORD_LINK}]

def rpc_lobby_button():
    if in_public_lobby():
        return [{"label": "Public Lobby - "  + str(lobby_num_players()) + "/10", "url": MPDISCORD_LINK}, {"label": lobby_status(), "url": MYDISCORD_LINK}]
    elif in_private_lobby():
        return [{"label": "Private Lobby - "  + str(lobby_num_players()) + "/10", "url": MPDISCORD_LINK}, {"label": lobby_status(), "url": MYDISCORD_LINK}]


def rpc_game_information():
    game_details = in_game_gamemode() + " on " + in_game_map()
    game_state = None

    if (pre_game() or in_game()) and not loadout_selected():
        game_state = "Selecting a Loadout"
    elif pre_game() and loadout_selected():
        game_state = "Waiting for Match to Begin"
    elif in_game() and loadout_selected():
        if player_dead():
            game_state = "Waiting to Respawn"
        elif player_melee() and not player_bigdaddy():
            game_state = "Meleeing with the " + current_melee()
        elif player_melee() and player_bigdaddy():
            game_state = "Meleeing with the Rivet Gun"
        elif player_bigdaddy():
            game_state = "Roaming as the Big Daddy"
            if current_plasmid() == "Stomp":
                game_state = "Big Daddy Stomping the Competition"
        else:
            if current_upgrade() != "No Upgrade":
                game_state = current_upgrade() + " " + current_weapon() + " and " + current_plasmid()
            else:
                game_state = current_weapon() + " and " + current_plasmid()
    elif end_game():
        end_screen = end_game_screen()
        if end_screen == "Match Results":
            game_state = "Viewing Match Results"
        elif end_screen == "Scoreboard":
            game_state = "Viewing the End-Match Scoreboard"
        else:
            game_state = "Match has Ended"


    game_button = [
        {
            "label": "In-Game - " + str(current_num_players()) + "/10" + ("  Round: " + str(current_round()) if in_game_gamemode() in ["Capture The Sister", "Last Splicer Standing"] else (" Time: " + str(current_timer()) if in_game() else "")),
            "url": MPDISCORD_LINK
        },
        {
            "label": "Kills: " + str(current_kills()) + " Assists: " + str(current_assists()) + " Deaths: " + str(current_deaths()),
            "url": MYDISCORD_LINK
        }
    ]

    return game_details, game_state, game_button

# Function debug()
# Debug function used to display values and test pointers.
def debug():
    while True:
        time.sleep(2)
        print("\n")
        print(screen_id())
        print("Current Character: ", current_character())
        print("Current Melee:", current_melee())
        if in_apartment():
            print("Apartment Screen:", apartment_screen())
        if(in_lobby()):
            print("Public Flag:", in_public_lobby())
            print("Private Flag:", in_private_lobby())
            print("Lobby NumPlayers: ", lobby_num_players())
            print("Lobby Map: ", lobby_map())
            print("Lobby GameMode: ", lobby_gamemode())
            print("Lobby Status Message:", lobby_status())
        if(in_game() and not player_dead() and loadout_selected()):
            print("Current NumPlayers: ", current_num_players())
            print("Current Weapon: ", current_weapon())
            print("Current Plasmid:" , current_plasmid())
            print("Current Upgrade: ", current_upgrade())
            print("Current Character: ", current_character())
            print("Current Kills: ", current_kills())
            print("Current Assists: ", current_assists())
            print("Current Deaths: ", current_deaths())
            print("Game Map: ", in_game_map())
            print("GameMode: ",in_game_gamemode())
            print("Big Daddy Flag: ", player_bigdaddy())
            print("Melee Flag: ", player_melee())
            if not loadout_selected():
                print("Player has yet to choose a loadout.")
        print("In-Game Flag: ", in_game())
        print("Pre-Game Flag: ", pre_game())
        print("End-Game Flag: ", end_game())