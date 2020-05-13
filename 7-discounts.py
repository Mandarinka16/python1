# Воспользоваться кодом из нашей функции assert
# прогнать все товары в словарь из файла  data.txt
# через скидки в discount.txt
# и итоговой товар с названием и ценником должен генерироваться программно

#Достаем исходные продукты и цены из файла
def get_products(input_file):
    products = {}
    with open(input_file,  "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            product = line.strip().split(',')
            try:
                products[product[0]] = product[1].strip()
            #если продукт и цена разделены не запятыми
            except IndexError:
                pass
    return products


def get_discounts(input_file):
    discounts = []
    with open(input_file, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            discounts.append(line.strip())
    return discounts


def apply_discount(products, discounts):
    """ на входе словарь продуктов с исходными ценами и список скидок, на выходе - словарь с итоговыми ценами"""
    try:
        assert len(products) == len(discounts)
    except AssertionError:
        return print("Количество продуктов и скидок не совпадает, проверьте данные в файлах!")
    else:
        discount_products = {}
        index = 0
        template = '{:.' + "2" + 'f}'
        for pr in products.keys():
            price = int(products[pr]) * (1 - float(discounts[index]))
            price = float(template.format(price))
            try:
                assert 0 <= price <= int(products[pr])
            except AssertionError:
                pass
            else:
                discount_products[pr] = price
            index += 1
        return discount_products


# 'files/data.txt'
product_file = input("Укажите путь и название файла с товарами и ценами (с расширением): ").strip()
# 'files/discount.txt'
discount_file = input("Укажите путь и название файла со скидками (с расширением): ").strip()
try:
    result = apply_discount(get_products(product_file), get_discounts(discount_file))
except FileNotFoundError:
    print("Такого/-их файла/-ов не существует!")
else:
    print("Итоговый список товаров со скидками:")
    for pr in result.keys():
        print(pr, "-", result[pr])