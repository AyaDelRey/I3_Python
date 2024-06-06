def display_grid(grid):
    for line in grid:
        if len(grid)>9:
            print("Tableau trop grand")
            return None
        text = ""
        for element in line:
            if element < 10:
                print(element, end='  ')
            else:
                print(element, end=' ')
        print(text)

def create_grid(lines, cols):
    if lines > 9 or cols > 9:
        print("Tableau trop grand")
        return None
    
    grid = []
    count = 1
    for i in range(lines):
        line = []
        for j in range(cols):
            line.append(count)
            count += 1
        grid.append(line)
    return grid

def create_snake(lines, cols):
    grid = []
    count = 1
    for i in range(lines):
        line = list(range(count, count + cols))
        count += cols
# l'expression if i % 2 == 0 est utilisée pour tester si l'indice de la ligne est pair
        if i % 2 != 0:
            line.reverse()
        grid.append(line)
    return grid

def colimaçon(lines, cols):

    result=[]

    for i in range(lines):
        line=[]
        for j in range(cols):
            line.append(0)
        result.append(line)

    elem = 1
    start_line=0
    end_line=lines-1
    start_col=0
    end_col=cols-1

    while start_col<=end_col and start_line<=end_line:

        for c in range(start_col,end_col+1):
            result[start_line][c] = elem
            elem += 1

        if elem>lines*cols:
            break


        for l in range(start_line+1,end_line+1):
            result[l][end_col] = elem
            elem+=1
        if elem>lines*cols:
            break

        # B : tu avais mis "-start_col" dans ton range
        for c in range(end_col-1,start_col-1,-1):
            result[end_line][c]= elem
            elem+=1
        if elem>lines*cols:
            break




        for l in range(end_line-1,start_line,-1):
            result[l][start_col] = elem
            elem+=1

        if elem>lines*cols:
            break


        start_line+=1
        start_col+=1
        end_line-=1
        end_col-=1

    return result



def ask_type_rangement():
    while True:
        choix = input("Choisissez un type de rangement (N pour normal, S pour serpent, E pour escargot) : ")
        if choix in ['N', 'S', 'E']:
            return choix
        else:
            print("Veuillez choisir parmi les options proposées.")

lines = int(input("Entrez le nombre de lignes : "))
cols = int(input("Entrez le nombre de colonnes : "))
type_rangement = ask_type_rangement()
    
if type_rangement == 'N':
        tableau = create_grid(lines, cols)
elif type_rangement == 'S':
        tableau = create_snake(lines, cols)
elif type_rangement == 'E':
        tableau = colimaçon(lines, cols)
    
print("voilààà!:")
display_grid(tableau)






