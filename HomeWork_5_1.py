# Create a tool, which will do user generated news feed:
# 1.User select what data type he wants to add
# 2.Provide record type required data
# 3.Record is published on text file in special format
#
#
# You need to implement:
# 1.News  text and city as input. Date is calculated during publishing.
# 2.Privat ad  text and expiration date as input. Day left is calculated during publishing.
# 3.Your unique one with unique publish rules.
#
#
# Each new record should be added to the end of file. Commit file in git for review.

import datetime


class Post:
    def __init__(self, title, text):
        self.title = title
        self.text = text

    @staticmethod
    def publish_article(text):
        with open("Posts.txt", "a") as file:
            file.write(text)


class News(Post):
    def __init__(self, title, text, city, date):
        Post.__init__(self, title, text)
        self.city = city
        self.date = date

    def to_text(self):
        return f"{self.title} {30 * '-'}\n" \
               f"{self.text} \n" \
               f"City: {self.city}, {self.date.strftime('%m/%d/%Y %H.%M')}\n" \
               f"{35 * '-'}\n"  \
               f"\n\n"


class Ad(Post):
    def __init__(self, title, text, end_date):
        Post.__init__(self, title, text)
        self.end_date = end_date

    def to_text(self):
        days_left = (datetime.datetime.strptime(self.end_date, "%m/%d/%Y") - datetime.datetime.today())
        return f"{self.title} {30 * '-'}\n" \
               f"{self.text} \n" \
               f"Actual until: {self.end_date}, {days_left.days} days left\n" \
               f"{35 * '-'}\n"  \
               f"\n\n"


class Recipe(Post):
    def __init__(self, title, text, date):
        Post.__init__(self, title, text)
        self.date = date

    def complexity_of_recipe(self):
        count = len(self.text) - len(self.text.replace(" ", ""))
        if count < 5:
            complexity = "Low"
        elif 5 < count < 10:
            complexity = "Medium"
        else:
            complexity = "High"
        return complexity

    def to_text(self):
        return f"{self.title} {25 * '-'}\n" \
               f"{self.text} \n" \
               f"Complexity of the recipe: {self.complexity_of_recipe()}, {self.date.strftime('%m/%d/%Y %H.%M')}\n" \
               f"{35 * '-'}\n"  \
               f"\n\n"


def start():
    while True:
        txt = input("Specify type of post:\n1 - News\n2 - Ad \n3 - Recipe\n")
        if txt == "1":
            new_news = News("News", input('Print your text\n'), input("Print your city\n"), datetime.datetime.today())
            new_news.publish_article(new_news.to_text())
        elif txt == "2":
            new_ad = Ad("Ad", input('Print your text\n'), input("Print endDate of ad in dd/mm/yyyy format\n"))
            new_ad.publish_article(new_ad.to_text())
        elif txt == "3":
            new_recipe = Recipe("Recipe of the day", input('Print your recipe\n'), datetime.datetime.today())
            new_recipe.publish_article(new_recipe.to_text())
        else:
            print('ERROR')
            exit(0)

if __name__ == '__main__':
    start()




