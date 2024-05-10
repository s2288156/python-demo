def hangman(word):
    stage = [
        "                        ",
        "|                       ",
        "|-------------          ",
        "|            |          ",
        "|            O          ",
        "|           /|\\         ",
        "|           / \\         ",
        "|                       ",
    ]
    wrong = 0
    win = False
    board = ["_"] * len(word)
    rletters = list(word)
    print("welcome to hangman!")
    while wrong < len(word):
        print("\n")
        char = input("Guess a letter: ")
        if char in word:
            char_index = rletters.index(char)
            board[char_index] = char
            rletters[char_index] = '$'
        else:
            wrong += 1
        print("".join(board))
        if "_" not in board:
            print("You win!!!")
            win = True
            break

    if not win:
        print("\n".join(stage[0:]))
        print("You lose!!!It was [{}].".format(word))


hangman("banana")
