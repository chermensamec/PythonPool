import sys

def filter_format_line(line):
    if len(line) == 32 and line[:5] == '00000' and line[5] != '0':
        return True
    return False

def getLine():
    for line in sys.stdin:
        yield line.strip()

def main():
    argv = sys.argv
    if (len(argv) != 2):
        raise Exception('Wrong number of arguments!')
    n = int(argv[-1])
    lines = list()
    geterLines = getLine()
    for _ in range(n):
        lines.append(next(geterLines))
    filtered_lines = list(filter(filter_format_line, lines))
    print(*filtered_lines, sep = '\n')

print(__name__)

if __name__ == '__main__':
    main()