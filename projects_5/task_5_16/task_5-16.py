import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    cursor = connection.cursor()

    cursor.execute('''
        SELECT 
            name AS "Название товара",
            category AS "Категория"
        FROM products;
    ''')

    rows = cursor.fetchall()

    for row in rows:
        print(f"{row[0]} - {row[1]}")

    cursor.close()
    connection.close()

except Exception as error:
    print(f"Ошибка: {error}")