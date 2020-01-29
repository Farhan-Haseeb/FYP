import queue
from maze import createMaze, createMaze2, nomanMaze

import time

start_time = time.time()

def position(maze):
    rows = 0
    cols = 0
    found = False
    for row in maze:
        cols = 0
        for col in row:
            if "O" in col:
                found = True
                break
            else:
                cols += 1
        if found:
            break
        else:
            rows += 1
    return [rows, cols]


def printMaze(maze, path=""):
    location = position(maze)

    i = location[1]
    j = location[0]
    pos = set()
    for move in path:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1
        pos.add((j, i))

    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    location = position(maze)

    i = location[1]
    j = location[0]
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

        if not (0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif maze[j][i] == "#":
            return False

    return True


def findEnd(maze, moves):
    location = position(maze)

    i = location[1]
    j = location[0]
    for move in moves:
        if move == "L":
            i -= 1

        elif move == "R":
            i += 1

        elif move == "U":
            j -= 1

        elif move == "D":
            j += 1

    if maze[j][i] == "X":
        print(moves)
        printMaze(maze, moves)
        return True

    return False


# MAIN ALGORITHM

nums = queue.Queue()
coords = queue.Queue()
nums.put("")
coords.put("")
add = ""
maze = nomanMaze()

while not findEnd(maze, add):
    add = nums.get()
    for j in ["L", "R", "U", "D"]:
        put = add + j
        if valid(maze, put):
            nums.put(put)

print("--- %s seconds ---" % (time.time() - start_time))
