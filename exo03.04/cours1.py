grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

for line in range(len(grid)):
    txt= ""	

    for column in range(len(grid[line])):
        txt+= f"{grid[line][column]/2}"
    print(txt)