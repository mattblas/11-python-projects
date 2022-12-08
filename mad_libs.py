import textwrap

def main():
    word = (ask_for_words())
    text = mad_libs_text(word)
    print(textwrap.fill(text, 40))

def ask_for_words():
    word = []
    print(f"Give me an adjective: ")
    word.append(get_word())
    print(f"Give me a noun: ")
    word.append(get_word())
    print(f"Give me a verb in past tense: ")
    word.append(get_word())
    print(f"Give me a verb an adverb: ")
    word.append(get_word())
    print(f"Give me a verb an adjective: ")
    word.append(get_word())
    print(f"Give me a noun: ")
    word.append(get_word())
    print(f"Give me a noun: ")
    word.append(get_word())
    print(f"Give me an adjective: ")
    word.append(get_word())
    print(f"Give me a verb: ")
    word.append(get_word())
    print(f"Give me an adverb: ")
    word.append(get_word())
    print(f"Give me a verb in past tense: ")
    word.append(get_word())
    print(f"Give me an adjective: ")
    word.append(get_word())
    return word

def mad_libs_text(word):
    text = f"\n Today I went to the zoo. I saw a(n) {word[0]} {word[1]} jumping up and down in its tree.He {word[2]} {word[3]} through the large tunnel that led to its {word[4]} {word[5]}. I got some peanuts and passed them through the cage to a gigantic gray {word[6]} towering above my head. Feeding that animal made me hungry. I went to get a {word[7]} scoop of ice cream. It filled my stomach. Afterwards I had to {word[8]} {word[9]} to catch our bus. When I got home I {word[10]} my mom for a {word[11]} day at the zoo."
    return text


def get_word():
    word = str(input("").lower().strip())
    while not word.isalpha():
        print(f"That's not a word. Try again: ", end="")
        word = str(input("").lower().strip())
    else:
        return word  


if __name__ == "__main__":
    main()
 