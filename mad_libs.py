import textwrap


questions = [
    "Give me an adjective: ",
    "Give me a noun: ",
    "Give me a verb in past tense: ",
    "Give me a verb an adverb: ",
    "Give me a verb an adjective: ",
    "Give me a noun: ",
    "Give me a noun: ",
    "Give me an adjective: ",
    "Give me a verb: ",
    "Give me an adverb: ",
    "Give me a verb in past tense: ",
    "Give me an adjective: "
]

def main():
    word = (ask_for_words(questions))
    text = mad_libs_text(word)
    print(textwrap.fill(text, 40))


def ask_for_words(questions):
    word = []
    for question in questions:
        print(question, end="")
        word.append(get_word())
    print("")
    return word


def get_word():
    word = str(input("").lower().strip())
    while not word.isalpha():
        print(f"That's not a word. Try again: ", end="")
        word = str(input("").lower().strip())
    else:
        return word  


def mad_libs_text(word):
    text = f"\n Today I went to the zoo. I saw a(n) {word[0]} {word[1]} jumping up and down in its tree.He {word[2]} {word[3]} through the large tunnel that led to its {word[4]} {word[5]}. I got some peanuts and passed them through the cage to a gigantic gray {word[6]} towering above my head. Feeding that animal made me hungry. I went to get a {word[7]} scoop of ice cream. It filled my stomach. Afterwards I had to {word[8]} {word[9]} to catch our bus. When I got home I {word[10]} my mom for a {word[11]} day at the zoo."
    return text
    

if __name__ == "__main__":
    main()
 