import os


def check_files(path_1: str, path_2: str) -> bool:

    """
    Проверка того что путь ведёт к файлу:
    если проверку прошли оба пути к файлу, то возвращается True
    """
    if os.path.isdir(path_1):
        print('По пути к файлу №1 находится директория')
        return False
    elif os.path.isdir(path_2):
        print('По пути к файлу №2 находится директория')
        return False

    return True


def check_dots(data: list[str], list_dots: list[list[float]]) -> None:
    """
    В функции формируем данные об окружности и проходимся по списку с точками для их проверки.
        Проверка происходит по формуле:
        (х1 - х)**2 + (у1 - у)**2 > R**2  -  точка снаружи окружности
        (х1 - х)**2 + (у1 - у)**2 < R**2  -  точка внутри окружности
        (х1 - х)**2 + (у1 - у)**2 = R**2  -  точка лежит на окружности
    """
    x_dot = float(data[0])
    y_dot = float(data[1])
    radius = float(data[2])

    for dot in list_dots:
        check_x: float = dot[0]
        check_y: float = dot[1]

        formula = (check_x - x_dot) ** 2 + (check_y - y_dot) ** 2

        if formula > radius**2:
            print('2')

        elif formula < radius ** 2:
            print('1')

        else:
            print('0')


def check_point_to_circle(path_one: str, path_two: str) -> None:

    if check_files(path_1=path_one, path_2=path_two):
        '''После проверки файлов запускаем контекстные менеджеры для открытия файлов и взятия информации'''
        with open(path_one, 'r') as file_one:
            '''Сплитуем данные из файла и делаем проверку на соответствие данных исходя из примера,
                если длина списка данных не равна 3 ,то в консоль пишем об ошибке!'''
            list_of_lines: list[str] = file_one.read().split()
            if len(list_of_lines) == 3:
                circle_data = list_of_lines
            else:
                print('Данные в файле №1 указаны не корректно!')

        with open(path_two, 'r') as file_two:
            list_of_lines: list[str] = file_two.read().splitlines()
            '''Здесь так же сплитуем данные по строкам и проверяем согласно условию 
                0<кол-во точек<100. Если кол-во данных не проходит условие, то в консоль пишем об ошибке!'''
            if len(list_of_lines) > 100:
                print('В файлу №2 более чем 100 значений')

            elif len(list_of_lines) == 0:
                print('Файл №2 пуст')

            else:
                '''Если кол-во данных прошло проверку, то в цикле формируем список с данными точек.
                    В самом цикле происходит проверка того что должно быть 2 координаты в строчке, 
                    если проверка прошла,то координаты добавляются в список. Если проверка не прошла,
                    то в консоль пишем об ошибке!'''
                list_coord_dots: list[list[float]] = []
                for line in list_of_lines:
                    coord_dot = line.split()
                    if len(coord_dot) != 2:
                        print(f'Некорректные координаты: {line}')
                        continue
                    list_coord_dots.append([float(number) for number in coord_dot])
        '''После формирования всех данных, передаём их в функция для проверки точек'''
        check_dots(data=circle_data, list_dots=list_coord_dots)


if __name__ == '__main__':
    file_one_path = os.path.abspath(input('Введите путь к файлу №1: '))
    file_two_path = os.path.abspath(input('Введите путь к файлу №2: '))
    check_point_to_circle(path_one=file_one_path,
                          path_two=file_two_path)

