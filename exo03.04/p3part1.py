table=[[" . "" . "" . "" . "" . "" . "],[" . "" . "" . "" . "" . "" . "],[" . "" . "" . "" . "" . "" . "],[" . "" . "" . "" . "" . "" . "],[" . "" . "" . "" . "" . "" . "]]

winner=None
player=1

def display_grid(table):
    count=-1
    for line in table:
        count+=1
        txt = ""
        for value in line:
            txt += str(count)+" "+str(value)
            print(str(txt))
            for i in table[0]:
                i += f"{i}"
                print(i)


def chek_winner(grid,current_player):
    if current_player == 2:
        return True
    return False




