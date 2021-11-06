# Expand previous Homework 5/6/7 with additional class, which allow to provide records by JSON file:
# 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed
import json
import datetime
import os
import HomeWork_5_1 as Post


class ByJson:

    def call_json(self):
        txt = input("Do you want to specify file name?\n1 - Yes\n2 - No \n")
        if txt == '1':
            file_name = input("Specify file name\n")
            try:
                self.parse_file(os.path.join(os.path.dirname(__file__), file_name))
                os.remove(os.path.join(os.path.dirname(__file__), file_name))
            except:
                print('Incorrect file name. File will be used from default folder.')
                self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.json'))
                os.remove(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.json'))

        else:
            print('File will be used from default folder.')
            self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.json'))
            os.remove(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.json'))

    def parse_file(self, file_input):
        with open(file_input) as json_file:
            data = json.load(json_file)
            for i in data:
                if i["type"] == "News":
                    new_news = Post.News("News", i["text"], i["city"], datetime.datetime.today())
                    new_news.publish_article(new_news.to_text())
                elif i["type"] == "Ad":
                    new_ad = Post.Ad("Ad", i["text"], i["data"])
                    new_ad.publish_article(new_ad.to_text())
                elif i["type"] == "Recipe":
                    new_recipe = Post.Recipe("Recipe of the day", i["text"], datetime.datetime.today())
                    new_recipe.publish_article(new_recipe.to_text())
                else:
                    print("error")

