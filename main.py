def main():
    book_path = "books/frankenstein.txt"
    file_contents = open_file(book_path)
    print_book_report(file_contents, book_path)

def get_book_report(text, book_path):
    word_count = count_words(text)
    sorted_char_list = get_sorted_char_list(text)
    book_report = ""
    book_report += f"--- Begin report of {book_path} ---\n"
    book_report += f"{word_count} words found in the document\n\n"
    for ch_tuple in sorted_char_list:
        if ord(ch_tuple[0]) in range(ord('a'), ord('z') + 1):
            book_report += f"\n the {ch_tuple[0]} character was found {ch_tuple[1]} times"
    book_report += "\n\n --- End report ---"
    return book_report

def get_sorted_char_list(text):
    char_count=count_chars(text)
    sorted_char_list = get_sorted_char_list_from_dict(char_count)
    return sorted_char_list

def print_book_report(text, book_path):
    book_report = get_book_report(text, book_path)
    print(book_report)

def open_file(path):
    with open(path) as f:
        return f.read()

def count_words(s):
    return len(s.split())

def count_chars(s):
    s_lower = s.lower()
    char_dict = {}
    for ch in s_lower:
        if ch not in char_dict:
            char_dict[ch] = 1
        else:
            char_dict[ch] += 1
    return char_dict

def get_sorted_char_list_from_dict(char_dict):
    char_list = char_dict.items()
    sorted_list = sorted(char_list, key = sort_chars_by_occurance, reverse = True) 
    return sorted_list

def sort_chars_by_occurance(char_occ):
    return char_occ[1]


main()
