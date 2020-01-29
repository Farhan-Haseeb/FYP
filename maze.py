def nomanMaze():
  maze = []
  maze.append([" "," "," "," "," "," "," "," "," "," "," "," "])
  maze.append(["#"," ","#","#"," ","#","#"," ","#"," ","#"," "])
  maze.append([" "," "," ","#"," "," "," "," "," "," "," "," "])
  maze.append([" ","#"," ","#","#"," ","#","#"," ","#","#"," "])
  maze.append([" "," "," "," "," "," "," "," "," "," "," ","O"])
  maze.append(["#"," ","#","#"," ","#","#"," ","#","#"," ","#"])
  maze.append(["#"," ","#","#"," ","#","#"," ","#","#"," ","#"])
  maze.append([" "," "," "," "," "," "," "," "," "," "," "," "])
  maze.append([" ","#","#"," ","#","#"," ","#","#"," ","#"," "])
  maze.append([" "," ","#"," ","#","#"," ","#","#"," ","#"," "])
  maze.append(["#"," "," "," "," "," "," "," "," "," "," "," "])
  maze.append(["#"," ","#","#"," ","#"," ","#"," ","#","#"," "])
  maze.append(["#"," ","#","#"," ","#"," "," "," "," "," "," "])
  maze.append([" "," "," "," "," "," "," ","#"," ","#"," ","#"])
  maze.append([" ","#","#","#"," ","#"," ","#"," ","#"," ","#"])
  maze.append([" "," "," "," "," "," ","X"," "," "," "," "," "])

  return maze

def createMaze():
    maze = []
    maze.append(["#","#", "#", "#", "#", " ","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", "#", " ","#"])
    maze.append(["#"," ", "#", " ", " ", " ","#"])
    maze.append(["#"," ", "#", "#", "#", "O","#"])
    maze.append(["#"," ", " ", " ", "#", " ","#"])
    maze.append(["#","#", "#", "#", "#", "X","#"])

    return maze

def createMaze2():
    maze = []
    maze.append(["#","#", "#", "#", "#", "O", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#"," ", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", "X", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#"," ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#"," ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#","#", "#", "#", "#", "#", "#", "#", "#"])

    return maze