"""""""""""""""""""""
Author: Blake Davis
File: textBase.py
Date: 11-19-18
Purpose: For fun & learning
"""""""""""""""""""""
import random
import time

class player:
    name = "Player"
    location = "Homer's Home"
    bounty = 0
    health = 1
    insta = 1
    rand = 1
    gold = 0
    xp = 0
    level = 1
    plyHp = 100
    ammo = 0
    weaponDmg = 1
    weapon = "Fist"
    weapons = {}
    armor = "None"
    items = {}
    armorDef = 0
    armors = {}
    armorslvl = {}
    weaponslvl = {}

#Combat Menu

    def InCombat(level,typeMonster):#Player's combat system
        if (typeMonster == "normal"):
            monsterList2 = []
            for x in monsters.monsterList:
                monsterList2.append(x)
            monster = random.choice(monsterList2)
            monsterDmg = level*2
            monsterHp = monsters.monsterList.get(monster)+level

        elif (typeMonster == "legendary"):
            monsterList2 = []
            for x in monsters.legenMonster:
                monsterList2.append(x)
            monster = random.choice(monsterList2)
            monsterDmg = level*2
            monsterHp = monsters.legenMonster.get(monster)+level

        elif (typeMonster == "mini boss"):
            monsterList2 = []
            for x in monsters.minibossMonsters:
                monsterList2.append(x)
            monster = random.choice(monsterList2)
            monsterHp = monsters.minibossMonsters.get(monster)+level
            monsterDmg = level*4+level

        elif (typeMonster == "boss"):
            monsterList2 = []
            for x in monsters.legenMonster:
                monsterList2.append(x)
            monster = random.choice(monsterList2)
            monsterHp = monsters.legenMonster.get(monster)+level
            monsterDmg = level*6+(level % 3)


        while (monsterHp > 0):#Keeps the  player in combat until monster or player is dead
            print("\n=====In Combat=====")
            print("++",str(monster), "Hp =", monsterHp,"--- level = ", level, "++")
            print("+++ Health = ", player.plyHp, "+++")

            print("1 - Attack")
            print("2 - Talk")
            print("3 - Potions")
            option = input("Choose an option: ")

            if (option == str(1) or option.lower() == "attack"):
                monsterHp = monsterHp - player.weaponDmg

                if (monsterHp > 0):
                    print("\nMonster attacks:", monsterDmg, "Dmg")
                    if (player.armorDef == 0):
                        player.plyHp = player.plyHp - monsterDmg
                    else:
                        print("Your armor protected", player.armorDef, "Dmg")
                        if ((monsterDmg - player.armorDef) < 0):
                            print("You took no Dmg!")
                        else:
                            player.plyHp = player.plyHp - (monsterDmg - player.armorDef)

            elif (option == str(2) or option.lower() == "talk"):
                if (monsterHp < monsterHp/2):
                    print("You talked him out of attacking")
                    monsterHp = monsterHp - monsterHP
                else:
                    print("Congrats...your nerdy lisp was interprettated as a threat by the monster.")
            elif (option == str(3) or option.lower() == "potions"):
                        potions = {"Health potion": player.health, "Insta kill": player.insta}

                        print("+++Potions+++")
                        print("1 - Health potion")
                        print("2 - insta kill")
                        option = input("Choose a potion: ")

                        if (option == str(1) or option.lower() == "health potion"):
                            if potions.get("Health potion") > 0:
                                if ((player.plyHp + 25) < 100):
                                    player.plyHp = player.plyHp + 25
                                    print("You healed")
                                    player.health = player.health - 1
                                else:
                                    print("\nYour health is too full.")
                            else:
                                print("\nYou have no health potions.\n")
                        elif (option == str(2) or option.lower() == "insta kill"):
                                if (potions.get("Insta kill") > 0):
                                    monsterHp = monsterHp - monsterHp
                                    player.insta = player.insta - 1
                                else:
                                    print("You have no insta kill potions")
                        else:
                            print("\nNot a valid option..")
            if (player.plyHp < 0):
                break

        if (player.plyHp > 0):
            if (typeMonster == "normal"):
                print("\n" + str(monster), "Sucessfully Killed")
                print("You earned", monsterDmg + 5, "xp")

                player.xp += level + 5

            elif (typeMonster == "legendary"):
                print("\n" + str(monster), "Sucessfully Killed")
                print("You earned", monsterDmg * 3, "xp")

                player.xp += level * 5

            if (level > 5):
                print("You found", level + 2, "Gold")
                player.gold += (level + 2)

#Encounter

class encounter:
    numbers = [1,2,3,4,5,6,7,8,9,10]
    people = ["Trading Troll","Trump","Whinnig Whimp"]
    person = random.choice(people)
    health = random.choice(numbers)
    insta = random.choice(numbers)
    weapons = {"Weiner":69,"Sticky Sword":30,"Toast":50,"Cancer Dagger":500,"Boned Bow":245,"Thorned Blade":100,"Water Trident":85,"Earthy Axe":80,"Rusted Mace":75}
    weaponslvl = {"Cancer Dagger":160,"Toast":45,"Sticky Sword":30,"Weiner":55,"Boned Bow":145,"Thorned Blade":85,"Water Trident":75,"Earthy Axe":65,"Rusted Mace":55}
    armors = {"Assless Chaps":95,"Wet Weeds":80,"Butter":100,"Cancerous Plates":250,"Flesh of the Dead":220,"Spiked":100,"Scale":85,"Blasted Steel":75,"Torn Mail":70}
    armorslvl = {"Cancerous Plates":150,"Butter":45,"Assless Chaps":40,"Wet Weeds":30,"Flesh of the Dead":140,"Spiked":70,"Scale":75,"Blasted Steel":45,"Torn Mail":50}

class traderInv:
    health = 20
    insta = 20
    weapons = {"Great Sword": 5, "The Makers Hammer": 4, "The Anarchist's Battleaxe": 7, "Bongo": 20, "Bong": 420,"Slap Stick":10,"Bear Mace":50}
    weaponslvl = {"Bong":150, "Bongo":16, "The Makers Hammer":2, "The Anarchist's Battleaxe":4, "Great Sword":2,"Slap Stick":8,"Bear Mace":45}
    gold = 200
    armors = {"Leather":3,"Chain Mail":5,"Iron":10,"Developer":150,"Steel":15,"Slave":7,"Guard":12}
    armorslvl = {"Iron":20, "Developer":100, "Chain Mail":3, "Leather":1,"Steel":30,"Slave":5,"Guard":10}


class monsters:
    monsterList = {"Gross Goblin":2, "Troubled Troll":4,"Overweight Ogre":5,"Dumb Donkey":3, "Sticky Shrek":7,"Horny Bear":10}
    legenMonster = {"Teddy Bear(len)": 32, "Wizard(len)": 3, "Beefy Behemoth(len)": 50}
    minibossMonsters = {"Dragon(mini)":250, "Better Version of You(mini)":300,"Three Headed Dog":200}
    bossmonsters = {"Three Headed Dragon(boss)":450}

class game:

    def craftingMenu():
        print("\n1 - Hachet -- lvl = 1")
        print("2 - arrows -- lvl = 1")

        option = input("Choose a weaon to craft: ")

        if (option == str(1)):
            print()
            hachet = {"wood":2,"iron":2,"screw":2}
            for x,y in hachet.items():
                print(y,"-",x)
            option = input("Do you wish to craft? [y/n]: ")

            if (option.lower() == 'y'):
                try:
                    player.items["wood"] = player.items.get("wood") - hachet.get("wood")
                    player.items["iron"] = player.items.get("iron") - hachet.get("iron")
                    player.items["screw"] = player.items.get("screw") - hachet.get("screw")
                    player.weapons["Hachet"] = 4
                    player.weaponslvl["Hachet"] = 1
                    print("You crafted a Hachet. (Its in your inventory)")
                except:
                    print("You don't have the right materials to craft this.")
            else:
                print("\nYou Canceled the craft.")
        elif(option == str(2)):
            print()
            arrow = {"ironn":1,"wood":1}
            for x,y in arrow.items():
                print(y, "--", x)
            option = input("Do you wish to craft? [y/n]: ")

            if (option.lower() == 'y'):
                amount = input("How many?: ")
                try:
                    player.items["wood"] = player.items.get("wood") - int(amount)
                    player.items["iron"] = player.items.get("iron") - int(amount)
                    player.ammo += int(amount)
                    print("\nYou crafted", amount, "arrow(s). (Its in your inventory)")
                except:
                    print("\nYou don't have the right materials to craft this.")
            else:
                print("\nYou Canceled the craft.")


##Encounters interaction Menu

    def encoutersMenu():
        print("\nHi my name is", encounter.person)

        while(True):
            print("\n=====",encounter.person,"Inventory =====")
            print("1 - Weapons")
            print("2 - Potions")
            print("3 - Armor")
            print("4 - Quit")


            option = input("Choose type of item: ")

            if (option == str(1) or option.lower() == "weapons"):
                while(True):
                    print("\n+++++Weapons+++++")
                    i = 0
                    for x,y in sorted(encounter.weapons.items()):
                        print(x, "-", y, "--- lvl Req =", encounter.weaponslvl.get(x))
                        i += 1
                    print(i,"- Quit")

                    option = input("Type a weapon to Purchuse: ")

                    print()

                    if (option in encounter.weapons):
                        print(option, "Cost:", (encounter.weapons.get(option) * 3), "Gold")
                        print("You have:", player.gold, "Gold")
                        buy = input("Would you like to buy this Wepaon[y/n]? ")

                        if (buy.lower() == 'y'):
                            if (player.gold >= (encounter.weapons.get(option)*3)):
                                print("\nThank for buying - ", option)
                                player.gold = player.gold - (encounter.weapons.get(option)*3)
                                player.weapons[option] = encounter.weapons.get(option)
                                player.weaponslvl[option] = encounter.weaponslvl.get(option)
                                del encounter.weapons[option]
                            else:
                                print("\nNot enough gold!")

                        elif (buy.lower() == 'n'):
                            print("\nCome back when your ready to purchase.")

                    elif (option.lower() == "quit" or option == str(i)):
                        break

            elif (option == str(2) or option.lower() == "potions"):
                print("\n+++Potions+++++")
                print("1 - Health --- Amount =", encounter.health)
                print("2 - insta --- Amount =", encounter.insta)
                print("3 - None")
                print("- Quit")

                option = input("Choose a Potion: ")

                if (option == str(1) or option.lower() == "health"):
                    print("\nHealth potion Cost 2 Gold")
                    print("You have:", player.gold, "Gold")
                    buy = input("Would you like to buy this item[y/n]? ")

                    if (buy.lower() == 'y'):
                        amount = input("\nHow many do you want?: ")
                        try:
                            if (player.gold - (2*int(amount)) < 0):
                                print("Not enough Gold!")
                            else:
                                player.gold = player.gold - (2*int(amount))
                                player.health = player.health + int(amount)
                                print("Thank you for buying", int(amount), "Health potion(s)")
                                encounter.health = encounter.health - int(amount)
                        except:
                            print("\nNot valid number!")
                            print()#Aaron creativity
                    else:
                        print("Come back when your ready to spend money")
                elif (option == str(2)):
                    print("insta potion Cost 150 Gold")
                    print("You have:", player.gold, "Gold")
                    buy = input("Would you like to buy this item[y/n]? ")

                    if (buy.lower() == 'y'):
                        amount = input("\nHow many do you want?: ")
                        try:
                            player.gold = player.gold - (150*int(amount))
                            player.insta = player.insta + int(amount)
                            print("Thank you for buying", int(amount), "Insta potion(s)")
                            encounter.insta = encounter.insta - int(amount)
                        except:
                            print("\nNot valid Number!")
                            print()#Aaron creativity
                    else:
                        print("Come back when your ready to spend money")



            elif (option == str(3) or option.lower() == "armor"):
                 while(True):
                    print("\n+++++Armor+++++")
                    i = 0
                    for x,y in sorted(encounter.armors.items()):
                        print(x, "-", y, "--- lvl Req =", encounter.armorslvl.get(x))
                        i += 1
                    print(i, "- Quit")

                    option = input("Type a armor to Purchase: ")

                    print()

                    if (option in encounter.armors):
                        print(option, "Cost:", (encounter.armors.get(option) * 5), "Gold")
                        print("You have:", player.gold, "Gold")
                        buy = input("Would you like to buy this Wepaon[y/n]? ")

                        if (buy.lower() == 'y'):
                            if (player.gold >= (encounter.armors.get(option)*5)):
                                print("\nThank for buying - ", option)
                                player.gold = player.gold - (encounter.armors.get(option)*5)
                                player.armors[option] = encounter.armors.get(option)
                                player.armorslvl[option] = encounter.armorslvl.get(option)
                                del encounter.armors[option]
                            else:
                                print("\nNot enough gold!")
                                print("Someone decided to buy that xbox instead of saving up for actual things...nice job")#Aaron Creative mind

                        elif (buy.lower() == 'n'):
                            print("Look if you don't buy the goods the merchant will have to kill you...the FBI is after his ring")#Aaron Creative mind
                    elif (option.lower() == "quit" or option.lower() == str(i)):
                        break
            elif (option == str(4) or option.lower() == "quit"):
                break


##Trader Menu

    def traderMenu():
        while(True):
            print("\n=====Trader Inventory=====")
            print("1 - Weapons")
            print("2 - Potions")
            print("3 - Armor")
            print("4 - Quit")


            option = input("Choose type of item: ")

            if (option == str(1) or option.lower() == "weapons"):
                while(True):
                    print("\n+++++Weapons+++++")
                    i = 0
                    for x,y in sorted(traderInv.weapons.items()):
                        print(x, "-", y, "--- lvl Req =", traderInv.weaponslvl.get(x))
                        i += 1
                    print(i,"- Quit")

                    option = input("Type a weapon to Purchase: ")

                    print()

                    if (option in traderInv.weapons):
                        print(option, "Cost:", (traderInv.weapons.get(option) + 5), "Gold")
                        print("You have:", player.gold, "Gold")
                        buy = input("Would you like to buy this Wepaon[y/n]? ")

                        if (buy.lower() == 'y'):
                            if (player.gold >= (traderInv.weapons.get(option)+5)):
                                print("\nThank for buying - ", option)
                                player.gold = player.gold - (traderInv.weapons.get(option)+5)
                                player.weapons[option] = traderInv.weapons.get(option)
                                player.weaponslvl[option] = traderInv.weaponslvl.get(option)
                                del traderInv.weapons[option]
                            else:
                                print("\nNot enough gold!")

                        elif (buy.lower() == 'n'):
                            print("\nCome back when your ready to purchase.")
                    elif (option.lower() == "quit" or option == str(i)):
                        break

            elif (option == str(2) or option.lower() == "potions"):
                print("\n+++Potions+++++")
                print("1 - Health ---", traderInv.health)
                print("2 - insta ---", traderInv.insta)
                print("3 - None")

                option = input("Choose a Potion: ")

                if (option == str(1) or option.lower() == "health"):
                    print("\nHealth potion Cost 2 Gold")
                    print("You have:", player.gold, "Gold")
                    buy = input("Would you like to buy this item[y/n]? ")

                    if (buy.lower() == 'y'):
                        amount = input("\nHow many do you want?: ")
                        if (int(amount) > traderInv.health):
                            print("\nNot enough in stock!")
                        else:
                            try:
                                if (player.gold - (2*int(amount)) < 0):
                                    print("\nNot enough Gold!")
                                else:
                                    player.gold = player.gold - (2*int(amount))
                                    player.health = player.health + int(amount)
                                    print("\nThank you for buying", int(amount), "Health potion(s)")
                                    traderInv.health = traderInv.health - int(amount)
                            except:
                                print("\nNot valid number!")
                                print()#Aaron creativity
                    elif (buy.lower() == 'n'):
                        print("\nCome back when your ready to spend money")
                    else:
                        print("\nNot a valid option")
                elif (option == str(2)):
                    print("\ninsta potion Cost 150 Gold")
                    print("You have:", player.gold, "Gold")
                    buy = input("Would you like to buy this item[y/n]? ")

                    if (buy.lower() == 'y'):
                        amount = input("\nHow many do you want?: ")
                        try:
                            player.gold = player.gold - (150*int(amount))
                            player.insta = player.insta + int(amount)
                            print("Thank you for buying", int(amount), "Insta potion(s)")
                            traderInv.insta = traderInv.insta - int(amount)
                        except:
                            print("\nNot valid Number!")
                            print()#Aaron creativity
                    elif (buy.lower() == 'n'):
                        print("Come back when your ready to spend money")
                    else:
                        print("\nNot a valid option")


            elif (option == str(3) or option.lower() == "armor"):
                 while(True):
                    print("\n+++++Armor+++++")
                    i = 0
                    for x,y in sorted(traderInv.armors.items()):
                        print(x, "-", y, "--- lvl Req =", traderInv.armorslvl.get(x))
                        i += 1
                    print(i, "- Quit")

                    option = input("Type a armor to Purchase: ")

                    print()

                    if (option in traderInv.armors):
                        print(option, "Cost:", (traderInv.armors.get(option) * 5), "Gold")
                        print("You have:", player.gold, "Gold")
                        buy = input("Would you like to buy this Armor[y/n]? ")

                        if (buy.lower() == 'y'):
                            if (player.gold >= (traderInv.armors.get(option)*5)):
                                print("\nThank for buying - ", option)
                                player.gold = player.gold - (traderInv.armors.get(option)*5)
                                player.armors[option] = traderInv.armors.get(option)
                                player.armorslvl[option] = traderInv.armorslvl.get(option)
                                del traderInv.armors[option]
                            else:
                                print("\nNot enough gold!")
                                print()#Aaron Creative mind

                        elif (buy.lower() == 'n'):
                            print("")#Aaron Creative mind
                    elif (option.lower() == "quit" or option.lower() == str(i)):
                        break
            elif (option == str(4) or option.lower() == "quit"):
                break

##Armor menu

    def Armors():
        print("\n++Armors++")

        while(True):
            i = 0
            for x,y in sorted(player.armors.items()):
                print(x, "-", y, "--- lvl Req =", player.armorslvl.get(x))
                i += 1
            print("quit")

            print("\nArmor equipped:", player.armor, "-", player.armorDef)
            option = input("Type a Armor: ")

            if (option == player.armor):
                print("\nAlready equipped")
            try:
                if (player.armorslvl.get(option) > player.level):
                    print("You need to be a level",player.armorslvl.get(option))
            except:

                if (option == "quit"):
                    break

                else:
                    print("\nInvalid choice, how about you actually be smart and know what weapon you wont struggle to use....oh wait....thats all of them...get a life nurd\n")


##Weapons Menu

    def weapons():
        print("\n++Weapons++")

        while(True):
            i = 0
            for x,y in sorted(player.weapons.items()):
                print(x, "-", y, "--- lvl =", player.weaponslvl.get(x))
                i += 1
            print(i, "- Quit")


            print("\nWeapon equipped:", player.weapon, "-", player.weaponDmg)
            option = input("Type a Weapon: ")

            try:
                if (option.lower() == player.weapon.lower()):
                    print("\nYou already have that weapon equipped....you're almost as dumb as Keaton -An actual midget.")
            finally:
                if (int(player.weaponslvl.get(option)) > player.level):
                    print("\nYou need to be a level",player.weaopnslvl.get(option))
                    print("Hey bud...you know that planet fitness card you got for your birthday? Go use it.")#Aaron creativity

            if (option in player.weapons):
                print("\nYou equipped", option)
                player.weapon = option
                player.weaponDmg = player.weapons.get(option)
                break

            if (option.lower() == "quit" or option == str(i)):
                break
            else:
                print("\nInvalid choice, how about you actually be smart and know what weapon you won't struggle to use....oh wait....that's all of them...get a life nurd\n")

##Travel Menu

    def fastTravel(choice):
        places = ["Homer's Home","Cancer City","Sticky Swamp","Toaster Tower","Gay Central","Dead Man's Hollow","Vined Forest","The Deep","The Blasted Lands","Ancient Castle"]


        while(True):
            print("\n++++++++++++")
            for i in range(len(places)):
                print((i+1), "-", places[i])

            location = input("Choose a loction: ")

            if (location == player.location):
                print("\nYou are already there!")
            elif (location != player.location):
                try:
                    player.location = places[int(location)-1]
                except:
                    player.location = location

                if (choice > 10 and choice < 20):
                    if (choice > 17 and player.level > 35):
                        print("\nYou ran into a legendary monster")
                        player.InCombat((choice*2),"legendary")#Player goes to combat menu
                        break

                    elif(choice > 17 or player.level < 25):
                        player.InCombat((choice - 10),"normal")
                        break

                elif (choice <= 6 and choice >= 1):
                    option = input("\nYou found a trader would you like to interact[y/n]?")
                    if (option.lower() == 'y'):
                        encoutersMenu()
                        break
                    else:
                        print("\nYou safely made it to", player.location)
                        break

                elif (choice >= 1 and choice <= 10):
                    print("\nYou found a health potion!")
                    player.health += 1
                    if (choice == 10):
                        print("\nYou found a insta potion!")
                        player.insta += 1
                        print("\nYou made it safely to", player.location)
                        break
                    print("\nYou made it safely to", player,location)
                    break
                elif (choice == 20):
                    player.InCombat(choice,"mini boss")


##Cheats Menu

    def developer():
        while(True):
            print("\n+++++++++")
            print("1 - Set level")
            print("2 - Set Dmg")
            print("3 - Set MonsterDmg")
            print("4 - Location")
            print("5 - Set player's Xp")
            print("6 - Set gold amount")
            print("7 - Set Health potion amount")
            print("8 - Set Insta potion amount")
            print("9 - Set Armor Deffence")
            print("10 - Quit")
            print("+++++++++")

            option = input("\nEnter: ")

            if (option == str(1)):
                setlvl = input("\nEnter level: ")
                player.level = int(setlvl)
            elif (option == str(2)):
                setDmg = input("\nEnter Dmg: ")
                player.weaponDmg = int(setDmg)
            elif (option == str(3)):
                setMonsterDmg = input("Enter Enemy Dmg: ")
            elif (option == str(4)):
                print("Player is at:", player.location)
            elif (option == str(5)):
                setXp = input("Enter Xp amount: ")
                player.xp = int(setXp)
            elif (option == str(6)):
                setGold = input("Enter Gold amount: ")
                player.gold += int(setGold)
            elif (option == str(7)):
                setHealth = input("Enter Health potion amount: ")
                player.plyHp = amount
            elif (option == str(8)):
                setInsta = input("Enter Insta potion amount: ")
                player.insta += int(setInsta)
            elif (option == str(9)):
                setarmor = input("Enter Armor rating: ")
                player.armorDef = int(setarmor)
            else:
                break

##Arena

    def arena(level):
        print("\n+++++Arena+++++")
        print("Easy")
        print("Normal")
        print("Hard")
        print("Legendary")
        print("Mini Boss")

        option = input("Type a difficulty: ")

        if (option.lower() == "easy"):
            player.InCombat(level,"normal")
        elif (option.lower() == "normal"):
            player.InCombat(level + 35,"normal")
        elif (option.lower() == "hard"):
            player.InCombat(level + 45,"normal")
        elif (option.lower() == "legendary"):
            player.InCombat(level + 120,"legendary")
        elif (option.lower() == "mini boss"):
            player.InCombat((level*5),"mini boss")
        else:
            print("Not valid difficulty, try again")

##Player Stats

    def playerStats():
        print("\n++++++Stats++++++")
        print("Weapon:", player.weapon)
        print("weapon Damge:", player.weaponDmg)
        print("Gold:", player.gold)
        print("Total xp:", player.xp)
        print("level:", player.level)
        print("Heatlh potions:", player.health)
        print("Insta potions:", player.insta)
        print("+++++++++++++++++")


##Main Game

    intro = "This game will contain vulgar jokes, and offensive memeage. If you are a whiny bitch, and can't take jokes, don't play this game. If you get offended, please don't rant about us on 4chan or Reddit, and don't leave a bad yelp review, cause we will find you, and we will kill you (were just kidding Mr FBI Man) You have been warned.\n\nHey. Hey you. Are you some rebellious kale loving millennial or some shit. Well...unfortunately you've clicked, and are now running this game..... I guess welcome to the game..... you shouldve quit. To bad you cant now..... strap in and strap on, this shit is gonna get intense. Before we begin, we must go over some safety precautions: \n1) Always have a toilet on standby \n2) Along with that, have Toilet paper, and a plunger on standby. \n3) Have water for the required spit takes. \n4) Have fun.....or dont, im not your father.\n\nThat said, enjoy.\n\n"
    print(intro)
    for i in intro:
        print(i, end = "")
        time.sleep(0.09)


    print("\n*****Type the number next to the option*****")
    print("*****Unless choosing a weapon type that weapon*****")

    backStory = "\n\nStory:\nYour walking on path and come across a dead body"

    for i in backStory:
        print(i, end = "")
        time.sleep(0.09)

    option = input("Do you wish to loot it?[y/n] ")

    if (option.lower() == 'y' or option.lower() == 'yes'):
        print("\nYou found 20 Gold")
        player.gold += 20
        backStory = "\nStory:\n(*Guard approches*) Gaurd: You there what's your name?"
        for i in backStory:
            print(i, end = "")
            time.sleep(0.09)
        option = input("Enter your name: ")
        player.name = option
        backStory = "\nStory:\nGuard: Well, looks like you'll be coming with me."
        for i in backStory:
            print(i, end = "")
            time.sleep(0.09)
        option = input("\nwill you go with the Gaurd? [y/n]: ")
        if (option.lower() == 'y' or option.lower() == 'yes'):
            backStory = "\nStory:\nGuard: Good, glad I don't have to chase you."
            for i in backStory:
                print(i, end = "")
                time.sleep(0.09)
            print("\nYou are able to kill the Gaurd.")
            option = input("Do you wish to do so? [y/n]: ")
            if (option.lower() == 'y' or option.lower() == 'yes'):
                backStory = "\nStory:\n(*You killed the Guard and found:*)"
                for i in backStory:
                    print(i, end = "")
                    time.sleep(0.09)
                print("\n15 Gold")
                player.gold += 15
                print("Sword - 3 --- lvl 1")
                player.weapons["Sword"] = 3
                player.weaponslvl["Sword"] = 1
                player.bounty += 20
                print()
            elif (option.lower() == 'n' or option.lower() == 'no'):
                backStory = "\nStory:\nGuard: You know what", player.name, ", Ill let you go  you seem like a harmless fellow here's a dagger and some crafting items, your free to go."
                for i in backStory:
                    print(i, end = "")
                    time.sleep(0.09)
                player.weapons["Dagger"] = 5
                player.weaponslvl["Dagger"] = 1
                print("\nYou now have a dagger in weaopns menu.")
                print("As well as:")
                print("3 - Wood")
                player.items["wood"] = 3
                print("4 - Iron ingots")
                player.items["iron"] = 4
                print("4 - Screws")
                player.items["screw"] = 4
        elif (option.lower() == 'n' or option.lower() == 'no'):
            backStory = "\nStory:\nYou ran off before the Guard was able to catch you, (whimp), you did mange to loot a cheat and found craftable items.\n"
            for i in backStory:
                print(i, end = "")
                time.sleep(0.09)
            print("found:")
            print("3 - wood")
            player.items["wood"] = 3
            print("4 - iron")
            player.items["iron"] = 4
            print("4 - screws")
            player.items["screw"] = 4
    if (option.lower() == 'n' or option.lower() == 'no'):
        backStory = "\nStory:\nYou continue to walk and you found a chest with craftable items.\n"
        for i in backStory:
            print(i, end = "")
            time.sleep(0.09)
        print("found:")
        print("3 - wood")
        player.items["wood"] = 3
        print("4 - iron")
        player.items["iron"] = 4
        print("4 - screws")
        player.items["screw"] = 4

        name = input("\nEnter your name: ")
        player.name = name

    while(player.plyHp > 0):
        numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        choice = random.choice(numbers)

        while (player.level * 7 < player.xp):
            if (player.xp > player.level*7):
                player.level += 1

                
##Main Menu Interations


        print("\n=====Menu=====")
        print("+++",player.name,"+++")
        print("+++",player.plyHp,"+++")
        print("1 - Choose a weapon")
        print("2 - Choose Armor")
        print("3 - Fast Travel")
        print("4 - Player's Stats")
        print("5 - Developer Cheats")
        print("6 - Trade with Vender")
        print("7 - Arena")
        print("8 - Use a health potion")
        print("9 - Craftable Items Inventory")
        print("10 - Craft Items")
        print("11 - Pay Bounty")
        print("12 - Credits")
        print("======Bounty======")
        print("+++",player.bounty,"+++")


        action = input("Choose an action: ")

        if (action == str(1) or action.lower() == "choose a weapon"):
            weapons()
        elif (action == str(2) or action.lower() == "choose armor"):
            Armors()

        elif (action == str(3) or action.lower() == "fast travel"):
            fastTravel(choice)

        elif (action == str(4) or action.lower() == "player's stats"):
            playerStats()

        elif (action == str(5) or action.lower() == "developer cheats"):
            code = "123691852"
            inputCode = input("Enter Code: ")
            if (code == inputCode):
                developer()
            else:
                print("\nTrying to hack the mainframe I see...well nice try Snowden, you ain't getting into clintons emails this time.")

        elif (action == str(6) or action.lower() == "trade with vender"):
            traderMenu()

        elif (action == str(7) or action.lower() == "arena"):
            arena(choice)

        elif (action == str(8) or action.lower() == "use a health potion"):
            if ((player.plyHp + 25) > 100):
                print("\nYour health is to full")
            else:
                print("\nYou healed")
                player.plyHp = player.plyHp + 25
                player.health -= 1

        elif (action == str(9) or action.lower() == "craftable items"):
            try:
                print("\nCraftable Items:")
                for x,y in player.items.items():
                    print(y, "--", x)
            except:
                print("\nYou have no craftable items")

        elif (action == str(10) or action.lower() == "craft items"):
            craftingMenu()

        elif (action == str(11) or action.lower() == "pay bounty"):
            option = input("Are yo usure you wat to pay bounty its", player.bounty, "Gold?[y/n]: ")

            if (option.lower() == 'y'):
                if ((player.gold - player.bounty) >= 0):
                    print("\nYou payed your bounty")
                    player.gold -= player.bounty
                    player.bounty = 0
                else:
                    print("\nNot enough Gold to pay bounty.")
            elif(option.lower() == 'n'):
                print("\nYou canceled paying bounty.")
            else:
                print("\nInvalid option type 'y' or 'n' next time.")

        elif (action == str(12) or action.lower() == "credits"):
            creds = "\nBlake Davis “The Nerd” - Lead Developer/Project Manager\nAaron Smith “The Anarchist” - Lead Creative/Support Developer\nKeaton Pedersen “The Insulter” - Lead Storywriter/Support Creative\n"
            for i in creds:
                print(i, end = "")
                time.sleep(0.09)

    print("\n*****You Died*****")
    playerStats()
