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
import HomeWork_7 as Csv
import HomeWork_8 as Json
import HomeWork_9 as Xml
import HomeWork_10 as db


class ByTxt:

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

    def parse_file(self, file_input):
        hm10 = db.DBConnetion('test1.db')
        with open(file_input) as file:
            text = file.read()
            text_from = text_from_list(list_of_line(text))
            k = text_from.split('\n')
            for line in k:
                if line.find('News') != -1:
                    parts = line.split('.')
                    new_news = Post.News("News", parts[1].rstrip(), parts[2].rstrip(), datetime.datetime.today())
                    new_news.publish_article(new_news.to_text())
                    if not hm10.select_param('*', 'News', parts[1].rstrip(), parts[2].rstrip()):
                        new_news.get_data_to_db('News', parts[1].rstrip(), parts[2].rstrip(), datetime.datetime.today())
                elif line.find('Ad') != -1:
                    parts = line.split('.')
                    new_ad = Post.Ad("Ad", parts[1].rstrip(), parts[2].rstrip())
                    new_ad.publish_article(new_ad.to_text())
                    if not hm10.select_param('*', 'Ad', parts[1].rstrip(), parts[2].rstrip()):
                        new_ad.get_data_to_db('Ad', parts[1].rstrip(), parts[2].rstrip(), datetime.datetime.today())
                elif line.find('Recipe') != -1:
                    parts = line.split('.')
                    new_recipe = Post.Recipe("Recipe of the day", parts[1].rstrip(), datetime.datetime.today())
                    new_recipe.publish_article(new_recipe.to_text())
                    if not hm10.select_param('*', 'Recipe', parts[1].rstrip(), new_recipe.complexity_of_recipe()):
                        new_recipe.get_data_to_db('Recipe', parts[1].rstrip(), new_recipe.complexity_of_recipe(),
                                              datetime.datetime.today())
                else:
                    print("error")
            # os.remove(file_input)


def user_choose():
    txt = input("Do you want to use manual input?\n1 - Yes\n2 - No \n")
    if txt == "1":
        Post.start()
    elif txt == "2":
        txt = input("Do you want to use TXT or JSON or Xml file?\n1 - TXT\n2 - JSON\n3 - XML\n")
        if txt == "1":
            start = ByTxt()
            start.call_txt()
        elif txt == "2":
            start = Json.ByJson()
            start.call_json()
        elif txt == "3":
            start = Xml.ByXml()
            start.call_xml()
        else:
            print('ERROR')
            exit(0)
    else:
        print('ERROR')
        exit(0)
    Csv.create_csv_words()
    Csv.create_csv_letters()


user_choose()
