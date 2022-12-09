
def main():
    print(f"oh nice, you just told me what's on your mind in {count_words(get_input())} words!")


def get_input():
    return input(f"What's on your mind today? ").strip()


def count_words(text):
    l = text.split()
    l_items = len(l)
    return l_items


if __name__ == "__main__":
    main()
    