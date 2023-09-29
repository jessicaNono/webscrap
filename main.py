import requests
from bs4 import BeautifulSoup


def news():
    # the target we want to open     
    url = 'https://www.bbc.com/news'

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")
        print("The news are as follow :-\n")

        # we need a parser,Python built-in HTML parser is enough . 
        soup = BeautifulSoup(resp.text, 'html.parser')
        # l is the list which contains all the text i.e news
        l = (soup.find("div", {"id": "news-top-stories-container"})).div.div.div.div.div


        # Extract primary article details
        primary_article_title = l.find("h3", class_="gs-c-promo-heading__title").text
        primary_article_link = l.find("a", class_="gs-c-promo-heading")["href"]
        primary_article_img = l.find("img", class_="qa-srcset-image")["src"]

        # Extract related content
        related_articles = soup.find_all("li", class_="nw-c-related-story")
        related_content = []

        for article in related_articles:
            title = article.find("span", class_="nw-o-link-split__text").text
            link = article.find("a")["href"]
            related_content.append({"title": title, "link": link})

        # Output the extracted data
        print("Primary Article:")
        print("Title:", primary_article_title)
        print("Link:", primary_article_link)
        print("Image:", primary_article_img)
        print("\nRelated Content:")

        for article in related_content:
            print("Title:", article["title"])
            print("Link:", article["link"])
            print("------")




    else:
        print("Error")


news()