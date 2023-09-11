from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.string)  # string as title
# print(soup.prettify())  # whole html

all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.getText())  # print tags
    print(tag.get("href"))  # print links

heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)
print(section_heading.getText())
print(section_heading.name)

company_url = soup.select_one(selector="p a")  # string is CSS selector
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings_list = soup.select(".heading")
print(headings_list)
