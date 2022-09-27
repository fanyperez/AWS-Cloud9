inicio = 1
fin = 250
print("los numeros primo son: ")

for num in range(inicio, fin + 1):
    if num > 1:
       for i in range(2, num):
           if(num % i) == 0:
              break
       else:
           print(num)