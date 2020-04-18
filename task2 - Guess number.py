import random


def define_attempts() -> int:
    difficulty = input("Выберите сложность игры (1 - низкий, 2 - средний, 3 - сложный:  ")
    while not difficulty.isdigit():
        print("Такого уровня сложности нет! Попробуйте снова! ")
        difficulty = input("Выберите сложность игры (1 - низкий, 2 - средний, 3 - сложный:  ")
    dff = int(difficulty)
    if dff == 1:
        return 12
    elif dff == 2:
        return 9
    elif dff == 3:
        return 6
    else:
        print ("Ошибка, попробуйте снова")
        return define_attempts()


def define_limit() ->int:
    lim = input("Задайте ограничение для загадываемых чисел (например, 25 - будем загадывать числа от 1 до 25): ")
    if lim.strip().isdigit():
        return int(lim)
    else:
        print("Неверно задано ограничение! Введите число")
        return define_limit()


def game():
    limit = define_limit()
    number = random.randint(1, limit)
    attempts = define_attempts()
    print("Проверьте свою удачу! Я загадаю число от 1 до " + str(limit) + ", а вы попробуете угадать")
    for i in range(attempts):
        guess_number = input("Ваша " + str(i+1) + " попытка: ")
        while not guess_number.isdigit():
            print("Вы ввели не числовое значение! Попробуйте снова! ")
            guess_number = input("Ваша " + str(i+1) + " попытка: ")
        if number == int(guess_number):
            print("Поздравляем! Вы выиграли!")
            if input("Хотите попробовать снова? Для продолжения введите да: ").strip().lower() == "да":
                return game()
            else:
                return print("Спасибо за игру! Всего хорошего! ")
        else:
            if number > int(guess_number):
                if number - int(guess_number) < 6:
                    print("Горячо! Загаданное число больше!")
                else:
                    print("Холодно! Загаданное число больше!")
            if number < int(guess_number):
                if int(guess_number) - number < 6:
                    print("Горячо! Загаданное число меньше!")
                else:
                    print("Холодно! Загаданное число меньше!")
            if i == attempts-1:
                print("Вы проиграли! Заданное число было " + str(number))
                print("Не расстраивайтесь, в следующий раз вам обязательно повезет!")
                if input("Хотите попробовать снова? Для продолжения введите да: ").strip().lower() == "да":
                    return game()
                else:
                    return print("Спасибо за игру! Всего хорошего и удачи! ")



print("Вас приветствует программа Угадай число!")
game()