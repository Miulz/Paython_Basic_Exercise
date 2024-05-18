# Млад програмист разполага с определен бюджет и свободно време в даден сезон.
# Напишете програма, която да приема на входа бюджета и сезона,
# а на изхода да изкарва къде ще почива програмистът и колко ще похарчи.
# Бюджетът определя дестинацията, а сезонът - колко от бюджета ще изхарчи.
# Ако е лято ще почива на къмпинг, а зимата в хотел. Ако е в Европа, независимо от сезона, ще почива в хотел.
# Всеки къмпинг или хотел, според дестинацията, има собствена цена, която отговаря на даден процент от бюджета:
# •	При 100 лв. или по-малко - някъде в България:
# o	Лято - 30% от бюджета;
# o	Зима - 70% от бюджета.
# •	При 1000 лв. или по малко - някъде на Балканите:
# o	Лято - 40% от бюджета;
# o	Зима - 80% от бюджета.
# •	При повече от 1000 лв. - някъде из Европа:
# o	При пътуване из Европа, независимо от сезона, ще похарчи 90% от бюджета.
# Вход
# Входът се чете от конзолата и се състои от два реда, въведени от потребителя:
# •	Бюджет - реално число;
# •	Един от двата възможни сезона - "summer” или "winter”.
# Изход
# На конзолата трябва да се отпечатат два реда:
# •	 "Somewhere in [дестинация]" измежду "Bulgaria", "Balkans" и "Europe"
# •	"{Вид почивка} - {Похарчена сума}":
# o	Почивката може да е между "Camp" и "Hotel"
# o	Сумата трябва да бъде форматирана с точност до вторият знак след десетичната запетая


budget = float(input())
season = input()

BULGARIAN_SUMMER_SPENT_MONEY = 30/100
BULGARIAN_WINTER_SPENT_MONEY = 70/100
BALKANS_SUMMER_SPENT_MONEY = 40/100
BALKANS_WINTER_SPENT_MONEY = 80/100
EUROPE_SPENT_MONEY = 90/100


destination = "Bulgaria" and "Balkans" and "Europe"
relax_type = "Camp" and "Hotel"
spent_money = 0

if season == "summer":
    relax_type = "Camp"
elif season == "winter":
    relax_type = "Hotel"
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * BULGARIAN_SUMMER_SPENT_MONEY
    elif season == "winter":
        spent_money = budget * BULGARIAN_WINTER_SPENT_MONEY
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * BALKANS_SUMMER_SPENT_MONEY
    elif season == "winter":
        spent_money = budget * BALKANS_WINTER_SPENT_MONEY
elif budget > 1000:
    destination = "Europe"
    relax_type = "Hotel"
    spent_money = budget * EUROPE_SPENT_MONEY
print(f"Somewhere in {destination}")
print(f"{relax_type} - {spent_money:.2f}")