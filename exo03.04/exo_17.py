symboles = ["cœur", "carreau", "pique", "trèfle"]
valeurs = ["as", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix", "valet", "dame", "roi"]

for symbole in symboles:
    for valeur in valeurs:
        print(str(valeur) + ' de ' + str(symbole))
        #f"{valeur} de {symbole}" = string formaté
