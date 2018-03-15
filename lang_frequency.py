import sys
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as file_contents:
        string_from_file = file_contents.read()
    return string_from_file


def get_most_frequent_words(text_string):
    number_of_words = 10
    list_of_all_the_words = re.findall(r'(\w+)', text_string.lower(), re.UNICODE)
    most_frequent_words = collections.Counter(list_of_all_the_words).most_common(number_of_words)
    return most_frequent_words


def print_top_words(frequency):
    print('Самые частые слова в тексте в порядке убывания частоты:')
    for word, number_of_repeats in frequency:
        print(word)


if __name__ == '__main__':
    try:
        user_file_path = sys.argv[1]
        string_from_user_file = load_data(user_file_path)
    except (FileNotFoundError, IndexError):
        exit('Указанный файл не найден')
    print_top_words(get_most_frequent_words(string_from_user_file))
