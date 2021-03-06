MIN_N = 1
MAX_N = 100


def play():
    start = MIN_N
    end = MAX_N
    print(f'Загадайте число от {MIN_N} до {MAX_N}, а я отгадаю его максимум за 7 попыток.')
    print('Если загаданное число больше введите символ >')
    print('Если меньше, то введите >')
    print('Если я угадал число, введите символ =')
    attempts = 1
    while True:
        guess = (end + start) // 2
        print(f'Это {guess}?')
        answer = input()
        if answer == '>':
            start = guess + 1
            attempts += 1
        elif answer == '<':
            end = guess
            attempts += 1
        elif answer == '=':
            print(f'Ура! Спасибо за игру! Число попыток {attempts}')
            break
        else:
            print(f'Я могу понять только ответ в виде одного из символов: >, < или =. Попробуем еще раз.')
