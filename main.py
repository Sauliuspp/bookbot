def count_letters(book_string):
    letter_count = {}

    for letter in book_string:
        if not letter.isalpha():
            continue
        elif letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1

    return letter_count

def sort_letters(letters):
    letter_count_list = []

    for letter in letters:
        letter_count_list.append({"letter": letter, "count": letters[letter]})

    return letter_count_list

def sort_on(dict):
    return dict["count"]

def print_report(word_count, letter_count):
    print(f"{word_count} words found in the book")

    for i in range(0, len(letter_count)):
        print(f"The letter {letter_count[i]['letter']} was found {letter_count[i]['count']} times in the book")

def main():
    count = 0

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        words = file_contents.split()
        # print(len(words))

        letter_count = count_letters(file_contents.lower())
        # print(letter_count)

        sorted_letter_count = sort_letters(letter_count)

        sorted_letter_count.sort(reverse=True, key=sort_on)

        print_report(len(words), sorted_letter_count)

main()