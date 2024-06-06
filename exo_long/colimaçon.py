def colimaçon(lines, cols):
    grid = [[0] * cols for _ in range(lines)]  
# Création du tableau avec des zéros
    
    value = 1
    gauche = 0
    droite = cols - 1
    haut = 0
    bas = cols - 1
    
    while value <= lines * cols:
# Remplissage de la partie supérieure de gauche à droite
        for j in range(gauche, droite + 1):
            grid[haut][j] = value
            value += 1
        haut += 1
        
# Remplissage de la partie droite de haut en bas
        for i in range(haut, bas + 1):
            grid[i][droite] = value
            value += 1
        droite -= 1
        
# Remplissage de la partie inférieure de droite à gauche
        for j in range(droite, gauche - 1, -1):
            grid[bas][j] = value
            value += 1
        bas -= 1
        
# Remplissage de la partie gauche de bas en haut
        for i in range(bas, haut - 1, -1):
            grid[i][gauche] = value
            value += 1
        gauche += 1
    
    return grid