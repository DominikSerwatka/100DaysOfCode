import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

title = soup.find(name="h3", class_="title").getText()
list_of_title = [item.getText() for item in soup.find_all(name="h3", class_="title")]
list_of_title_in_order = list_of_title[::-1]

with open("films.txt", mode="w", encoding="utf-8") as file:
    for item in list_of_title_in_order:
        file.write(f"{item}\n")
