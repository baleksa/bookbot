import string


def count_words(text):
    return len(text.split())


def count_each_char(text: str):
    text = text.lower()
    # chars = set(text)
    chars = string.ascii_lowercase
    return {c: text.count(c) for c in chars}


def print_book_report(book):
    with open(book) as f:
        file_contents = f.read()
    print(f"--- Begin report of {book} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print()

    counts = count_each_char(file_contents)
    for item in sorted(counts.items(), key=lambda x: x[1], reverse=True):
        print(f"The '{item[0]}' character was found {item[1]} times")

    print("--- End report ---")


def main():
    print_book_report("books/frankenstein.txt")


main()
