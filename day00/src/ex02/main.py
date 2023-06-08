import sys


def checkFilrstLine(line):
    if (all([line[0] == line[4] == '*', line[1] != '*',
         line[2] != '*', line[3] != '*'])):
        return True
    return False

def checkSecondLine(line):
    if (all([line[0] == line[1] == line[3] == line[4] == '*',
        line[2] != '*'])):
        return True
    return False


def checkThirdLine(line):
    if (all([line[0] == line[2] == line[4] == '*',
        line[1] != '*' and line[3] != '*'])):
        return True
    return False

def checkImage(lines):
    if (all([checkFilrstLine(lines[0]), checkSecondLine(lines[1]),
        checkThirdLine(lines[2])])):
        return True
    return False

def main():
    lines = sys.stdin.readlines()
    if (checkImage(lines)):
        print('M')
    else:
        print("False")

if __name__ == '__main__':
    main()