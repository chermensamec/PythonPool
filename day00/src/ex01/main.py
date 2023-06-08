import sys

def extract(word):
    return word[0]

def main():
    argv = sys.argv
    if (len(argv) != 2):
        raise Exception('Wrong number of arguments!')
    encryptedString = argv[1].strip()
    decryptedString = ''.join(map(extract, encryptedString.split(' ')))
    print(decryptedString)


if __name__ == '__main__':
    main()