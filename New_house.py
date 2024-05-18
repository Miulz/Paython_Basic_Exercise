# Марин и Нели си купуват къща недалеч от София. Нели толкова много обича цветята, че Ви убеждава да напишете програма,
# която да изчисли колко  ще им струва, за да засадят определен брой цветя и дали наличният бюджет ще им е достатъчен.
# Различните цветя са с различни цени:

# цвете	              Роза	Далия	Лале   Нарцис	Гладиола
# Цена на брой в лева	5	3.80	2.80	3	      2.50

# Съществуват следните отстъпки:
# •	Ако Нели купи повече от 80 Рози - 10% отстъпка от крайната цена;
# •	Ако Нели купи повече от 90  Далии - 15% отстъпка от крайната цена;
# •	Ако Нели купи повече от 80 Лалета - 15% отстъпка от крайната цена;
# •	Ако Нели купи по-малко от 120 Нарциса - цената се оскъпява с 15%;
# •	Ако Нели Купи по-малко от 80 Гладиоли - цената се оскъпява с 20%.
# От конзолата се четат 3 реда:
# •	Вид цветя - текст с възможности "Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus";
# •	Брой цветя - цяло число;
# •	Бюджет - цяло число.
# Да се отпечата на конзолата на един ред:
#     Ако бюджетът им е (достатъчен -
#         "Hey, you have a great garden with {броя цвета} {вид цветя} and {останалата сума} leva left.");
# •	Ако бюджета им е НЕ достатъчен -
#         "Not enough money, you need {нужната сума} leva more.".
# Сумата да бъде форматирана до втория знак след десетичната запетая.

flowers_type = input()
count_flowers = int(input())
budget = int(input())

discount = 0
price = 0
increase_in_price = 0

if flowers_type == "Roses":
    price = count_flowers * 5
    if count_flowers > 80:
        discount = 0.10
        price = price - (price * discount)
elif flowers_type == "Dahlias":
    price = count_flowers * 3.80
    if count_flowers > 90:
        discount = 0.15
        price = price - (price * discount)
elif flowers_type == "Tulips":
    price = count_flowers * 2.80
    if count_flowers > 80:
        discount = 0.15
        price = price - (price * discount)
elif flowers_type == "Narcissus":
    price = count_flowers * 3
    if count_flowers < 120:
        increase_in_price = 0.15
        price = price + (price * increase_in_price)
elif flowers_type == "Gladiolus":
    price = count_flowers * 2.50
    if count_flowers < 80:
        increase_in_price = 0.20
        price = price + (price * increase_in_price)
if budget >= price:
        money_left = budget - price
        print(f"Hey, you have a great garden with {count_flowers} {flowers_type} and {money_left:.2f} leva left.")
else:
        money_needed = price - budget
        print(f"Not enough money, you need {money_needed:.2f} leva more.")


