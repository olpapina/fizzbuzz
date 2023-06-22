num = int(input("Enter any integer number: "))
print('\n'.join('Fizz' * (i%3==0) + 'Buzz' * (i%5==0) or str(i) for i in range(1, num+1)))
