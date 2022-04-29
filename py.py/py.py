import sqlite3



connect = sqlite3.connect('Box.db')

cursor = connect.cursor()
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shop(
        name TEXT,
        old  INTEGER,
        user TEXT
        
    )          
""")
cursor.execute("""
    INSERT INTO shop VALUES
    ('Durbek', 17, 'pattoyev'),     
    ('Durbek', 17, 'pattoyev'),  
    ('Durbek', 17, 'pattoyev')  
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS fruit(
        nomi TEXT,
        narxi INTEGER,
        rangi TEXT
        
    )          
""")
cursor.execute("""
    INSERT INTO fruit VALUES
    ('olma', 1, 'qizil'),     
    ('nok', 1.2, 'sariq'),  
    ('banan', 2, 'sariq')  
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS car(
        nomi TEXT,
        motori INTEGER,
        rangi TEXT
        
    )          
""")
cursor.execute("""
    INSERT INTO car VALUES
    ('Gentra', 1.6, 'qora'),     
    ('Cobalt', 1.2, 'qizil'),  
    ('Malibu', 2, 'kok')  
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vag(
        nomi TEXT,
        narxi INTEGER,
        rangi TEXT
        
    )          
""")
cursor.execute("""
    INSERT INTO vag VALUES
    ('sabzi', 1600, 'sariq'),     
    ('kartoshka', 5600, 'sariq'),  
    ('piyoz', 2000, 'sariq')  
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS vaga(
        nomi TEXT,
        narxi INTEGER,
        rangi TEXT
        
    )          
""")
cursor.execute("""
    INSERT INTO vaga VALUES
    ('ot', 1, 'qora'),     
    ('mushuk', 2, 'oq'),  
    ('it', 1, 'yashil')  
""")
restart = 1

cursor.execute("SELECT * FROM shop")
result = cursor.fetchall()

cursor.execute("SELECT * FROM fruit")
result2 = cursor.fetchall()

cursor.execute("SELECT * FROM car")
result3 = cursor.fetchall()

cursor.execute("SELECT * FROM vag")
result4 = cursor.fetchall()

cursor.execute("SELECT * FROM vaga")
result5 = cursor.fetchall()




while restart==1:
    int = input("Qanday ma`lumot olishni xoxlaysiz?: ")
    if int == "shop":
         print(result)
         restart=1
    elif int == "fruit":
        print(result2)
    elif int == "car":
        print(result3)
    elif int == "vag":
        print(result4)
    elif int == "vaga":
        print(result5)
    elif int == "yoq":
        print("xayr!")
        restart = 3
    else:
        print("ma`lumotlar bazasida bu ma`lumot yoq!")
        restart=1
    
    