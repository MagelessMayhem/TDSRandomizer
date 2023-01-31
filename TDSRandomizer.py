from random import choice, randint
from time import sleep
import os
try:
	print("Attempting to import termcolor.")
	sleep(1)
	from termcolor import cprint
except ModuleNotFoundError:
	print("Unable to find the termcolor module.\n\nOn Linux, this can be provided by python3-termcolor, python-termcolor, dev-python/termcolor, etc. If your package manager does not provide it, install the module using pip.\n\nContrarily, if you are using macOS or Windows, you'll need to use pip.")
	sleep(5)
	print("I will now attempt to install it for you.")
	sleep(1)
	os.system("python -m pip install termcolor")
	sleep(1)
	from termcolor import cprint

print("We have termcolor, proceeding...")
sleep(1)
baseTowers = ["Farm","Commander","DJ Booth","Soldier","Freezer","Demoman","Paintballer","Pyromancer","Militant","Ace Pilot","Shotgunner","Rocketeer","Medic","Minigunner","Hunter","Military Base","Ranger","Electroshocker"
]
def TowerHandler(arr):
	owned = []
	cprint("I will now ask you about owning each tower in the specified list. Simply answer yes (or y) or no (or n).", "green", attrs=["bold"])
	sleep(2)
	if "Commander" in arr:
		cprint("\nAutomatically adding the starter towers.", "light_magenta", attrs=["bold"])
		sleep(1)
		owned.append("Scout")
		owned.append("Sniper")
	
	for tower in arr:
		cprint("\nDo you have", "green", attrs=["bold"], end=" ")
		cprint(tower, "blue", attrs=["bold"], end="")
		cprint("? [y/n]", "green", attrs=["bold"], end=" ")
		promptif = input()
		if promptif == "y" or promptif == "yes":
			sleep(0.25)
			owned.append(tower)
			cprint("\n" + tower, "blue", attrs=["bold"], end=" ")
			cprint("has been included in the local pool.", "green", attrs=["bold"])
		elif promptif == "n" or promptif == "no":
			sleep(0.25)
			cprint("\nOK. I'll omit", "green", attrs=["bold"], end=" ")
			cprint(tower, "blue", attrs=["bold"], end=" ")
			cprint("from the pool.", "green", attrs=["bold"])
		else:
			raise ValueError("Invalid input given.")
	
	cprint("\nWe're now done. Your custom pool with be used later on.", "green", attrs=["bold"])
	sleep(0.5)
	return owned
	
hardcoreTowers = ["Accelerator", "Engineer"]
levelTowers = ["Crook Boss", "Turret", "Mortar", "Pursuit"]
mapTowers = ["Cowboy", "Warden"]
eventTowers = ["Gladiator", "Commando", "Slasher", "Archer", "Frost Blaster", "Swarmer", "Toxic Gunner", "Sledger", "Executioner", "Elf Camp"]
goldenTowers = ["Scout", "Soldier", "Pyromancer", "Cowboy", "Minigunner", "Crook Boss"]
loadout = []
cprint("\n\nTDS Randomizer v2.0 - Written by MagelessMayhem (Thymestl)\n\nPlease wait...\n\n", "cyan", attrs=["bold"])
sleep(2)
if os.path.isfile("customlist.txt"):
	cprint("Welcome! What would you like to do?", "cyan", attrs=["bold"], end="\n\n")
	cprint("1.", "green", attrs=["bold"], end=" ")
	cprint("Randomize a loadout from scratch", "blue", attrs=["bold"], end="\n")
	cprint("2.", "green", attrs=["bold"], end=" ")
	cprint("Use an existing list for loadout randomization (customlist.txt)", "blue", attrs=["bold"], end="\n\n")
	cprint("Please select an option:", "cyan", attrs=["bold"], end=" ")
	promptfile = int(input())
	if promptfile == 1:
		cprint("OK, proceeding normally.", "green", attrs=["bold"])
		sleep(1)
	elif promptfile == 2:
		cprint("OK, I'll use your list for customization.", "green", attrs=["bold"])
		sleep(1)
		list = open("customlist.txt", "r")
		#Define variables early
		customBase = []
		for line in list.readlines():
			customBase.append(line.strip("\n"))
		
		if "Farm" in customBase:
			cprint("\nYou had chosen Farm during the base tower phase of configuration. Should it be automatically included in the final loadout? This will help fund any offensive towers the randomizer generates. [y/n]", "cyan", attrs=["bold"], end=" ")
			promptfarm = input()
			if promptfarm == "y" or promptfarm == "yes":
				cprint("\nOK. Farm will be generated in slot 1.", "green", attrs=["bold"])
				sleep(0.5)
				loadout.append("Farm")
				customBase.remove("Farm")
			else:
				cprint("\nOK. I'll proceed normally.", "green", attrs=["bold"])
				sleep(0.5)
		
		cprint("\nNow randomizing, please wait...", "light_magenta", attrs=["bold"])
		sleep(3)
		fileData = customBase
		if len(loadout) < 1:
			for i in range(0, 5):
				# Generate normally
				selection = choice(customBase)
				loadout.append(selection)
				customBase.remove(selection)
		else:
			for i in range(0, 4):
				selection = choice(customBase)
				loadout.append(selection)
				customBase.remove(selection)
					
						
		cprint("\nThe loadout has successfully been generated:", "cyan", attrs=["bold"], end="\n\n")
		cprint("1:", "green", attrs=["bold"], end=" ")
		cprint(loadout[0], "blue", attrs=["bold"], end="\n")
		cprint("2:", "green", attrs=["bold"], end=" ")
		cprint(loadout[1], "blue", attrs=["bold"], end="\n")
		cprint("3:", "green", attrs=["bold"], end=" ")
		cprint(loadout[2], "blue", attrs=["bold"], end="\n")
		cprint("4:", "green", attrs=["bold"], end=" ")
		cprint(loadout[3], "blue", attrs=["bold"], end="\n")
		cprint("5:", "green", attrs=["bold"], end=" ")
		cprint(loadout[4], "blue", attrs=["bold"], end="\n\n")
		
		cprint("TDSRandomizer will now exit. Have fun!", "cyan", attrs=["bold"])
		sleep(1)
		os._exit(0)
		
cprint("First, I need to know what base towers you have.", "cyan", attrs=["bold"])
sleep(1)
customBase = TowerHandler(baseTowers)
cprint("\nNow, do you have either of the hardcore towers? [y/n]", "cyan", attrs=["bold"], end=" ")
prompthc = input()
if prompthc == "y" or prompthc == "yes":
	cprint("\nDo you have", "green", attrs=["bold"], end=" ")
	cprint("Accelerator", "blue", attrs=["bold"], end="")
	cprint("? [y/n]", "green", attrs=["bold"], end=" ")
	prompt1 = input()
	if prompt1 == "y" or prompt1 == "yes":
		sleep(0.25)
		cprint("\nOK, I'll append it to your list.", "green", attrs=["bold"])
		customBase.append("Accelerator")
	elif prompt1 == "n" or prompt1 == "no":
		sleep(0.25),
		cprint("\nOK, I'll omit it from your list.", "green", attrs=["bold"])
	else:
		raise ValueError("Invalid input given.")
	cprint("\nDo you have", "green", attrs=["bold"], end=" ")
	cprint("Engineer", "blue", attrs=["bold"], end="")
	cprint("? [y/n]", "green", attrs=["bold"], end=" ")
	prompt1 = input()
	if prompt1 == "y" or prompt1 == "yes":
		sleep(0.25)
		cprint("\nOK, I'll append it to your list.", "green", attrs=["bold"])
		customBase.append("Engineer")
	elif prompt1 == "n" or prompt1 == "no":
		sleep(0.25),
		cprint("\nOK, I'll omit it from your list.", "green", attrs=["bold"])
	else:
		raise ValueError("Invalid input given.")

else:
	# Continue normally
	sleep(0.5)
	cprint("\nOK, you won't be asked about them.", "green", attrs=["bold"])
	sleep(0.5)
	
cprint("\nDo you have either of the map towers? [y/n]", "cyan", attrs=["bold"], end=" ")
promptm = input()
if promptm == "y" or promptm == "yes":
	cprint("\nDo you have", "green", attrs=["bold"], end=" ")
	cprint("Cowboy", "blue", attrs=["bold"], end="")
	cprint("? [y/n]", "green", attrs=["bold"], end=" ")
	prompt1 = input()
	if prompt1 == "y" or prompt1 == "yes":
		sleep(0.25)
		cprint("\nOK, I'll append it to your list.", "green", attrs=["bold"])
		customBase.append("Cowboy")
	elif prompt1 == "n" or prompt1 == "no":
		sleep(0.25),
		cprint("\nOK, I'll omit it from your list.", "green", attrs=["bold"])
	else:
		raise ValueError("Invalid input given.")
	cprint("\nDo you have", "green", attrs=["bold"], end=" ")
	cprint("Warden", "blue", attrs=["bold"], end="")
	cprint("? [y/n]", "green", attrs=["bold"], end=" ")
	prompt1 = input()
	if prompt1 == "y" or prompt1 == "yes":
		sleep(0.25)
		cprint("\nOK, I'll append it to your list.", "green", attrs=["bold"])
		customBase.append("Warden")
	elif prompt1 == "n" or prompt1 == "no":
		sleep(0.25),
		cprint("\nOK, I'll omit it from your list.", "green", attrs=["bold"])
	else:
		raise ValueError("Invalid input given.")

else:
	# Continue normally
	sleep(0.5)
	cprint("\nOK, you won't be asked about them.", "green", attrs=["bold"])
	sleep(0.5)
	
cprint("\nWhat is your level in TDS?", "cyan", attrs=["bold"], end=" ")
intprompt = int(input())
if intprompt >= 30 and intprompt < 50:
	cprint("\nOK, you should at least have", "green", attrs=["bold"], end=" ")
	cprint("Crook Boss", "blue", attrs=["bold"], end="")
	cprint(". I'll add it to your list.", "green", attrs=["bold"])
	customBase.append("Crook Boss")
	sleep(0.5)
elif intprompt >= 50 and intprompt < 75:
	cprint("\nOK, you should at least have", "green", attrs=["bold"], end=" ")
	cprint("Crook Boss", "blue", attrs=["bold"], end=" ")
	cprint("and", "green", attrs=["bold"], end=" ")
	cprint("Turret", "blue", attrs=["bold"], end="")
	cprint(". I'll add them to your list.", "green", attrs=["bold"])
	customBase.append("Crook Boss")
	customBase.append("Turret")
	sleep(0.5)
elif intprompt >= 75 and intprompt < 100:
	cprint("\nOK, you should at least have", "green", attrs=["bold"], end=" ")
	cprint("Crook Boss", "blue", attrs=["bold"], end="")
	cprint(",", "green", attrs=["bold"], end=" ")
	cprint("Turret", "blue", attrs=["bold"], end="")
	cprint(", and", "green", attrs=["bold"], end=" ")
	cprint("Mortar", "blue", attrs=["bold"], end="")
	cprint(". I'll add them to your list.", "green", attrs=["bold"])
	customBase.append("Crook Boss")
	customBase.append("Turret")
	customBase.append("Mortar")
	sleep(0.5)
elif intprompt >= 100:
	cprint("\nOK, you should have all of the level towers. I'll add them to your list.", "green", attrs=["bold"])
	customBase.append("Crook Boss")
	customBase.append("Turret")
	customBase.append("Mortar")
	customBase.append("Pursuit")
	sleep(0.5)
else:
	cprint("\nHmm, you don't seem to have any level towers. You might have bought them via gamepass; you may specify this next.", "green", attrs=["bold"])

if intprompt < 100:
	cprint("\nDid you buy any of the level towers via gamepass (and are not currently the appropriate level to obtain them freely)? [y/n]", "green", attrs=["bold"], end=" ")
	promptlv = input()
	if promptlv == "y" or promptlv == "yes":
		cprint("\nOK. You'll be redirected to the handler to enter the towers you have bought. If you already own the towers via level, you may simply answer no to the appropriate questions.", "green", attrs=["bold"])
		sleep(1)
		GPlist = TowerHandler(levelTowers)
		customBase = customBase + GPlist
		
	else:
		cprint("\nOK, you won't be asked about them.", "green", attrs=["bold"])
		sleep(0.5)
		
cprint("\nDo you have any event towers? [y/n]", "cyan", attrs=["bold"], end=" ")
promptev = input()
if promptev == "y" or promptev == "yes":
	cprint("\nOK, you'll be redirected to the handler.", "green", attrs=["bold"])
	sleep(1)
	customEvent = TowerHandler(eventTowers)
	customBase = customBase + customEvent
else:
	cprint("\nOK, you won't be asked about them.", "green", attrs=["bold"])
	sleep(0.5)

goldenIndependent = True
canUseGolden = False
cprint("\nDo you have any", "cyan", attrs=["bold"], end=" ")
cprint("golden perks", "yellow", attrs=["bold", "dark"], end="")
cprint("? [y/n]", "cyan", attrs=["bold"], end=" ")
promptg = input()
customGolden = None
if promptg == "y" or promptg == "yes":
	canUseGolden = True
	cprint("\nOK, you'll be redirected to the handler. You should answer each question based on whether you have the golden perk for that tower unlocked.", "green", attrs=["bold"])
	sleep(1)
	customGolden = TowerHandler(goldenTowers)
	cprint("\nHow would you like to handle the randomization of golden perks?\n\n", "green", attrs=["bold"])
	cprint("1.", "cyan", attrs=["bold"], end=" ")
	cprint("Use them as a separate list and override corresponding towers based on a 50/50 chance", "blue", attrs=["bold"], end="\n")
	cprint("2.", "cyan", attrs=["bold"], end=" ")
	cprint("Replace corresponding towers in the list with their golden variants, and therefore only choose their golden variants if they are ever randomly chosen", "blue", attrs=["bold"], end="\n\n")
	cprint("Please select an option:", "green", attrs=["bold"], end=" ")
	promptgopt = int(input())
	if promptgopt == 1:
		cprint("\nOK, applying choice 1.", "green", attrs=["bold"])
		sleep(1)
		print(customGolden)
	elif promptgopt == 2:
		cprint("\nOK, applying choice 2. I am now merging the golden list into the custom one...", "green", attrs=["bold"])
		goldenIndependent = False
		sleep(1)
		for tower in customGolden:
			for target in customBase:
				if tower == target:
					cprint(tower + ":", "blue", attrs=["bold"], end=" ")
					sleep(0.5)
					newtower = target.replace(target, "Golden " + target)
					customBase.append(newtower)
					customBase.remove(target)
					cprint("OK", "light_green", attrs=["bold"])
		
		cprint("\nFinished.", "green", attrs=["bold"])
		
cprint("\nConfiguration has finally finished. Now proceeding to randomization.", "cyan", attrs=["bold"])
sleep(2)
if "Farm" in customBase:
	cprint("\nYou had chosen Farm during the base tower phase of configuration. Should it be automatically included in the final loadout? This will help fund any offensive towers the randomizer generates. [y/n]", "cyan", attrs=["bold"], end=" ")
	promptfarm = input()
	if promptfarm == "y" or promptfarm == "yes":
		cprint("\nOK. Farm will be generated in slot 1.", "green", attrs=["bold"])
		sleep(0.5)
		loadout.append("Farm")
	else:
		cprint("\nOK. I'll proceed normally.", "green", attrs=["bold"])
		sleep(0.5)
		
cprint("\nNow randomizing, please wait...", "light_magenta", attrs=["bold"])
sleep(3)
fileData = customBase
if len(loadout) < 1:
	for i in range(0, 5):
		# Generate normally
		selection = choice(customBase)
		loadout.append(selection)
		customBase.remove(selection)
else:
	for i in range(0, 4):
		selection = choice(customBase)
		loadout.append(selection)
		customBase.remove(selection)
					
if goldenIndependent and canUseGolden:
		for tower in loadout:
			for gold in customGolden:
				if gold == tower:
					coinflip = randint(1,2)
					if coinflip == 1:
						newGolden = tower.replace(tower, "Golden " + tower)
						loadout.append(newGolden)
						loadout.remove(tower)
						
cprint("\nThe loadout has successfully been generated:", "cyan", attrs=["bold"], end="\n\n")
cprint("1:", "green", attrs=["bold"], end=" ")
cprint(loadout[0], "blue", attrs=["bold"], end="\n")
cprint("2:", "green", attrs=["bold"], end=" ")
cprint(loadout[1], "blue", attrs=["bold"], end="\n")
cprint("3:", "green", attrs=["bold"], end=" ")
cprint(loadout[2], "blue", attrs=["bold"], end="\n")
cprint("4:", "green", attrs=["bold"], end=" ")
cprint(loadout[3], "blue", attrs=["bold"], end="\n")
cprint("5:", "green", attrs=["bold"], end=" ")
cprint(loadout[4], "blue", attrs=["bold"], end="\n\n")

cprint("Would you like to save your custom tower list for future randomization? (Only recommended if golden perks were merged) [y/n]", "cyan", attrs=["bold"], end=" ")
promptsv = input()
if promptsv == "y" or promptsv == "yes":
	sleep(0.5)
	f = open("customlist.txt", "w")
	f.write('\n'.join(fileData))
	cprint("Your list has been saved to customlist.txt. You may modify it at any time.", "cyan", attrs=["bold"])
	sleep(0.5)

cprint("TDSRandomizer will now exit. Have fun!", "cyan", attrs=["bold"])
sleep(1)
