# Expand previous Homework 5/6/7/8 with additional class, which allow to provide records by XML file:
# 1.Define your input format (one or many records)
# 2.Default folder or user provided file path
# 3.Remove file if it was successfully processed
import xml.etree.ElementTree as ET
import datetime
import os
import HomeWork_5_1 as Post


class ByXml:

    def call_xml(self):
        txt = input("Do you want to specify file name?\n1 - Yes\n2 - No \n")
        if txt == '1':
            file_name = input("Specify file name\n")
            try:
                self.parse_file(os.path.join(os.path.dirname(__file__), file_name))
                os.remove(os.path.join(os.path.dirname(__file__), file_name))
            except:
                print('Incorrect file name. File will be used from default folder.')
                self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.xml'))
                os.remove(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.xml'))

        else:
            print('File will be used from default folder.')
            self.parse_file(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.xml'))
            os.remove(os.path.join(os.path.dirname(__file__), 'Default_folder', 'New.xml'))

    def parse_file(self, file_input):
        xml_file = ET.parse(file_input)
        root = xml_file.getroot()
        for row in root:
            for tags in row:
                if tags.text == "News":
                    new_news = Post.News("News", root.find('row/text').text, root.find('row/city').text, datetime.datetime.today())
                    new_news.publish_article(new_news.to_text())
                elif tags.text == "Ad":
                    new_ad = Post.Ad("Ad", row.find('text').text, row.find('data').text)
                    new_ad.publish_article(new_ad.to_text())
                elif tags.text == "Recipe":
                    new_recipe = Post.Recipe("Recipe of the day", row.find('text').text, datetime.datetime.today())
                    new_recipe.publish_article(new_recipe.to_text())

# Draft version
# xml_file = ET.parse('New.xml')
# root = xml_file.getroot()
#
# for row in root:
#     for tags in row:
#         if tags.text == "Ad":
#             print(ET.dump(row))
#             print(row.find('data').text)


