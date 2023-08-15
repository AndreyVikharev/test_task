import json
import sys


def find_id_and_rewrite(dict_values: [dict], list_tests: list) -> None:
    """Функция проходит по списку словарей tests и проверяет ключи:
        1) 'values' - проверяет на наличие в словаре данного ключа, если есть то запускается рекурсия
        2) 'id' - проверяется на соответствие с таким же ключом из dict_values, 
            если они равны то перезаписывает значение ключа 'value'
        """
    for item in list_tests:

        if item.get('values'):
            find_id_and_rewrite(dict_values, item['values'])

        if item['id'] == dict_values['id']:
            item['value'] = dict_values['value']


def open_files_and_crate_reports(path_values_file: str, path_tests_file: str) -> dict:
    """В функцию передаётся пути файлов, после чего они записываются в переменные при помощи json и менеджера"""
    with open(path_values_file, 'r') as input_file_values:

        file_value: list = json.load(input_file_values)['values']

    with open(path_tests_file, 'r') as input_file_tests:

        file_tests: list = json.load(input_file_tests)['tests']
    """Далее в цикле в функцию поиска id и перезаписи словаря передаются аргументы:
        1) словарь находящийся в списке file_value
        2) список file_tests"""
    for result_value in file_value:
        find_id_and_rewrite(result_value, file_tests)
    """После перезаписи формируем и возвращаем словарь с ключом 'reports' и значением перезаписанным file_tests"""
    report_dict = {'reports': file_tests}
    return report_dict


def create_report_file(path_values_file: str, path_tests_file: str) -> None:
    out_file = open_files_and_crate_reports(path_values_file, path_tests_file)

    with open('reports.json', 'w') as file:
        json.dump(out_file, file, indent=4)


if __name__ == '__main__':
    create_report_file(sys.argv[1], sys.argv[2])
    print('Файл reports.json создан')
