def main():
    is_odd(get_input())
    try_again()


def get_input():
    try:
        number = int(input(f'What number are you thinking? '))
        while number > 1000 or number < 0:
            print(f'Your number mus be in range 0 to 1000. Try again.')
            number = int(input(f'What number are you thinking? '))
        else:
            return number
    except ValueError:
        print(f"That's not a number. Try again.")
        main()


def is_odd(number):
    if number%2 == 0:
        print(f"That's an even number!")
    else:
        print(f"That's an odd number!")


def try_again():
    answer = str(input(f'Have another? (y/n)\n').strip().lower())
    while answer not in ('y', 'n', 'yes', 'no'):
        answer = str(input(f'Did not get that, can you repeat? (y/n)\n').strip().lower())
    else:
        if answer in ('y', 'yes'):
            main()
        else:
            exit()


if __name__ == "__main__":
    main()