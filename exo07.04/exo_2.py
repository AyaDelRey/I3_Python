tableau=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
somme=0
def somme_grid(grid):  
    somme=0 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            somme=somme+grid[i][j]
    print(somme)
            

somme_grid(tableau)