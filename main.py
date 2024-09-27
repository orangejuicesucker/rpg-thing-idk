import time
import random
for i in range(100):
        print(" ")

print("insert name")
playername = input()
cheats = False
invincibility = False
infinitemoney = False
surehit = False
oldhitpoints = 0
oldmoney = 0
print("loading..")
time.sleep(2)
print("type anything to begin")
if input() == "enablecheats" or "debug" or "cheats" or "debugenable" or "cheats enable" or "enabledebug":
    cheats = True
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
    oldhitpoints = healthpoints
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
playermoney = 0
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
               if surehit == False:
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
               else:
                for item in invetoryitems:
                        if item.itemname == weaponusing:
                            weaponbonusattack = item.damage
                        damage = strength + weaponbonusattack
                        df = df-damage
                        print("")
                        print("you attack the enemy dealing",damage," damage!")
                        time.sleep(2)
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
if weapon == "sword" or "swor" or "sw" or "s" or "sord" or "sowr" or "swpr":
    swordBegin = ItemClass("woodensword","attack",1,0)
    print("")
    print("1+ damage!")
elif weapon == "sheild" or "sheil" or "sheld" or "sield" or "shel" or "shelm":
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
 print("you see a path ahead of you, a (test dummy) to your left, a chest to your right, and a ATM behind you")
 print("")
 if cheats == False:
    print("-go ahead- -go backwards- -go left- -go right- -check invetory-")
 else:
    print("-go ahead- -go backwards- -go left- -go right- -check invetory- -debug menu-")
 pathh = input()
 invlist = list()
 if pathh == "check invetory":
     for i in range(100):
         print(" ")
     print("--",playername,"--")
     print("--",healthpoints,"hp--")
     print("--",playermoney,"dabloons--")
     for item in invetoryitems:
        invlistnameadd = item.itemname
        invlist.append(invlistnameadd)
     print(*['-' + item + '- ' for item in invlist])
     time.sleep(2)
 elif pathh == "debug menu":
     if cheats == False:
         print("NO")
     else:
         for i in range(100):
            print(" ")
         print("-debug menu-")
         print("")
         print("-invincibility-","sure-hit","infinitemoney-")
         choice = input()
         if choice == invincibility:
             if invincibility == False:
                healthpoints = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                invincibility = True
                print("inv on")
                time.sleep(1)
             else:
                 healthpoints = oldhitpoints
                 invincibility = False
                 print("inv off")
                 time.sleep(1)
         elif choice == "sure-hit":
             if surehit == False:
                 surehit = True
                 print("surehit on")
                 time.sleep(1)
             else:
                 surehit = False
                 print("surehit off")
                 time.sleep(1)
         elif choice == "infinitemoney":
             if infinitemoney == True:
                 infinitemoney = False
                 playermoney = oldmoney
                 print("infmoney off")
                 time.sleep(1)
             else:
                 print("infmoney on")
                 infinitemoney = True
                 playermoney = 9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
                 time.sleep(1)
 elif pathh == "go left":
     Battle("dummy", 5, 10, 1)
     print("")
     print("you got 1 dabloons!")
     playermoney += 1#
     if infinitemoney == False:
        oldmoney = playermoney#
     time.sleep(3)
 elif pathh == "go right":
  for i in range(100):
         print(" ")
  print("a chest lies ahead of you, would you like to open it?")
  print("-yes- -no-")
  if input() == "yes":
      Loot("testloot","stick","attack",9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999,0)
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
                time.sleep(2)
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
                print("-enemy creator- -weapon creator-")
                choice = input()
                if choice == "enemy creator":
                    print("")
                    print("this costs 3 dabloons")
                    print("-buy- -dont buy-")
                    choice = input()
                    if choice == "buy":
                        if playermoney >= 3:
                            print("obtained enemy creator!")
                            playermoney = playermoney - 3
                            enemycreator = ItemClass("enemy creator","misc","0","0")
                            time.sleep(1)
                        else:
                            print("you broke donkey butt with only", playermoney, "dabloons")
                            time.sleep(1)
                elif choice == "weapon creator":
                    print("")
                    print("this costs 1000 dabloons")
                    print("-buy- -dont buy-")
                    choice = input()
                    if choice == "buy":
                        if playermoney >= 1000:
                            print("obtained weapon creator!")
                            playermoney = playermoney - 3
                            enemycreator = ItemClass("weapon creator","misc","0","0")
                            time.sleep(1)
                        else:
                            print("you broke donkey butt with only", playermoney, "dabloons")
                            time.sleep(1)
 elif pathh == "go backwards":
    print("you go backwards and aproach the ATM")
    time.sleep(1)
    for i in range(100):
        print(" ")
    print("-do you wish to use the ATM-")
    print("")
    print("-yes- -no-")
    choice = input()
    if choice == "yes":
        print("men")





    