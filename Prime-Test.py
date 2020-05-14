def is_prime(num):
    factor = num
    for i in range(2,num):
        num -= 1
        if factor % num == 0:
            print("This number is NOT prime. %s is a factor of %s" % (num, factor))
            break

        if num == 2:
            print("This number is a PRIME")

print("Prime Number Checker!")
is_prime(int(input("what is your number: ")))