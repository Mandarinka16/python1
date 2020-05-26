def calc(num1, num2, oper):
    if oper == 1:
        result = num1 - num2
        return print(str(num1)," - ", str(num2), " = ", str(result))
    else:
        result = num1 + num2
        return print(str(num1), " + ", str(num2), " = ", str(result))


print("*** Вас приветствует элементарный калькулятор ***\n")
while True:
    print("Для выхода из программы введите exit вместо числа")
    number1 = input("Введите первое число: ").lower().strip()
    if number1 == "exit":
        break
    number2 = input("Введите второе число: ").strip()
    operation = input("Введите операцию, выполняемую над числами:\n1 - вычитание, 2 - сложение: ").strip()
    if number1.isdigit() and number2.isdigit() and operation.isdigit() and operation in ["1", "2"]:
        calc(int(number1), int(number2), int(operation))
    else:
        print("!!! Невозможно выполнить операцию, т.к. вы ввели некорректные данные! Попробуйте снова")
