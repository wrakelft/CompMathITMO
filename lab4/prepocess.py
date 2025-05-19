import os
import re
import sys


def preprocess(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    replacements = {
        r'импортировать': r'import',
        r'нампай': r'numpy',
        r'как': r'as',
        r'функция': r'def',
        r'вернуть': 'return',
        r'цикл': r'for',
        r'в': r'in',
        r'соединить': r'zip',
        r'набор': r'array',
        r'решить_систему': r'linalg.solve',
        r'длин': r'len',
        r'сумма': r'sum',
        r'корень': r'sqrt'
    }

    for pattern, repl in replacements.items():
        code = re.sub(pattern, repl, code)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(code)


def clean(f):
    for file in f:
        try:
            os.remove(file)
        except FileNotFoundError:
            print(f"Файл {file} не найден, удаление не требуется")
        except Exception as e:
            print(f"Ошибка при удалении {file}: {str(e)}")