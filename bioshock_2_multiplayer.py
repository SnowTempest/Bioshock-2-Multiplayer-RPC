from bioshock_2_multiplayer_memory import level_load, read_memory, Engine_U, ShockGame_U

ADAM_GRAB_MAX_PLAYERS = 6
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

class UnrealReader:
    u_file = None

    @classmethod
    @level_load()
    def read(u_class, *attributes, num_bytes=None):
        u_class_name = u_class.__name__
        return read_memory(u_class.u_file, (u_class_name,) + attributes, num_bytes)


class GameEngine(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def last_url_map_name_size():
        return GameEngine.read("LastURL", "DE_Map NameSize")

    @staticmethod
    def last_url_map_name():
        return GameEngine.read("LastURL", "DE_Map Name", num_bytes=GameEngine.last_url_map_name_size())


class OnlineLobbyController(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def online_game_settings_load():
        return OnlineLobbyController.online_lobby() != 0 and OnlineLobby.game_settings() != 0

    @staticmethod
    def online_lobby():
        return OnlineLobbyController.read("mOnlineLobby")
    
    @staticmethod
    def game_lobby_status():
        return OnlineLobbyController.read("mGUIGameLobbyStatus", num_bytes=OnlineLobbyController.game_lobby_status_size())

    @staticmethod
    def game_lobby_status_size():
        return OnlineLobbyController.read("mGUIGameLobbyStatusSize")
    
    @staticmethod
    def using_bathysphere():
        return OnlineLobbyController.read("mGUIUsingBathysphere")


class OnlineLobby(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def game_settings():
        return OnlineLobby.read("mGameSettings")
    
    @staticmethod
    def lobby_num_players():
        return OnlineLobby.read("mGameNumPlayers")
    
    @staticmethod
    def player_nickname_size(player_index):
        return OnlineLobby.read("mGamePlayers", "Player " + str(player_index), "NickNameSize")
    
    @staticmethod
    def player_nickname(player_index):
        return OnlineLobby.read("mGamePlayers", "Player " + str(player_index), "NickNameID", num_bytes=OnlineLobby.player_nickname_size(player_index))

    @staticmethod
    def player_rank(player_index):
        return OnlineLobby.read("mGamePlayers", "Player " + str(player_index), "Rank")
    
    @staticmethod
    def player_rebirth_count(player_index):
        return OnlineLobby.read("mGamePlayers", "Player " + str(player_index), "RebirthCount")

    @staticmethod
    def player_steam_id(player_index):
        return OnlineLobby.read("mGamePlayers", "Player " + str(player_index), "UniqueId")


class OnlineGameSettings(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def ogs_props_load():
        return OnlineGameSettings.read("Engine.Settings", "Properties") != 0

    @staticmethod
    def property_id(prop_index):
        return OnlineGameSettings.read("Engine.Settings", "Properties", "Properties [" + str(prop_index) + "]")

    @staticmethod
    def property_value_1(prop_index):
        return OnlineGameSettings.read("Engine.Settings", "Properties", "Properties [" + str(prop_index) + "]", "Data", "Value_1")
    
    @staticmethod
    def num_public_connections():
        return OnlineGameSettings.read("NumPublicConnections")
    
    @staticmethod
    def num_private_connections():
        return OnlineGameSettings.read("NumPrivateConnections")


class FlashGUIController(UnrealReader):
    u_file = Engine_U
    
    @staticmethod
    def hud_movie():
        return FlashGUIController.read("HUDMovie")
    
    @staticmethod
    def bink_movie_container():
        return FlashGUIController.read("BackgroundBinkMovieContainer")
    
    @staticmethod
    def hud_file_name_size():
        return FlashGUIController.read("HUDMovie", "Filename Size")
    
    @staticmethod
    def hud_movie_file_name():
        return FlashGUIController.read("HUDMovie", "FlashFilename", num_bytes=FlashGUIController.hud_file_name_size())

    @staticmethod
    def bink_movie_name_size():
        return FlashGUIController.read("BackgroundBinkMovieContainer", "Filename Size")
    
    @staticmethod
    def bink_movie_file_name():
        return FlashGUIController.read("BackgroundBinkMovieContainer", "FlashFilename", num_bytes=FlashGUIController.bink_movie_name_size())


class PlayerReplicationInfo(UnrealReader):
    u_file = Engine_U
    
    @staticmethod
    def player_steam_id():
        return PlayerReplicationInfo.read("OnlineId")

    @staticmethod
    def team_info():
        return PlayerReplicationInfo.read("Team")

    @staticmethod
    def team_index():
        return PlayerReplicationInfo.read("Team", "TeamIndex")

    @staticmethod
    def player_is_dead():
        return PlayerReplicationInfo.read("bIsDead")

    @staticmethod
    def player_score():
        return PlayerReplicationInfo.read("GameScore")

    @staticmethod
    def player_kills():
        return PlayerReplicationInfo.read("Kills")

    @staticmethod
    def player_assists():
        return PlayerReplicationInfo.read("Assists")

    @staticmethod
    def player_deaths():
        return PlayerReplicationInfo.read("Deaths")

    @staticmethod
    def player_kill_streaks():
        return PlayerReplicationInfo.read("KillingStreaks")

    @staticmethod
    def player_adam_vials_collected():
        return PlayerReplicationInfo.read("ADAMVialsCollected")

    @staticmethod
    def player_hacks():
        return PlayerReplicationInfo.read("Hacks")
    
    @staticmethod
    def player_bigdaddy_takedowns():
        return PlayerReplicationInfo.read("BigDaddyTakedowns")

    @staticmethod
    def player_bigdaddy_spawns():
        return PlayerReplicationInfo.read("BigDaddySpawns")

    @staticmethod
    def player_little_sister_saves():
        return PlayerReplicationInfo.read("LittleSisterSaves")

    @staticmethod
    def player_humiliations():
        return PlayerReplicationInfo.read("Humiliations")

    @staticmethod
    def player_adam_grab_score():
        return PlayerReplicationInfo.player_score() * ShockPlayerController.game_stat_adam_grab_multiplier_value()
    
    @staticmethod
    def player_debug_score():
        return PlayerReplicationInfo.read("DebugMetaScore")


class GameReplicationInfo(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def pri_array_player_count():
        return GameReplicationInfo.read("PRINumPlayers")

    @staticmethod
    def pri_array_online_id(prop_id):
        return GameReplicationInfo.read("PRIArray", "Player " + str(prop_id) + " PRI", "OnlineId")


class UserProfile(UnrealReader):
    u_file = Engine_U

    @staticmethod
    def player_rank():
        return UserProfile.read("mRank")

    @staticmethod
    def seconds_played():  
         return UserProfile.read("mSecondsPlayed")

    @staticmethod
    def player_banked_adam():
        return UserProfile.read("mBankedAdam")

    @staticmethod
    def player_lifetime_kills():
        return UserProfile.read("mNumKills")

    @staticmethod
    def player_lifetime_wins():
       return UserProfile.read("mNumWins")


class ShockPlayerController(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def game_replication_info_load():
        return ShockPlayerController.read("GRI") != 0

    @staticmethod
    def shock_player_load():
        return ShockPlayerController.read("SMP") != 0

    @staticmethod
    def in_apartment_intro():
        return ShockPlayerController.read("bApartmentIntro")

    @staticmethod
    def in_apartment_outro():
        return ShockPlayerController.read("bApartmentOutro")

    @staticmethod
    def game_has_ended():
        return ShockPlayerController.read("bGameHasEnded")

    @staticmethod
    def game_stat_kill_value():
        return ShockPlayerController.read("GameStatKillValue")

    @staticmethod
    def game_stat_assist_value():
        return ShockPlayerController.read("GameStatAssistValue")

    @staticmethod
    def game_stat_kill_streak_value():
        return ShockPlayerController.read("GameStatKillStreakValue")

    @staticmethod
    def game_stat_adam_vial_value():
        return ShockPlayerController.read("GameStatADAMVialValue")

    @staticmethod
    def game_stat_hack_value():
        return ShockPlayerController.read("GameStatHackValue")

    @staticmethod
    def game_stat_bigdaddy_takedown_value():
        return ShockPlayerController.read("GameStatBigDaddyTakedownValue")

    @staticmethod
    def game_stat_bigdaddy_spawn_value():
        return ShockPlayerController.read("GameStatBigDaddySpawnValue")

    @staticmethod
    def game_stat_litte_sister_save_value():
        return ShockPlayerController.read("GameStatLittleSisterSaveValue")

    @staticmethod
    def game_stat_humiliation_value():
        return ShockPlayerController.read("GameStatHumiliationValue")

    @staticmethod
    def game_stat_first_place_value():
        return ShockPlayerController.read("GameStatFirstPlaceValue")

    @staticmethod
    def game_stat_second_place_value():
        return ShockPlayerController.read("GameStatSecondPlaceValue")

    @staticmethod
    def game_stat_last_place_value():
        return ShockPlayerController.read("GameStatLastPlaceValue")

    @staticmethod
    def game_stat_adam_grab_multiplier_value():
        return ShockPlayerController.read("GameAdamGrabMultiplier")

    @staticmethod
    def game_stat_debug_value():
        return ShockPlayerController.read("GameStatDebugValue")

    @staticmethod
    def player_trial_adam_earned():
        return ShockPlayerController.read("TrialAdamEarnedThisMatch")

    @staticmethod
    def game_winning_team():
        return ShockPlayerController.read("GameWinningTeam")
    
    @staticmethod
    def game_end_reason():
        return ShockPlayerController.read("GameWinningReason")
    
    @staticmethod
    def match_results():
        return ShockPlayerController.read("DisplayingMatchResult")

    @staticmethod
    def match_scoreboard():
        return ShockPlayerController.read("bGameEndHasShownScoreboard")
    

class ShockMPPlayerController(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def streamed_in_loadout():
        return ShockMPPlayerController.read("StreamedInLoadout")


class ShockMPGameReplicationInfo(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def current_round():
        return ShockMPGameReplicationInfo.read("CurrentRound")
    
    @staticmethod
    def main_timer():
        return ShockMPGameReplicationInfo.read("MainTimer")

    @staticmethod
    def round_timer():
        return ShockMPGameReplicationInfo.read("RoundTimer")

    @staticmethod
    def game_ready():
        return ShockMPGameReplicationInfo.read("bGameReady")

    @staticmethod
    def game_running():
        return ShockMPGameReplicationInfo.read("bGameRunning")
    
    @staticmethod
    def game_mode():
        return ShockMPGameReplicationInfo.read("GameMode")

    @staticmethod
    def hardcore_mode():
        return ShockMPGameReplicationInfo.read("bHardcoreMode")


class ShockUserSettings(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def character_id():
        return ShockUserSettings.read("UserProfileCharacterId")

    @staticmethod
    def melee_weapon_index():
        return ShockUserSettings.read("UserProfileMeleeWeaponIndex")


class DualWieldHands(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def current_weapon():
        return DualWieldHands.read("CurrentWeapon")

    @staticmethod
    def current_ability():
        return DualWieldHands.read("CurrentAbility")


class Weapon(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def friendly_name_size():
        return Weapon.read("FriendlyNameSize")

    @staticmethod
    def friendly_name():
        return Weapon.read("FriendlyNameID", num_bytes=Weapon.friendly_name_size())

    @staticmethod
    def active_upgrade():
        return Weapon.read("ActiveUpgrade", "ActiveUpgrade 0")


class PlayerWeapon(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def quick_melee():
        return PlayerWeapon.read("IsQuickMelee")


class Ability(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def friendly_name_size():
        return Ability.read("FriendlyNameSize")
    
    @staticmethod
    def friendly_name():
        return Ability.read("FriendlyNameID", num_bytes=Ability.friendly_name_size())


class Upgrade(UnrealReader):
    u_file = ShockGame_U

    @staticmethod
    def friendly_name_size():
        return Upgrade.read("FriendlyNameSize")
    
    @staticmethod
    def friendly_name():
        return Upgrade.read("FriendlyNameID", num_bytes=Upgrade.friendly_name_size())
    

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


def in_lobby():
    return OnlineLobbyController.online_game_settings_load() == True and OnlineLobby.lobby_num_players() > 0


def lobby_max_players():
    return ADAM_GRAB_MAX_PLAYERS if lobby_game_mode() == "GAMEMODE_ODDFFA" else MAX_PLAYERS

def lobby_type():
    if not in_lobby():
        return "None"
    
    if  OnlineGameSettings.num_public_connections() > 0:
        return "Public"
    elif OnlineGameSettings.num_private_connections() > 0:
        return "Private"
    else:
        return "None"

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

def lobby_game_mode():
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

    return f"{mHours:02}:{mMinutes:02}:{mSeconds:02}"

def player_splicer():
    return Bioshock2Multiplayer.CHARACTERS[ShockUserSettings.character_id()]

def player_ranking():
    rankings = player_replication_array()

    if rankings == "None":
        return 0
    
    if team_game():
        local_player_team = PlayerReplicationInfo.team_index()
        game_winning_team = ShockPlayerController.game_winning_team()
        if game_winning_team != 255:
            if game_winning_team == local_player_team:
                player_position = 1
            else:
                player_position = 2
        else:
            player_position = 2
    else:
        player_id = PlayerReplicationInfo.player_steam_id()
        if player_id == rankings[0]:
            player_position = 1
        else:
            player_position = rankings.index(player_id) + 1

    return player_position

def player_scoreboard_score():
    player_position = player_ranking()

    if player_position == 0:
        return 0

    if player_position == 1:
        raw_rank_value = ShockPlayerController.game_stat_first_place_value()
    else:
        ranking_percent = 1.0 - (float(player_position - 2) / float(game_num_players()))
        raw_rank_value = (ranking_percent * float(ShockPlayerController.game_stat_second_place_value())) + ((1.0 - ranking_percent) * float(ShockPlayerController.game_stat_last_place_value()))
   
    scoreboard_rank_score = int(raw_rank_value)

    if ((float(scoreboard_rank_score) % float(10)) != float(0)):
        scoreboard_rank_score = int(float(scoreboard_rank_score) + (float(10) - (float(scoreboard_rank_score) % float(10))))

    return scoreboard_rank_score

def player_replication_array():
    if not ShockPlayerController.game_replication_info_load():
        return "None"

    current_pri_index = 1
    rankings = []

    while current_pri_index <= game_num_players() and current_pri_index <= game_max_players():
        player_id = GameReplicationInfo.pri_array_online_id(current_pri_index)
        rankings.append(player_id)
        current_pri_index += 1

    return rankings

def player_total_score():
    if not ShockPlayerController.game_replication_info_load():
        return 0

    total_score = 0
    kill_score = PlayerReplicationInfo.player_kills() * ShockPlayerController.game_stat_kill_value()
    assist_score = PlayerReplicationInfo.player_assists() * ShockPlayerController.game_stat_assist_value()
    kill_streak_score = PlayerReplicationInfo.player_kill_streaks() * ShockPlayerController.game_stat_kill_streak_value()
    adam_vial_score = PlayerReplicationInfo.player_adam_vials_collected() * ShockPlayerController.game_stat_adam_vial_value()
    hack_score = PlayerReplicationInfo.player_hacks() * ShockPlayerController.game_stat_hack_value()
    big_daddy_score = PlayerReplicationInfo.player_bigdaddy_spawns() * ShockPlayerController.game_stat_bigdaddy_spawn_value()
    big_daddy_takedown_score = PlayerReplicationInfo.player_bigdaddy_takedowns() * ShockPlayerController.game_stat_bigdaddy_takedown_value()
    little_sister_score = PlayerReplicationInfo.player_little_sister_saves() * ShockPlayerController.game_stat_litte_sister_save_value()
    humiliation_score = PlayerReplicationInfo.player_humiliations() * ShockPlayerController.game_stat_humiliation_value()
    debug_score = PlayerReplicationInfo.player_debug_score() * ShockPlayerController.game_stat_debug_value()
    trial_adam_score = ShockPlayerController.player_trial_adam_earned()
    adam_grab_score = 0
    scoreboard_rank_score = player_scoreboard_score()

    if lobby_game_mode() == "GAMEMODE_ODD" or lobby_game_mode() == "GAMEMODE_ODDFFA":
        adam_grab_score = PlayerReplicationInfo.player_adam_grab_score()

    total_score = ((((((((((((kill_score + assist_score) + kill_streak_score) + adam_vial_score) + hack_score) + big_daddy_score) + big_daddy_takedown_score) + little_sister_score) + humiliation_score) + adam_grab_score) + debug_score) + trial_adam_score) + scoreboard_rank_score)

    return total_score

def player_weapon():
    if not ShockPlayerController.shock_player_load()  or DualWieldHands.current_weapon() == 0:
        return "None"
    
    weapon = Weapon.friendly_name()

    if weapon == "Wrench" and game_mode() == "GAMEMODE_DLC_2":
        return "Golf Club"
    elif weapon == "Wrench":
        return "Melee Weapon"

    return weapon if weapon in Bioshock2Multiplayer.WEAPONS else "No Weapon"

def player_plasmid():
    if not ShockPlayerController.shock_player_load()  or DualWieldHands.current_ability() == 0:
        return "None"

    plasmid = Ability.friendly_name()

    return plasmid if plasmid in Bioshock2Multiplayer.PLASMIDS else "No Plasmid"

def player_upgrade():
    if not ShockPlayerController.shock_player_load() or Weapon.active_upgrade() == 0:
        return "No Upgrade"
    
    upgrade = Upgrade.friendly_name()

    return upgrade if upgrade in Bioshock2Multiplayer.UPGRADES else "No Upgrade"

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

def player_dead():
    return not ShockPlayerController.game_replication_info_load() or PlayerReplicationInfo.player_is_dead()

def player_bigdaddy():
    return player_weapon() == "Rivet Gun" and (player_plasmid() == "Proximity Mine" or player_plasmid() == "Stomp")

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
        elif game_mode() == "GAMEMODE_DLC_2":
            return "Whacking other players with the " + player_weapon()
        else: 
            return player_upgrade() + " " + player_weapon() + " with " + player_plasmid() if player_upgrade() != "No Upgrade" else player_weapon() + " with " + player_plasmid()
    elif end_game():
        return end_movie()

def team_game():
    return False if not ShockPlayerController.game_replication_info_load() else PlayerReplicationInfo.team_info() != 0

def game_mode():
    if not ShockPlayerController.game_replication_info_load():
        return Bioshock2Multiplayer.GAME_MODES["None"]

    gamemode = ShockMPGameReplicationInfo.game_mode()
    mode_hardcore = ShockMPGameReplicationInfo.hardcore_mode()
    return Bioshock2Multiplayer.GAME_MODES[9] if gamemode == 1 and mode_hardcore else Bioshock2Multiplayer.GAME_MODES[gamemode]        

def game_map():
    return Bioshock2Multiplayer.MAP_URLS[GameEngine.last_url_map_name()]

def game_num_players():
    return 0 if not ShockPlayerController.game_replication_info_load() else GameReplicationInfo.pri_array_player_count()

def game_max_players():
    return ADAM_GRAB_MAX_PLAYERS if game_mode() == "GAMEMODE_ODDFFA" else MAX_PLAYERS

def game_round():
    return 0 if not ShockPlayerController.game_replication_info_load() else ShockMPGameReplicationInfo.current_round()

def game_timer():
    if not ShockPlayerController.game_replication_info_load():
        return f"00:00"
    
    main_timer = ShockMPGameReplicationInfo.main_timer()
    main_minutes, main_seconds = divmod(main_timer, 60)
    return f"{int(main_minutes):2d}:{int(main_seconds):02d}"

def game_round_timer():
    return 0 if not ShockPlayerController.game_replication_info_load() else int(ShockMPGameReplicationInfo.round_timer())

def streamed_loadout():
    return ShockMPPlayerController.streamed_in_loadout() >= 0

def pre_game():
    return False if not ShockPlayerController.game_replication_info_load() else game_round_timer() > 0

def running_game():
    return False if not ShockPlayerController.game_replication_info_load() else not ShockMPGameReplicationInfo.game_ready() and ShockMPGameReplicationInfo.game_running()

def end_game(): 
    return False if not ShockPlayerController.game_replication_info_load() else ShockPlayerController.game_has_ended()

def end_game_reason():
    return Bioshock2Multiplayer.GAME_WINNING_REASON[ShockPlayerController.game_end_reason()]

def end_movie():
    if ShockPlayerController.match_scoreboard() and not ShockPlayerController.match_results():
        return "Score: "  + str(PlayerReplicationInfo.player_score()) + " Kills: " + str(PlayerReplicationInfo.player_kills()) + " Streaks: " + str(PlayerReplicationInfo.player_kill_streaks())
    elif ShockPlayerController.match_results():
        total_score = player_total_score()
        player_position = player_ranking()
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


# Double check code
# Finish any final refactorizations
# readme
# Start initial testing.

# Create PyInstaller .bat script for easy .exe creation.
# Test .exe
# Modify readme for Discord Application Instructions
# Begin Intial RPC tests (Non-Anti Cheat)