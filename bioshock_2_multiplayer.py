from bioshock_2_multiplayer_unreal import *

ADAM_GRAB_MAX_PLAYERS = 6
TEAM_ADAM_GRAB_MIN_PLAYERS = 6
MIN_PLAYERS = 4
MAX_PLAYERS = 10
OGS_MAP_PROP_ID = 0x10000010
OGS_MODE_PROP_ID = 0x1000000F
OGS_HC_PROP_ID = 0x1000004E

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
        9: "Louie McGraff",
        "None": "Loading..."
    }

    PLASMID_IDS = {
        0: "Electro Bolt",     
        1: "Telekinesis",      
        2: "Aero Dash",       
        3: "Insect Swarm",
        4: "Geyser Trap",      
        5: "Houdini",          
        6: "Poison Quills",
        7: "Incinerate!",       
        8: "Winter Blast",
        9: "Sonic Boom"
    }

    PLASMIDS = {
        "Electro Bolt",
        "Telekinesis",
        "Aero Dash",
        "Insect Swarm",
        "Geyser Trap", 
        "Houdini",
        "Poison Quills",
        "Incinerate!", 
        "Winter Blast",
        "Proximity Mine",
        "Stomp",
        "Sonic Boom",
        "None"
    }

    WEAPON_IDS = {
        0: "Pistol",
        1: "Shotgun",
        2: "Crossbow",
        3: "Grenade Launcher",
        4: "Machine Gun",
        5: "Nail Gun",
        6: "Elephant Gun",
        7: "Melee Weapon"
    }

    WEAPONS = {
        "Pistol",
        "Shotgun",
        "Crossbow",
        "Grenade Launcher",
        "Machine Gun",
        "Nail Gun",
        "Elephant Gun",
        "Melee Weapon",
        "Rivet Gun",
        "Wrench"
        "WrenchEquipped"
        "WYKWrenchEquipped",
        "Golf Club",
        "None"
    }

    UPGRADES = {
        0: "Ammo Capacity",
        1: "Automatic Firing",
        2: "Damage Increase",
        4: "Automatic Reload",
        5: "Rate of Fire",
        6: "Sawed-Off Barrel",
        8: "Magazine Size",
        9: "Kickback Reduction",
        10: "Firing Boost",
        12: "Rate of Fire",
        13: "Damage Increase",
        14: "Piercing Bolt",
        16: "Velocity Boost",
        17: "Rate of Fire",
        18: "Homing Grenades",
        20: "Slug Capacity",
        21: "Sniper Scope",
        22: "Damage Increase",
        24: "Damage Increase",
        25: "Magazine Size",
        26: "Burst Firing"
    }

    MELEE_WEAPONS = {
        "Default Melee": ["Wrench", "Candle Stick","Pipe","Machete","Rolling Pin","Mallet","Barbed Wire","Crowbar","Flashlight","Hatchet"],
        "Mlle Blanche de Glace": [0, 18, 28, "Knife"],
        "Naledi Atkins": [1, 18, 28, "Pipe Wrench"],
        "Jacob Norris": [1, 20, 30, "Torch"],
        "Barbara Johnson": [0, 17, 27, "Frying Pan"],
        "Buck Raleigh": [0, 18, 28, "Golf Club"],
        "Zigo d'Acosta": [1, 19, 29, "Fisherman Club"],
        "Danny Wilkins": [0, 18, 28, "Football Trophy"],
        "Oscar Calraca": [0, 18, 28, "Cricket Bat"],
        "Suresh Sheti": [1, 19, 29, "Cane"],       
        "Louie McGraff": [0, 18, 28, "Shank"]
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
        16: "Testbox",
        17: "DLC",
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
        "DE_Apartmentlobby": "Apartment Lobby",
        "Entry": "Main Menu",
        "None": "Loading...",
        "Loading...": "None"
    }

    GAME_MODES = {
        0: "GAMEMODE_FFA",
        1: "GAMEMODE_TDM",
        3: "GAMEMODE_HOG",
        4: "GAMEMODE_ODD",
        5: "GAMEMODE_TC",
        6: "GAMEMODE_DLC_2",
        8: "GAMEMODE_ODDFFA",
        9: "GAMEMODE_TDMHC",
        "None": "GAMEMODE_NONE"
    }

    GAME_WINNING_REASON = {
        0:  "WinningReason_Invalid",
        1:  "WinningReason_TimeLimit",
        2:  "WinningReason_ScoreLimit",
        3:  "WinningReason_LastManStanding",
        4:  "WinningReason_Defense",
        5:  "WinningReason_Save",
        6:  "WinningReason_Harvest",
        7:  "WinningReason_Forced",
    }

    QUICKMATCH_STATE = {
        0: "LOBBYQUICKMATCHSTATE_NONE",
        1: "LOBBYQUICKMATCHSTATE_SEARCH",  
        2: "LOBBYQUICKMATCHSTATE_JOIN",    
        3: "LOBBYQUICKMATCHSTATE_CLIENT",
        4: "LOBBYQUICKMATCHSTATE_HOST"
    }

    FLASH_MOVIES = {
        "MatchMakingPortal.swf": "Lobby",
        "ConfigureLoadout.swf": "Loadout",
        "CustomizeCharacter.swf": "Customize Character",
        "CharacterSelect.swf": "Select Character",
        "ViewProfile.swf": "Personal Statistics",
        "Trials.swf": "Trials",
        "MainMenu.swf": "MainMenu",
        "Credits.swf": "Credits",
        "Options.swf": "Options",
        "AttractVideoContainer.swf": "Promotional Video",
        "Apartment": "Apartment",
        "Apartment Lobby": "Apartment Lobby",
        "Apartment Intro": "Prologue",
        "Apartment Outro": "Epilogue",
        "HUDMultiplayer.swf": "In-Game",
        "PlasmidVideoContainer.swf": "Showcase Video",
        "AdjustBrightness.swf": "Adjust Brightness",
        "Controls.swf": "Controls",
        "RankRewards.swf": "Rank Up",
        "PressStart.swf": "Intro Movies",
        "End Game": "Match Ended",
        "Scoreboard": "Scoreboard",
        "Match Results": "Match Results",
        "Loading": "Loading",
        "None": "Loading...",
    }
    

def bioshock_2_status():
    return bioshock_2_is_active()

def flash_movie():
    if in_apartment():
        return apartment_movie()

    hud_movie = FlashGUIController.hud_movie()
    bink_movie = FlashGUIController.bink_movie_container()

    if hud_movie != 0:
        flash_movie = FlashGUIController.hud_movie_file_name()
    elif bink_movie != 0:
        flash_movie = FlashGUIController.bink_movie_file_name()
    else:
        return Bioshock2Multiplayer.FLASH_MOVIES["Loading"]

    flash_movie = flash_movie.split('\\')[2]

    return Bioshock2Multiplayer.FLASH_MOVIES[flash_movie]

def is_host():
    return OnlineLobby.active_unique_id() == OnlineGameSettings.owning_player_id()

def in_lobby():
    return OnlineLobbyController.online_game_settings_load() and OnlineLobby.lobby_num_players() > 0

def lobby_players():
    return OnlineLobby.lobby_num_players()

def lobby_min_players():
    return TEAM_ADAM_GRAB_MIN_PLAYERS if game_mode() == "GAMEMODE_ODD" else MIN_PLAYERS

def lobby_max_players():
    return ADAM_GRAB_MAX_PLAYERS if game_mode() == "GAMEMODE_ODDFFA" else MAX_PLAYERS

def lobby_type():
    if not in_lobby():
        return "None"
    
    if  OnlineGameSettings.num_public_connections() > 0:
        return "Public"
    elif OnlineGameSettings.num_private_connections() > 0:
        return "Private"
    else:
        return "None"

def lobby_quickmatch_state():
    return Bioshock2Multiplayer.QUICKMATCH_STATE.get(OnlineLobby.quickmatch_state(), "LOBBYQUICKMATCHSTATE_NONE")

def lobby_game_map():
    if not in_lobby() or not OnlineGameSettings.ogs_props_load():
        return Bioshock2Multiplayer.MAPS[17]
    
    properties_index = 0
    while properties_index < 7:
        prop_id = OnlineGameSettings.property_id(properties_index)

        if prop_id == OGS_MAP_PROP_ID:
            lobby_map_id = OnlineGameSettings.property_value_1(properties_index)

        properties_index += 1
    
    return Bioshock2Multiplayer.MAPS[lobby_map_id]

def lobby_header_status():
    if in_lobby():
        lobby_host = is_host()
        lobby_version = lobby_type()
        match_timer = int(OnlineLobby.game_countdown_timer())

        if lobby_quickmatch_state() == "LOBBYQUICKMATCHSTATE_SEARCH":
            return f'Searching for game...'

        if match_timer != 0:
            return f'Match starting in {match_timer}...'

        if lobby_version == "Private":
            return f'Waiting for host to start.' if lobby_host == False else f'Select Start Match to begin.'

        if lobby_version == "Public":
            num_players = lobby_players()
            players_needed = lobby_min_players() - num_players

            return f'Match Starting...' if match_timer == 0 and players_needed <= 0 else f'Waiting for {players_needed} {"players" if players_needed > 1 else "player"} to join...'
        
    return f'Searching for game...'

def game_mode():
    if not in_lobby() or not OnlineGameSettings.ogs_props_load():
        return Bioshock2Multiplayer.GAME_MODES["None"]

    properties_index = 0
    while properties_index < 7:
        prop_id = OnlineGameSettings.property_id(properties_index)

        if prop_id == OGS_MODE_PROP_ID:
            lobby_mode_id = OnlineGameSettings.property_value_1(properties_index)

        if prop_id == OGS_HC_PROP_ID:
            mode_hardcore = OnlineGameSettings.property_value_1(properties_index) != 0
        
        properties_index += 1
    
    return Bioshock2Multiplayer.GAME_MODES[9] if lobby_mode_id == 1 and mode_hardcore else Bioshock2Multiplayer.GAME_MODES[lobby_mode_id]

def player_time_played():
    mTime = UserProfile.seconds_played()
    mHours = mTime // 3600
    mSeconds_left = mTime % 3600
    mMinutes = mSeconds_left // 60
    mSeconds = mSeconds_left % 60

    return f'{mHours:02}:{mMinutes:02}:{mSeconds:02}'

def player_splicer():
    return Bioshock2Multiplayer.CHARACTERS[ShockUserSettings.character_id()]

def player_ranking():
    if team_game():
        local_player_team = PlayerReplicationInfo.team_index()
        game_winning_team = ShockPlayerController.game_winning_team()
        last_rank = 2
        if game_winning_team != 255:
            if game_winning_team == local_player_team:
                player_position = 1
            else:
                player_position = 2
        else:
            player_position = 2

        return player_position, last_rank
    
    player_rank, last_rank = player_replication_array()

    if player_rank == "None" or last_rank == "None":
        return 0, 0
    
    return player_rank, last_rank

def player_scoreboard_score():
    player_position, last_position = player_ranking()

    if player_position == 0:
        return 0

    if player_position == 1:
        raw_rank_value = float(ShockPlayerController.game_stat_first_place_value())
    else:
        ranking_percent = 1.0 - (float(player_position - 2) / float(last_position - 1))
        raw_rank_value = (ranking_percent * float(ShockPlayerController.game_stat_second_place_value())) + ((1.0 - ranking_percent) * float(ShockPlayerController.game_stat_last_place_value()))

    scoreboard_rank_score = int(raw_rank_value)
    if float(scoreboard_rank_score) % float(10) != float(0):
        scoreboard_rank_score = int(float(scoreboard_rank_score) + (float(10) - (float(scoreboard_rank_score) % float(10))))

    return scoreboard_rank_score

def player_replication_array():
    if not ShockPlayerController.game_replication_info_load():
        return "None", "None"

    current_pri_index = 1
    previous_id = None
    previous_game_score = 0
    current_rank = 1

    local_id = PlayerReplicationInfo.player_steam_id()

    while current_pri_index <= game_num_players() and current_pri_index <= game_max_players():
        current_player_id = GameReplicationInfo.pri_array_online_id(current_pri_index)
        current_game_score = GameReplicationInfo.pri_game_score(current_pri_index)

        if previous_id == None or current_player_id == None or previous_game_score != current_game_score:
            current_rank = current_pri_index
        
        previous_game_score = current_game_score
        previous_id = current_player_id

        if local_id == current_player_id:
            player_rank = current_rank

        current_pri_index += 1

    return player_rank, current_rank

def player_total_score():
    if not ShockPlayerController.game_replication_info_load():
        return 0

    total_score = 0

    player_scores = {
        "kill": PlayerReplicationInfo.player_kills() * ShockPlayerController.game_stat_kill_value(),
        "assist": PlayerReplicationInfo.player_assists() * ShockPlayerController.game_stat_assist_value(),
        "kill_streak": PlayerReplicationInfo.player_kill_streaks() * ShockPlayerController.game_stat_kill_streak_value(),
        "adam_vial": PlayerReplicationInfo.player_adam_vials_collected() * ShockPlayerController.game_stat_adam_vial_value(),
        "hack": PlayerReplicationInfo.player_hacks() * ShockPlayerController.game_stat_hack_value(),
        "big_daddy_spawn": PlayerReplicationInfo.player_bigdaddy_spawns() * ShockPlayerController.game_stat_bigdaddy_spawn_value(),
        "big_daddy_takedown": PlayerReplicationInfo.player_bigdaddy_takedowns() * ShockPlayerController.game_stat_bigdaddy_takedown_value(),
        "little_sister": PlayerReplicationInfo.player_little_sister_saves() * ShockPlayerController.game_stat_litte_sister_save_value(),
        "humiliation": PlayerReplicationInfo.player_humiliations() * ShockPlayerController.game_stat_humiliation_value(),
        "debug": PlayerReplicationInfo.player_debug_score() * ShockPlayerController.game_stat_debug_value(),
        "trial": ShockPlayerController.player_trial_adam_earned(),
        "adam_grab": 0,
        "scoreboard": player_scoreboard_score()
    }

    if game_mode() in  ["GAMEMODE_ODDFFA", "GAMEMODE_ODD"]:
        player_scores["adam_grab"] = PlayerReplicationInfo.player_adam_grab_score()

    total_score = sum(player_scores.values())
    return total_score

def player_weapon():
    if not ShockPlayerController.shock_player_load() or PlayerReplicationInfo.player_dead() or DualWieldHands.current_weapon() == 0:
        return "None"
    
    weapon = Weapon.unique_weapon_id()

    if weapon == -1:
        weapon_friendly_name = Weapon.friendly_name()

        if weapon == "Wrench" and game_mode() == "GAMEMODE_DLC_2":
            return "Golf Club"
        elif weapon == "Wrench":
            return "Melee Weapon"
        return weapon_friendly_name if weapon_friendly_name in Bioshock2Multiplayer.WEAPONS else "None"

    return Bioshock2Multiplayer.WEAPON_IDS.get(weapon,"None")

def player_plasmid():
    if not ShockPlayerController.shock_player_load() or PlayerReplicationInfo.player_dead() or DualWieldHands.current_ability() == 0:
        return "None"

    plasmid = Ability.unique_ability_id()

    if plasmid == -1:
        plasmid_friendly_name = Ability.friendly_name()
        return plasmid_friendly_name if plasmid_friendly_name in Bioshock2Multiplayer.PLASMIDS else "None"
    else:
        return Bioshock2Multiplayer.PLASMID_IDS.get(plasmid, "None")

def player_upgrade():
    if not ShockPlayerController.shock_player_load() or PlayerReplicationInfo.player_dead() or DualWieldHands.current_weapon() == 0 or Weapon.active_upgrade() == 0:
        return "None"
    
    upgrade = Upgrade.unique_upgrade_id()

    return Bioshock2Multiplayer.UPGRADES.get(upgrade, "None")

def player_quick_melee():
    splicer = player_splicer()

    quick_weapon = ShockUserSettings.melee_weapon_index()

    unique_id, min_range, max_range, unique = Bioshock2Multiplayer.MELEE_WEAPONS[splicer]

    if quick_weapon == unique_id:
        return unique
    elif quick_weapon in range(min_range, max_range):
        return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][quick_weapon - min_range]
    
def player_melee():
    if not ShockPlayerController.shock_player_load() or DualWieldHands.current_weapon() == 0:
        return False
    
    return PlayerWeapon.quick_melee()

def player_bigdaddy():
    return False if not ShockPlayerController.shock_player_load() else Pawn.menu_name() == "ShockMPRosie"

def player_stats():
    stats = {
        "kills": PlayerReplicationInfo.player_kills(),
        "deaths": PlayerReplicationInfo.player_deaths(),
        "score": PlayerReplicationInfo.player_score(),
    }
    return stats

def player_status():
    if PlayerReplicationInfo.player_dead():
        return "PLAYER_DEAD"
    elif player_bigdaddy():
        return "PLAYER_BIGDADDY"
    elif player_melee():
        return "PLAYER_MELEE"
    else:
        return "PLAYER_ALIVE"

def player_game_status():
    game_state = match_status()

    if (game_state in {"MATCH_BEGIN", "MATCH_STARTED"}) and not streamed_loadout():
        return "Selecting a Loadout"
    elif game_state == "MATCH_BEGIN" and streamed_loadout():
        return f'Match Starting in {int(ShockMPGameReplicationInfo.round_timer())}'
    elif game_state == "MATCH_STARTED" and streamed_loadout():
        player_state = player_status()
        if player_state == "PLAYER_DEAD":
            return "Waiting to Respawn" 
        elif player_state == "PLAYER_BIGDADDY":
            return "Roaming as the Big Daddy" if player_plasmid() != "Stomp" else "Stomping as the Big Daddy"
        elif player_state == "PLAYER_MELEE":
            return "Melee-ing with the " + (player_quick_melee() if not player_bigdaddy() else "Rivet Gun")
        elif game_mode() == "GAMEMODE_DLC_2":
            return "Whacking other players with the " + player_weapon() 
        return f'{player_upgrade()} {player_weapon()} with {player_plasmid()}' if player_upgrade() != "None" else f'{player_weapon()} with {player_plasmid()}'
    elif game_state == "MATCH_ENDED":
        return end_movie()
    elif game_state == "MATCH_UNKNOWN":
        return "Match Status Currently Unavailable."
    
    return "Match Status Currently Unavailable."

def player_all_time_stats():
    player_stats =  {
        "rank": UserProfile.player_rank(),
        "adam": UserProfile.player_banked_adam(),
        "wins": UserProfile.player_lifetime_wins(),
        "kills": UserProfile.player_lifetime_kills(),
        "playtime": player_time_played()
    }
    return player_stats

def team_game():
    return PlayerReplicationInfo.team_info() != 0

def game_map():
    return Bioshock2Multiplayer.MAP_URLS.get(GameEngine.last_url_map_name(),"Entry")

def game_num_players():
    return 0 if not ShockPlayerController.game_replication_info_load() else GameReplicationInfo.pri_array_player_count()

def game_max_players():
    return ADAM_GRAB_MAX_PLAYERS if game_mode() == "GAMEMODE_ODDFFA" else MAX_PLAYERS

def game_timer():
    main_timer = ShockMPGameReplicationInfo.main_timer()
    main_minutes, main_seconds = divmod(main_timer, 60)
    return f"{int(main_minutes):2d}:{int(main_seconds):02d}"

def game_round():
    return ShockMPGameReplicationInfo.current_round() + 1

def streamed_loadout():
    return ShockMPPlayerController.streamed_in_loadout() >= 0

def match_status():
    if not ShockPlayerController.game_replication_info_load():
        return "MATCH_UNKNOWN"
    
    if ShockMPGameReplicationInfo.game_ready() and ShockMPGameReplicationInfo.round_timer() > 0:
        return "MATCH_BEGIN"
    elif not ShockMPGameReplicationInfo.game_ready() and ShockMPGameReplicationInfo.game_running():
        return "MATCH_STARTED"
    elif ShockPlayerController.game_has_ended():
        return "MATCH_ENDED"

    return "MATCH_UNKNOWN"

def end_game_reason():
    return Bioshock2Multiplayer.GAME_WINNING_REASON[ShockPlayerController.game_end_reason()]

def end_movie():
    if ShockPlayerController.match_scoreboard() and not ShockPlayerController.match_results():
        return "Score: "  + str(PlayerReplicationInfo.player_score()) + " Kills: " + str(PlayerReplicationInfo.player_kills()) + " Streaks: " + str(PlayerReplicationInfo.player_kill_streaks())
    elif ShockPlayerController.match_results():
        total_score = player_total_score()
        player_position, last_position = player_ranking()
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(player_position, "th")
        return "Total Adam: " + str(total_score) + " Ranking: " + str(player_position) + suffix
    else:
        return "Match has Ended"

def apartment_movie():
    if OnlineLobbyController.using_bathysphere():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Lobby"]
    elif ShockPlayerController.in_apartment_intro():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Intro"]
    elif ShockPlayerController.in_apartment_outro():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Outro"]
    else:
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment"]

def in_apartment():
    return game_map() == "Apartment Lobby"

def debug():
    print(flash_movie() + "\n")
    if (in_apartment()):
        print("Apartment Lobby", in_apartment())
        print("Apartment Lobby Menu", OnlineLobbyController.using_bathysphere())
        print("Apartment Intro:", ShockPlayerController.in_apartment_intro())
        print("Apartment Outro", ShockPlayerController.in_apartment_outro())
    print(player_splicer())



# Fix Multi-Language Support (remove friendlynames and use Ids instead).
# Find a way to determine if bigdaddy is currently stomping
# Make clearer readme


# Create PyInstaller .bat script for easy .exe creation.
# Test .exe
# Modify readme for Discord Application Instructions
# Begin Intial RPC tests (Non-Anti Cheat)