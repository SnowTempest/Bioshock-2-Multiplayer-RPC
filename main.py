__author__ = "SnowTempest"
__copyright__ = "Copyright (C) 2024 SnowTempest"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__= "1.02"

from bioshock_2_multiplayer_rpc import rpc_loop, rpc_test_error

def main():
    print("*****************************************************************************")
    print(" \nBioshock 2 Multiplayer Discord RPC by SnowTempest (ADTempest on YT/Twitch)\n")
    print(" \nRPC Version 1.02")
    print("*****************************************************************************")
    rpc_loop()

# Safe Function Calling.
if __name__ == "__main__":
    main()
