#loading of packages
import random
import os
import sys
import ast 
#game Variable
game_vars={
    'turn':1,
    'score':0,
    'coin':16
    }
#main menu function
def show_main_menu():
    print("1. Start new game")
    print("2. Load saved game")
    print("3. Display High Scores")
    print("4. Quit")
    print()
    while True:
        try:
            option = input('Your choice? ')
            if option == '1':
                new_game()
            elif option == '2':
                load_game()
                draw_field()
                show_menu()

            elif option == '3':
                load_highscore()
                show_high_scores()
                show_main_menu()
            elif option == '4':
                print("See you Next time")
                exit()    
            else:
                print('Invalid input. Please enter 1, 2, 3 or 4.')
                show_main_menu()
        except Exception as e:
            print(f'An error occurred: {e}')
            show_main_menu()


Building = {'Residential': {'symbol':'R',
                            'name':'Residential'},
            'Industry':  {'symbol':'I',
                            'name':'Industry'},
            'Commercial': { 'symbol':'C',
                            'name':'Commercial'},
            'Park': { 'symbol':'O',
                            'name':'Park'},
            'Road': { 'symbol':'*',
                            'name':'Road'}
             }
#20x20 Board
field = [ [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],        
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],
          [None, None, None, None, None, None, None,None, None, None, None, None, None, None,None, None, None, None, None, None],]
#----------------------------
# new_game()
#
#    Display New Game Menu
#----------------------------      
def new_game():
    global field,game_vars
    field = [[None] * 20 for _ in range(20)]
    game_vars={
    'turn':1,
    'score':0,
    'coin':16
    }
    for _ in range(2):
        row = random.randint(0, len(field) - 1)
        col = random.randint(0, len(field[0]) - 1)
        building_type = random.choice(list(Building.keys()))
        field[row][col] = Building[building_type]['symbol']
    draw_field()
    show_menu()


        


def draw_field():
    print('   ', end='')
    for i in range(len(field)):
        print(" {0:^3}".format(i), end='')
    print()
    numrow = 0
    for row in field:
        print('   ', end='')
        print(('+---' * len(row)), end='')
        print("+")
        print('{0:2} '.format(numrow), end='')
        numrow+=1
        for cell in row:
            if cell is None:
                print("|   ", end="")
            else:
                print(f"| {cell} ", end="")
        print("|")
    print('   ', end='')
    print(('+---' * len(field[0])), end='')
    print("+")
    print(f"Turn: {game_vars['turn']}")
    print(f"Coin: {game_vars['coin']}")
    print(f"Score: {game_vars['score']}")



def show_menu():
    print("1. Build Building   2. Current Score")
    print("3. Save game       4. Exit to Main Menu")
    choice = (input("Your Choice? " ))
    

    if choice == '1':
        Build_Building()
        
                                  
    elif choice == '2':
        Current_score()      
        show_menu()

    elif choice == '3':
        save_game()
        show_main_menu()
    elif choice == '4':
        print("See you Next time")
        show_main_menu()
    

    else:
        print("\nInvalid\n")
        show_menu()


def Build_Building():
    global game_vars

    try:
        # For turn 1, allow building anywhere
        if game_vars['turn'] == 1:
            row = int(input("Enter the row (0-19): "))
            col = int(input("Enter the column (0-19): "))
        else:
            # For turns other than 1, prompt the user to enter row and column
            while True:
                try:
                    row = int(input("Enter the row (0-19): "))
                    col = int(input("Enter the column (0-19): "))
                    if is_valid_location(row, col) and is_adjacent_to_building(row, col):
                        break
                    else:
                        print("Invalid location. Please enter a valid location.")
                except ValueError:
                    print("Invalid input. Please enter valid numeric values.")

        # Check if the selected location is valid and empty
        if not (0 <= row < len(field) and 0 <= col < len(field[0])) or field[row][col] is not None:
            print("Invalid coordinates or the cell is not empty. Please enter valid values.")
            return Build_Building()

        building_type = choose_building_type()
        cost = 1  # Construction cost is 1 coin
        if game_vars['coin'] >= cost:
            game_vars['coin'] -= cost
            field[row][col] = Building[building_type]['symbol']
            print(f"{building_type} built at ({row}, {col})")
            game_vars['turn'] += 1

            # Calculate and update the score
            building_score, extra_info = calculate_building_score(row, col, building_type)
            game_vars['score'] += building_score

            print(f"Building score: {building_score}")
            if extra_info is not None:
                print(f"Extra information: {extra_info}")

            print(f"Total score: {game_vars['score']}")

            draw_field()
            if game_vars['coin'] == 0 or all(cell is not None for row in field for cell in row):
                end_of_game()
            else:
                show_menu()
        else:
            print("Insufficient coins to build.")

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
        Build_Building()
# New function to check if a location is orthogonally adjacent to an existing building
def is_adjacent_to_building(row, col):
    # Check in the four cardinal directions (north, east, south, west)
    for i, j in [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]:
        if 0 <= i < len(field) and 0 <= j < len(field[0]) and field[i][j] is not None:
            return True
    return False



def is_valid_location(row, col):
    # Check if the location is within the bounds of the field and is not already occupied
    return 0 <= row < len(field) and 0 <= col < len(field[0]) and field[row][col] is None


# Implementing calculate_building_score and other functions as per the previous messages

# Remaining features like Display High Scores, Exit to Main Menu, and End of Game are not implemented yet.
# Implement these features based on your requirements.



def choose_building_type():
    print("Choose a building type:")
    building_options = random.sample(list(Building.keys()), 2)
    print("1. ", Building[building_options[0]]['name'])
    print("2. ", Building[building_options[1]]['name'])
    
    while True:
        try:
            choice = int(input("Enter the number corresponding to your choice: "))
            if 1 <= choice <= 2:
                print(Building[building_options[choice - 1]]['name'])
                return Building[building_options[choice - 1]]['name']
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def Current_score():
    print("Current Score : ",game_vars['score'])
    show_menu()
#-----------------------------------------
# save_game()
#
#    Saves the game in the file 'save.txt'
#-----------------------------------------
def save_game():
    save = open('save.txt','w')
    save.write(str(game_vars)+'\n')
    save.write(str(field)+'\n')
    
    save.close()
    print("Game Saved")


#-----------------------------------------
# load_game()
#
#    Loads the game from 'save.txt'
#-----------------------------------------
def load_game():
    load = open('save.txt', 'r')
    global game_vars, field
    game_vars = ast.literal_eval(load.readline())
    field = ast.literal_eval(load.readline())
    load.close()
        

def calculate_building_score(row, col, building_type):
    score = 0
    extra_info = None  # Variable to store additional information

    if building_type == 'Residential':
        score, extra_info = calculate_residential_score(row, col)
    elif building_type == 'Industry':
        score = calculate_industry_score(row, col)
    elif building_type == 'Commercial':
        score, extra_info = calculate_commercial_score(row, col)
    elif building_type == 'Park':
        score = calculate_park_score(row, col)
    elif building_type == 'Road':
        score = calculate_road_score(row)

    print(f"Building: {building_type}, Row: {row}, Col: {col}, Score: {score}, Extra Info: {extra_info}")
    return score, extra_info  # Return both score and extra information
def calculate_residential_score(row, col):
    score = 0
    extra_info = None

    # Check if it is next to an industry
    if is_adjacent_building_type(row, col, 'Industry'):
        score = 1
        extra_info = "Residential next to Industry gets +1 score."
    else:
        # Score 1 point for each adjacent Residential or Commercial
        score += count_adjacent_buildings(row, col, ['Residential', 'Commercial'])
        # Score 2 points for each adjacent Park
        score += 2 * count_adjacent_buildings(row, col, ['Park'])

    print(f"Row: {row}, Col: {col}, Score: {score}, Extra Info: {extra_info}")

    return score, extra_info




# Function to calculate the score for an Industry building
def calculate_industry_score(row, col):
    score = 0

    # Score 1 point per industry in the city
    score += count_adjacent_buildings(row, col, ['Industry'])

    # Generate 1 coin per residential building adjacent to it
    score += count_adjacent_buildings(row, col, ['Residential'])

    return score

def calculate_commercial_score(row, col):
    score = 0
    residential_count = 0

    # Score 1 point per commercial adjacent to it
    score += count_adjacent_buildings(row, col, ['Commercial'])
    # Generate 1 coin per residential adjacent to it
    residential_count += count_adjacent_buildings(row, col, ['Residential'])

    # Multiply the residential count by the coin generation factor
    coin_generation_factor = 1
    coin_generated = residential_count * coin_generation_factor

    return score + coin_generated, f"Commercial gets +{residential_count} coin(s) for each adjacent Residential."

# Function to calculate the score for a Park building
def calculate_park_score(row, col):
    # Score 1 point per park adjacent to it
    return count_adjacent_buildings(row, col, ['Park'])

# Function to calculate the score for a Road building
def calculate_road_score(row):
    # Score 1 point per connected road in the same row
    return count_connected_road(row)

# Helper function to check if a building of a specific type is adjacent to a given location
def is_adjacent_building_type(row, col, building_type):
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(field) and 0 <= j < len(field[0]) and field[i][j] == Building[building_type]:
                return True
    return False

def count_adjacent_buildings(row, col, building_types):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < len(field) and 0 <= j < len(field[0]) and (i, j) != (row, col) and field[i][j] == Building[building_types[0]]['symbol']:
                count += 1
    return count


# Helper function to count the number of buildings of a specific type in the city
def count_buildings(building_type):
    count = 0
    for row in field:
        for cell in row:
            if cell == Building[building_type]['symbol']:
                count += 1
    return count

# Helper function to count the number of connected road cells in a specific row
# Helper function to count the number of connected road cells in a specific row
def count_connected_road(row):
    count = 0
    for cell in field[row]:
        if cell == Building['Road']['symbol']:
            count += 1
    return count


highscore =[]
def end_of_game():
    # ...
    load_highscore()

    if is_high_score(game_vars['score']):
        print("Congratulations! You made it to the top score list.")
        name = input('Enter your name: ')

        # Add the player's score with their name to the high score list
        highscore.append({'name': name, 'score': game_vars['score']})
        highscore.sort(key=lambda x: x['score'], reverse=True)

        # Truncate the list to keep only the top N scores (adjust N as needed)
        top_scores = highscore[:10]

        # Save the updated high scores back to the file
        with open('highscore.txt', 'w') as save:
            for entry in top_scores:
                save.write(f"{entry['name']} {entry['score']}\n")

        show_high_scores()
    else:
        print("You did not make into the top score list.")
    print("Returning to the main menu.")
    show_main_menu()

def show_high_scores():
    print("Top Scores:")
    for i, entry in enumerate(highscore, start=1):
        print(f"{i}. {entry['name']} - {entry['score']}")

def is_high_score(score):
    # Load existing high scores
    load_highscore()

    # Check if the score is higher than any of the existing high scores
    return score > max(entry['score'] for entry in highscore)


    




def load_highscore():
    global highscore
    try:
        load = open('highscore.txt', 'r')
        highscore = [{'name': line.split()[0], 'score': int(line.split()[1])} for line in load.readlines()]
    except FileNotFoundError:
        # Create the file if it doesn't exist
        open('highscore.txt', 'w').close()
        highscore = []
    return highscore

#main software
menu = show_main_menu()
