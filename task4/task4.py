import statistics
import sys


def count_steps(file_path: str) -> int:
    """Функция принимает список чисел.
        В переменную 'median' записывается округленная до целого числа медиана массива чисел и в цикле проходя
        по содержимому списка абсолютное число разницы элемента и медианы прибавляется к result"""
    with open(file_path, 'r') as file:
        input_list: list[int] = [int(item) for item in (file.read().splitlines())]

    median = int(statistics.median(input_list))
    result: int = 0
    for item in input_list:
        result += abs(item - median)

    return result


if __name__ == '__main__':
    count = count_steps(sys.argv[1])
    print(count)