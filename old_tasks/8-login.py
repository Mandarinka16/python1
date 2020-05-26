# Сделать программу, которая собирает данные пользователей -
# в нем можно ввести логин пользователя и почту,
# и если с помощью проверки регулярными выражениями валидны,
# тогда они записываются в файл. В другом случае, пользователю говорится,
# что у него ошибка в введеных данных и нужно заново ввести данные.
import re


def check_login(log):
    if re.fullmatch("([a-zA-Z]+[a-zA-Z0-9\_]+){,20}", log.lower()):
        return True
    else:
        return False


def check_mail(mail):
    if re.fullmatch("[\w\d_-]+[\w\d\-_.]+[\w\d]+@\w+\.\w+", mail.lower()):
        return True
    else:
        return False


print("Вас приветствует программа учета логина/почты пользователей")
print("Логин может состоять из букв, цифр и нижнего подчеркивания, начинаться должен с буквы. "
      "Максимальная длина 20 символов")
success = False
while not success:
    max_users = input("Сколько пользователей вы собираетесь добавить? ")
    if max_users.strip().isdigit() and int(max_users) > 0:
        max_users = int(max_users)
        success = True
    else:
        print("Вы ввели некорректное число, попробуйте снова")

name_of_file = input("Введите название файла, в который будут сохраняться пользователи (без расширения): ") + ".txt"
users = 1
with open(name_of_file, 'w') as file:
    while users <= max_users:
        login = input("Введите логин " + str(users) + "-го пользователя: ")
        if check_login(login):
            mail_address = input("Введите почту " + str(users) + "-го пользователя: ")
            if check_mail(mail_address):
                file.write(login + ", " + mail_address + "\n")
                users += 1
            else:
                print("Почта введена некорректно!")
        else:
            print("Логин введен некорректно!")


