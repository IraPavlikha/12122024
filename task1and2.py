import time
from typing import Callable, List

# Завдання 1: Функція для пошуку простих чисел

def timer_decorator(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання: {end_time - start_time:.2f} секунд")
        return result
    return wrapper
@timer_decorator
def find_primes(start: int, end: int) -> List[int]:
    primes = []
    for num in range(start, end + 1):
        if num > 1:  # Просте число більше за 1
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes
# Виклик функції для Завдання 1 і 2
primes = find_primes(0, 1000)
print(f"Прості числа: {primes}")
# Завдання 3: Формати звітності
def report_decorator(format_type: str):
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            report = func(*args, **kwargs)
            if format_type == "json":
                import json
                return json.dumps(report, indent=4)
            elif format_type == "xml":
                import dicttoxml
                return dicttoxml.dicttoxml(report).decode()
            elif format_type == "text":
                return "\n".join(f"{key}: {value}" for key, value in report.items())
            else:
                raise ValueError("Непідтримуваний формат звіту")
        return wrapper
    return decorator
@report_decorator("json")
def financial_report():
    return {
        "company": "MyCompany",
        "year": 2024,
        "revenue": 1000000,
        "expenses": 500000,
        "profit": 500000
    }
print(financial_report())