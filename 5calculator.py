def calc(num1, num2, operation):
    if operation == "1":
        return print(str(num1 - num2))
    else:
        return print(str(num1 + num2))


print("Вас приветствует элементарный калькулятор")

a = input("Введите первое число: ")
b = input("Введите второе число: ")
c = input("Введите операцию, выполняемую над числами:\n1 - вычитание, 2 - сложение: ")

calc(int(a), int(b), c)