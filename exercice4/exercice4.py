def asknumber():
    n = int(input("Give a number : "))
    stockNumber = []
    for x in range(1,n+1):
        if n % x == 0:
            stockNumber.insert(1, x)
    stockNumber.sort(reverse=True)
    print(stockNumber)
    return n
asknumber()


"""Create a program that asks the user for a number and then prints out a list of all the divisors of that number. (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""