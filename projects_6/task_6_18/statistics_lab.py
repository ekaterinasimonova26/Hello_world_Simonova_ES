import psycopg2
import pandas as pd

try:
    # Подключение к вашему контейнеру student_task
    connection = psycopg2.connect(
        host="localhost",
        port="5435",
        user="postgres",
        password="student",
        database="student_task"
    )
    print("✓ Подключение установлено\n")

    # 2. SQL-запрос с JOIN цен и товаров
    query = """
    SELECT
        p.id AS product_id,
        p.name AS product_name,
        p.category,
        pr.price,
        pr.created_at
    FROM prices pr
    JOIN products p ON pr.product_id = p.id
    ORDER BY p.category, p.name
    """

    df = pd.read_sql_query(query, connection)
    print("=== Данные загружены ===")
    print(f"Всего записей о ценах: {len(df)}")
    print(f"Уникальных товаров: {df['product_id'].nunique()}")
    print(f"Уникальных категорий: {df['category'].nunique()}\n")

    print(df.head(10))
    print("\n")

    # 3. Основные показатели по столбцу price
    print("=== 3. Описательная статистика цен (руб.) ===")
    print(f"Среднее значение (mean):     {df['price'].mean():.2f} руб.")
    print(f"Медиана (median):           {df['price'].median():.2f} руб.")
    print(f"Стандартное отклонение (std):{df['price'].std():.2f} руб.")
    print(f"Минимальная цена (min):      {df['price'].min():.2f} руб.")
    print(f"Максимальная цена (max):     {df['price'].max():.2f} руб.\n")

    # 4. Квартили, IQR и товары дороже Q3
    print("=== 4. Квартильный анализ ===")
    q1 = df['price'].quantile(0.25)
    q2 = df['price'].quantile(0.50)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1

    print(f"Q1 (25%): {q1:.2f} руб.")
    print(f"Q2 (50%): {q2:.2f} руб. (медиана)")
    print(f"Q3 (75%): {q3:.2f} руб.")
    print(f"IQR (межквартильный размах): {iqr:.2f} руб.\n")

    # Товары, цена которых превышает Q3
    expensive = df[df['price'] > q3]
    print(f"Товары с ценой выше Q3 (>{q3:.2f} руб.): {len(expensive)} записей")
    if not expensive.empty:
        print(expensive[['product_name', 'category', 'price']].to_string(index=False))
    print("\n")

    # 5. Группировка по категориям
    print("=== 5. Статистика цен по категориям (сортировка по убыванию средней цены) ===")
    by_category = df.groupby('category')['price'].agg(
        count='count',
        mean='mean',
        median='median',
        std='std'
    ).round(2).sort_values('mean', ascending=False)

    print(by_category.to_string())
    print("\n")

    # 6. Пять товаров с наибольшим разбросом цен (max - min)
    print("=== 6. Топ-5 товаров с наибольшим разбросом цен ===")
    price_range = df.groupby('product_id').agg(
        product_name=('product_name', 'first'),
        category=('category', 'first'),
        min_price=('price', 'min'),
        max_price=('price', 'max')
    )
    price_range['range'] = price_range['max_price'] - price_range['min_price']
    top5_range = price_range.sort_values('range', ascending=False).head(5)

    for idx, row in top5_range.iterrows():
        print(f"Товар: {row['product_name']}")
        print(f"  Категория: {row['category']}")
        print(f"  Мин. цена: {row['min_price']:.2f} руб.")
        print(f"  Макс. цена: {row['max_price']:.2f} руб.")
        print(f"  Разброс:   {row['range']:.2f} руб.\n")

    connection.close()

except Exception as error:
    print(f"Ошибка: {error}")