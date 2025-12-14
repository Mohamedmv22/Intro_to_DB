import mysql.connector

# 1) Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="MohamedVevo12#",
    database="my_db",      # حط اسم الداتابيز الصح
    port=3306,
    use_pure=True
)

# 2) Cursor
cursor = db.cursor()

# 3) Execute SELECT
cursor.execute("SELECT * FROM students")

# 4) Fetch النتائج
rows = cursor.fetchall()

# 5) طباعة النتائج
for row in rows:
    print(row)

# 6) قفل الاتصال
cursor.close()
db.close()



