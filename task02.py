def is_float(text: str) -> bool:
    try:
        float(text)
        return True
    except ValueError:
        return False


def generator_numbers(text: str) -> list[float]:
    yield from [float(word) for word in text.split() if is_float(word)]


def sum_profit(text: str, func) -> float:
    return sum(list(func(text)))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
