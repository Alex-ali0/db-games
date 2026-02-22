import sqlite3 
con = sqlite3.connect("tutorial.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS games(
    Name TEXT NOT NULL, 
    developers TEXT,
    Release date TEXT, 
    genre TEXT,
    description TEXT,
)
""")
data = [
        ("Metro exodus", "4A Games", "15 февраля 2019 года", "сюжетный шутер от первого лица (FPS) с элементами survival horror (выживание) и стелс-экшена", "Герои покидают радиоактивную Москву на поезде «Аврора», путешествуя через постапокалиптическую Россию в поисках безопасного места.")
    ]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()
con.close()