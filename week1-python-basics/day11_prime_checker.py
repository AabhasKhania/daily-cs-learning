# Day 11 – Prime Checker (Optimized)
# Aabhas Khaniya
# A classic coding question — used in interviews and foundational math.

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check from 5 to sqrt(n), skip even multiples
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

try:
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(f"✅ {number} is a prime number.")
    else:
        print(f"❌ {number} is not a prime number.")
except ValueError:
    print("⚠️ Please enter a valid integer.")
