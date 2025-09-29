from datetime import datetime
from collections import defaultdict

def analyze_pizzeria_data():
    """
    Программа для анализа данных пиццерии с группировкой по датам
    """
    print("=== АНАЛИЗ ДАННЫХ ПИЦЦЕРИИ ===")
    print("Введите данные о заказах:")
    print("Формат: сначала строка с датой (ДД.ММ.ГГГГ), затем строки с заказами (Пицца Стоимость)")
    print("Для завершения ввода введите пустую строку")
    print()
    print("Пример:")
    print("15.03.2024")
    print("Маргарита 850")
    print()
    
    orders = []
    current_date = None
    
    while True:
        line = input().strip()
        if not line:
            break

        try:
            date_candidate = datetime.strptime(line, "%d.%m.%Y").date()
            current_date = date_candidate
            continue  
        except ValueError:
            pass
            
        if current_date is None:
            continue
            
        parts = line.split()
        if len(parts) < 2:
            continue
        
        pizza_name = ' '.join(parts[:-1])
        cost = float(parts[-1])
        
        orders.append({
            'date': current_date,
            'pizza': pizza_name,
            'cost': cost
        })
    
    if not orders:
        print("\nНет данных для анализа.")
        return
    
    # Анализ данных
    
    # а) Статистика по пиццам
    pizza_stats = defaultdict(int)
    for order in orders:
        pizza_stats[order['pizza']] += 1
    
    # Сортируем по убыванию количества заказов
    sorted_pizzas = sorted(pizza_stats.items(), key=lambda x: x[1], reverse=True)
    
    # б) Статистика по датам
    date_stats = defaultdict(float)
    for order in orders:
        date_stats[order['date']] += order['cost']
    
    # Сортируем даты хронологически
    sorted_dates = sorted(date_stats.items(), key=lambda x: x[0])
    
    # в) Самый дорогой заказ
    most_expensive = max(orders, key=lambda x: x['cost'])
    
    # г) Средняя стоимость заказа
    average_cost = sum(order['cost'] for order in orders) / len(orders)
    
    # Вывод результатов
    
    print("\n" + "="*50)
    print("РЕЗУЛЬТАТЫ АНАЛИЗА:")
    print("="*50)
    
    # а) Вывод статистики по пиццам
    print("\nа) СТАТИСТИКА ПО ПИЦЦАМ (отсортировано по популярности):")
    print("-" * 40)
    for pizza, count in sorted_pizzas:
        print(f"{pizza}: {count} заказ(ов)")
    
    # б) Вывод статистики по датам
    print("\nб) СТАТИСТИКА ПО ДАТАМ (отсортировано хронологически):")
    print("-" * 40)
    for date, total in sorted_dates:
        date_str = date.strftime("%d.%m.%Y")
        print(f"{date_str}: {total:.2f} руб.")
    
    # в) Вывод информации о самом дорогом заказе
    print("\nв) САМЫЙ ДОРОГОЙ ЗАКАЗ:")
    print("-" * 40)
    date_str = most_expensive['date'].strftime("%d.%m.%Y")
    print(f"Дата: {date_str}")
    print(f"Пицца: {most_expensive['pizza']}")
    print(f"Стоимость: {most_expensive['cost']:.2f} руб.")
    
    # г) Вывод средней стоимости
    print("\nг) СРЕДНЯЯ СТОИМОСТЬ ЗАКАЗА:")
    print("-" * 40)
    print(f"{average_cost:.2f} руб.")

analyze_pizzeria_data()