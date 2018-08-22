import pymysql.cursors

# Connect to the database.
connection = pymysql.connect(host='aguaelrubi.no-ip.com',
                             user='gg',
                             password='1234',
                             db='pipas',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

print("connect successful!!")

query = connection.cursor()

loop= 'true'
while(loop=='true')
    username= input("Username: ")
    password= input("Password: ")
    if(query.execute("SELECT * FROM `usuarios` WHERE `id`="))