import sqlite3

def view_users():
    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cooks')  # Выбираем все записи из таблицы поваров
    cooks = cursor.fetchall()
    conn.close()

    # Выводим результаты на экран
    print("Повары:")
    for cook in cooks:
        print(cook)

    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM waiters')  # Выбираем все записи из таблицы официантов
    waiters = cursor.fetchall()
    conn.close()

    # Выводим результаты на экран
    print("\nОфицианты:")
    for waiter in waiters:
        print(waiter)

    conn = sqlite3.connect('cafe.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM orders')  # Выбираем все записи из таблицы заказов
    orders = cursor.fetchall()
    conn.close()

    # Выводим результаты на экран
    print("\nЗаказы:")
    for order in orders:
        print(order)

# Вызываем функцию для просмотра данных в базе данных
view_users()
