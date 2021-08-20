import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="a7788123",
    database = "assignment"

             #建立完database,設定database 名
)


with mydb:
    with mydb.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))



my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE assignment") #建立一個新的database name:testdb

# my_cursor.execute("SHOW DATABASES") #以tuple的形式存除現有database

# for db in my_cursor:
#     print(db[0])

# my_cursor.execute("CREATE TABLE user (id INTEGER AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255), password VARCHAR(255) )")#建立一個table, name user, colume type name, 一格最大字元255, so forth and so on

my_cursor.execute("SHOW TABLES")
for table in my_cursor:
    print(table[0])

# sqlStuff = "INSERT INTO user (name, email, age) VALUE (%s, %s, %s)"
# record1 = ("John", "john@codemy.com", 40)

# my_cursor.execute(sqlStuff, record1)
# mydb.commit() #需要做commit的動作, 到mysql bench 更新後就可以看到新的值

# #example for # Insert Multiple Records
# sqlStuff = "INSERT INTO user (name, email, age) VALUE (%s, %s, %s)"
# records = [("B", "B@codemy.com", 40),
#            ("e", "E@codemy.com", 30),
#            ("n", "N@codemy.com", 20),]
# my_cursor.executemany(sqlStuff, records)
# mydb.commit()

#  # Read
# my_cursor.execute("SELECT * FROM user")
# result = my_cursor.fetchall()
# for row in result:
#     print(row)

# # Update  (這邊以users table 作範例)
# update_users = "UPDATE user SET age = 23 WHERE user_id = 4"
# my_cursor.execute(update_users)
# mydb.commit()


# # Delete
# delete_users = "DELETE FROM user WHERE user_id = 4"
# my_cursor.execute(delete_users)
# mydb.commit()

# # Delete Drpo Table
# delete_table = "DROP TABLE IF EXISTS users"
# cursor.execute(delete_table)