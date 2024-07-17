arr = []
num = 0
for i in range(3) :
    arr.append(input())

for i in range(3) :
    if arr[i] != 'Fizz' and arr[i] != 'Buzz' and arr[i] != 'FizzBuzz' :
        num = int(arr[i]) + (3-i)
        break

if num % 3 == 0 and num % 5 == 0 :
    print('FizzBuzz')
elif num % 3 == 0 :
    print('Fizz')
elif num % 5 == 0 :
    print('Buzz')
else :
    print(num)