number = int(input("Please enter a number: "))

def prime(number):
    if number <= 1:
        print(f"{number} is not a prime number.")
        return
    for i in range(2, number - 1):
        if number % i == 0:
            print(f"{number} is not prime")
            return
        else:
            print(f"{number} is prime")
            return
        
prime(number)

    