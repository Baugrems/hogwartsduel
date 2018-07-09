import random
#gather stats for each player
def main():
    playerOne = {}
    playerTwo = {}

    def initialisePlayer(player):
        player["name"] = input("Enter player name:\n")
        player["hp"] = int(input("Enter current hp: \n"))
        player["acc"]= int(input("Enter accuracy: \n"))
        player["agi"] = int(input("Enter agility: \n"))
        player["arcpow"] = int(input("Enter Arcane Power: \n"))
        player["cntrl"] = int(input("Enter control: \n"))
        return;
    initialisePlayer(playerOne)
    initialisePlayer(playerTwo)
    play(playerOne, playerTwo)


#Define base for each category by student year
CAST_CHANCE = {
    "First-Year" : 80,
    "Second-Year" : 75,
    "Third-Year" : 65,
    "Fourth-Year" : 55,
    "Fifth-Year" : 45,
    "Sixth-Year" : 35,
    "Seventh-Year" : 30,
    "Graduate" : 25
}
HIT_CHANCE = {
    "First-Year" : 100,
    "Second-Year" : 80,
    "Third-Year" : 75,
    "Fourth-Year" : 65,
    "Fifth-Year" : 50,
    "Sixth-Year" : 40,
    "Seventh-Year" : 35,
    "Graduate" : 25
}
SPELL_DAMAGE = {
    "First-Year" : 200,
    "Second-Year" : 300,
    "Third-Year" : 500,
    "Fourth-Year" : 750,
    "Fifth-Year" : 900,
    "Sixth-Year" : 1100,
    "Seventh-Year" : 1400,
    "Graduate" : 1800
}

def play(playerOne, playerTwo):
    print("\n",playerOne["name"], "has", playerOne["hp"], "health and", playerTwo["name"], "has", playerTwo["hp"], "health currently.")
    print("\nWhat spell does", playerOne["name"], "use? Type First-Year, Second-Year, etc: \n")
    spell1 = input()
    print("\nWhat spell does", playerTwo["name"], "use? Type First-Year, Second-Year, etc: \n")
    spell2 = input()
    print("\n",playerOne["name"], "is using a spell from", spell1, "and",playerTwo["name"], "is using a spell from", spell2)
    print("\n",playerOne["name"], "has a", CAST_CHANCE[spell1] + (playerOne["cntrl"] * 2), "percent and",playerTwo["name"], "has a", CAST_CHANCE[spell2] + (playerTwo["cntrl"] * 2), "percent chance to cast their spell.")
    if (CAST_CHANCE[spell1] + (playerOne["cntrl"] * 2)) >= random.randint(1,101):
        print("\n",playerOne["name"], "casts their spell with success.")
        cast1 = True
    else:
        print("\n",playerOne["name"], "fails to cast their spell correctly.")
        cast1 = False
    if (CAST_CHANCE[spell2] + (playerTwo["cntrl"] * 2)) >= random.randint(1,101):
        print("\n",playerTwo["name"], "casts their spell with success.")
        cast2 = True
    else:
        print("\n",playerTwo["name"], "fails to cast their spell correctly.")
        cast2 = False

    # get stance of each player
    print("\nStance used by ",playerOne["name"], "? Type agg, agg+, neutral, def, or def+: \n")
    stance1 = input()
    print("\nStance used by ",playerTwo["name"], "? Type agg, agg+, neutral, def, or def+: \n")
    stance2 = input()

    #calculate chance to hit and roll to see if it hits
    hit1 = int((HIT_CHANCE[spell1] + (playerOne["acc"] - playerTwo["agi"])))
    hit2 = int((HIT_CHANCE[spell2] + (playerTwo["acc"] - playerOne["agi"])))
    if stance1 == "def":
        hit1 = int(hit1 * 0.8)
        hit2 = int(hit2 * 0.8)
    if stance2 == "def":
        hit1 = int(hit1 * 0.8)
        hit2 = int(hit2 * 0.8)
    if stance1 == "def+":
        hit1 = int(hit1 * 0.5)
        hit2 = int(hit2 * 0.7)
    if stance2 == "def+":
        hit1 = int(hit1 * 0.7)
        hit2 = int(hit2 * 0.5)
    if stance1 == "agg+":
        hit2 = int(hit2 * 1.5)
    if stance2 == "agg+":
        hit1 = int(hit1 * 1.5)
    hit1_success = False
    hit2_success = False
    if cast1 and cast2:
        print("\n",playerOne["name"], " has a", hit1, "percent and ",playerTwo["name"], " has a", hit2, "percent chance to hit with their spell.")
        if hit1 >= random.randint(1,101):
            print("\n",playerOne["name"], " hits their opponent.")
            hit1_success = True
        else:
            print("\n",playerOne["name"], " fails to hit the opponent.")
            hit1_success = False
        if hit2 >= random.randint(1,101):
            print("\n",playerTwo["name"], " hits their opponent.")
            hit2_success = True
        else:
            print("\n",playerTwo["name"], " fails to hit the opponent.")
            hit2_success = False
    elif cast1 and not cast2:
        print("\n",playerOne["name"], " has a", hit1, "percent and ",playerTwo["name"], " failed to cast their spell.")
        if hit1 >= random.randint(1,101):
            print("\n",playerOne["name"], " hits their opponent.")
            hit1_success = True
        else:
            print("\n",playerOne["name"], " fails to hit the opponent.")
            hit1_success = False
    elif not cast1 and cast2:
        print("\n",playerOne["name"], " failed to cast and ",playerTwo["name"], " has a", hit2, "percent chance to hit with their spell.")
        if hit2 >= random.randint(1,101):
            print("\n",playerTwo["name"], " hits their opponent.")
            hit2_success = True
        else:
            print("\n",playerTwo["name"], " fails to hit the opponent.")
            hit2_success = False
    elif not cast1 and not cast2:
        print("\nBoth players failed to cast.")
    print("\n======================================\n")

    #Calculate damage done
    dmg1 = SPELL_DAMAGE[spell1] + (playerOne["arcpow"] * 5)
    dmg2 = SPELL_DAMAGE[spell2] + (playerTwo["arcpow"] * 5)
    if stance1 == "agg":
        dmg1 = int(dmg1 * 1.2)
        dmg2 = int(dmg2 * 1.2)
    if stance2 == "agg":
        dmg1 = int(dmg1 * 1.2)
        dmg2 = int(dmg2 * 1.2)
    if stance1 == "agg+":
        dmg1 = int(dmg1 * 1.3)
    if stance1 == "agg+":
        dmg2 = int(dmg2 * 1.3)
    if hit1_success:
        playerTwo["hp"] = playerTwo["hp"] - dmg1
        print("\n",playerTwo["name"], " is hit for", dmg1, "damage and is down to", playerTwo["hp"], "hp.")
    if hit2_success:
        playerOne["hp"] = playerOne["hp"] - dmg2
        print("\n",playerOne["name"], " is hit for", dmg2, "damage and is down to", playerOne["hp"], "hp.")
    if (playerOne["hp"] >= 0) and (playerTwo["hp"] >= 0):
        input("Hit enter to start next round\n")
        play(playerOne, playerTwo)
    elif playerOne["hp"] == playerTwo["hp"]:
        print("Game over.. it is a draw!")
    elif playerOne["hp"] > playerTwo["hp"]:
        print("%s wins!" % (playerOne["name"]))
    elif playerOne["hp"] < playerTwo["hp"]:
        print("%s wins!" % (playerTwo["name"]))
    return;


#Forces main() to run first
if __name__ == '__main__':
    main()
