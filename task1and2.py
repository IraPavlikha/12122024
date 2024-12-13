import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Час виконання: {elapsed_time:.2f} секунд")
        return result
    return wrapper

@timer_decorator
def find_primes_in_range(start, end):
    primes = []
    for num in range(max(2, start), end + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
try:
    start_range = int(input("Введіть початок діапазону: "))
    end_range = int(input("Введіть кінець діапазону: "))
    print(f"Прості числа в діапазоні від {start_range} до {end_range}:")
    primes = find_primes_in_range(start_range, end_range)
    print(primes)
except ValueError:
    print("Будь ласка, введіть коректні цілі числа для діапазону.")
