import time
import random
for i in range(100):
        print(" ")

print("insert name")
playername = input()
print("loading..")
time.sleep(2)
print("type anything to begin")
if input() == "enablecheats":
    print("cheats enabled")
    for i in range(100):
        print(" ")
    print("insert health")
    healthpoints = int(input())
    print("insert armor class")
    armorclass = int(input())
    print("insert strength")
    strength = int(input())
    print("insert dexterity")
    dexterity = int(input())
    print("insert constitution")
    constitution = int(input())
    print("insert intelligence")
    intelligence = int(input())
    print("insert wisdom")
    wisdom = int(input())
    print("insert charisma")
    charisma = int(input())

    for i in range(100):
        print(" ")
    print("--stats--")
    print("hp =", healthpoints)
    print("strength =", strength)
    print("dexterity =", dexterity)
    print("constitution =", constitution)
    print("intelligence =", intelligence)
    print("charisma =", charisma)
else:
    for i in range(100):
        print(" ")
    print("--stats--")
    healthpoints = (random.randrange(1, 20))
    print("hp =", healthpoints)
    armorclass = (random.randrange(1, 19))
    print("ac =", armorclass)
    strength = (random.randrange(1, 20))
    print("strength =", strength)
    dexterity = (random.randrange(1, 20))
    print("dexterity =", dexterity)
    constitution = (random.randrange(1, 20))
    print("constitution =", constitution)
    intelligence = (random.randrange(1, 20))
    print("intelligence =", intelligence)
    charisma = (random.randrange(1, 20))
    print("charisma =", charisma)

time.sleep(2)
for i in range(100):
        print(" ")
print("loading...")
firsttime = True    
invetoryitems = list()
class ItemClass: #attack = weapon,, armor = health bonus,, misc = misc,, equiment = food and stuff..
    def __init__(self, itemname, type, damage, armorbonus):
        self.itemname = itemname
        self.type = type
        self.damage = damage
        self.armorbonus = armorbonus
        invetoryitems.append(self)
fists = ItemClass("fists","attack",0,0)
def Battle(enemyname, ac, df, at):
    for i in range(100):
        print(" ")
    print(enemyname," APROACHES!")
    time.sleep(2)
    for i in range(100):
        print(" ")
    print("loading")
    time.sleep(2)
    temphealthpoints = healthpoints
    while df > 0 and temphealthpoints > 0:
     for i in range(100):
        print(" ")
     print("--",enemyname,"--")
     print("-",ac,"armor class-", "-",df,"hp-", "-",at,"attack-")
     print("")
     print("-fight- -equiment-")
     choice = input()
     if choice == "fight":
          invlist = list()
          invlist.clear()
          for item in invetoryitems:
              if item.type == "attack":
                invlistnameadd = item.itemname
                invlist.append(invlistnameadd)
          print(*['-' + item + '- ' for item in invlist])
          weaponusing = input()
          if weaponusing in invlist:
               roll = (random.randrange(1, 20))
               print("rolling...")
               time.sleep(1)
               print(roll,"!")
               if roll >= ac:
                for item in invetoryitems:
                    if item.itemname == weaponusing:
                        weaponbonusattack = item.damage
                damage = strength + weaponbonusattack
                df = df-damage
                print("")
                print("you attack the enemy dealing",damage," damage!")
                time.sleep(2)
               else:
                   print("you missed!")
                   time.sleep(1)
     elif choice == "equiment":    
        invlist = list()
        invlist.clear()
        for item in invetoryitems:
            if item.type == "attack":
                x = 0
            else:
              invlistnameadd = item.itemname
              invlist.append(invlistnameadd)
        print(*['-' + item + '- ' for item in invlist])
        time.sleep(1)
     print("")
     if df > 0:   
      print("DUMMY ATTACKS!")
      roll = (random.randrange(1, 20))
      print("rolling...")
      time.sleep(1)
      print(roll,"!")
      if roll >= armorclass:
            weaponbonusdefense = 0
            for item in invetoryitems:
                    if item.type == "armor":
                        weaponbonusdefense = item.armorbonus
            temphealthpoints = (healthpoints + weaponbonusdefense) - at
            time.sleep(1)
            print("")
            print("dummy deals", (at-weaponbonusdefense), "damage!")
            print("")
            print("you have", temphealthpoints,"hp!")
            time.sleep(2)
      else:
          print(enemyname, "missed!")
          time.sleep(1)
    if temphealthpoints <= 0:      
     print("you lost")
    elif df <= 0:
     print(enemyname," died!")
    time.sleep(2)
def Loot(scriptname, itemname, type, damage, armorbonus):
    scriptname = ItemClass(itemname, type, damage, armorbonus)
    print("you obtained", itemname, "!")    

time.sleep(2)
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
    swordBegin = ItemClass("woodensword","attack",1,0)
    print("")
    print("1+ damage!")
elif weapon == "sheild":
    sheildbegin = ItemClass("woodensheild","armor",0,1)
    print("")
    print("1+ damage!")
    print("")
    print("+1 defense!")
else:
     print("no weapon selected")
print("")
print("setup complete! now loading...")
time.sleep(5)
debugworld = True

while debugworld == True:
 for i in range(100):
         print(" ")
 print("--Welcome to (debugworld)--")
 print("")
 print("you see a path ahead of you, a (test dummy) to your left, and a chest to your right")
 print("")
 print("-go ahead- -go left- -go right- -check invetory-")
 pathh = input()
 invlist = list()
 if pathh == "check invetory":
     for i in range(100):
         print(" ")
     for item in invetoryitems:
        invlistnameadd = item.itemname
        invlist.append(invlistnameadd)
     print(*['-' + item + '- ' for item in invlist])
     time.sleep(2)
 elif pathh == "go left":
     Battle("dummy", 5, 10, 1)
     time.sleep(3)
 elif pathh == "go right":
  for i in range(100):
         print(" ")
  print("a chest lies ahead of you, would you like to open it?")
  print("-yes- -no-")
  if input() == "yes":
      Loot("testloot","stick","attack",9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,0)
      time.sleep(3)
 elif pathh == "go ahead":
   print("")
   print("do you wish to exit (debugworld)?")
   print("-yes- -no-")
   if input() == "yes":
       shop = True
       while shop == True:
            for i in range(100):
             print(" ")
            print("--Welcome to the shop--")
            print("")
            print("there is a old man behind a desk, items are all over the walls")
            print("")
            print("--go ahead, go back--")
            pathh = input()
            if pathh == "go back":
                print("you leave")
                shop = False
            if pathh == "go ahead":
                if firsttime == False:
                    print("welcome back", playername)
                else:
                    firsttime = False
                    print("you aproach the man and he speaks to you")
                    print("")
                    print("shopkeeper: hello there traveler! whats your name? ")
                    time.sleep(2)
                    print("well hello there", playername, "and welcome to my shop")
                time.sleep(2)
                for i in range(100):
                    print(" ")
                print("--shop--")
                print("")
                print("shop not done")
                time.sleep(2)
                shop = False