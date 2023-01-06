from random import choice, randint
towerList = [ # Add/remove towers as needed.
"Farm",
"Commander",
"DJ Booth",
"Scout",
"Soldier",
"Sniper",
"Freezer",
"Demoman",
"Paintballer",
"Pyromancer",
"Militant",
"Ace Pilot",
"Shotgunner",
"Rocketeer",
"Medic",
"Minigunner",
"Hunter",
"Military Base",
"Ranger",
"Electroshocker",
"Accelerator",
"Engineer",
"Crook Boss",
"Turret",
"Mortar",
"Pursuit",
"Cowboy",
"Warden"#,
#"Gladiator",
#"Commando",
#"Slasher",
#"Frost Blaster",    
#"Archer",
#"Swarmer",
#"Toxic Gunner",
#"Sledger",
#"Executioner",
#"Elf Camp"
]

#goldenTowers = ["Scout", "Soldier", "Pyromancer", "Cowboy", "Minigunner", "Crook Boss"]
goldenTowers = None # Use if you have no golden towers; comment out the above table as well
# You may also modify goldenTowers to only include the golden towers you currently own.
def loadoutGen():
    chosenLoadout = []
    goldenConditions = []
    for i in range(0, 5):
        tower = choice(towerList)
        if tower in chosenLoadout:
            while tower in chosenLoadout:
                tower = choice(towerList)
            chosenLoadout.append(tower)
            if goldenTowers == None:
                print("The golden table does not exist, skipping golden condition.")
                continue
            if tower in goldenTowers:
                goldenConditions.append(tower)
        else:
            chosenLoadout.append(tower)
            if goldenTowers == None:
                print("The golden table does not exist, skipping golden condition.")
                continue
            if tower in goldenTowers:
                goldenConditions.append(tower)
            
      
    return chosenLoadout, goldenConditions


loadout, gold = loadoutGen()
if len(gold) > 0:
    for i in range(0, len(gold) - 1):
        canBeGolden = randint(1,2)
        if canBeGolden == 1:
            locatedTower = loadout.index(gold[i])
            loadout[locatedTower] = "Golden " + gold[i]
            
print(loadout, gold)
