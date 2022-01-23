
import random

#ship = (x, y, horizontal, length, hits)

def is_sunk(ship):
    # This funtion checks if a ship is sunk by checking how many hits the "hits" set have.
    # It there are the same number of hits as the length of the ship,
    # then the ship is sunk

    if ship[3] == len(ship[4]): return True
    elif ship[3] > len(ship[4]): return False

def ship_type(ship):
    # This function checks the type of the ship that is given as input,
    # it does this by checking the length of the given ship.

    if ship[3] == 1: return "submarine"
    elif ship[3] == 2: return "destroyer"
    elif ship[3] == 3: return "cruiser"
    elif ship[3] == 4: return "battleship"

def is_open_sea(row, column, fleet):

    # This part checks if the number of rows and columns are not higher that what they should be.
    if row > 9 or column > 9:
        return False

    # here I am using a for loop to check for each ship in the fleet that the given square is legal
    for s in fleet:

        # this checks if the ship is horizontal or not
        if s[2] == True:

            # this checks if the square given is within 1 distance of the ship being checked,
            # first the column is checked, then the row is checked.
            if column <= (s[1] + s[3]) and column >= (s[1] - 1):
                if (row <= (s[0] + 1) and row >= (s[0] - 1)):
                    return False

        # this checks if the ship is horizontal or not
        elif s[2] == False:

            # this checks if the square given is within 1 distance of the ship being checked,
            # first the column is checked, then the row is checked.
            if column <= (s[1] + 1) and column >= (s[1] - 1):
                if row <= (s[0] + s[3]) and row >= (s[0] - 1):
                    return False

    # if the square passes all the checks, then it should be legal with the given the fleet
    return True


def ok_to_place_ship_at(row, column, horizontal, length, fleet):

    # a for loop is used to see if is_open_sea function holds True for each square of the given ship.
    for i in range(0, length):

        # if the ship is horizontal, i is added to the column input, if vertical, i is added to row input
        # i is added until the length of the ship is checked
        if horizontal == True:
            if is_open_sea(row, column + i, fleet) == False:
                return False
        elif horizontal == False:
            if is_open_sea(row + i, column, fleet) == False:
                return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):
    # here a ship (which is a list) is added to the fleet (which is a list of ships)
    # if the ship given is legal to place for the given fleet.
    # to check this, the function ok_to_place_ship_at is used

    if ok_to_place_ship_at(row, column, horizontal, length, fleet) == True:
        ship = (row, column, horizontal, length, set())
        fleet.append(ship)

    # output is the enlarged fleet
    return fleet


def randomly_place_all_ships(seed = None):

    # a seed can be used as an optional input, this is for testing purposes
    # for the game, no seed will be used to ensure a random fleet is generated each time
    if seed != None:
        random.seed(seed)
    fleet = []

    # first the blattleship is placed into the empty list that is fleet
    while len(fleet) == 0:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        h = random.randint(0, 1)
        if h == 1:
            horizontal = True
        elif h == 0:
            horizontal = False
        length = 4
        place_ship_at(x, y, horizontal, length, fleet)

    # the 2 cruisers are placed now. To make the right number of ships are placed,
    # I am using the total length of the fleet as a checking mechanism.
    # Once the correct number of ships are placed for each class,
    # the while loop is satisfied and the next loop begins
    while len(fleet) <= 2:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        h = random.randint(0, 1)
        if h == 1:
            horizontal = True
        elif h == 0:
            horizontal = False
        length = 3
        place_ship_at(x, y, horizontal, length, fleet)

    # the destroyers
    while len(fleet) <= 5:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        h = random.randint(0, 1)
        if h == 1:
            horizontal = True
        elif h == 0:
            horizontal = False
        length = 2
        place_ship_at(x, y, horizontal, length, fleet)

    # the submarines
    while len(fleet) <= 9:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
        h = random.randint(0, 1)
        if h == 1:
            horizontal = True
        elif h == 0:
            horizontal = False
        length = 1
        place_ship_at(x, y, horizontal, length, fleet)

    # the final fleet with 10 ships is the output
    return fleet


def check_if_hits(row, column, fleet):

    for s in fleet:
        if s[2] == True:
            if column <= (s[1] + s[3] - 1) and column >= s[1]:
                if row == s[0]:
                    return True

        elif s[2] == False:
            if column == s[1]:
                if row <= (s[0] + s[3] - 1) and row >= s[0]:
                    return True

    return False


def hit(row, column, fleet):
    ship = "not_hit"
    for s in fleet:
        if s[2] == True:
            if column <= (s[1] + s[3] - 1) and column >= s[1]:
                if row == s[0]:
                    ship = s
                    break

        elif s[2] == False:
            if column == s[1]:
                if row <= (s[0] + s[3] - 1) and row >= s[0]:
                    ship = s
                    break
    if ship != "not_hit":
        ship[4].add((row, column))
        index_ship = fleet.index(s)
        fleet[index_ship][4].add((row, column))
        return fleet, ship
    else: return False


def are_unsunk_ships_left(fleet):
    counter = 0
    for ship in fleet:
        if is_sunk(ship) == True:
            counter += 1
    if counter == len(fleet):
        return False
    else:
        return True


def main():

    print("Type 'quit' to quit game")
    current_fleet = randomly_place_all_ships()
    game_over = False
    shots = 0
    loc_str = ""
    cont_num = [str(i) for i in range(0, 10)]
    while not game_over:
        loc_str = input("Enter row and column to shoot (separated by space):")

        if loc_str == "quit":
            break

        elif len(loc_str) != 3 or loc_str[0] not in cont_num \
                or loc_str[2] not in cont_num or loc_str[1] != " ":
            print("illegal input, please try again")
            continue

        loc_str = loc_str.split()
        current_row = int(loc_str[0])
        current_column = int(loc_str[1])
        shots += 1
        if check_if_hits(current_row, current_column, current_fleet):
            print("You have a hit!")
            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")
        else:
            print("You missed!")

        if not are_unsunk_ships_left(current_fleet): game_over = True

    if loc_str == "quit": return print("Game over! You quit the game")

    print("Game over! You required", shots, "shots.")
