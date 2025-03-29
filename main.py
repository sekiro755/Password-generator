import random


symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

lenght = int(input("Введите длину пароля: "))

password = ""

if lenght > 8:

    for i in range(lenght):
         password += random.choice(symbols)

print(password)

if lenght <= 8:
     print('короткий пароль')
