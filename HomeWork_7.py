# Calculate number of words and letters from previous Homeworks 5/6 output test file.
# Create two csv:
# 1.word-count (all words are preprocessed in lowercase)
# 2.letter, cout_all, count_uppercase, percentage (add header, spacecharacters are not included)
# CSVs should be recreated each time new record added.
import csv
import re


class GenerateCsv:

    def read_all(self):
        init_file = open("Posts.txt", "r")
        words = init_file.read()
        init_file.close()
        return words

    def unique_words(self, text):
        lower_text = text.lower()
        all_words = re.findall(r'\b[a-z]{1,15}\b', lower_text)
        unique = dict(zip(list(all_words), [list(all_words).count(i) for i in list(all_words)]))
        return unique

    def new_csv_words(self, words):
        with open('test.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for word in words:
                writer.writerow([word, words[word]])
        csvfile.close()

    def read_all_letters(self, text):
        all_words = re.findall(r'[a-zA-Z]', text)
        unique = dict(zip(list(all_words),[list(all_words).count(i) for i in list(all_words)]))
        print(unique)
        return unique

    def new_csv_letters(self, words):
        with open('test_2.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter='-')
            for word in words:
                writer.writerow([word, words[word]])
        csvfile.close()


def create_csv_words():
    call = GenerateCsv()
    words_from_file = call.read_all()
    unique_words = call.unique_words(words_from_file)
    call.new_csv_words(unique_words)

def create_csv_letters():
    call = GenerateCsv()
    words_from_file = call.read_all()
    unique_letters = call.read_all_letters(words_from_file)
    call.new_csv_letters(unique_letters)


create_csv_letters()