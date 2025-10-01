# Add up to Even Number with Primes

def check_prime(num):
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5)+1, 2):
        if num % i == 0:
            return False
    return True


def prime_pair_list(num):
    ans = []
    for i in range(2, num):
        if check_prime(i):
            j = num - i
            if check_prime(j) and j >= i:
                ans.append(f"{i}+{j}")
    return ans


print(prime_pair_list(10))
print(prime_pair_list(50))
print(prime_pair_list(100))
