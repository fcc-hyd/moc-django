import json
import requests


class NewsParser(object):
    """
    This class is used for parsing news articles from newsapi and is used for inserting the values to the database

    Usage:
        news_parser = NewsParser(url = "some_valid_url", source = "source_of_news")
        result = news_parser.parse()
    """

    def __init__(self, url, source):
        """

        :param url: valid url string
        :param source: valid source of the url string
        """
        self.url = url
        self.source = source

    def parse(self):
        """

        :return: this function returns list of lists. This can be parsed to push the values to the database
        """
        json_result = requests.get(self.url)
        data = json.loads(json_result.text)
        final_list = []
        for article in data["articles"]:
            temp = [article["author"], article["title"], article["description"], article["url"], article["urlToImage"],
                    article["publishedAt"]]
            final_list.append(temp)
        return final_list


'''
    def store(self, final_list):
        for value in final_list:
            author = value[0]
            title = value[1]
            description = value[2]
            url = value[3]
            url_to_image = value[4]
            published_at = value[5]
            tempObj = NewsArticle(author=author, title=title, description=description, url=url,
                                          url_to_image=url_to_image, published_at=published_at, source=self.source)
            tempObj.save()
'''
