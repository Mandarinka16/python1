##дз Написать код для класса Calculator, у которого есть все методы, которые выполняют математические
# операции = сложение, вычитание, деление, умножение. Класс должен быть покрыт тестами, в котором тестируется его работа,
# если пользователь забивает 1.цифру 2.букву 3.Пустой символ

class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def func_add(self):
        return self.x + self.y

    def func_sub(self):
        return self.x - self.y

    def func_mult(self):
        return self.x * self.y

    def func_div(self):
        try:
            result = self.x / self.y
        except ZeroDivisionError:
            return print("На ноль делить нельзя!")
        else:
            return result
