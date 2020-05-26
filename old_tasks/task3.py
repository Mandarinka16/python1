print("*****ТАБЛИЦА УМНОЖЕНИЯ*****")
maxlen = 10 #максимальное значение длины у 9 * 9 = 81
for j in range(1,10):
    temp_str = ""
    for i in range(1,10):
        result = str(i) + " * " + str(j)+" = "+str(i*j)
        while len(result) < 10:
            result = result + " "
        temp_str = temp_str + result + "   "
    print(temp_str)