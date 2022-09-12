# Game WORDS

igroki = []
words = []

players = None

def player(): # функция которая отвечает за создание игроков
    while True:
        players = input("Введите имя игрока: ")
        if players == "Start":
            print("Сейчас играют: ", igroki)
            print(" \n Начало игры \n")
            break
        else:
            igroki.append(players)


def game_start(): # финкционал игры, сохранение в список введеных слов, проверка на повторение, проверка первой и последней буквы в словах
    while True:
        for i in igroki:
            word = input()
            print("Игрок ", i, "Ввел слово ", word)
            while word in words:
                if word in words:
                    print(i, "это слово уже вводилось, введите другое")
                    word = input()
                elif word == "exit":
                    print("Конец игры!")
                    return 0
                else:
                    words.append(word)
                    break

            words.append(word)


player()
game_start()
