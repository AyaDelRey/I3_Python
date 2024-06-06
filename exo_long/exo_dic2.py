ranks = {"Marie": 1,"Bernard" : 4,"François": 2,"Thomas": 12,"Hila": 15}
sum_rank = 0




for rank in ranks.values():
    sum_rank += ranks

avg= sum_rank / len(ranks)

print("Moyenne du club: "+ str(avg))