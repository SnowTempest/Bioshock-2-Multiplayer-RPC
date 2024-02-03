# Bioshock 2 Multiplayer Discord Rich Presence

## Overview

Bioshock 2 Multiplayer Discord Rich Presence (RPC) is a Python-based application that seamlessly integrates Bioshock 2 Multiplayer gameplay information into the user's Discord profile through the Discord Rich Presence feature.

## Setup

1. **Download:** Obtain the program from the "Releases" section on the [GitHub repository](https://github.com/SnowTempest/Bioshock-2-Multiplayer-RPC/releases).
2. **Folder Placement:** Place the downloaded program into a new folder or any folder that you'll remember.
3. **Configuration File:** Create a text file named `app.txt`.
4. **Discord Developer Portal:** Log in to the [Discord Developer Portal](https://discord.com/developers/applications).
5. **Create Application:** Generate a new application named "Bioshock 2 Multiplayer."
6. **Application ID:** Copy the Application ID from the "General Information" tab in the Discord Developer Portal.
7. **Configuration File Update:** Paste the copied Application ID into the `app.txt` file in the format `APP_ID="INSERT_APP_ID_HERE"`.
8. **Save:** Save the `app.txt` file.
9. **Launch:** Open the program to initiate the Rich Presence client.

## Libraries

### 1. Functools

- [Documentation](https://docs.python.org/3/library/functools.html)
- Utilized with wrappers to mitigate memory crashes and enforce loading before checking values.

### 2. Pathlib

- [Documentation](https://docs.python.org/3/library/pathlib.html)
- Facilitates improved control over file directories.

### 3. Psutil

- [Documentation](https://pypi.org/project/psutil/)
- Enables access to process information for enhanced functionality.

### 4. Pymem

- [Documentation](https://pypi.org/project/Pymem/)
- Facilitates access to Bioshock 2's memory, retrieving current game status information.

### 5. PyPresence

- [GitHub Repository](https://github.com/qwertyquerty/pypresence)
- Facilitates the connection to the Discord Rich Presence client.

## Usage

1. **Initialization:** Open the program to initiate the Rich Presence client, ensuring the correct Discord Application ID is configured and Bioshock 2 is running.
2. **Runtime:** The program will run continuously until Bioshock 2 is closed.
3. **Termination:** Close the program at any time by clicking on it and pressing `CTRL + C`.

## License

This project is licensed under the [GNU PUBLIC LICENSE](LICENSE).
