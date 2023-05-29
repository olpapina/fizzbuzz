num = int(input("Enter any integer number: "))


def fizzbuzz(number):
    rem3 = number % 3
    rem5 = number % 5
    if not rem3 and not rem5:
        return "FizzBuzz"
    elif not rem5:
        return "Buzz"
    elif not rem3:
        return "Fizz"
    else:
        return number


for n in range(1, num + 1):
    print(fizzbuzz(n))
