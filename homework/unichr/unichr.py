import random


def random_str():

    rand_str = ''
    
    for _ in range(1000):

        while True:
            try:
                char = chr(random.randint(0x0000, 0xFFFF))
                char.encode('utf-8')
                rand_str += char
                break
            except UnicodeEncodeError:
                continue

    return rand_str


def write_to_file(rand_str):

    with open('randomstring.txt', 'w', encoding='utf-8') as file:
        file.write(rand_str)


def main():

    rand_str = random_str()
    write_to_file(rand_str)


if __name__ == '__main__':
    main()