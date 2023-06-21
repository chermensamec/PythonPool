'''Проверка на валиность изображения'''
import sys


def check_filrst_line(line) -> bool:
    '''Проверка первой строки'''
    if (all([line[0] == line[4] == '*', line[1] != '*',
         line[2] != '*', line[3] != '*'])):
        return True
    return False

def check_second_line(line) -> bool:
    '''Проверка второй строки'''
    if (all([line[0] == line[1] == line[3] == line[4] == '*',
        line[2] != '*'])):
        return True
    return False


def check_third_line(line) -> bool:
    '''Проверка третьей строки'''
    if (all([line[0] == line[2] == line[4] == '*',
        line[1] != '*' and line[3] != '*'])):
        return True
    return False

def check_size(lines: list(str)) -> bool:
    '''Проверка на правильность размеров'''
    if len(lines) != 3:
        return False
    for line in lines:
        if len(line) != 5:
            return False
    return True

def check_image(lines) -> bool:
    '''Проверка изображения'''
    if (all(check_size(lines),[check_filrst_line(lines[0]), check_second_line(lines[1]),
        check_third_line(lines[2])])):
        return True
    return False

def main():
    lines = sys.stdin.readlines()
    if check_image(lines):
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
