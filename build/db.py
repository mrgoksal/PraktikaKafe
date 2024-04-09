import sqlite3

conn = sqlite3.connect('cafe.db')

# Создание курсора для выполнения операций с базой данных
cursor = conn.cursor()

# Создание таблицы для поваров
cursor.execute('''
    CREATE TABLE IF NOT EXISTS cooks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Создание таблицы для официантов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS waiters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')

# Создание таблицы для заказов
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        item TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

# Сохранение изменений в базе данных
conn.commit()

# Закрытие соединения с базой данных
conn.close()
