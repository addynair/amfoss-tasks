from bs4 import BeautifulSoup
import requests
url = "https://www.espncricinfo.com/live-cricket-score"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())


match = doc.find(class_= "div.ds-flex ds-flex-col ds-mt-2 ds-mb-2")
print(match)

