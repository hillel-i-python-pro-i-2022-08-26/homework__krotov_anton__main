#Game WORDS

igroki = []


def player():

    players = input()
    while players != "Start":
         print(player())
         igroki.append(players)
         print(igroki)
    else:
        print(igroki)
        print("Поехали")

player()
