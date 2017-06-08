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

'''
#temp function to push to the values to models

def parse(url, source):
   jsonResult = requests.get(url)
   data = json.loads(jsonResult.text)
   for article in data["articles"]:
      author = article["author"]
      title = article["title"]
      description = article["description"]
      url = article["url"]
      urlToImage = article["urlToImage"]
      publishedAt = article["publishedAt"]
      if publishedAt != None:
         publishedAt = publishedAt[:publishedAt.find("T")]
      tempObj = tbl_MST_NewsArticle(author = author,title = title,description = description,url = url,urlToImage = urlToImage,publishedAt = publishedAt,source = source)
      tempObj.save()
'''