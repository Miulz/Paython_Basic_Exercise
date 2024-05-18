# Хотел предлага 2 вида стаи: студио и апартамент. Напишете програма, която изчислява цената за целия престой
# за студио и апартамент. Цените зависят от месеца на престоя:
# Май и октомври	                             Юни и септември	                Юли и август
# Студио - 50 лв./нощувка	                 Студио - 75.20 лв./нощувка	            Студио - 76 лв./нощувка
# Апартамент - 65 лв./нощувка	             Апартамент - 68.70 лв./нощувка	        Апартамент - 77 лв./нощувка
# Предлагат се и следните отстъпки:
# •	За студио, при повече от 7 нощувки през май и октомври : 5% намаление.
# •	За студио, при повече от 14 нощувки през май и октомври : 30% намаление.
# •	За студио, при повече от 14 нощувки през юни и септември: 20% намаление.
# •	За апартамент, при повече от 14 нощувки, без значение от месеца : 10% намаление.
# Вход
# Входът се чете от конзолата и съдържа точно 2 реда, въведени от потребителя:
# •	На първия ред е месецът - May, June, July, August, September или October;
# •	На втория ред е броят на нощувките - цяло число.
# Изход
# Да се отпечатат на конзолата 2 реда:
# •	На първия ред: "Apartment: {цена за целият престой} lv."
# •	На втория ред: "Studio: {цена за целият престой} lv."
# Цената за целия престой да е форматирана с точност до два знака след десетичната запетая.

STUDIO_PRICE_MAY_OCTOBER = 50
FLAT_PRICE_MAY_OCTOBER = 65
STUDIO_PRICE_JUNE_SEPTEMBER = 75.20
FLAT_PRICE_JUNE_SEPTEMBER = 68.70
STUDIO_PRICE_JULY_AUGUST = 76
FLAT_PRICE_JULY_AUGUST = 77

DISCOUNT_STUDIO_MID_MAY_OCTOBER = 5/100
DISCOUNT_STUDIO_HIGH_MAY_OCTOBER = 30/100
DISCOUNT_STUDIO_HIGH_JUNE_SEPTEMBER = 20/100
DISCOUNT_FLAT = 10/100

month = input()
count_night = int(input())
flat_total_price = 0
studio_total_price = 0



if month == "May" or month == "October":
    if count_night > 7 and count_night < 14:
       STUDIO_PRICE_MAY_OCTOBER = STUDIO_PRICE_MAY_OCTOBER - (STUDIO_PRICE_MAY_OCTOBER * DISCOUNT_STUDIO_MID_MAY_OCTOBER)
       studio_total_price = count_night * STUDIO_PRICE_MAY_OCTOBER
       flat_total_price = count_night * FLAT_PRICE_MAY_OCTOBER
    elif count_night >= 14:
        STUDIO_PRICE_MAY_OCTOBER = STUDIO_PRICE_MAY_OCTOBER - (STUDIO_PRICE_MAY_OCTOBER * DISCOUNT_STUDIO_HIGH_MAY_OCTOBER)
        FLAT_PRICE_MAY_OCTOBER = FLAT_PRICE_MAY_OCTOBER - (FLAT_PRICE_MAY_OCTOBER * DISCOUNT_FLAT)
        studio_total_price = count_night * STUDIO_PRICE_MAY_OCTOBER
        flat_total_price = count_night * FLAT_PRICE_MAY_OCTOBER
if month == "June" or month == "September":
    if count_night <= 14:
        STUDIO_PRICE_JULY_AUGUST = STUDIO_PRICE_JULY_AUGUST
        FLAT_PRICE_JUNE_SEPTEMBER = FLAT_PRICE_JUNE_SEPTEMBER
        studio_total_price = count_night * STUDIO_PRICE_JUNE_SEPTEMBER
        flat_total_price = count_night * FLAT_PRICE_JUNE_SEPTEMBER
    elif count_night > 14:
        STUDIO_PRICE_JUNE_SEPTEMBER = STUDIO_PRICE_JUNE_SEPTEMBER - (STUDIO_PRICE_JUNE_SEPTEMBER * DISCOUNT_STUDIO_HIGH_JUNE_SEPTEMBER)
        FLAT_PRICE_JUNE_SEPTEMBER = FLAT_PRICE_JUNE_SEPTEMBER - (FLAT_PRICE_JUNE_SEPTEMBER * DISCOUNT_FLAT)
        studio_total_price = count_night * STUDIO_PRICE_JUNE_SEPTEMBER
        flat_total_price = count_night * FLAT_PRICE_JUNE_SEPTEMBER
if month == "July" or month == "August":
    FLAT_PRICE_JULY_AUGUST = FLAT_PRICE_JULY_AUGUST
    STUDIO_PRICE_JULY_AUGUST = STUDIO_PRICE_JULY_AUGUST
    studio_total_price = count_night * STUDIO_PRICE_JULY_AUGUST
    flat_total_price = count_night * FLAT_PRICE_JULY_AUGUST
    if count_night > 14:
        FLAT_PRICE_JULY_AUGUST = FLAT_PRICE_JULY_AUGUST - (FLAT_PRICE_JULY_AUGUST * DISCOUNT_FLAT)
        STUDIO_PRICE_JULY_AUGUST = STUDIO_PRICE_JULY_AUGUST
        studio_total_price = count_night * STUDIO_PRICE_JULY_AUGUST
        flat_total_price = count_night * FLAT_PRICE_JULY_AUGUST



print(f"Apartment: {flat_total_price:.2f} lv.")
print(f"Studio: {studio_total_price:.2f} lv.")

