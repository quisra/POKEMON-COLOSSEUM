from Pokemon import Pokemon
from SkillMoves import SkillMoves
import random, math, ast, copy, csv

#############################################################
###             FUNCTIONS 
#############################################################

def readPokemonData(pokemon_filename,pokemon_list):
    with open(pokemon_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

        for row in reader:
            # name, type, HP, attack, defense, height, weight, moves
            name =  row[0]
            pok_type =   row[1]
            hp =   int(float(row[2]))
            attack =  int(row[3])
            defense = int(row[4])
            height = int(row[5])
            weight = int(row[6])
            moves=''
            end_of_moves=False
            for s in row:
                if s[0]=='[':
                    end_of_moves = True
                    moves = s
                elif end_of_moves == True:
                    moves += ','+s
                    if s[-1] == ']':
                        end_of_moves = False
            # print(moves)
            pokemon_moves = ast.literal_eval(moves)  
            # string to list
            
            # Store pokemon data
            pokemonInfo =  Pokemon(name, pok_type, hp, attack, defense, height, weight, pokemon_moves)
            pokemon_list[name] = pokemonInfo
    # TEST POKEMON LIST
    # for pokemon in pokemon_list:
    #     print("Printing Pokemon List")
    #     pokemon_list[pokemon].display_info()
    #     print("\n")
    
###########END POKEMON DATA
    
########READ MOVES DATA
def readMovesData(moves_filename, moves_list):
    with open(moves_filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)

# Store  the data in a dictionary where the keys are move names and values are lists of (type, damage, Category, Contest, PP, Power, Accuracy).

        for row in reader:
            # name,type,category,contest,pp,power,accuracy
            name =  row[0]
            move_type =   row[1]
            category =   row[2]
            contest =  row[3]
            pp = int(row[4])
            power = int(row[5])
            accuracy = row[6]
            
            movesInfo = SkillMoves(name, move_type, category, contest, pp, power, accuracy)
            moves_list[name] = movesInfo
    
    # TEST MOVES LIST
    # for moves in moves_list:
    #     print("Printing Moves List")
    #     moves_list[moves].displayMoves_info()
    #     print("\n")
    
###########END MOVES DATA

########### ASSIGN POKEMONS ##############

def  assignPokemon(playerTeam, teamRocket, pokemon_list):
    num_of_pokemons = len(pokemon_list)
    
    # find random number  between 1 and the total amount of pokemons -1
    rand_num = random.sample(range(0, num_of_pokemons), 6)
    
    for i in  range(len(rand_num)):
        if  (i < 3):
            playerTeam.append(list(pokemon_list.keys())[rand_num[i]])
        else:
            teamRocket.append(list(pokemon_list.keys())[rand_num[i]])


########### END RANDOM POKEMONS  ##########

########### DAMAGE CALCULATOR ##############

def damageCalc(moves, attacker,  defender):
    # Get type match up Dictionary
    type_matchup = {
    'Normal': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1},
    'Fire': {'Normal': 1, 'Fire': 0.5, 'Water': 0.5, 'Electric': 1, 'Grass': 2},
    'Water': {'Normal': 1, 'Fire': 2, 'Water': 0.5, 'Electric': 1, 'Grass': 0.5},
    'Electric': {'Normal': 1, 'Fire': 1, 'Water': 2, 'Electric': 0.5, 'Grass': 0.5},
    'Grass': {'Normal': 1, 'Fire': 0.5, 'Water': 2, 'Electric': 1, 'Grass': 0.5},
    'Others': {'Normal': 1, 'Fire': 1, 'Water': 1, 'Electric': 1, 'Grass': 1}
    }
    
    # create variables for damage formula
    P = moves.get_power()
    A = attacker.get_attack()
    D = defender.get_defense()
    move_type =  moves.get_move_type()
    if move_type not in  type_matchup:
        move_type = 'Others'
        
    defend_type = defender.get_type()
    if move_type == defend_type:
        stabBonus = 1.5
    else:
        stabBonus = 1
    Damage_TE = type_matchup[move_type].get(defend_type, 1)
    Random = random.uniform(0.5, 1)
    
    # Calculate damage
    damage_amount = (P * A / D) *  stabBonus * Damage_TE * Random
    return math.ceil(damage_amount)

########### END DAMAGE CALCULATOR ##############
        
        
#############################################################
###             END FUNCTIONS
#############################################################

pokemon_filename = 'pokemon-data.csv'
moves_filename = 'moves-data.csv'
pokemon_list = {}
moves_list = {}

# Read and assign Data in classes
readPokemonData(pokemon_filename, pokemon_list)
readMovesData(moves_filename, moves_list)

print("\n**************** WELCOME TO THE POKEMON COLOSSEUM! ***************\n")
teamName = input("Enter Player Name: ")
print("\n")


# Assign  player team with random Pokemon from the list of available ones
playerTeam = []
teamRocket = []
assignPokemon(playerTeam, teamRocket,  pokemon_list)

print("Team Rocket enters with: ", teamRocket[0],",",teamRocket[1],",",teamRocket[2],"\n")
print("Team ", teamName, "enters with: ",playerTeam[0], ",",   playerTeam[1], ",",   playerTeam[2],"\n")

print("<<<<<< LET THE  BATTLE BEGIN! >>>>>>",)
# Coint toss
tossResult = ["Heads","Tails"]
result = tossResult[random.randint(0,1)]
if  result == "Heads":
    print("Coin toss goes to -------> Team  ", teamName," to start the attack!\n")
    turn = 0 
else:
    print("Coin toss goes to ---------> Team Rocket to start the attack!\n")
    turn = 1 

# Variables move tracker 
currentRocketPoke = copy.deepcopy(pokemon_list.get(teamRocket[0]))
currentPlayerPoke = copy.deepcopy(pokemon_list.get(playerTeam[0]))
rocketAvailableMoves,  rocketUsedMoves, playerAvailableMoves, playerUsedMoves = [], [], [], []
rocketAvailableMoves = list(currentRocketPoke.get_moves()) #moves list of crnt rocket pokemon
playerAvailableMoves = list(currentPlayerPoke.get_moves()) #moves list of crnt player pokemon

################ START THE BATTLE ####################
gameEnd =  False

while gameEnd is not True:
    if turn == 0:
        #Player attacks
        print("----->PLAYER TURN<-----")
        while turn ==  0:
            if  len(playerAvailableMoves) == 0:
                playerAvailableMoves = list(currentPlayerPoke.get_moves()) #moves list of crnt player pokemon
                playerUsedMoves = [None] * len(playerAvailableMoves) #create equivalent empty slots for used move
                
            else:
                totalMoves = len(playerAvailableMoves)
                
                 # Choices for Player
                print("Choose the move for " + currentPlayerPoke.get_name() +  ": ")
                for i in range(totalMoves):
                    if playerAvailableMoves[i] in playerUsedMoves:
                        print(f"{i + 1}. {playerAvailableMoves[i]} (Unavailable)")
                    else:
                        print(f"{i + 1}. {playerAvailableMoves[i]}")
                    
                # Enter  choice and validate it
                moveIndex = input("\nTeam " + teamName + "'s choice: ")
                while True:
                    # Check if moveIndex is in the correct range, right  type, & not already used
                    if not moveIndex.isdigit() or int(moveIndex) < 1 or int(moveIndex) > totalMoves or playerAvailableMoves[int(moveIndex) - 1] in playerUsedMoves:
                        
                        # Check again to provide specific feedback
                        if moveIndex.isdigit() and int(moveIndex) <= totalMoves and playerAvailableMoves[int(moveIndex) - 1] in playerUsedMoves:
                            print("\nThis move has already been used. Please choose another one.")
                        else:
                            print("\nInvalid input! Please enter a valid choice.")
                                   
                    else:
                        break
                    # Let User Know their choices again
                    print("Choose the move for " + currentPlayerPoke.get_name() +  ": ")
                    for i in range(totalMoves):
                        if playerAvailableMoves[i] in playerUsedMoves:
                            print(f"{i + 1}. {playerAvailableMoves[i]} (Unavailable)")
                        else:
                            print(f"{i + 1}. {playerAvailableMoves[i]}")
                    moveIndex = input(f"\nTeam {teamName}'s choice: ")
                    

                moveIndex = int(moveIndex) - 1
                playerAttack = playerAvailableMoves[moveIndex]
                playerUsedMoves.insert(moveIndex,playerAvailableMoves[moveIndex])# removes from available moves list
                
                damage = damageCalc(moves_list.get(playerAttack), currentPlayerPoke, currentRocketPoke) #get damage amount
                rocket_hp_left = currentRocketPoke.get_hp() - damage
                currentRocketPoke.set_hp(rocket_hp_left)
                player_hp_left = currentPlayerPoke.get_hp()
                turn = 1
                
                print("Team " + teamName + "'s " + currentPlayerPoke.get_name() + " cast '" + playerAttack + "' to "+ currentRocketPoke.get_name() + ":")
                print("Damage to " + currentRocketPoke.get_name() + " is " + str(damage) + " points.")
            
                # if no hp is left for player go to poke ball
                if rocket_hp_left < 1:
                    print("Now " + currentPlayerPoke.get_name() + " has " + str(player_hp_left) + " HP," + " and " + currentRocketPoke.get_name() + " faints back to poke ball.\n")
                    teamRocket.pop(0)
                    if  len(teamRocket) == 0 : 
                        gameEnd = True
                        break
                    else:
                        currentRocketPoke = copy.deepcopy(pokemon_list.get(teamRocket[0]))
                        rocketAvailableMoves = list(currentRocketPoke.get_moves()) #moves list of the current pokemon
                        rocketUsedMoves = [None] * len(rocketAvailableMoves) #create equivalent empty slots for used move
                        
                        print("\nNext for Team Rocket, " + currentRocketPoke.get_name() + " enters battle!\n")
                else:
                    print("Now " + currentPlayerPoke.get_name() + " has " + str(player_hp_left) + " HP," + " and " + currentRocketPoke.get_name() + " has " + str(rocket_hp_left) + " HP.\n")

    else :
        # team rocket attacks
        print("----->ROCKET TURN<-----")
        while turn == 1:
            if len(rocketAvailableMoves) == 0:
                rocketAvailableMoves = list(currentRocketPoke.get_moves()) #moves list of the current pokemon
                rocketUsedMoves = [None] * len(rocketAvailableMoves) #create equivalent empty slots for used move
                
            else:
                totalMoves = len(rocketAvailableMoves)
                moveIndex = random.randint(0, totalMoves - 1)
                rocketAttack = rocketAvailableMoves[moveIndex]
                rocketUsedMoves.insert(moveIndex,rocketAvailableMoves.pop(moveIndex))# removes from available moves list
                
                damage = damageCalc(moves_list.get(rocketAttack), currentRocketPoke, currentPlayerPoke) #get damage amount
                player_hp_left = currentPlayerPoke.get_hp() - damage
                currentPlayerPoke.set_hp(player_hp_left)
                rocket_hp_left = currentRocketPoke.get_hp()
                turn = 0
                
                print("Team Rocket's " + currentRocketPoke.get_name() + " cast '" + rocketAttack + "' to " + currentPlayerPoke.get_name() + ":")
                print("Damage to " + currentPlayerPoke.get_name() + " is " + str(damage) + " points.")
                
                # if no hp is left for player go to poke ball
                if player_hp_left < 1:
                    print("Now " + currentRocketPoke.get_name() + " has " + str(rocket_hp_left) + " HP," + " and " + currentPlayerPoke.get_name() + " faints back to poke ball.\n")
                    playerTeam.pop(0)
                    if  len(playerTeam) == 0 : 
                        gameEnd = True
                        break
                    else:
                        currentPlayerPoke = copy.deepcopy(pokemon_list.get(playerTeam[0]))
                        playerAvailableMoves = list(currentPlayerPoke.get_moves()) #moves list of crnt player pokemon
                        playerUsedMoves = [None] * len(playerAvailableMoves) #create equivalent empty slots for used move
                        
                        print("\nNext for Team " + teamName +"'s " + currentPlayerPoke.get_name() + " enters battle!\n")
                else:
                    print("Now " + currentRocketPoke.get_name() + " has " + str(rocket_hp_left) + " HP," + " and " + currentPlayerPoke.get_name() + " has " + str(player_hp_left) + " HP.\n")
                    
# WINNER / LOSER
print("****** THE GAME HAS ENDED ******")
if  len(playerTeam) == 0 and len(teamRocket) > 0:
    print("\nYou have been defeated.\nTry Again Next Time!")
elif len(playerTeam) > 0 and len(teamRocket) == 0:
    print("\nCongratulations! You have defeated all Pokémon in Team Rocket's Party.\nYou are the POKEMON CHAMPION!")
print("******************************")    



