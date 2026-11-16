def display_all(baggage):
    if not baggage:
        print("\nСловник порожній.")
        return
    print(f"\nУсі записи про багаж (всього {len(baggage)} пасажирів):")
    for passenger_id, info in baggage.items():
        print(f"Пасажир №{passenger_id}: {info['items']} реч., загальна вага — {info['weight']} кг")
def display_sorted(baggage):
    if not baggage:
        print("\nСловник порожній.")
        return
    print("\nЗаписи про багаж (відсортовано за номером пасажира):")
    for passenger_id in sorted(baggage.keys()):
        info = baggage[passenger_id]
        print(f"Пасажир №{passenger_id}: {info['items']} реч., загальна вага — {info['weight']} кг")
def add_record(baggage):
    try:
        passenger_id = int(input("Введіть номер пасажира (ціле додатне число): "))
        if passenger_id <= 0:
            raise ValueError("Номер пасажира має бути більшим за нуль.")
        if passenger_id in baggage:
            print(f"Помилка: пасажир №{passenger_id} вже існує в базі.")
            return
        items = int(input("Введіть кількість речей: "))
        weight = float(input("Введіть загальну вагу багажу (кг): "))
        if items <= 0 or weight <= 0:
            raise ValueError("Кількість речей та вага мають бути додатними числами.")
        baggage[passenger_id] = {'items': items, 'weight': weight}
        print(f"Запис для пасажира №{passenger_id} успішно додано.")
    except ValueError as e:
        print(f"Помилка введення даних: {e}")
def delete_record(baggage):
    try:
        passenger_id = int(input("Введіть номер пасажира для видалення: "))
        del baggage[passenger_id]
        print(f"Запис для пасажира №{passenger_id} видалено.")
    except ValueError:
        print("Помилка: номер пасажира має бути цілим числом.")
    except KeyError:
        print("Помилка: пасажира з таким номером не існує у словнику.")
def solve_variant_tasks(baggage):
    if not baggage:
        print("\nНеможливо виконати розрахунки: словник порожній.")
        return
    print("\n--- Результати обчислень (Варіант 20) ---")
    # а) кількість пасажирів, які мають більше двох речей
    passengers_more_than_two = sum(1 for data in baggage.values() if data['items'] > 2)
    print(f"а) Кількість пасажирів, які мають більше двох речей: {passengers_more_than_two}")
    # б) чи є хоч один пасажир, багаж якого складається з однієї речі вагою менше 25 кг
    has_one_light_item = any(data['items'] == 1 and data['weight'] < 25 for data in baggage.values())
    if has_one_light_item:
        print("б) Так, є хоча б один пасажир з однією річчю вагою менше 25 кг.")
    else:
        print("б) Ні, такого пасажира немає.")
    # в) номер багажу, в якому вага однієї речі відрізняється від загальної середньої ваги не більше ніж на 0,5 кг
    total_items = sum(data['items'] for data in baggage.values())
    total_weight = sum(data['weight'] for data in baggage.values())
    try:
        overall_avg_weight = total_weight / total_items
    except ZeroDivisionError:
        print("в) Помилка: загальна кількість речей дорівнює нулю.")
        return
    print(f"[Інфо] Загальна середня вага однієї речі становить: {overall_avg_weight:.2f} кг")
    matching_baggage_numbers = []
    for baggage_num, data in baggage.items():
        if data['items'] > 0:
            avg_item_weight = data['weight'] / data['items']
            if abs(avg_item_weight - overall_avg_weight) <= 0.5:
                matching_baggage_numbers.append(baggage_num)
    print(f"в) Номери багажу, що відповідають умові: {matching_baggage_numbers}")
def main():
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
    while True:
        print("\n=== МЕНЮ РОБОТИ ЗІ СЛОВНИКОМ (БАГАЖ) ===")
        print("1 - Вивести всі значення словника")
        print("2 - Додати новий запис")
        print("3 - Видалити запис за номером пасажира")
        print("4 - Переглянути словник за відсортованими ключами")
        print("5 - Виконати завдання варіанта (а, б, в)")
        print("0 - Вихід")
        choice = input("Оберіть дію: ").strip()
        if choice == "1":
            display_all(baggage_data)
        elif choice == "2":
            add_record(baggage_data)
        elif choice == "3":
            delete_record(baggage_data)
        elif choice == "4":
            display_sorted(baggage_data)
        elif choice == "5":
            solve_variant_tasks(baggage_data)
        elif choice == "0":
            print("Роботу програми завершено.")
            break
        else:
            print("Невірний вибір! Спробуйте ввести число від 0 до 5.")
if __name__ == "__main__":
    main()