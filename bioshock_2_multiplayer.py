from bioshock_2_multiplayer_memory import engine_load, read_memory, Engine_U, ShockGame_U

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
        "Burst Firing",
        "None"
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

    MAP_URLS ={
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

    GAMEMODES ={
        0: ["FFA", "Survival of the Fittest"],
        1: ["TDM", "Civil War"],
        3: ["HOG", "Capture The Sister"],
        4: ["ODD", "Team Adam Grab"],
        5: ["TC", "Turf War"],
        6: ["DLC2", "Kill 'Em Kindly"],
        8: ["ODDFFA", "Adam Grab"],
        9: ["TDMHC", "Last Splicer Standing"],
        "None": ["NONE", "Loading..."],
    }

    WIN_REASONS = {
        0: "Match ended with Invalid Win",
        1: "Time Limit has been Reached",
        2: "Score Limit has been Reached",
        3: "All Players Left the Match",
        4: "Defenders have Won the Match",
        5: "Little Sister was Saved",
        6: "Little Sister was Harvested",
        7: "Match has been Aborted by Host"

    }

    FLASH_MOVIES ={
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
        "Loading": "Loading the Match",
        "None": "Loading...",
    }


class PlayerReplicationInfo:
    def read_stat(self, attribute):
        return read_memory(Engine_U, ["PlayerReplicationInfo", attribute])

@engine_load()
def game_replication_info_load():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GRI"]) != 0

@engine_load()
def shock_player_load():
    return read_memory(ShockGame_U, ["ShockPlayerController", "SMP"]) != 0

@engine_load()
def online_game_settings_load():
    return read_memory(Engine_U, ["OnlineLobbyController", "mOnlineLobby"]) != 0 and read_memory(Engine_U, ["OnlineLobby", "mGameSettings"]) != 0


@engine_load()
def online_game_settings_properties_load():
    return read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties"]) != 0

@engine_load()
def flash_movie():
    if in_apartment():
        return apartment_movie()

    hud_movie = read_memory(Engine_U, ["FlashGUIController","HUDMovie"])
    bink_movie = read_memory(Engine_U, ["FlashGUIController", "BackgroundBinkMovieContainer"])

    if hud_movie != 0:
        hud_movie_name_size = read_memory(Engine_U,  ["FlashGUIController", "HUDMovie", "Filename Size"])
        flash_movie = read_memory(Engine_U, ["FlashGUIController", "HUDMovie", "FlashFilename"], hud_movie_name_size)
    elif bink_movie != 0:
        bink_movie_name_size = read_memory(Engine_U, ["FlashGUIController", "BackgroundBinkMovieContainer", "Filename Size"])
        flash_movie = read_memory(Engine_U, ["FlashGUIController", "BackgroundBinkMovieContainer", "FlashFilename"], bink_movie_name_size)
    
    flash_movie = flash_movie.split('\\')[2]

    return Bioshock2Multiplayer.FLASH_MOVIES[flash_movie]

@engine_load()
def in_lobby():
    return online_game_settings_load() == True and lobby_num_players() > 0

@engine_load()
def lobby_num_players():
    return read_memory(Engine_U, ["OnlineLobby", "mGameNumPlayers"])

@engine_load()
def lobby_max_players():
    return 6 if lobby_game_mode()[0] == "ODDFFA" else 10

@engine_load()
def lobby_type():
    if not in_lobby():
        return "None"
    
    if read_memory(Engine_U, ["OnlineGameSettings", "NumPublicConnections"]) > 0:
        return "Public"
    elif read_memory(Engine_U, ["OnlineGameSettings", "NumPrivateConnections"]) > 0:
        return "Private"
    else:
        return "None"

@engine_load()
def lobby_game_map():
    if not in_lobby() or not online_game_settings_properties_load():
        return Bioshock2Multiplayer.MAPS[17]
    
    properties_index = 0
    while properties_index < 7:
        current_properties = read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties", "Properties [" + str(properties_index) + "]"])

        if current_properties == 0x10000010:
            lobby_map_id = read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties", "Properties [" + str(properties_index) + "]", "Data", "Value_1"])

        properties_index += 1
    
    return Bioshock2Multiplayer.MAPS[lobby_map_id]

@engine_load()
def lobby_game_mode():
    if not in_lobby() or not online_game_settings_properties_load():
        return "No Gamemode Found"

    properties_index = 0
    while properties_index < 7:
        current_properties = read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties", "Properties [" + str(properties_index) + "]"])

        if current_properties == 0x1000000F:
            lobby_mode_id = read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties", "Properties [" + str(properties_index) + "]", "Data", "Value_1"])

        if current_properties == 0x1000004E:
            mode_hardcore = read_memory(Engine_U, ["OnlineGameSettings", "Engine.Settings", "Properties", "Properties [" + str(properties_index) + "]", "Data", "Value_1"]) != 0
        
        properties_index += 1
    
    return Bioshock2Multiplayer.GAMEMODES[9] if lobby_mode_id == 1 and mode_hardcore else Bioshock2Multiplayer.GAMEMODES[lobby_mode_id]

@engine_load()
def lobby_status():
    lobby_status_size = read_memory(Engine_U, ["OnlineLobbyController", "mGUIGameLobbyStatusSize"])
    lobby_status_message = read_memory(Engine_U, ["OnlineLobbyController", "mGUIGameLobbyStatus"], lobby_status_size)

    if lobby_status_message == 'Waiting for host to start match.':
        return "Waiting for host to start game."

    return lobby_status_message

@engine_load()
def player_rank():
    return read_memory(Engine_U, ["UserProfile", "mRank"])

@engine_load()
def player_banked_adam():
    return read_memory(Engine_U, ["UserProfile", "mBankedAdam"])

@engine_load()
def player_lifetime_kills():
    return read_memory(Engine_U, ["UserProfile", "mNumKills"])

@engine_load()
def player_lifetime_wins():
    return read_memory(Engine_U, ["UserProfile", "mNumWins"])

@engine_load()
def player_time_played():
    mTime = read_memory(Engine_U, ["UserProfile", "mSecondsPlayed"])
    
    mHours = mTime // 3600
    mSeconds_left = mTime % 3600
    mMinutes = mSeconds_left // 60
    mSeconds = mSeconds_left % 60

    return f"{mHours:02}:{mMinutes:02}:{mSeconds:02}"

@engine_load()
def player_splicer():
    return Bioshock2Multiplayer.CHARACTERS[read_memory(ShockGame_U, ["ShockUserSettings", "UserProfileCharacterId"])]

@engine_load()
def player_kills():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "Kills"])

@engine_load()
def player_assists():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "Assists"])

@engine_load()
def player_deaths():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "Deaths"])

@engine_load()
def player_kill_streaks():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "KillingStreaks"])

@engine_load()
def player_adam_vials_collected():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "ADAMVialsCollected"])

@engine_load()
def player_hacks():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "Hacks"])

@engine_load()
def player_bigdaddy_takedowns():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "BigDaddyTakedowns"])

@engine_load()
def player_bigdaddy_spawns():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "BigDaddySpawns"])

@engine_load()
def player_little_sister_saves():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "LittleSisterSaves"])

@engine_load()
def player_humiliations():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "Humiliations"])

@engine_load()
def player_adam_grab_score():
    return player_score() * game_stat_adam_grab_multiplier_value()

@engine_load()
def player_debug_score():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "DebugMetaScore"])

@engine_load()
def player_trial_adam_earned():
    return read_memory(ShockGame_U, ["ShockPlayerController", "TrialAdamEarnedThisMatch"])

@engine_load()
def player_score():
    return read_memory(Engine_U, ["PlayerReplicationInfo", "GameScore"])

@engine_load()
def player_ranking():
    rankings = player_replication_array()

    if game_mode()[0] == "FFA" or game_mode()[0] == "ODDFFA" or game_mode()[0] == "DLC2":
        player_id = read_memory(Engine_U, ["PlayerReplicationInfo", "OnlineId", "Uid"])
        if player_id == rankings[0]:
            player_position = 1
        else:
            player_position = rankings.index(player_id) + 1
    elif game_mode()[0] == "TDM" or game_mode()[0] == "TDMHC" or game_mode()[0] == "HOG" or game_mode()[0] == "TC" or  game_mode()[0] == "ODD":
        if team_game():
            local_player_team = read_memory(Engine_U, ["PlayerReplicationInfo", "Team", "TeamIndex"])
            game_winning_team = read_memory(ShockGame_U, ["ShockPlayerController", "GameWinningTeam"])
            if game_winning_team != 255:
                if game_winning_team == local_player_team:
                    player_position = 1
                else:
                    player_position = 2
            else:
                player_position = 2

    return player_position

@engine_load()
def player_scoreboard_score():
    player_position = player_ranking()

    if player_position == 1:
        raw_rank_value = game_stat_first_place_value()
    else:
        ranking_percent = 1.0 - (float(player_position - 2) / float(game_num_players()))
        raw_rank_value = (ranking_percent * float(game_stat_second_place_value())) + ((1.0 - ranking_percent) * float(game_stat_last_place_value()))
   
    scoreboard_rank_score = int(raw_rank_value)

    if ((float(scoreboard_rank_score) % float(10)) != float(0)):
        scoreboard_rank_score = int(float(scoreboard_rank_score) + (float(10) - (float(scoreboard_rank_score) % float(10))))

    return scoreboard_rank_score

@engine_load()
def player_replication_array():
    if not game_replication_info_load():
        return 3

    current_pri_index = 1
    rankings = []

    while current_pri_index <= game_num_players() and current_pri_index <= game_max_players():
        player_id = read_memory(Engine_U, ["GameReplicationInfo", "PRIArray", "Player " + str(current_pri_index) + " PRI", "OnlineId"])
        rankings.append(player_id)
        current_pri_index += 1

    return rankings

@engine_load()
def player_total_score():
    total_score = 0
    kill_score = player_kills() * game_stat_kill_value()
    assist_score = player_assists() * game_stat_assist_value()
    kill_streak_score = player_kill_streaks() * game_stat_kill_streak_value()
    adam_vial_score = player_adam_vials_collected() * game_stat_adam_vial_value()
    hack_score = player_hacks() * game_stat_hack_value()
    big_daddy_score = player_bigdaddy_spawns() * game_stat_bigdaddy_spawn_value()
    big_daddy_takedown_score = player_bigdaddy_takedowns() * game_stat_bigdaddy_takedown_value()
    little_sister_score = player_little_sister_saves() * game_stat_litte_sister_save_value()
    humiliation_score = player_humiliations() * game_stat_humiliation_value()
    debug_score = player_debug_score() * game_stat_debug_value()
    trial_adam_score = player_trial_adam_earned()
    adam_grab_score = 0
    scoreboard_rank_score = player_scoreboard_score()

    if lobby_game_mode()[0] == "ODDFFA" or lobby_game_mode()[0] == "ODD":
        adam_grab_score = player_adam_grab_score()

    total_score = ((((((((((((kill_score + assist_score) + kill_streak_score) + adam_vial_score) + hack_score) + big_daddy_score) + big_daddy_takedown_score) + little_sister_score) + humiliation_score) + adam_grab_score) + debug_score) + trial_adam_score) + scoreboard_rank_score)

    return total_score

@engine_load()
def player_weapon():
    if not shock_player_load()  or read_memory(ShockGame_U, ["DualWieldHands", "CurrentWeapon"]) == 0:
        return "None"
    
    weapon_friendly_name_size = read_memory(ShockGame_U, ["Weapon", "FriendlyNameSize"])
    weapon_friendly_name = read_memory(ShockGame_U, ["Weapon", "FriendlyNameID"], weapon_friendly_name_size)

    if weapon_friendly_name == "Wrench" and game_mode()[0] == "DLC2":
        return "Golf Club"
    elif weapon_friendly_name == "Wrench":
        return "Melee Weapon"


    return weapon_friendly_name if weapon_friendly_name in Bioshock2Multiplayer.WEAPONS else "No Weapon"

@engine_load()
def player_plasmid():
    if not shock_player_load()  or read_memory(ShockGame_U, ["DualWieldHands", "CurrentAbility"]) == 0:
        return "None"

    plasmid_friendly_name_size = read_memory(ShockGame_U, ["Ability", "FriendlyNameSize"])
    plasmid_friendly_name = read_memory(ShockGame_U, ["Ability", "FriendlyNameID"], plasmid_friendly_name_size)

    return plasmid_friendly_name if plasmid_friendly_name in Bioshock2Multiplayer.PLASMIDS else "No Plasmid"

@engine_load()
def player_upgrade():
    if not shock_player_load() or read_memory(ShockGame_U, ["Weapon", "ActiveUpgrade", "ActiveUpgrade 0"]) == 0:
        return "No Upgrade"

    upgrade_friendly_name_size = read_memory(ShockGame_U, ["Upgrade", "FriendlyNameSize"])
    upgrade_friendly_name = read_memory(ShockGame_U, ["Upgrade", "FriendlyNameID"], upgrade_friendly_name_size)

    return upgrade_friendly_name if upgrade_friendly_name in Bioshock2Multiplayer.UPGRADES else "No Upgrade"

@engine_load()
def player_quick_melee():
    splicer = player_splicer()

    quick_weapon = read_memory(ShockGame_U, ["ShockUserSettings", "UserProfileMeleeWeaponIndex"])

    unique_id, min_range, max_range, unique = Bioshock2Multiplayer.MELEE_WEAPONS[splicer]

    if quick_weapon == unique_id:
        return unique
    elif quick_weapon in range(min_range, max_range):
        return Bioshock2Multiplayer.MELEE_WEAPONS["Default Melee"][quick_weapon - min_range]

@engine_load()
def player_dead():
    if not game_replication_info_load():
        return True

    return read_memory(Engine_U, ["PlayerReplicationInfo", "bIsDead"])

@engine_load()
def player_melee():
    if not shock_player_load() or read_memory(ShockGame_U, ["DualWieldHands", "CurrentWeapon"]) == 0:
        return False
    
    return read_memory(ShockGame_U, ["PlayerWeapon", "IsQuickMelee"])

@engine_load()
def player_bigdaddy():
    return player_weapon() == "Rivet Gun" or player_plasmid == "Proximity Mine" or player_plasmid() == "Stomp"

@engine_load()
def player_game_status():
    if (pre_game() or running_game()) and not streamed_loadout():
        return "Selecting a Loadout"
    elif pre_game() and streamed_loadout():
        return "Match Starting in " + str(game_round_timer())
    elif running_game() and streamed_loadout():
        if player_dead():
            return "Waiting to Respawn"
        elif player_melee() and not player_bigdaddy():
            return "Melee-ing with the " + player_quick_melee()
        elif player_melee() and player_bigdaddy():
            return "Melee Attacking with the Rivet Gun"
        elif player_bigdaddy():
            return "Roaming as the Big Daddy" if player_plasmid() != "Stomp" else "Stomping as the Big Daddy"
        elif game_mode()[0] == "DLC2":
            return "Whacking other players with the " + player_weapon()
        else: 
            return player_upgrade() + " " + player_weapon() + " with " + player_plasmid() if player_upgrade() != "No Upgrade" else player_weapon() + " with " + player_plasmid()
    elif end_game():
        match_ending_screen = end_movie()
        return match_ending_screen

@engine_load()
def team_game():
    if not game_replication_info_load():
        return False
    
    return read_memory(Engine_U, ["GameReplicationInfo", "Teams"]) != 0

@engine_load()
def game_mode():
    if not game_replication_info_load():
        return Bioshock2Multiplayer.GAMEMODES["None"]

    gamemode = read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "GameMode"])
    mode_hardcore = read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "bHardcoreMode"])
    return Bioshock2Multiplayer.GAMEMODES[9] if gamemode == 1 and mode_hardcore else Bioshock2Multiplayer.GAMEMODES[gamemode]        

@engine_load()
def game_num_players():
    if not game_replication_info_load():
        return 0
    
    return read_memory(Engine_U, ["GameReplicationInfo", "PRINumPlayers"])

@engine_load()
def game_max_players():
    return 6 if game_mode()[0] == "ODDFFA" else 10

@engine_load()
def game_round():
    if not game_replication_info_load():
        return 0
    
    return read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "CurrentRound"])

@engine_load()
def game_timer():
    if not game_replication_info_load():
        return f"00:00"
    
    main_timer = read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "MainTimer"])
    main_minutes, main_seconds = divmod(main_timer, 60)
    return f"{int(main_minutes):2d}:{int(main_seconds):02d}"

@engine_load()
def game_round_timer():
    if not game_replication_info_load():
        return 0
    
    return int(read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "RoundTimer"]))

@engine_load()
def game_end_reason():
    return Bioshock2Multiplayer.WIN_REASONS[read_memory(ShockGame_U, ["ShockPlayerController", "GameWinningReason"])]

@engine_load()
def game_stat_kill_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatKillValue"])

@engine_load()
def game_stat_assist_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatAssistValue"])

@engine_load()
def game_stat_kill_streak_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatKillStreakValue"])

@engine_load()
def game_stat_adam_vial_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatADAMVialValue"])

@engine_load()
def game_stat_hack_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatHackValue"])

@engine_load()
def game_stat_bigdaddy_takedown_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatBigDaddyTakedownValue"])

@engine_load()
def game_stat_bigdaddy_spawn_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatBigDaddySpawnValue"])

@engine_load()
def game_stat_litte_sister_save_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatLittleSisterSaveValue"])

@engine_load()
def game_stat_humiliation_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatHumiliationValue"])

@engine_load()
def game_stat_first_place_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatFirstPlaceValue"])

@engine_load()
def game_stat_second_place_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatSecondPlaceValue"])

@engine_load()
def game_stat_last_place_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatLastPlaceValue"])

@engine_load()
def game_stat_adam_grab_multiplier_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameAdamGrabMultiplier"])

@engine_load()
def game_stat_debug_value():
    return read_memory(ShockGame_U, ["ShockPlayerController", "GameStatDebugValue"])


@engine_load()
def streamed_loadout():
    return read_memory(ShockGame_U, ["ShockMPPlayerController", "StreamedInLoadout"]) >= 0

@engine_load()
def pre_game():
    return game_round_timer() > 0 if game_replication_info_load() else False

@engine_load()
def running_game():
    if not game_replication_info_load():
        return False
    
    game_ready = read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "bGameReady"]) == False
    return game_ready and read_memory(ShockGame_U, ["ShockMPGameReplicationInfo", "bGameRunning"])

@engine_load()
def end_game():
    if not game_replication_info_load():
        return False
    
    return read_memory(ShockGame_U, ["ShockPlayerController", "bGameHasEnded"])

@engine_load()
def end_movie():
    if match_scoreboard() and not match_results():
        return "Score: "  + str(player_score()) + " Kills: " + str(player_kills()) + " Streaks: " + str(player_kill_streaks())
    elif match_results():
        total_score = player_total_score()
        player_position = player_ranking()
        suffix = {1: "st", 2: "nd", 3: "rd"}.get(player_position, "th")
        return "Total Adam: " + str(total_score) + " Ranking: " + str(player_position) + suffix
    else:
        return "Match has Ended"
    
@engine_load()
def match_results():
    return read_memory(ShockGame_U, ["ShockPlayerController", "DisplayingMatchResult"])

@engine_load()
def match_scoreboard():
    return read_memory(ShockGame_U, ["ShockPlayerController", "bGameEndHasShownScoreboard"])

@engine_load()
def apartment_movie():
    if in_apartment_lobby():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Lobby"]
    elif in_apartment_intro():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Intro"]
    elif in_apartment_outro():
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment Outro"]
    else:
        return Bioshock2Multiplayer.FLASH_MOVIES["Apartment"]

@engine_load()
def in_apartment():
    last_url_size = read_memory(Engine_U, ["GameEngine", "LastURL", "Map Size"])
    last_url_map = read_memory(Engine_U, ["GameEngine", "LastURL", "DE_Map Name"], last_url_size)
    return Bioshock2Multiplayer.MAP_URLS[last_url_map] == "Apartment Lobby"

@engine_load()
def in_apartment_lobby():
    return read_memory(Engine_U, ["OnlineLobbyController", "mGUIUsingBathysphere"])

@engine_load()
def in_apartment_intro():
    return read_memory(ShockGame_U, ["ShockPlayerController", "bApartmentIntro"])

@engine_load()
def in_apartment_outro():
    return read_memory(ShockGame_U, ["ShockPlayerController", "bApartmentOutro"])

def debug():
    print(flash_movie() + "\n")
    if (in_apartment()):
        print("Apartment Lobby", in_apartment())
        print("Apartment Lobby Menu", in_apartment_lobby())
        print("Apartment Intro:", in_apartment_intro())
        print("Apartment Outro", in_apartment_outro())
    print(player_splicer())

