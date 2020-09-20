# Index
- [Usage](#Usage)
    - [Dependencies](##Dependencies)
    - [Installation](##Installation)
- [Resources](#Resources)
- [Gallery](#Gallery)
- [Licence](#Licence)

# Usage
It suffices with downloading the repository and running the `run.py` file from the root directory of the project. Executing the following command (from project root directory) will run the program:
```
python run.py
```
A Graphical User Interface (GUI) will appear, in which the numbers of columns and rows to be generated can be entered, along with an entry for the size of the maze.

Once all three fields have been filled up without any validation conflicts, pressing the `Generate` buttom will display the maze as it's being generated, and the recursive-backtracking algorithm can be seen at play.

## Dependencies
- `Pygame`

## Installation
In order to successfully run the program though, the library `Pygame` must be installed. In order to not pollute the local Python installation with third-party libraries, a virtual environment can be created in which third-party libraries can be installed without affecting the local Python installation.

In order to create a virtual environment, navigate to the project root directory and enter the following command (on a Unix-based system):
```
python3 -m venv .venv
```
where `.venv` is the virtual environment directory name.

On Windows, the command remains all the same except instead of typing `python3`, one should type `python`.

Now that the virtual environment has been created, it must be activated. On a Unix-based system, the following command will activate the virtual environment:
```
source ./.venv/bin/activate
```
On Windows, the `activate` script must be ran, depending on the shell used. Assuming that Powershell is being used, typing:
```
.\.venv\Scripts\Activate.ps1
```
would activate the virtual environment.

These commands will only work if executed in the same directory where `.venv` is.

Once activated, third-party libraries can be installed in the virtual environment. In order to install all libraries contained in the `requirements.txt` file, type the following command:
```
pip install -r requirements.txt
```
which should work on both Unix-based systems and on Windows.


# Resources
- [Maze Generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm) (Wikipedia)
- [Maze Generator with with `p5.js`](https://thecodingtrain.com/CodingChallenges/010.1-maze-dfs-p5.html) (The Coding Train)
