import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='aguaelrubi.no-ip.com',
                             user='gg',
                             password='1234',
                             db='pipas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

try:

    with connection.cursor() as cursor:

        # SQL
        #sql = "select * from usuario1 order by identrada"
        sql = "INSERT INTO usuario1(identrada,fecha,litros) VALUES (%s,%s,%s)"

        # Execute query.
        cursor.execute(sql,(2,"hola","kd"))

        for row in cursor:
            print(row)

finally:
    # Close connection.
    connection.commit()
    connection.close()
