from bs4 import BeautifulSoup

with open("website.html", mode="r") as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup)
# print(soup.prettify())
# print(soup.a)
# print(soup.p)
all_a_tag = soup.find_all(name='a')
print(all_a_tag)

for tag in all_a_tag:
    # print(tag.string)
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_='heading')
print(section_heading)
print(section_heading.get("class"))

company_url = soup.select_one(selector="p a")
print(company_url)
name_h1 = soup.select_one(selector="#name")
print(name_h1)
heading_classes = soup.select(selector='.heading')
print(heading_classes)