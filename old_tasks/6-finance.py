#дз 1.  Cделать программу  финансового учета, которая на вход принимает файл, который ей указали,
# в котором цифры должны быть расположены построчно.
# Программа выдает простейшие статистики, такие как суммы и среднее, которые она записывает в файл вывода,
# которые она сама генерирует

#files/fininput.txt - тестовый файл
name_of_file = input("Введите имя файла финансового учета, по которому будем считать статистику: ")

name_out_sum = "files/result/fin_sum.txt"
name_out_avr = "files/result/fin_avr.txt"
with open(name_out_sum, 'w') as file_sum:
    file_sum.write("Сумма показателей(построчно):\n")
with open(name_out_avr, 'w') as file_avr:
    file_avr.write("Среднее значение показателей(построчно):\n")

with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        line_list = line.strip().split(' ') #["1","2","3"]
        sum = 0
        for digit in line_list:
            sum += int(digit) #6
        avr = sum / len(line_list) #2
        with open(name_out_sum, 'a') as file_sum:
            file_sum.write(str(sum) + "\n")
        with open(name_out_avr, 'a') as file_avr:
            file_avr.write(str(avr) + "\n")
print("Результаты расчетов были записаны в файлы fin_sum.txt, fin_avr.txt в папке result")