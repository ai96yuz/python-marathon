# Task 1


def double_string(data):
    counter = 0
    answer = []
    for str in data:
        for el in data:
            answer.append(str + el)
        if str in set(answer):
            counter += 1
    return counter


# Task 2


LETTERS_TO_MC = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/' }


def morse_number(words):
    return " ".join(LETTERS_TO_MC[char] for char in words.upper())


# Task 3



# Task 4



# Task 5