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

    def count_all_letters(self, text):
        all_words = re.findall(r'[a-zA-Z]', text)
        unique = dict(zip(list(all_words), [list(all_words).count(i) for i in list(all_words)]))
        res = sum(unique.values())
        return res

    def read_all_lover_letters(self, text):
        all_words = re.findall(r'[a-z]', text)
        lover = dict(zip(list(all_words), [list(all_words).count(i) for i in list(all_words)]))
        return lover

    def read_all_upper_letters(self, text):
        all_words = re.findall(r'[A-Z]', text)
        upper = dict(zip(list(all_words), [list(all_words).count(i) for i in list(all_words)]))
        upper = {k.lower(): upper[k] for k in upper}
        return upper

    def new_csv_letters(self, lover_letters, upper_letters, count):
        with open('test_2.csv', 'w') as csvfile:
            header = ['letter', 'count_all', 'count_uppercase', 'percentage']
            writer = csv.DictWriter(csvfile, delimiter='-', fieldnames=header)
            writer.writeheader()
            for word in lover_letters:
                if word in upper_letters:
                    writer.writerow({'letter': word, 'count_all': (lover_letters[word] + upper_letters[word]),
                                     'count_uppercase': upper_letters[word], 'percentage': round(100*(lover_letters[word]
                                                                                                      + upper_letters[word])/count, 2)})
                else:
                    writer.writerow({'letter': word, 'count_all': lover_letters[word], 'count_uppercase': '0',
                                     'percentage': round(100*(lover_letters[word])/count, 2)})
        csvfile.close()


def create_csv_words():
    call = GenerateCsv()
    words_from_file = call.read_all()
    unique_words = call.unique_words(words_from_file)
    call.new_csv_words(unique_words)


def create_csv_letters():
    call = GenerateCsv()
    words_from_file = call.read_all()
    unique_lover_letters = call.read_all_lover_letters(words_from_file)
    unique_upper_letters = call.read_all_upper_letters(words_from_file)
    count_all_letters = call.count_all_letters(words_from_file)
    call.new_csv_letters(unique_lover_letters, unique_upper_letters, count_all_letters)


if __name__ == '__main__':
    create_csv_letters()



