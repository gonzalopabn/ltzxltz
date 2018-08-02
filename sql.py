import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='aguaelrubi.no-ip.com',
                             user='gg',
                             password='1234',
                             db='gonzalom_lotes',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:

    with connection.cursor() as cursor:

        # SQL
        sql = "select * from producto order by idproducto"

        # Execute query.
        cursor.execute(sql)

        print("cursor.description: ", cursor.description)

        print()

        for row in cursor:
            print(row)

finally:
    # Close connection.
    connection.close()
