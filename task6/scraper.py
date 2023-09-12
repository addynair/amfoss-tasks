from bs4 import BeautifulSoup
import requests
url = "https://www.espncricinfo.com/live-cricket-score"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")



match = doc.find(class_= "ds-flex ds-flex-col ds-mt-2 ds-mb-2")
score = match.get_text()

