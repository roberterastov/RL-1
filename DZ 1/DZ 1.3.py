secunda = int(input("Введите время в секундах-----> "))
chas = secunda // 3600
minuta = (secunda - chas * 3600) // 60
secunda = secunda - (chas * 3600 + minuta * 60)
print(f"Время в формате чч:мм:сс   {chas} : {minuta} : {secunda}")