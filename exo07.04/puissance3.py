TOKEN_1 = "X"
TOKEN_2 = "O"

def get_token(player):
    if player == 1:
        return TOKEN_1
    return TOKEN_2


def display_grid(grid):
    for line in range(len(grid)):
        text = ""
        for col in range(len(grid[line])):
            text = text + " " + grid[line][col]
        print(str(line) + text)

    text = ""
    for last_line in range(len(grid[0])):
        text = text + f" {last_line}"
    print(f" {text}")


def display_grid2(grid):
    i = 0
    for line in grid:
        text = ""
        for element in line:
            text = text + " " + element
        print(str(i) + text)
        i = i + 1

    text = ""
    i = 0
    for last_line in grid[0]:
        text = text + f" {i}"
        i = i + 1
    print(f" {text}")


def check_vertical(grid, column, line):

    if line >= 3:
        return False
    
    if grid[line][column] == grid[line + 1][column]:
        if grid[line][column] == grid[line + 2][column]:
            return True

    return False


def check_winner(grid, column, current_player):

    line = 0

    while grid[line][column] == '.':
        line += 1

    if check_vertical(grid, column, line):
        return True
    

    return False


def play(grid, column, player):
    
    # trouver pour la colonne passeée en paramètre la première ligne vide
    line = 4

    while grid[line][column] != '.' and line > -1:
        line -= 1

    # placer le bon token dans la colonne à la ligne trouvée. 
    if line > -1:
        grid[line][column] = get_token(player)

    return grid


tableau = [
    [".", ".", ".", "O", "."],
    [".", ".", ".", "O", "."],
    [".", ".", ".", "O", "."],
    [".", ".", ".", "O", "."],
    [".", ".", ".", "O", "."],
]

winner = None
player = 1

while winner == None:
    display_grid(tableau)

    column = input(f"Joueur {get_token(player)}, où va tu jouer? ")
    column = int(column)

    play(tableau, column, player)

    if check_winner(tableau, column, player):
        winner = player
    else:
        if player == 1:
            player = 2
        else:
            player = 1
