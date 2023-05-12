import subprocess
import os
import time
from paths import PATHS
from file_reader import FileReader

round_duration = 2

# # # Start player processes
player1 = subprocess.Popen([PATHS.player_exe, PATHS.map_file, PATHS.status_file, PATHS.commands_file, 
                            str(round_duration)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
player2 = subprocess.Popen([PATHS.player_exe, PATHS.map_file, PATHS.status_file, PATHS.commands_file, 
                            str(round_duration)], stdin=subprocess.PIPE, stdout=subprocess.PIPE)

fr = FileReader()

print("Game will start in 3 seconds..")
for i in range(1):
    print(3-i)
    time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

# # Mediator main loop
for round in range(5):
    print("Player 1 turn...")
    player1.stdin.write(b"start\n")
    player1.stdin.flush()
    
    #Wait for 1st response ()
    player1_response = -1
    while player1_response:
        player1_response = int(player1.stdout.readline().strip().decode())
        time.sleep(0.05)

    # TODO manage responses, write to files and read the commands
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Current map status: \n" + fr.read_map())

    print("Player 2 turn...")
    player2.stdin.write(b"start\n")
    player2.stdin.flush()
    
    #Wait for 2nd response
    player2_response = -1
    while player2_response:
        player2_response = int(player2.stdout.readline().strip().decode())
        time.sleep(0.05)

    os.system('cls' if os.name == 'nt' else 'clear')
    print("Current map status: \n" + fr.read_map())
    
    # Do something with the responses...

# Clean up the processes
player1.terminate()
player2.terminate()
