
name_of_file = "pi.txt"
print("Пришло время узнать, есть ли ваша дата рождения в числе Пи")

pi_str = ''
with open(name_of_file) as file:
    lines = file.readlines()
    for line in lines:
        pi_str += line.strip()

birth = input("Введите дату вашего рождения?: ")

result = pi_str.find(birth) - 1 #отнимаем 1, чтобы считать, начиная с 1-го символа после точки
if result > 0:
    print("Здорово! Дата вашего рождения в числе ПИ на ", result, "-", result+len(birth)-1, "символах после точки!")
else:
    print("К сожалению, вашего дня рождения нет в числе Пи")
