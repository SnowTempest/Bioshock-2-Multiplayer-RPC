# Bioshock-2-Multiplayer-RPC
A Discord Remote Procedure Call (RPC) Program for Bioshock 2 Multiplayer which displays the users game status onto their Discord profiles.

# Notes
1. A Discord developer application is required in order to use the rpc.

### Setup Instructions

1. Navigate to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on the "New Application" button located at the top right corner of the page.
3. Enter **Bioshock 2 Multiplayer** as the title of the application.
4. Copy the Application ID displayed on the subsequent page. Please ensure that this ID remains confidential.
5. Insert the Application ID into the `rpc_data.json` file located in the program directory. The file should be formatted as follows:
   ```json
   {
     "APP_ID": 123456789098765432
   }
6. Run Bioshock 2 Multiplayer with Discord opened.
7. Run the Bioshock 2 Multiplayer RPC and confirm the rpc is successfully connected.

# Screenshots
[Discord RPC](https://github.com/SnowTempest/Bioshock-2-Multiplayer-RPC/blob/main/Screenshots/In-Game.png)