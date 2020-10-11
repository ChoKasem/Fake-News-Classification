import requests
import html2text
from bs4 import BeautifulSoup

URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='ResultsContainer')

h = html2text.HTML2Text()
h.ignore_links = True

print(results.prettify())
print(h.handle(results.prettify()))

