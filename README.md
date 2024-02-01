# Bioshock 2 Multiplayer RPC

Bioshock 2 Multiplayer RPC is a python-based application which showcases what the user is doing on Bioshock 2 Multiplayer onto the users Discord profile.

# Setup 
1 - Download the Program under the Releases section of the Github. <br>
2 - Put the Downloaded Program into a New Folder. <br>
3 - Create a Text File named app. Should look like app.txt. <br>
4 - Login into the Discord Developer Portal: https://discord.com/developers/applications <br>
5 - Create a new Application and Name it Bioshock 2 Multiplayer. <br>
6 - Copy the Application ID value located under the General Information Tab. <br>
7 - Put the value into the app.txt file. <br>
8 - The value should look like so: APP_ID="INSERT_APP_ID_HERE". <br>
9 - Save the file and now Open up the program to start the Rich Presence Client. <br>

# Libraries
## Functools
Link - https://docs.python.org/3/library/functools.html
Used with Wrappers to prevent memory crashes and enforce loading before checking values.
## Pathlib
Link - https://docs.python.org/3/library/pathlib.html
Used for better file directory control.
## Psutil
Link - https://pypi.org/project/psutil/
Used for accessing process information.
## Pymem
Link - https://pypi.org/project/Pymem/
Used for accessing Bioshock 2's memory for retrieving current game status information.
## PyPresence
Link - https://github.com/qwertyquerty/pypresence
Used for the Discord Rich Presence Client Connection


# Usage
1 - Open the Program and RPC will start as long as the Discord Application ID is correct and if the game is open. <br>
2 - It will run until Bioshock 2 is closed. <br>
3 - You can close the program at any time by clicking on it and pressing CTRL + C. <br>
