# Project Title: Minesweeper

## Team Members:
- Cedric Murairi
- Mthabisi Ndlovu
- Samuel Anumudu

## Data Structure and Algorithm used:
- Data Structure: 2D arrays and single arrays
    - These Data Structures are used to store cell location on the screen and build up the board game. We used two dimensions arrays to come up with rows, columns, and individual cells for the Game.

- Algorithm: Depth First Search Algorithm
    - The algorithm plays a critical part in playing the game; given that each time a user clicks a cell, it get revealed if it is empty or displays the number of mined cells around,.We chose to use Depth First Search since you need to check every adjacent cell to the current cell if they got mines; if not, you do it recursively until you find mined cells around. And that's for each cell, starting from the one that got clicked.

## Project Description:
Minesweeper is a single-player puzzle video game. The game's objective is to clear a rectangular board containing hidden "mines" or bombs without detonating any of them, with help from clues about the number of neighboring mines in each field. The game originates from the 1960s, and it has been written for many computing platforms in use today. It has many variations and offshoots.

Some Minesweeper versions will set up the board by never placing a mine on the first square revealed. However, our version will have a mine in the first square in some cases since the pattern is random.

If a square containing a mine is revealed, the player loses the game. If no mine is revealed, a digit is instead displayed in the square, indicating how many adjacent squares contain mines; if no mines are adjacent, the square becomes blank, and all adjacent squares will be recursively revealed. The player uses this information to deduce the contents of other squares and may either safely reveal each square or mark the square as containing a mine.

There is only one life for the entire game, so you die once you hit the wrong spot. And the only way to win is to reveal all the empty squares or cells successfully

## Project Motivation:
This project is the sole purpose to play around with search algorithm, in this case being the "Depth First Search Algorithm". And we found out that Minesweeper would be a great fit to illustrate this, however, dealing with arrays, not trees or graphs.

It is an algorithm for exploring a graph, a tree, or another data structure systematically. In a depth-first search, you go as far in any direction you can before backtracking and trying a different approach.
To traverse or search this tree using depth-first search, you start at the top. You then go left until you hit a place where you must choose, and then again, you take the left branch. If you find no paths are branching off a node, then you backtrack and then go right. You do this until you achieve your goal.

However, Minesweeper does not have anything that looks like a tree. It turns out you can still use depth-first search when revealing squares after a player's click. When the player clicks on a square with no mines nearby, we reveal that square. Then we check to see if the square above it has any mines nearby. If it does not, we check the square above that one and so on until we find a square with mines nearby. After we find a square with mines nearby, we check all of its neighbors (upper right, right, lower right…) going clockwise until we find a neighbor without any mines nearby (value 0) and then making that one my current focus.

## How to run
If you want to run this application and test it on your local environment, here are few things you need to check off to get it up and running, it won't run if you do not follow the instructions:

### SetUp Development Environment
- This project uses Python Programming language with a Processing layer; you can learn more about [Processing](https://www.processing.org). With that in mind the first thing you need to do is have Python 3 or above installed on your machine.
- Next you need of course Processing itself and you can download it from [the official Processing site](https://www.processing.org/download/)
- Then you need to install the downloaded Processing application depending on your operating system
- After that, you need to open it up and install the Python Mode as shown in the picture bellow:

![Installing Python Mode in Processing](https://camo.githubusercontent.com/8154f4f84860569c2a4851c0ce187bd00cf89d0f477b94b2c30a01db40550954/687474703a2f2f70792e70726f63657373696e672e6f72672f6164645f6d6f64652e706e67)

![Installing Python Mode in Processing step 2](https://camo.githubusercontent.com/108b2a67bcf6c78fca5d5e74afa18f2fa1f2aa7ff6de9a95693fd2be44bd8893/687474703a2f2f70792e70726f63657373696e672e6f72672f696e7374616c6c2e706e67)

### Clone the repository on you local machine and get ready
- Make sure you are in processing and click File -> Open
- A window should open depending on your OS, leading you to your Finder or File Manager
- Make sure you navigate to the right location you cloned the repo
- Open the application folder and finally select Mineswepper.pyde
- If you followed all the steps above, this should bring you back to processing with the application code
- After that, what you need is to hit RUN and you should see the Game

## Bibliography/References:
- Processing Foundation, 2018. Processing Mode Installation--01. [image] Available at: <https://camo.githubusercontent.com/8154f4f84860569c2a4851c0ce187bd00cf89d0f477b94b2c30a01db40550954/687474703a2f2f70792e70726f63657373696e672e6f72672f6164645f6d6f64652e706e67> [Accessed 21 April 2021].
- Processing Foundation, 2018. Processing Python Mode Installation--02. [image] Available at: <https://camo.githubusercontent.com/108b2a67bcf6c78fca5d5e74afa18f2fa1f2aa7ff6de9a95693fd2be44bd8893/687474703a2f2f70792e70726f63657373696e672e6f72672f696e7374616c6c2e706e67> [Accessed 21 April 2021].
- En.wikipedia.org. 2021. Minesweeper (video game) - Wikipedia. [online] Available at: <https://en.wikipedia.org/wiki/Minesweeper_(video_game)> [Accessed 22 April 2021].