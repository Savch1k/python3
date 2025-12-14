# Рекурсивная версия
def to_str_recursive(lst):
    """
    Преобразует вложенные списки в строку формата '1 -> 2 -> 3 -> ... -> None'
    """
    if not lst:
        return "None"
    
    if isinstance(lst, list):
        if len(lst) == 0:
            return "None"
        first = lst[0]
        rest = lst[1] if len(lst) > 1 and isinstance(lst[1], list) else []
        
        if rest:
            return f"{first} -> {to_str_recursive(rest)}"
        else:
            return f"{first} -> None"
    else:
        return f"{lst} -> None"

# Итеративная версия
def to_str_iterative(lst):
    """
    Преобразует вложенные списки в строку формата '1 -> 2 -> 3 -> ... -> None'
    """
    result = []
    current = lst
    
    while current:
        if isinstance(current, list) and len(current) > 0:
            result.append(str(current[0]))
            if len(current) > 1 and isinstance(current[1], list):
                current = current[1]
            else:
                break
        else:
            break
    
    result.append("None")
    return " -> ".join(result)


# Задача 2: Расчёт последовательности a_i = a_{i-2} + a_{i-1}/(2^i-1)

# Рекурсивная версия
def sequence_recursive(n, memo=None):
    """
    Вычисляет n-й элемент последовательности:
    a_i = a_{i-2} + a_{i-1}/(2^i-1), a_0 = a_1 = 1
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n == 0 or n == 1:
        return 1
    
    result = sequence_recursive(n-2, memo) + sequence_recursive(n-1, memo) / (2**n - 1)
    memo[n] = result
    return result

# Итеративная версия
def sequence_iterative(n):
    """
    Вычисляет n-й элемент последовательности:
    a_i = a_{i-2} + a_{i-1}/(2^i-1), a_0 = a_1 = 1
    """
    if n == 0 or n == 1:
        return 1
    
    a_prev2 = 1  # a_{i-2}
    a_prev1 = 1  # a_{i-1}
    
    for i in range(2, n + 1):
        current = a_prev2 + a_prev1 / (2**i - 1)
        a_prev2, a_prev1 = a_prev1, current
    
    return a_prev1


# Тестирование функций
if __name__ == "__main__":
    print("Задача 1: Преобразование вложенных списков в строку")
    test_list = [1, [2, [3, [4, [5]]]]]
    
    print("Рекурсивная версия:")
    print(f"to_str_recursive({test_list}) = {to_str_recursive(test_list)}")
    
    print("Итеративная версия:")
    print(f"to_str_iterative({test_list}) = {to_str_iterative(test_list)}")
    
    print("\nЗадача 2: Расчёт последовательности")
    n = 5
    print(f"a_{n} (рекурсивно) = {sequence_recursive(n)}")
    print(f"a_{n} (итеративно) = {sequence_iterative(n)}")
    
    # Вывод первых 6 элементов последовательности
    print("\nПервые 6 элементов последовательности:")
    for i in range(6):
        print(f"a_{i} = {sequence_iterative(i)}")