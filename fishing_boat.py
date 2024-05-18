# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова,
# че решават да отидат на риболов с кораб. Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен -
# тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# От конзолата се четат три реда:
# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.

budget = int(input())
season = input()
count_fisherman = int(input())
rent_price = 0
discount = 0

if season == "Spring":
    rent_price = 3000
    if count_fisherman <= 6:
        discount = 0.10
        rent_price = rent_price - (rent_price * discount)
    elif count_fisherman <= 6 and count_fisherman % 2 == 0:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11 and count_fisherman % 2 == 0:
        discount = 0.20
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman:
        discount = 0.25
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman and count_fisherman % 2 == 0:
        discount = 0.30
        rent_price = rent_price - (rent_price * discount)
elif season == "Summer":
    rent_price = 4200
    if count_fisherman <= 6:
        discount = 0.10
        rent_price = rent_price - (rent_price * discount)
    elif count_fisherman <= 6 and count_fisherman % 2 == 0:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11 and count_fisherman % 2 == 0:
        discount = 0.20
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman:
        discount = 0.25
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman and count_fisherman % 2 == 0:
        discount = 0.30
        rent_price = rent_price - (rent_price * discount)
elif season == "Autumn":
    rent_price = 4200
    if count_fisherman <= 6:
        discount = 0.10
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman:
        discount = 0.25
        rent_price = rent_price - (rent_price * discount)
elif season == "Winter":
    rent_price = 2600
    if count_fisherman <= 6:
        discount = 0.10
        rent_price = rent_price - (rent_price * discount)
    elif count_fisherman <= 6 and count_fisherman % 2 == 0:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11:
        discount = 0.15
        rent_price = rent_price - (rent_price * discount)
    elif 7 <= count_fisherman <= 11 and count_fisherman % 2 == 0:
        discount = 0.20
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman:
        discount = 0.25
        rent_price = rent_price - (rent_price * discount)
    elif 12 <= count_fisherman and count_fisherman % 2 == 0:
        discount = 0.30
        rent_price = rent_price - (rent_price * discount)
if budget >= rent_price:
    money_left = budget - rent_price
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = rent_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")




