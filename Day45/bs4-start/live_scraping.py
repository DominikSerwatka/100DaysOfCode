from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text
# print(response.text)
soup = BeautifulSoup(yc_web_page, 'html.parser')
# print(soup.title)
first_article_title = soup.find(name="span", class_="titleline")
print(first_article_title.getText())
print(first_article_title.find(name="a").get_text())
article_link = soup.find(name="span", class_="titleline").a.get("href")
article_upvote = soup.find(name="span", class_='score').getText()
print(article_link)
print(article_upvote)
list_of_socore = []
list_of_tags = soup.find_all(name="span", class_='score')
for tag in list_of_tags:
    print(tag.getText())
    score = tag.getText().split()[0]
    list_of_socore.append(score)
list_of_titles = [tag.getText() for tag in soup.find_all(name="span", class_="titleline")]
list_of_links = [tag.a.get("href") for tag in soup.find_all(name="span", class_="titleline")]
print(list_of_links)
print(list_of_socore)
list_socres = [eval(score) for score in list_of_socore]
print(list_socres)
print(max(list_socres))
print(list_socres.index(max(list_socres)))
index = list_socres.index(max(list_socres))
max_upvote = list_socres.index(max(list_socres))
print(list_of_links[index+1])
print(list_of_titles[index+1])
