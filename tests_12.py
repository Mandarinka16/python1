# если пользователь забивает 1.цифру 2.букву 3.Пустой символ

import unittest
from task12 import Calculator


class CalcTest(unittest.TestCase):
    def test_addition1(self):
        """Сложение - позитианя проверка (пользователь ввел цифры)"""
        test = Calculator(15, 8).func_add()
        self.assertEqual(test, 23)

    def test_substraction1(self):
        """Вычитание - позитианя проверка (пользователь ввел цифры)"""
        test = Calculator(15, 8).func_sub()
        self.assertEqual(test, 7)

    def test_multiplication1(self):
        """Умножение - позитианя проверка (пользователь ввел цифры)"""
        test = Calculator(15, 8).func_mult()
        self.assertEqual(test, 120)

    def test_division1(self):
        """Деление - позитианя проверка (пользователь ввел цифры)"""
        test = Calculator(20, 10).func_div()
        self.assertEqual(test, 2)

    def test_addition2(self):
        """Сложение - буквы"""
        with self.assertRaises(TypeError):
            Calculator("sd", "A").func_add()

    def test_substraction2(self):
        """Вычитание - буквы"""
        with self.assertRaises(TypeError):
            Calculator("B", "7D").func_sub()

    def test_multiplication2(self):
        """Умножение - буквы"""
        with self.assertRaises(TypeError):
            Calculator("7F", "FF").func_mult()

    def test_division2(self):
        """Деление - буквы"""
        with self.assertRaises(TypeError):
            Calculator("Aasf", "т").func_div()

    def test_addition3(self):
        """Сложение - пробел"""
        with self.assertRaises(TypeError):
            Calculator(" ", "A ").func_add()

    def test_substraction3(self):
        """Вычитание - пробел"""
        with self.assertRaises(TypeError):
            Calculator(" ", " ").func_sub()

    def test_multiplication3(self):
        """Умножение - пробел"""
        with self.assertRaises(TypeError):
            Calculator("   ", " ").func_mult()

    def test_division3(self):
        """Деление - пробел"""
        with self.assertRaises(TypeError):
            Calculator(" ", " ").func_div()


unittest.main()