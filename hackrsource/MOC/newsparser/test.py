from news_parser import NewsParser

def main():
	url = "https://newsapi.org/v1/articles?source=the-telegraph&sortBy=top&apiKey=07dcf26d0ded41ba8436fb8bd233edba"
	source = "TheTelegraph"
	np = NewsParser(url, source)
	result_set = np.parse()
	np.store()

if __name__ == "__main__":
	main()

for value in final_list:
    author = value[0]
    title = value[1]
    description = value[2]
    url = value[3]
    url_to_image = value[4]
    published_at = value[5]
    if published_at is not "":
	    published_at = published_at[:published_at.find("T")]
    tempObj = NewsArticle(author=author, title=title, description=description, url=url,
                                  url_to_image=url_to_image, published_at=published_at, source=source)
    tempObj.save()
    