#Prime Number Analyzer
# 1. Take input from the user
number = int(input("Enter a number: "))
# 2. Check if the number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# factor 
def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors
print(f"Prime factors of {number}: {prime_factors(number)}")
# 3. Analyze the number and print the result
if is_prime(number):
    print(f"{number} is a prime number.")
else:    print(f"{number} is not a prime number.")

