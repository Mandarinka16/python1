import random


numbers = [0,32,15,19,4,21,2,25,17,34,6,27,13,36,11,30,8,23,10,5,24,16,33,1,20,14,31,9,22,18,29,7,28,12,35,3,26]
colours = ["зеленый"]
for i in range(1,len(numbers)):
    if i % 2 != 0:
        colours.append("красный")
    else:
        colours.append("черный")

roulette = []
for i in range(0,len(numbers)):
    temp = str(numbers[i]) + " " + colours[i]
    roulette.append(temp)

bank = 1000
casino = 0
print("Вас приветствует Рулетка! У вас в активе 1000 рублей, делайте ставки и выигрывайте! \nВы выбираете вид ставки и сумму, если выпадает ячейка 1-36 и совпадает с вашей ставкой, вы выиграете, если выпадет 0 - проиграете")
print("Перед вами рулетка:")
print(roulette)
game = True

while bank > 0 and game:
    print("Выберите вид ставки\n1 - на число (четное/нечетное), выигрыш составит х2 от вашей ставки\n2 - на цвет(красный/черный), выигрыш составит х2 от вашей ставки\n3 - на конкретную ячейку, выигрыш составит х3 от вашей ставки")
    type_bet = input("Вид ставки: ")
    if type_bet == "1":
        bet = input("Выберите ставку:\n1 - четное \n2 - нечетное: ")
    elif type_bet == "2":
        bet = input("Выберите ставку:\n1 - красный \n2 - черный: ")
    if type_bet == "3":
        bet = input("Выберите ячейку (1-36): ")
    sum_bet = input("Сколько поставите? Ставка должна быть не более " + str(bank) + " рублей: ")
    bank -= int(sum_bet)
    random_roulette = roulette[:]
    random.shuffle(random_roulette)
    win = random.choice(random_roulette).split(' ')
    print("Выпала ячейка: " + win[0] + " " + win[1])
    if type_bet == "1":
        temp = int(win[0]) % 2
        if (temp == 0 and bet == "1") or (temp == 1 and bet == "2"):
            print("Поздравляем! Вы выиграли " + str(int(sum_bet)*2) + " рублей")
            bank += int(sum_bet)*2
        else:
            print("Вы проиграли " + sum_bet + " рублей")
            casino += int(bet)
    elif type_bet == "2":
        if (bet == "1" and win[1] == "красный") or (bet == "2" and win[1] == "черный"):
            print("Поздравляем! Вы выиграли " + str(int(sum_bet)*2) + " рублей")
            bank += int(sum_bet)*2
        else:
            print("Вы проиграли " + sum_bet + " рублей")
            casino += int(sum_bet)
    if type_bet == "3":
        if bet == win[1]:
            print("Поздравляем! Вы выиграли " + str(int(sum_bet)*3) + " рублей")
            bank += int(sum_bet)*3
        else:
            print("Вы проиграли " + sum_bet + " рублей")
            casino += int(sum_bet)
    if input("У вас в банке " + str(bank) + " рублей. Хотите продолжить играть? Введите да для продолжения: ").strip() == "да":
        game = True
    else:
        game = False
if bank == 0:
    print("У вас в банке 0 рублей. Ждем вас снова, всего хорошего и спасибо за игру!")
else:
    print("Спасибо за игру! Ждем вас снова!")
