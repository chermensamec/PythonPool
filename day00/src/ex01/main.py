import sys

def extract(word):
    return word[0]

def main():
    argv = sys.argv
    if (len(argv) != 2):
        raise Exception('Wrong number of arguments!')
    encrypted_string = argv[1].strip()
    decrypted_string = ''.join(map(extract, encrypted_string.split(' ')))
    print(decrypted_string)


if __name__ == '__main__':
    main()