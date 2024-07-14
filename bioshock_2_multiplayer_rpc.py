from bioshock_2_multiplayer import *
from bioshock_2_multiplayer import PlayerReplicationInfo as PRI
from bioshock_2_multiplayer import UserProfile as ACTIVE_PROFILE


MAP_IMAGE_LINK = "https://raw.githubusercontent.com/SnowTempest/Bioshock-2-Multiplayer-RPC/main/Assets/Maps/Icons/"
SPLICER_IMAGE_LINK = "https://raw.githubusercontent.com/SnowTempest/Bioshock-2-Multiplayer-RPC/main/Assets/Characters/"
PLASMID_IMAGE_LINK = "https://raw.githubusercontent.com/SnowTempest/Bioshock-2-Multiplayer-RPC/main/Assets/Plasmids/"
DISCORD_LINK = "https://discord.gg/4ydTGHfFPQ"

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
        "Ranked Rewards": "20-RankRewards.jpeg",
        "Main Menu": "21-Entry.png",
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

def rpc_status():
    bio2_details, bio2_states = rpc_flash_details()
    bio2_image, bio2_text = MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES["DLC"], bio2_details
    bio2_buttons = [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]
    bio2_small_image, bio2_small_text = rpc_splicer()

    if bio2_details in ["Main Menu", "Credits", "Promotional Movie", "Intro Movies", "Controls", "Showcase Video", "Settings", "Adjust Brightness"]:
        bio2_image = MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES["Main Menu"] 
        bio2_text = bio2_details
    elif bio2_details in ["Apartment", "Prologue", "Epilogue"]:
        bio2_image = MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES["Apartment"] 
        bio2_text = bio2_details
    elif bio2_details in ["Lobby", "Apartment Lobby"]:
        bio2_details, bio2_states, bio2_buttons = rpc_lobby_details()
        bio2_image, bio2_text = rpc_lobby_map()
    elif bio2_details in ["Rank Up"]:
        bio2_details, bio2_states, bio2_buttons = rpc_rank_details()
        bio2_image, bio2_text = MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES["Ranked Rewards"], "Ranked Rewards"
    elif in_lobby() and bio2_details not in ["Lobby",  "Apartment Lobby", "In-Game"]:
        bio2_buttons = rpc_lobby_buttons()
        bio2_image, bio2_text = rpc_lobby_map()
    elif bio2_details == "In-Game" and end_game():
        bio2_details, bio2_states, bio2_buttons = rpc_end_details()
        bio2_image, bio2_text = rpc_game_map()
        bio2_small_image, bio2_small_text = rpc_plasmid()
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
        return Bioshock2MultiplayerRPC.GAME_MODES_FRIENDLY_NAMES[lobby_game_mode()], lobby_game_map(), rpc_lobby_buttons()
    else:
        return "Lobby", "Main Menu", [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]

def rpc_lobby_map():
    lobby_map = lobby_game_map()
    return MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES[lobby_map], lobby_map

def rpc_lobby_buttons():
    lobby = lobby_type()

    if lobby != "None":
        return [
            {
                "label": lobby + " Lobby - "  + str(OnlineLobby.lobby_num_players()) + "/" + str(lobby_max_players()), 
                "url": DISCORD_LINK
            }, 
            {
                "label": OnlineLobbyController.game_lobby_status(), 
                "url": DISCORD_LINK
            }
        ]
    else:
        return "Lobby", "Main Menu", [{"label": "Not Currently in a Lobby", "url": DISCORD_LINK}]

def rpc_game_details():
    bio2_details = Bioshock2MultiplayerRPC.GAME_MODES_FRIENDLY_NAMES[game_mode()] + " on " + game_map()
    bio2_states = player_game_status()

    bio2_buttons = [
        {
            "label": "Match: " + str(game_num_players()) + "/" + str(game_max_players()) + (" Round: " + str(game_round() + 1) + (" Time: " + str(game_timer())) if game_mode() in ["GAMEMODE_HOG", "GAMEMODE_TDMHC"] else (" Time: " + str(game_timer()) if running_game() else "")),
            "url": DISCORD_LINK
        },
        {
            "label": "Score: " + str(PRI.player_score()) + " Kills: " + str(PRI.player_kills()) + " Deaths: " + str(PRI.player_deaths()),
            "url": DISCORD_LINK
        }
    ]

    return bio2_details, bio2_states, bio2_buttons

def rpc_game_map():
    map = game_map()
    return MAP_IMAGE_LINK + Bioshock2MultiplayerRPC.MAP_IMAGES[map], map

def rpc_end_details():
    bio2_details = Bioshock2MultiplayerRPC.GAME_MODES_FRIENDLY_NAMES[game_mode()] + " on " + game_map()
    bio2_states = player_game_status()

    bio2_buttons = [
        {
            "label": "Ended: " + str(game_num_players()) + "/" + str(game_max_players()) + " Total Adam: " + str(player_total_score()),
            "url": DISCORD_LINK,
        },
        {
            "label": Bioshock2MultiplayerRPC.WINNING_REASON[end_game_reason()],
            "url": DISCORD_LINK
        }
    ]

    return bio2_details, bio2_states, bio2_buttons

def rpc_rank_details():
    bio2_details = "Rank Up"
    bio2_states = "Player has reached Rank " + str(ACTIVE_PROFILE.player_rank())
    bio2_buttons =  [
        {
            "label": "Kills: " + str(ACTIVE_PROFILE.player_lifetime_kills()) + " Wins: " + str(ACTIVE_PROFILE.player_lifetime_wins()), 
            "url": DISCORD_LINK
        }, 
        {
            "label": "Adam: " + str(ACTIVE_PROFILE.player_banked_adam()) + " Time: " + player_time_played(), 
            "url": DISCORD_LINK
        }
    ]

    return bio2_details, bio2_states, bio2_buttons 

def rpc_splicer():
    return SPLICER_IMAGE_LINK + Bioshock2MultiplayerRPC.SPLICER_IMAGES[player_splicer()], "Playing as " + player_splicer()

def rpc_plasmid():
    if not player_dead() and streamed_loadout():
        return PLASMID_IMAGE_LINK + Bioshock2MultiplayerRPC.PLASMID_IMAGES[player_plasmid()], "Using " + player_plasmid()
    
    return Bioshock2MultiplayerRPC.PLASMID_IMAGES["None"], "Using " + "No Plasmid"