n = int(input())
a = n // 100000 + n % 100000 //10000 + n % 10000 // 1000
b = n % 1000 // 100 + n % 100 // 10 + n % 10
if a == b:
   print('yes')
else:
 print('no')