def display_grid(grid):

    for line in grid:
        if len(grid)>=10 or len(line)>=10:
            print("Tableau trop grand")
            return None
        text = ""
        for element in line:
            if element < 10:
                print(element, end='  ')
            else:
                print(element, end=' ')
        print(text)

tab = [[1,2,3,4],
       [5,6,7,8,1,1,1,1,1,1,1,1,1,1],
       [9,10,11,12],
       [13,14,15,16],
       ]

display_grid(tab)