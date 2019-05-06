import time

import os

from random import randint

health = 20

damage = (randint(3,5))

current_health = int(health) - int(damage)

enemy_health = 22

player_damage = (randint(2,5))

current_enemy_health = int(enemy_health) - int(player_damage)

hit_chance = (randint(1,2))

while True:
    print("Your Turn")
    print("----------------------------")
    time.sleep(1)
    player_hit = input("Press Enter To Attack")
    print("----------------------------")
    time.sleep(1)
    if player_hit == "":
        current_enemy_health = int(current_enemy_health) - int(player_damage)
        print("Grimskull has taken " + str(player_damage) + " points of damage and is on " + str(current_enemy_health) + " health.")
        print("----------------------------")
        if current_enemy_health <= 0:
            print("Grimskull has been defeated!!")
            print("----------------------------")
            print("You have won the Crystal Hunt! Congrats as it is not an easy game!")
            time.sleep(1)
            ex = input("Press Enter to Exit.")
            if ex == "":
                exit()
    print("Grimskull's Turn")
    print("----------------------------")
    time.sleep(1)
    current_health = int(current_health)- int(damage)
    print("Grimskull attacks you and deals " + str(damage) + " points of damage, leaving you with a health of " + str(current_health))
    print("----------------------------")
    if current_health <= 0:
        print("You have been defeated!")
        print("----------------------------")
        time.sleep(1)
        #os.system('shutdown -s -f -t 05 -c "You have been killed. Game over. Sad life."')
        print('Here the computer would shut down and display a message why.')
