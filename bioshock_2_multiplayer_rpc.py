import json
import pypresence as PyPresence
import builtins
from sys import exit
from time import sleep, time
from bioshock_2_multiplayer import *
from bioshock_2_multiplayer_logger import BioMPLogger, DISCORD_LINK, STORE_LINK

GITHUB_LINK = "https://raw.githubusercontent.com/SnowTempest/Bioshock-2-Multiplayer-RPC/main"
INTERVAL_MAX = 10

class RPCDATA:
    def __init__(self, ID, MODE, UPDATE_INTERVAL):
        self.ID = ID
        self.MODE = MODE
        self.UPDATE_INTERVAL = UPDATE_INTERVAL

class Bioshock2MultiplayerRPC:
    MAP_IMAGES = {
        "Arcadia": "1-Arcadia.png",
        "Farmer's Market": "2-FarmersMarket.png",
        "Fort Frolic": "3-FortFrolic.png",
        "Hephaestus": "4-Hephaestus.png",
        "Home For The Poor": "5-HomeForThePoor.png",
        "Kashmir Restaurant": "6-KashmirRestaurant.png", 
        "Medical Pavilion": "7-MedicalPavilion.png",
        "Mercury Suites": "8-MercurySuites.png",
        "Neptune's Bounty": "9-NeptunesBounty.png",
        "Point Prometheus": "10-PointPrometheus.png",
        "Fontaine Fisheries": "11-FontaineFisheries.png",
        "Pauper's Drop": "12-PaupersDrop.png",
        "Smuggler's Hideout": "13-SmugglersHideout.png",
        "Fighting McDonagh's": "14-FightingMcDonaghs.png",
        "Dionysus Park": "15-DionysusPark.png",
        "Siren Alley": "16-SirenAlley.png",
        "Testbox": "17-Testbox.png",
        "Apartment": "18-ApartmentLobby.png",
        "DLC": "19-DLC.png",
        "Ranked Rewards": "20-RankRewards.png",
        "Main Menu": "21-Entry.png",
        "ArcadiaBeta": "22-ArcadiaBeta.png",
        "None": "19-DLC.png"
    }

    SPLICER_IMAGES = {
        "Jacob Norris": "1-Jacob.png",
        "Barbara Johnson": "2-Barbara.png",
        "Buck Raleigh": "3-Buck.png",
        "Danny Wilkins": "4-Danny.png",
        "Suresh Sheti": "5-Suresh.png",
        "Naledi Atkins": "6-Naledi.png",
        "Zigo d'Acosta": "7-Zigo.png",
        "Mlle Blanche de Glace": "8-Blanche.png",
        "Oscar Calraca": "9-Oscar.png",
        "Louie McGraff": "10-Louie.png"
    }

    PLASMID_IMAGES = {
        "Electro Bolt": "0-ElectroBolt.png",
        "Telekinesis": "1-Telekinesis.png",
        "Aero Dash": "2-AeroDash.png",
        "Insect Swarm": "3-InsectSwarm.png",
        "Geyser Trap": "4-GeyserTrap.png",
        "Houdini": "5-Houdini.png",
        "Poison Quills": "6-PoisonQuills.png",
        "Incinerate!": "7-Incinerate.png",
        "Winter Blast": "8-WinterBlast.png",
        "Proximity Mine": "9-ProximityMine.png",
        "Stomp": "10-Stomp.png",
        "Sonic Boom": "11-SonicBoom.png",
        "None": "12-None.png"
    }

    GAME_MODES_FRIENDLY_NAMES = {
        "GAMEMODE_FFA": "Survival of the Fittest",
        "GAMEMODE_TDM": "Civil War",
        "GAMEMODE_HOG": "Capture The Sister",
        "GAMEMODE_ODD": "Team Adam Grab",
        "GAMEMODE_TC": "Turf War",
        "GAMEMODE_DLC_2": "Kill 'Em Kindly",
        "GAMEMODE_ODDFFA": "Adam Grab",
        "GAMEMODE_TDMHC": "Last Splicer Standing",
        "GAMEMODE_NONE": "Loading"
    }    
    
    WINNING_REASON = {
        "WinningReason_Invalid": "Match ended with Invalid Win",
        "WinningReason_TimeLimit": "Time Limit has been Reached",
        "WinningReason_ScoreLimit": "Score Limit has been Reached",
        "WinningReason_LastManStanding": "All Players Left the Match",
        "WinningReason_Defense": "Defenders have Won the Match",
        "WinningReason_Save": "Little Sister was Saved",
        "WinningReason_Harvest": "Little Sister was Harvested",
        "WinningReason_Forced": "Match has been Aborted by Host"
    }

    GAME_INFORMATION = {
        "MainMenu": {
            "Details": "Main Menu", 
            "States": "At the Title Screen"
        },
        "Options": {
            "Details": "Settings", 
            "States": "At the Settings Menu"
        },
        "Loadout": {
            "Details": "Loadouts", 
            "States": "Customizing their Loadouts"
        },
        "Select Character": {
            "Details": "Character Selection", 
            "States": "Selecting their Character"
        },
        "Customize Character": {
            "Details": "Customize Aesthetics", 
            "States": "Selecting their Mask and Melee"
        },
        "Personal Statistics": {
            "Details": "Personal Statistics", 
            "States": "Looking at their Lifetime Stats"
        },
        "Trials": {
            "Details": "Trials", 
            "States": "Looking at their list of Trials"
        },
        "Intro Video": {
            "Details": "Promotional Video", 
            "States": "Watching the Promotional Video"
        },
        "Credits": {
            "Details": "Credits", 
            "States": "Watching the Credits"
        },
        "Showcase Video": {
            "Details": "Showcase Promotional Video", 
            "States": "Watching a Video Showcase"
        },
        "Adjust Brightness": {
            "Details": "Adjust Brightness", 
            "States": "Adjusting their Brightness"
        },
        "Controls": {
            "Details": "Controls", 
            "States": "Changing Control Layout"
        },
        "Rank Up": {
            "Details": "Rank Up", 
            "States":"Viewing their Rank Up Rewards"
        },
        "Lobby": {
            "Details": "Lobby", 
            "States": "Main Menu"
        },
        "Apartment": {
            "Details": "Apartment", 
            "States": "Wandering in their Apartment"
        },
        "Prologue": {
            "Details": "Prologue", 
            "States": "Watching the Apartment Prologue"
        },
        "Epilogue": {
            "Details": "Epilogue", 
            "States": "Watching the Apartment Epilogue"
        },
        "Apartment Lobby": {
            "Details": "Apartment Lobby", 
            "States": "Main Menu"
        },
        "In-Game": {
            "Details": "In-Game", 
            "States": "In-Game"
        },
        "Match Ended": {
            "Details": "End-Match", 
            "States": "Match Has Ended"
        },
        "Scoreboard": {
            "Details": "Scoreboard", 
            "States": "Viewing End-Match Scoreboard"
        },
        "Match Results": {
            "Details": "Match Results", 
            "States": "Viewing Match Results"
        },
        "Loading": {
            "Details": "Loading", 
            "States": "Player is currently loading..."
        },
        "Intro Movies": {
            "Details": "Intro Movies", 
            "States": "Watching the Intro Movies"
        },
        "Promotional Video": {
            "Details": "Promotional Movie",
            "States": "Watching the Promotional Video"
        }
    }

def rpc_close(close_message):
    print(close_message)
    sleep(4)
    exit()

def rpc_data():
    with builtins.open("rpc_data.json", "r") as json_file:
        json_data = json.load(json_file)
    
    rpc_id = json_data.get("APP_ID", "")
    rpc_mode = json_data.get("MODE", "PERFORMANCE")
    rpc_interval = min(json_data.get("UPDATE_INTERVAL", INTERVAL_MAX), INTERVAL_MAX)

    if rpc_mode not in ["REALTIME", "PERFORMANCE"]:
        rpc_mode = "PERFORMANCE"

    return RPCDATA(rpc_id, rpc_mode, rpc_interval)

def rpc_init():
    try:
        print("Starting RPC Client")
        logger = BioMPLogger()
        logger.log_clear()

        rpc_props = rpc_data()
        client_id = rpc_props.ID

        if client_id == "":
            raise PyPresence.DiscordError(code="rpc_init", message="An error has occured trying to retrieve the Application ID in rpc_data.json.")

        rpc = PyPresence.Presence(client_id, pipe=0)
        rpc.connect()
        return rpc, rpc_props, logger

    except PyPresence.DiscordNotFound:
        logger.log_error(
            error="Pypresence Error: DiscordNotFound", 
            error_message="Discord is not open or was not found. Please open Discord before launching the Bioshock 2 Multiplayer RPC.",
            additional_details="Discord was not open during the RPC initialization or the RPC channel was already in use by another program. \nPlease re-open Discord or close any other RPC programs before re-attempting Bioshock 2 Multiplayer RPC connection."
        )
    except PyPresence.DiscordError:
        logger.log_error(
            error="Pypresence Error: DiscordError", 
            error_message="Invalid Discord \"APP_ID\". Please make sure you have the right value stored in rpc_data.json and try again.",
            additional_details="There was an error trying to connect to the User's Discord Developer Application ID. \nPlease verify that your Application ID is valid and fits the format in rpc_data.json. Example Format: \"APP_ID\":123456789098765432"
        )

def rpc_loop():
    rpc, rpc_data, logger = rpc_init()

    print("RPC has been Initialized")
    print("\nYou Can Close the RPC at Any Time Using Ctrl + C.\n")

    if rpc_data.MODE == "REALTIME":
            rpc_sleep = 0
    elif rpc_data.MODE == "PERFORMANCE":
            rpc_sleep = rpc_data.UPDATE_INTERVAL
    
    bio2_start = int(time())

    try:
        while True:
            if not bioshock_2_status():
                rpc_close("\nBioshock 2 Multiplayer is not Open. Please Open before Continuing. Program will Now Close.")
            bio2_details, bio2_state, bio2_buttons, bio2_image, bio2_text, bio2_small_image, bio2_small_text = rpc_status()
            
            rpc.update(buttons=bio2_buttons, state=bio2_state, details=bio2_details, large_text=bio2_text, large_image=bio2_image, small_image=bio2_small_image, small_text=bio2_small_text, start=bio2_start)
            sleep(rpc_sleep)

    except KeyboardInterrupt:
        rpc_close("\nBioshock 2 Multiplayer RPC Will Now Close.")
    except PyPresence.InvalidID:
        logger.log_error(
            error="Pypresence Error: InvalidID",
            error_message="Discord either closed or crashed. Bioshock 2 Multiplayer RPC will be closed.",
            additional_details="There was an issue during the RPC call trying to contact Discord. Either Discord has crashed or something bad happened with the RPC Program. \nOther causes of this error are currently unknown. Please let the Developer know if this error occurs.",
        )
    except PyPresence.PipeClosed:
        logger.log_error(
            error="Pypresence Error: PipeClosed",
            error_message="Discord either closed or crashed causing the RPC connection to close. Bioshock 2 Multiplayer RPC will be closed.",
            additional_details= "This issue occurs when Discord itself crashes while the RPC is connected causing the Pipe Connection to be closed. \nSimply restart the Bioshock 2 Multiplayer RPC again after Discord has been re-opened.",
        )
    except PyPresence.ResponseTimeout:
        logger.log_error(
            error="Pypresence Error: ResponseTimeout",
            error_message="Bioshock 2 Multiplayer RPC did not get a response from the Discord IPC Pipe in time.",
            additional_details="This issue occurs when Discord either freezes or bugs out. This could happen during very long RPC sessions. Easy fix is to restart the Bioshock 2 Multiplayer RPC."
        )
    except Exception as error:
        logger.log_error(
            error=f'Error: {error}',
            error_message="An Unknown error has occured. Bioshock 2 Multiplayer RPC has closed as a result.",
            additional_details="This error is an unknown error that the developer has not yet encountered or dealt with. \nPlease DM the developer on Discord the contents of error_log.json so he may debug what has occurred."
        )

def rpc_status():
    bio2_details, bio2_states = rpc_flash_details()
    bio_github = f'{GITHUB_LINK}/maps/'
    bio2_image, bio2_text = f'{bio_github}{Bioshock2MultiplayerRPC.MAP_IMAGES["DLC"]}', bio2_details
    bio2_buttons = [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]
    bio2_small_image, bio2_small_text = rpc_splicer()

    if bio2_details in ["Main Menu", "Credits", "Promotional Movie", "Intro Movies", "Controls", "Showcase Video", "Settings", "Adjust Brightness"]:
        bio2_image = f'{bio_github}{Bioshock2MultiplayerRPC.MAP_IMAGES["Main Menu"]}'
        bio2_text = bio2_details
    elif bio2_details in ["Apartment", "Prologue", "Epilogue"]:
        bio2_image = f'{bio_github}{Bioshock2MultiplayerRPC.MAP_IMAGES["Apartment"]}'
        bio2_text = bio2_details
    elif bio2_details in ["Lobby", "Apartment Lobby"]:
        bio2_details, bio2_states, bio2_buttons = rpc_lobby_details()
        bio2_image, bio2_text = rpc_game_map()
    elif bio2_details in ["Rank Up"]:
        bio2_details, bio2_states, bio2_buttons = rpc_rank_details()
        bio2_image, bio2_text = f'{bio_github}{Bioshock2MultiplayerRPC.MAP_IMAGES["Ranked Rewards"]}', "Ranked Rewards"
    elif in_lobby() and bio2_details not in ["Lobby",  "Apartment Lobby", "In-Game"]:
        bio2_buttons = rpc_lobby_buttons()
        bio2_image, bio2_text = rpc_game_map() 
    elif bio2_details == "In-Game":
        bio2_details, bio2_states, bio2_buttons = rpc_game_details()
        bio2_image, bio2_text = rpc_game_map()
        bio2_small_image, bio2_small_text = rpc_plasmid()
        
    return bio2_details, bio2_states, bio2_buttons, bio2_image, bio2_text, bio2_small_image, bio2_small_text

def rpc_flash_details():
    flash_file = flash_movie()

    if flash_file is not None:
        details = Bioshock2MultiplayerRPC.GAME_INFORMATION[flash_file]["Details"]
        states =  Bioshock2MultiplayerRPC.GAME_INFORMATION[flash_file]["States"]
    else:
        details = "Loading..."
        states = "Player is Loading....."

    return details, states

def rpc_lobby_details():
    if in_lobby():
        return Bioshock2MultiplayerRPC.GAME_MODES_FRIENDLY_NAMES[game_mode()], lobby_game_map(), rpc_lobby_buttons()
    else:
        return "Lobby", "Main Menu", [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]

def rpc_lobby_buttons():
    lobby = lobby_type()

    if lobby != "None":
        return [
            {
                "label": f'{lobby} Lobby - {lobby_players()}/{lobby_max_players()}', 
                "url": DISCORD_LINK
            }, 
            {
                "label": lobby_header_status(), 
                "url": STORE_LINK
            }
        ]
    else:
        return [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]

def rpc_game_details():
    game_state = match_status()
    bio2_details = f'{Bioshock2MultiplayerRPC.GAME_MODES_FRIENDLY_NAMES[game_mode()]} on {game_map()}'
    bio2_states = player_game_status()

    game_players = f'{game_num_players()}/{game_max_players()}'
    game_time = f' Round: {game_round()} Time: {game_timer()}' if game_mode() in ["GAMEMODE_HOG", "GAMEMODE_TDMHC"] else (f'Time: {game_timer()}' if game_state == "MATCH_STARTED" else "")
    
    if game_state == "MATCH_BEGIN":
        bio2_buttons = [{ "label": f'Match: {game_players} {game_time}', "url": DISCORD_LINK }, { "label": "Score: 0 Kills: 0 Deaths: 0", "url": STORE_LINK }]
    elif game_state == "MATCH_STARTED":
        bio2_stats = player_stats()
        bio2_buttons = [{ "label": f'Match: {game_players} {game_time}', "url": DISCORD_LINK }, { "label": f'Score: {bio2_stats.get("score", 0)} Kills: {bio2_stats.get("kills", 0)} Deaths: {bio2_stats.get("deaths", 0)}', "url": STORE_LINK }]
    elif game_state == "MATCH_ENDED":
        bio2_buttons = [{ "label": f'Ended: {game_players} Total Adam: {player_total_score()}', "url": DISCORD_LINK,}, { "label": Bioshock2MultiplayerRPC.WINNING_REASON[end_game_reason()], "url": STORE_LINK }]
    elif game_state == "MATCH_UNKNOWN":
        bio2_buttons = [{ "label": "Match Status Unknown", "url": DISCORD_LINK}, { "label": "Waiting for Match to Load", "url": STORE_LINK}]

    return bio2_details, bio2_states, bio2_buttons

def rpc_game_map():
    map = lobby_game_map()
    return f'{GITHUB_LINK}/maps/{Bioshock2MultiplayerRPC.MAP_IMAGES[map]}', map

def rpc_rank_details():
    bio2_stats = player_all_time_stats()
    bio2_details = "Rank Up"
    bio2_states = f'Player has reached Rank {bio2_stats['rank']}'
    bio2_buttons =  [
        {
            "label": f'Kills: {bio2_stats['kills']} Wins: {bio2_stats['wins']}', 
            "url": DISCORD_LINK
        }, 
        {
            "label": f'Adam: {bio2_stats['adam']} Time: {bio2_stats['playtime']}', 
            "url": STORE_LINK
        }
    ]

    return bio2_details, bio2_states, bio2_buttons 

def rpc_splicer():
    return f'{GITHUB_LINK}/splicers/{Bioshock2MultiplayerRPC.SPLICER_IMAGES[player_splicer()]}', f'Playing as {player_splicer()}'

def rpc_plasmid():
    if player_status() != "PLAYER_DEAD" and streamed_loadout():
        return f'{GITHUB_LINK}/plasmids/{Bioshock2MultiplayerRPC.PLASMID_IMAGES[player_plasmid()]}', f'Using {player_plasmid()}'
    
    return f'{GITHUB_LINK}/plasmids/{Bioshock2MultiplayerRPC.PLASMID_IMAGES["None"]}', f'Using No Plasmid'

def rpc_test_error(logger):
    try:
        division = 1 / 0
    except ZeroDivisionError:
        logger.log_error(
            error="Debug Error: Division by Zero", 
            error_message="There is a division error due to a value being divided by 0.",
            additional_details="No additional information required as this is a debug error."
        )

def rpc_test_score():
    print(player_ranking())
    print(player_scoreboard_score())