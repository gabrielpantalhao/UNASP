def grupos():
    i = 1
    victory = 0
    while i <= 6:
        i += 1
        games = input()
        if games == "V" :
            victory += 1
     
            
    if victory <= 2 and victory > 0:
        return 3
    elif victory > 2 and victory <= 4:
        return 2
    elif victory > 4 and victory <= 6:
        return 1
    elif victory == 0:
        return -1
    
print(grupos())