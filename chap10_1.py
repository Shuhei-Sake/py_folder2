def hangman(word):
    while true:
        if type(word) == list:
            break
        else:
            print('引数はlistにしてね!')
            
    wrong = 0
    stages = ['',
              '_______         ',
              '|               ',
              '|      |        ',
              '|      0        ',
              '|     /|\       ',
              '|     / \       ',
              '|               '
              ]
    import random
    listlen = random.randint(0, len(word))
    answer = word[listlen]
    rletters = list(answer)
    board = ['_'] * len(answer)
    win = False
    print('ハングマンへようこそ!')
    
    while wrong < len(stages) - 1:
        print('\n')
        msg = '1文字を予想してね'
        char = input(msg)
        if char in rletters:
            cing = rletters.index(char)
            board[cing] = char
            rletters[cing] = '$'
        else:
            wrong += 1
        print(' '.join(board))
        e = wrong + 1
        print('\n'.join(stages[0:e]))
        if '_' not in board:
            print('あなたの勝ち!')
            print(' '.join(board))
            win = True
            break

    if not win:
        print('\n'.join(stages[0:wrong+1]))
        print('あなたの負け!正解は {}'.format(word))
