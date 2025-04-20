def a(n):
   a = set()
   for i in range(1, int(n ** 0.5) + 1):
       if n % i == 0:
           a.add(i)
           a.add(n // i)


   return sorted(a)
n = int(input("Введите натуральное число n: "))
result = a(n)




print(" ".join(map(str, result)))
