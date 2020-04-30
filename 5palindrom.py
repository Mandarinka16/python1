def palindrom(str):
    str = str.lower().strip()
    list1 = []
    for i in str:
        if i not in [" ", "_","-","!","?",",",".",":",";"]:
            list1.append(i)
    list2 = list1[:]
    list2.reverse()
    if list1 == list2:
        return 1
    else:
        return 0

word = input("Введите слово или фразу, и я скажу, является ли оно палиндромом\n:")
if palindrom(word) == 1:
    print("Да, это слово/фраза - палиндром")
else:
    print("Нет, это слово/фраза - не палиндром")
