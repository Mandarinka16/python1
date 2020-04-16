import datetime

# Функция, проверяющая, прошел ли день рождения у человека в текущем году (для точного определения возраста)
def check_b_day():
    bday_gone_quiz = (input("Ваш День рождения в этом году уже прошел? Введите да/нет: ")).strip().lower()
    if bday_gone_quiz == "да":
        return True
    elif bday_gone_quiz == "нет":
	    #b_day_today = (input("Возможно, Ваш День Рождения сегодня? Введите да/нет: ")).strip()
	    #if b_day_today == "да":
		#    birthday_gone = True
		#    print("Поздравляю с Днем Рождения!")
        return False
    else:
        print("Вы ввели некорректный ответ, попробуйте снова")
        return check_b_day()


# Функция, которая выясняет возраст человека в текущем году
def how_old() -> int:
    age = input ("Сколько Вам лет?  ").strip()
    if age.isdigit():
    #если введено число
    # 117 - возраст самого старого человека в мире 
        age = int(age)
        if age > 117:
	        print("Вы долгожитель, это здорово!")
        now = datetime.datetime.now()
        if check_b_day() is False: 
            age += 1
        return int(now.year) - age     
    else:
        print("К сожалению, Вы ввели не число, повторите попытку")
        return how_old()

# Фукнция, которая вычисляет, сколько человеку было или будет в заданном году
def define_age(birth_year: int):
    year = input("Введите интересующий Вас год и я скажу, сколько лет Вам будет: ").strip()
    if year.isdigit():
        year = int(year)
        now = datetime.datetime.now()
        if year < birth_year:
            print("В этот год Вы еще не родились")
        elif year==birth_year:
            print("В этом году Вы родились")
        elif year < int(now.year):
            result = year - birth_year
            print("В этом году Вам было " + str(result))
        else:
            result = year - birth_year
            print("В " + str(year) + " году Вам будет " + str(result))
    else:
        if year.strip().lower() == "выход":
            return print("Спасибо за внимание! Всего хорошего!")
        else:
            print("Вы ввели не числовое значение/Программа не поддерживает заданный формат")
    print("Для выхода из программы введите слово 'выход' вместо года")
    define_age(birth_year)



print("Здравствуйте! Вас приветствует программа по определению Вашего возраста в заданный год")
# Определяем год рождения
birth_year = how_old()
# Отвечаем на вопрос - сколько лет будет в заданный год
define_age(birth_year)