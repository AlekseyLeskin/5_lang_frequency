import sys
import re


def load_data(filepath):
    with open(filepath, 'r') as open_file:
        text_string = open_file.read().lower()
    return text_string


def get_most_frequent_words(text):
    frequency = {}
    match_pattern = re.findall(r'(\w+)', text, re.UNICODE)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    sorted_list_of_values = sorted(frequency.values(), reverse=True)
    sorted_list_of_values = sorted_list_of_values[:10]

    for item in sorted_list_of_values:
        for key, value in frequency.items():
            if value == item:
                print(key)
                frequency.pop(key)
                break


if __name__ == '__main__':
    try:
        user_file_path = sys.argv[1]
        text = load_data(user_file_path)
    except (FileNotFoundError, IndexError):
        exit('Указанный файл не найден')
    get_most_frequent_words(text)
