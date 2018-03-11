import sys
import re
import collections


def load_data(filepath):
    with open(filepath, 'r') as file_contents:
        text_string = file_contents.read().lower()
    all_the_words = re.findall(r'(\w+)', text_string, re.UNICODE)
    frequency = collections.Counter(all_the_words).most_common()[:10]
    return frequency


def get_most_frequent_words(text):

    for item in text:
        print(item[0])


if __name__ == '__main__':
    try:
        user_file_path = sys.argv[1]
        text = load_data(user_file_path)
    except (FileNotFoundError, IndexError):
        exit('Указанный файл не найден')
    get_most_frequent_words(text)
