# дз 11
import re
import SnakeGame


class Validate:
    @staticmethod
    def validate_login(login):
        if re.fullmatch("([a-zA-Z]+[a-zA-Z0-9\_]+){,20}", login.lower()):
            return True
        else:
            return False

    @staticmethod
    def validate_password(password):
        if re.fullmatch("[A-Za-z0-9]{6,20}", password.lower()):
            return True
        else:
            return False


class User:
    # инициализация
    def __init__(self, login, password, unique_id):
        self.login = login
        self.password = password
        self.unique_id = str(unique_id)

    # добавление нового юзера в общий файл со списком пользователей
    def add_user(self):
        with open("profiles/login_list.txt", 'a') as file:
            file.write(self.unique_id + ", " + self.login + ", " + self.password + "\n")

    # создание файла с профилем пользователя
    def create_profile(self):
        name = "profiles/login" + self.unique_id + ".txt"
        with open(name, 'w') as file:
            file.write("Профайл пользователя " + self.login + "(уникальный номер " + self.unique_id + "\n")


# проверка существования пользователя и регистрация нового
def greet_user():
    answer = input("Приветствуем! Вы уже зарегистрированы в системе? Да/нет: ")
    if answer.lower().strip() == "да":
        # проверяем логин и пароль пользователя
        print("Данная программа предназначена только для новых пользователей")
        exit()
    else:
        # регистрируем нового пользователя
        # сначала определяем основные данные
        with open("profiles/login_list.txt") as file:
            lines = file.readlines()
        user_id = len(lines) + 1
        end = False
        while not end:
            user_login = input("Введите логин(до 20 символов, цифры+буквы+нижнее подчеркивание): ")
            user_password = input("Введите пароль(6-20 символов, цифры+буквы): ")
            if Validate.validate_login(user_login) and Validate.validate_password(user_password):
                # все ок, заводим пользователя
                new_user = User(user_login, user_password, user_id)
                new_user.add_user()
                new_user.create_profile()
                end = True
            else:
                print("Вы ввели недопустимые значения для логина или пароля, в регистрации отказано, попробуйте снова!")


greet_user()
print("Добро пожаловать в систему! Предлагаем сыграть в следующую игру")
SnakeGame.launch_game()
exit()