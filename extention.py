
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
    for i in range(0, length):
        if horizontal == True:
            if is_open_sea(row, column + i, fleet) == False:
                return False
        elif horizontal == False:
            if is_open_sea(row + i, column, fleet) == False:
                return False
    return True


def place_ship_at(row, column, horizontal, length, fleet):

    if ok_to_place_ship_at(row, column, horizontal, length, fleet) == True:
        ship = (row, column, horizontal, length, set())
        fleet.append(ship)

    return fleet


def randomly_place_all_ships(seed = None):
    if seed != None:
        random.seed(seed)
    fleet = []

    #first the blattleship
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

    # the cruisers
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

    # the submarine
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


def create_sea():
    sea = []
    for row in range(0, 10):
        sea.append([])
        for column in range(0, 10):
            sea[row].append(".")

    return sea


def update_sea(current_row, current_column, sea_list, fleet):
    sea = sea_list
    for row in range(0, 10):
        for column in range(0, 10):
            if current_row == row and current_column == column:

                if check_if_hits(current_row, current_column, fleet) == True:

                    ship_hit = hit(current_row, current_column, fleet)[1]

                    if is_sunk(ship_hit) == True:
                        list_of_hits = list(ship_hit[4])
                        if ship_type(ship_hit) == "submarine":
                            sea[list_of_hits[0][0]][list_of_hits[0][1]] = "S"

                        if ship_type(ship_hit) == "destroyer":
                            sea[list_of_hits[0][0]][list_of_hits[0][1]] = "D"
                            sea[list_of_hits[1][0]][list_of_hits[1][1]] = "D"

                        if ship_type(ship_hit) == "cruiser":
                            sea[list_of_hits[0][0]][list_of_hits[0][1]] = "C"
                            sea[list_of_hits[1][0]][list_of_hits[1][1]] = "C"
                            sea[list_of_hits[2][0]][list_of_hits[2][1]] = "C"

                        if ship_type(ship_hit) == "battleship":
                            sea[list_of_hits[0][0]][list_of_hits[0][1]] = "B"
                            sea[list_of_hits[1][0]][list_of_hits[1][1]] = "B"
                            sea[list_of_hits[2][0]][list_of_hits[2][1]] = "B"
                            sea[list_of_hits[3][0]][list_of_hits[3][1]] = "B"

                    else:
                        sea[row][column] = "X"

                else:
                    sea[row][column] = "o"

    return sea



def vizualisation(sea):
    print("    0 1 2 3 4 5 6 7 8 9")
    print("  ---------------------")
    for i in range(0, 10):
        print(i, "|", end = " ")
        for j in range(0, 10):
            print(sea[i][j], end = " ")
        print()


def extention():
    print("Type 'quit' to quit game")
    current_fleet = randomly_place_all_ships()
    sea = create_sea()
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
            update_sea(current_row, current_column, sea, current_fleet)
            vizualisation(sea)

            (current_fleet, ship_hit) = hit(current_row, current_column, current_fleet)
            if is_sunk(ship_hit):
                print("You sank a " + ship_type(ship_hit) + "!")

        else:
            print("You missed!")
            update_sea(current_row, current_column, sea, current_fleet)
            vizualisation(sea)

        if not are_unsunk_ships_left(current_fleet): game_over = True

    if loc_str == "quit": return print("Game over! You quit the game")

    print("Game over! You required", shots, "shots.")


extention()