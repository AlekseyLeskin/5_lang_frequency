import sys
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as file_contents:
        text_string = file_contents.read().lower()
    return text_string


def get_most_frequent_words(text_string):
    number_of_words = 10
    list_of_all_the_words = re.findall(r'(\w+)', text_string, re.UNICODE)
    frequency = collections.Counter(list_of_all_the_words).most_common(number_of_words)
    return frequency


def print_top_ten_words(frequency):
    for word, number_of_repeats in frequency:
        print(word)


if __name__ == '__main__':
    try:
        user_file_path = sys.argv[1]
        text_string = load_data(user_file_path)
    except (FileNotFoundError, IndexError):
        exit('Указанный файл не найден')
    print_top_ten_words(get_most_frequent_words(text_string))
