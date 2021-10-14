# Expand previous Homework 5 with additional class, which allow to provide records by text file:
# # 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed
# 4.Apply case normalization functionality form Homework 3/4

import datetime
import os
import HomeWork_5_1 as Post
from HomeWork_4_1 import text_from_list
from HomeWork_4_1 import list_of_line
import HomeWork_7 as CSV


class By_txt:
    def read_from(self, path):
        with open("Posts.txt", "r") as file:
            file.write(path)

    def call_txt(self):
        txt = input("Do you want to specify file name?\n1 - Yes\n2 - No \n")
        if txt == '1':
            file_name = input("Specify file name\n")
            try:
                self.parse_file(os.path.join(os.path.dirname(__file__), file_name))
            except:
                print('Incorrect file name. File will be used from default folder.')
                self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.txt'))
        else:
            print('File will be used from default folder.')
            self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.txt'))

    def parse_file(self,file_input):
        with open(file_input) as file:
            text = file.read()
            text_from = text_from_list(list_of_line(text))
            k = text_from.split('\n')
            for line in k:
                if line.find('News') != -1:
                    parts = line.split('.')
                    new_news = Post.News("News", parts[1].rstrip(), parts[2].rstrip(), datetime.datetime.today())
                    new_news.publish_article(new_news.to_text())
                elif line.find('Ad') != -1:
                    parts = line.split('.')
                    new_ad = Post.Ad("Ad", parts[1].rstrip(), parts[2].rstrip())
                    new_ad.publish_article(new_ad.to_text())
                elif line.find('Recipe') != -1:
                    parts = line.split('.')
                    new_recipe = Post.Recipe("Recipe of the day", parts[1].rstrip(), datetime.datetime.today())
                    new_recipe.publish_article(new_recipe.to_text())
                else:
                    print("error")
            os.remove(file_input)


def user_choose():
    txt = input("Do you want to use manual input?\n1 - Yes\n2 - No \n")
    if txt == "1":
        Post.start()
        CSV.create_csv_words()
    elif txt == "2":
        start = By_txt()
        start.call_txt()
        CSV.create_csv_words()
    else:
        print('ERROR')
        exit(0)


user_choose()