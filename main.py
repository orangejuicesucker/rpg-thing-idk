import time
import random
for i in range(100):
        print(" ")

print("insert name")
playername = input()
print("loading")
time.sleep(5)
print("type anything to begin")
if input() == "enablecheats":
    print("cheats enabled")
    for i in range(100):
        print(" ")
    print("insert strength")
    strength = input()
    print("insert dexterity")
    dexterity = input()
    print("insert constitution")
    constitution = input()
    print("insert intelligence")
    intelligence = input()
    print("insert wisdom")
    wisdom = input()
    print("insert charisma")
    charisma = input()
    for i in range(100):
        print(" ")
    print("--stats--")
    print("strength =", strength)
    print("dexterity =", dexterity)
    print("constitution =", constitution)
    print("intelligence =", intelligence)
    print("charisma =", charisma)
else:
    for i in range(100):
        print(" ")
    print("--stats--")
    strength = (random.randrange(1, 20, 3))
    print("strength =", strength)
    dexterity = (random.randrange(1, 20, 3))
    print("dexterity =", dexterity)
    constitution = (random.randrange(1, 20, 3))
    print("constitution =", constitution)
    intelligence = (random.randrange(1, 20, 3))
    print("intelligence =", intelligence)
    charisma = (random.randrange(1, 20, 3))
    print("charisma =", charisma)

time.sleep(5)
for i in range(100):
        print(" ")
print("loading...")
def Battle(enemyname: int, ac: int, df: int, at: int):
     for i in range(100):
        print(" ")
     print("--",enemyname,"--")
     print("-",ac,"armor class-", "-",df,"hp-", "-",at,"attack-")
     print("")
     print("-fight- -equiment-")
     if input == "fight":
          print("--",weapon,"--")
          if input == weapon:
               damage = strength + weaponbonusattack
               df = df-damage
               print("")
               print("you attack the enemy dealing",damage," damage!")

time.sleep(5)
for i in range(100):
        print(" ")
print("welcome", playername, "to (UNTITLED RPG 1#)")
print("")
print("--please select a weapon from the list below--")
print("")
print("sword -- +1 damage")
print("sheild -- +1 defense")
weapon = input()
if weapon == "sword":
    weaponbonusattack = 1
    weaponbonusdefense = 0
    print("")
    print("1+ damage!")
elif weapon == "sheild":
     weaponbonusattack = 0
     weaponbonusdefense = 1
     weapon = "fists"
     print("")
     print("+1 defense!")
else:
     print("no weapon selected")
     weaponbonusattack = 0
     weaponbonusdefense = 0
     weapon = "fists"
print("")
print("setup complete! now loading...")
time.sleep(5)
for i in range(100):
        print(" ")
print("--Welcome to (debugworld)--")
print("")
print("you see a path ahead of you, a (test dummy) to your left, and a chest to your right")
print("")
print("--go ahead, go left, go right--")
if input() == "go left":
    Battle("dummy")
    for i in range(100):
        print(" ")
    print("DUMMY APROACHES!")
    time.sleep(2)
    for i in range(100):
        print(" ")
    print("loading")
    time.sleep(2)
    Battle("dummy", 5, 10, 1)
    print("g")