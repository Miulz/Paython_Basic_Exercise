# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня,
# които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
# Като изход да се отпечата на конзолата на един ред: "It's {градуси} degrees, get your {облекло} and {обувки}."


degrees = int(input())
part_of_day = input()

outfit = "Sweatshirt" and "Shirt" and "T-Shirt" and "Swim Suit"
shoes = "Sneakers" and "Moccasins" and "Sandals" and "Barefoot"

if part_of_day == "Morning":
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif degrees >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif part_of_day == "Afternoon":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif degrees >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
elif part_of_day == "Evening":
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif 18 < degrees <= 24:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
    elif degrees >= 25:
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
