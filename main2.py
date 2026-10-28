#------Тут код розробника 2 (перша половина)------------

#---------------------------------------
baggage_data = {
    1: {'items': 3, 'weight': 45.0},
    2: {'items': 1, 'weight': 20.0},
    3: {'items': 4, 'weight': 62.0},
    4: {'items': 2, 'weight': 31.0},
    5: {'items': 1, 'weight': 28.0},
    6: {'items': 5, 'weight': 75.0},
    7: {'items': 3, 'weight': 40.0},
    8: {'items': 2, 'weight': 31.5},
    9: {'items': 1, 'weight': 15.0},
    10: {'items': 2, 'weight': 29.5}
}
#------Тут код розробника 2 (друга половина)------------

#---------------------------------------
# а) кількість пасажирів, які мають більше двох речей
passengers_more_than_two = sum(1 for data in baggage_data.values() if data['items'] > 2)
print(f"а) Кількість пасажирів, які мають більше двох речей: {passengers_more_than_two}")
# б) чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг
has_one_light_item = any(data['items'] == 1 and data['weight'] < 25 for data in baggage_data.values())
if has_one_light_item:
    print("б) Так, є хоча б один такий пасажир.")
else:
    print("б) Ні, такого пасажира немає.")
# в) номер багажу, в якому вага однієї речі відрізняється від
# загальної середньої ваги однієї речі не більше ніж на 0,5 кг
total_items = sum(data['items'] for data in baggage_data.values())
total_weight = sum(data['weight'] for data in baggage_data.values())
overall_avg_weight = total_weight / total_items if total_items > 0 else 0
print(f"\n[Інфо] Загальна середня вага однієї речі становить: {overall_avg_weight:.2f} кг")
matching_baggage_numbers = []
for baggage_num, data in baggage_data.items():
    if data['items'] > 0:
        avg_item_weight = data['weight'] / data['items']
        if abs(avg_item_weight - overall_avg_weight) <= 0.5:
            matching_baggage_numbers.append(baggage_num)
print(f"в) Номери багажу, що відповідають умові: {matching_baggage_numbers}")