# Battleship
An assignment done for my Principles of Programming class in Birkbeck in 2021 fall semester.
The images below were provided by the instructor to us.

About the game:

This assignment asked the student to create a one player version of the game battleship, where one inputs co-ordinates in order to sink all the ships of your opponent. 
In the one player version your only goal is to sink all the ships the game generates in the fewest number of total shots.  
The locations of all the ships are generated randomly each time and there are a total of 10 ships of various sizes in a sea of 10x10 squares.

The ships that we are looking to sink are:
One battleship, occupying 4 squares
Two cruisers, each occupying 3 squares
Three destroyers, each occupying 2 squares
Four submarines, each occupying 1 square

![ships](https://www.dcs.bbk.ac.uk/~vlad/pop1/project2021/battleships.PNG)

The random ship placement follows the rules of the battleship game, meaning that each ship can be placed either horizontally or vertically and no ships may be immediately adjacent to each other, either horizontally, vertically, or diagonally.

![legal and illegal arrangements](https://www.dcs.bbk.ac.uk/~vlad/pop1/project2021/arrangement.PNG)

Everytime the player takes a shot the computer will tell whether it is a hit or a miss, and it will keep track of all the shots made so far and show it graphically.
Once a ship is sunk, it is told to the player.
Once all the ships are sunk, the game is over :)

About the files:

There are 2 files I am sharing here, one is for the game and the other is for the testing.
The assignment asked us to use a test driven approach to coding so all the tests for the functions used were developed before the functions were.
Tests were done using pytest and they can be found in the test_battleship file.


