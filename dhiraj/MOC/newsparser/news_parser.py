'''
Author : Dhiraj Subramanian B
This python module will be used for requesting NewsApi for fetching latest news. The latest news will be then updated to the application database.
'''

import requests, json

class NewsParser(object):
	# two methods, for initializing the json and pushing it to db
	def parse(self):
		jsonResult = requests.get("https://newsapi.org/v1/articles?source=the-verge&sortBy=top&apiKey=07dcf26d0ded41ba8436fb8bd233edba")
		data = json.loads(jsonResult.text)
		finalList = []
		for article in data["articles"]:
			temp = [article["author"], article["title"], article["description"], article["url"], article["urlToImage"], article["publishedAt"]]
			finalList.append(temp)
		return(finalList)