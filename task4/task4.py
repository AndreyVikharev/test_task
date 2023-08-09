import statistics


def count_steps(input_list: list[int]) -> int:
    """Функция принимает список чисел.
        В переменную 'median' записывается окрушленная до целого числа медиана массива чисел и в цикле проходя
        по содержимому списка абсолютное число разницы элемента и медианы прибавляется к result"""
    median = int(statistics.median(input_list))
    result: int = 0
    for item in input_list:
        result += abs(item - median)

    return result


file_path = input('Введите имя файла: ')

with open(file_path, 'r') as file:
    input_data: list[int] = [int(item) for item in (file.read().splitlines())]

print(count_steps(input_data))
