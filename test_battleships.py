import pytest
from battleships import *

def test_is_sunk1():
    # Here I am checking if a destroyer with 2 hits is sunk,
    # since the Destroyer has a length of 2, the outcome should be True

    s = (2, 2, False, 2, {(2,2), (3,2)})
    assert is_sunk(s) == True

def test_is_sunk2():
    s = (7, 0, False, 1, {(7,0)})
    assert is_sunk(s) == True

def test_is_sunk3():
    s = (3, 6, True, 3, {(3,6), (3,7), (3,8)})
    assert is_sunk(s) == True

def test_is_sunk4():
    s = (1, 4, True, 3, set())
    assert is_sunk(s) == False

def test_is_sunk5():
    s = (5, 7, False, 4, {(5,7), (7,7), (8,7)})
    assert is_sunk(s) == False



def test_ship_type1():
    # Here the test checks if the function outputs a "submarine"
    # when a ship with the length of 1 is given in the input.
    # It should do this to pass the test

    s = (2, 2, False, 1, {(2, 2)})
    assert ship_type(s) == "submarine"

def test_ship_type2():
    s = (2, 2, False, 2, {(2, 2)})
    assert ship_type(s) == "destroyer"

def test_ship_type3():
    s = (2, 2, False, 3, {(2, 2)})
    assert ship_type(s) == "cruiser"

def test_ship_type4():
    s = (2, 2, False, 4, {(2, 2)})
    assert ship_type(s) == "battleship"

def test_ship_type5():
    # This test simply checks if the output is of the str type, which it should be.

    s = (2, 2, False, 3, {(2, 2)})
    assert type(ship_type(s)) == str



def test_is_open_sea1():
    # Here I am manually generating a fleet for my tests,
    # for this fleet the given row and column should be legal, resulting in a "True" output

    row = 0
    column = 2
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s6 = (6, 4, True, 2, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert is_open_sea(row, column, fleet) == True

def test_is_open_sea2():
    row = 1
    column = 8
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s6 = (6, 4, True, 2, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert is_open_sea(row, column, fleet) == True

def test_is_open_sea3():
    row = 8
    column = 5
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s6 = (6, 4, True, 2, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert is_open_sea(row, column, fleet) == True

def test_is_open_sea4():
    # Here the given row and column is right next to the battleship (s8),
    # so for this fleet the given row and column should be illegal, resulting in a "False" output

    row = 7
    column = 6
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s6 = (6, 4, True, 2, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert is_open_sea(row, column, fleet) == False

def test_is_open_sea5():
    row = 4
    column = 1
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s6 = (6, 4, True, 2, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert is_open_sea(row, column, fleet) == False



def test_ok_to_place_ship_at1():
    row = 2
    column = 0
    horizontal = False
    length = 4
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s7, s8, s9]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at2():
    row = 1
    column = 8
    horizontal = True
    length = 2
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s7, s8, s9]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at3():
    row = 5
    column = 8
    horizontal = True
    length = 2
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s7, s8, s9]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False

def test_ok_to_place_ship_at4():
    row = 6
    column = 3
    horizontal = True
    length = 2
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s7, s8, s9]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == True

def test_ok_to_place_ship_at5():
    row = 0
    column = 1
    horizontal = False
    length = 2
    s1 = (2, 2, False, 2, set())
    s2 = (7, 0, True, 1, set())
    s3 = (9, 0, True, 1, set())
    s4 = (9, 3, True, 1, set())
    s5 = (1, 4, True, 3, set())
    s7 = (3, 6, True, 3, set())
    s8 = (5, 7, False, 4, set())
    s9 = (8, 9, False, 2, set())
    fleet = [s1, s2, s3, s4, s5, s7, s8, s9]
    assert ok_to_place_ship_at(row, column, horizontal, length, fleet) == False



def test_place_ship_at0():
    row = 1
    column = 0
    horizontal = True
    length = 4

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    blue_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    fleet = blue_fleet
    assert type(place_ship_at(row, column, horizontal, length, fleet)) == list

def test_place_ship_at1():
    row = 1
    column = 0
    horizontal = True
    length = 4

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8]

    test_fleet = [s1, s2, s3, s4, s5, s6, s7, s8, (1, 0, True, 4, set())]
    assert place_ship_at(row, column, horizontal, length, fleet) == test_fleet

def test_place_ship_at2():
    #illegal ship
    row = 4
    column = 2
    horizontal = False
    length = 4

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    blue_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    fleet = blue_fleet

    test_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    assert place_ship_at(row, column, horizontal, length, fleet) == test_fleet

def test_place_ship_at3():
    row = 5
    column = 5
    horizontal = False
    length = 1

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    blue_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    fleet = blue_fleet

    test_fleet = [s1, s2, s3, s4, s5, s6, s7, s8, (5, 5, False, 1, set())]
    assert place_ship_at(row, column, horizontal, length, fleet) == test_fleet

def test_place_ship_at4():
    row = 3
    column = 9
    horizontal = False
    length = 3

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    blue_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    fleet = blue_fleet

    test_fleet = [s1, s2, s3, s4, s5, s6, s7, s8, (3, 9, False, 3, set())]
    assert place_ship_at(row, column, horizontal, length, fleet) == test_fleet

def test_place_ship_at5():
    #illegal ship
    row = 8
    column = 6
    horizontal = False
    length = 2

    s1 = (0, 5, True, 4, set())
    s2 = (3, 3, False, 3, set())
    s3 = (3, 5, True, 2, set())
    s4 = (6, 1, False, 1, set())
    s5 = (7, 5, False, 1, set())
    s6 = (5, 7, False, 2, set())
    s7 = (8, 1, True, 3, set())
    s8 = (8, 9, False, 1, set())
    fleet = [s1, s2, s3, s4, s5, s6, s7, s8]

    test_fleet = [s1, s2, s3, s4, s5, s6, s7, s8]
    assert place_ship_at(row, column, horizontal, length, fleet) == test_fleet



def test_randomly_place_all_ships0():
    # checks if 10 ships are placed
    assert len(randomly_place_all_ships()) == 10

def test_randomly_place_all_ships1():
    # checks if all the ships in the fleet are of the right length
    assert randomly_place_all_ships()[0][3] == 4 and \
           randomly_place_all_ships()[1][3] == 3 and \
           randomly_place_all_ships()[2][3] == 3 and \
           randomly_place_all_ships()[3][3] == 2 and \
           randomly_place_all_ships()[4][3] == 2 and \
           randomly_place_all_ships()[5][3] == 2 and \
           randomly_place_all_ships()[6][3] == 1 and \
           randomly_place_all_ships()[7][3] == 1 and \
           randomly_place_all_ships()[8][3] == 1 and \
           randomly_place_all_ships()[9][3] == 1

def test_randomly_place_all_ships2():
    # this checks if a given ship taken out of the randomly generated fleet is legal if it is put back in
    # it should be legal because it was taken out of the generated fleet in the first place.
    # the result can also be legal by chance, but it is extremely unlikely given that the test is repeated a few times.

    assert ok_to_place_ship_at(randomly_place_all_ships(seed = 100)[0][0],
                               randomly_place_all_ships(seed = 100)[0][1],
                               randomly_place_all_ships(seed = 100)[0][2],
                               randomly_place_all_ships(seed = 100)[0][3],
                               randomly_place_all_ships(seed = 100)[1:]) == True

def test_randomly_place_all_ships3():

    assert ok_to_place_ship_at(randomly_place_all_ships(seed = 102)[4][0],
                               randomly_place_all_ships(seed = 102)[4][1],
                               randomly_place_all_ships(seed = 102)[4][2],
                               randomly_place_all_ships(seed = 102)[4][3],
                               randomly_place_all_ships(seed = 102)[0:4] +
                               randomly_place_all_ships(seed = 102)[5:]) == True

def test_randomly_place_all_ships4():

    assert ok_to_place_ship_at(randomly_place_all_ships(seed = 103)[1][0],
                               randomly_place_all_ships(seed = 103)[1][1],
                               randomly_place_all_ships(seed = 103)[1][2],
                               randomly_place_all_ships(seed = 103)[1][3],
                               randomly_place_all_ships(seed = 103)[0:1] +
                               randomly_place_all_ships(seed = 102)[2:]) == True

def test_randomly_place_all_ships5():

    assert ok_to_place_ship_at(randomly_place_all_ships(seed = 106)[9][0],
                               randomly_place_all_ships(seed = 106)[9][1],
                               randomly_place_all_ships(seed = 106)[9][2],
                               randomly_place_all_ships(seed = 106)[9][3],
                               randomly_place_all_ships(seed = 106)[:-1]) == True



def test_check_if_hits0():
    row = 3
    column = 2
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == True

def test_check_if_hits1():
    row = 7
    column = 2
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == True

def test_check_if_hits2():
    row = 7
    column = 7
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == True

def test_check_if_hits3():
    row = 5
    column = 1
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == False

def test_check_if_hits4():
    row = 2
    column = 6
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == False

def test_check_if_hits5():
    row = 5
    column = 8
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert check_if_hits(row, column, fleet) == False


def test_hit0():
    row = 6
    column = 7
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]

    assert type(hit(row, column, fleet)) == tuple and len(hit(row, column, fleet)) == 2

def test_hit1():
    row = 6
    column = 7
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    s0 = (5, 7, False, 4, {(6, 7)})
    new_fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert hit(row, column, fleet) == (new_fleet, s0)

def test_hit2():
    row = 1
    column = 5
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    s2 = (1, 4, True, 3, {(1, 5)})
    new_fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert hit(row, column, fleet) == (new_fleet, s2)

def test_hit3():
    row = 3
    column = 8
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    s1 = (3, 6, True, 3, {(3, 8)})
    new_fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert hit(row, column, fleet) == (new_fleet, s1)

def test_hit4():
    row = 9
    column = 3
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    s8 = (9, 3, True, 1, {(9,3)})
    new_fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert hit(row, column, fleet) == (new_fleet, s8)

def test_hit5():
    row = 5
    column = 1
    s0 = (5, 7, False, 4, set())
    s1 = (3, 6, True, 3, set())
    s2 = (1, 4, True, 3, set())
    s3 = (2, 2, False, 2, set())
    s4 = (8, 9, False, 2, set())
    s5 = (6, 4, True, 2, set())
    s6 = (7, 0, True, 1, set())
    s7 = (9, 0, True, 1, set())
    s8 = (9, 3, True, 1, set())
    s9 = (7, 2, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert hit(row, column, fleet) == False



def test_are_unsunk_ships_left0():
    s0 = (1, 1, True, 4, {(1, 1), (1, 2), (1, 3), (1, 4)})
    s1 = (3, 1, False, 3, {(3, 1), (4, 1), (5, 1)})

    fleet = [s0, s1]
    assert type(are_unsunk_ships_left(fleet)) == bool

def test_are_unsunk_ships_left1():
    s0 = (1, 1, True, 4, {(1, 1), (1, 2), (1, 3), (1, 4)})
    s1 = (3, 1, False, 3, {(3, 1), (4, 1), (5, 1)})

    fleet = [s0, s1]
    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left2():
    s0 = (1, 1, True, 4, set())
    s1 = (3, 1, False, 3, set())
    s2 = (7, 9, False, 3, set())
    s3 = (8, 0, False, 2, set())
    s4 = (3, 7, True, 2, set())
    s5 = (5, 6, True, 2, set())
    s6 = (7, 3, True, 1, set())
    s7 = (7, 5, True, 1, set())
    s8 = (9, 4, True, 1, set())
    s9 = (8, 7, True, 1, set())
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left3():
    s0 = (1, 1, True, 4, set())
    s1 = (3, 1, False, 3, set())
    s2 = (7, 9, False, 3, set())
    s3 = (8, 0, False, 2, set())
    s4 = (3, 7, True, 2, set())
    s5 = (5, 6, True, 2, set())
    s6 = (7, 3, True, 1, {(7, 3)})
    s7 = (7, 5, True, 1, {(7, 5)})
    s8 = (9, 4, True, 1, {(9, 4)})
    s9 = (8, 7, True, 1, {(8, 7)})
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert are_unsunk_ships_left(fleet) == True

def test_are_unsunk_ships_left4():
    s0 = (1, 1, True, 4, {(1, 1), (1, 2), (1, 3), (1, 4)})
    s1 = (3, 1, False, 3, {(3, 1), (4, 1), (5, 1)})
    s2 = (7, 9, False, 3, {(7, 9), (8, 9), (9, 9)})
    s3 = (8, 0, False, 2, {(8, 0), (9, 0)})
    s4 = (3, 7, True, 2, {(3, 7), (3, 8)})
    s5 = (5, 6, True, 2, {(5, 6), (5, 7)})
    s6 = (7, 3, True, 1, {(7, 3)})
    s7 = (7, 5, True, 1, {(7, 5)})
    s8 = (9, 4, True, 1, {(9, 4)})
    s9 = (8, 7, True, 1, {(8, 7)})
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert are_unsunk_ships_left(fleet) == False

def test_are_unsunk_ships_left5():
    s0 = (1, 1, True, 4, {(1, 1), (1, 2), (1, 3)})
    s1 = (3, 1, False, 3, {(3, 1), (4, 1), (5, 1)})
    s2 = (7, 9, False, 3, {(7, 9), (8, 9), (9, 9)})
    s3 = (8, 0, False, 2, {(8, 0), (9, 0)})
    s4 = (3, 7, True, 2, {(3, 7), (3, 8)})
    s5 = (5, 6, True, 2, {(5, 6), (5, 7)})
    s6 = (7, 3, True, 1, {(7, 3)})
    s7 = (7, 5, True, 1, {(7, 5)})
    s8 = (9, 4, True, 1, {(9, 4)})
    s9 = (8, 7, True, 1, {(8, 7)})
    fleet = [s0, s1, s2, s3, s4, s5, s6, s7, s8, s9]
    assert are_unsunk_ships_left(fleet) == True

