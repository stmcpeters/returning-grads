import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/section/technology'

try:
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  # print(soup.prettify())
  # extract all the article titles
  titles = soup.find_all('h3', class_="css-1j88qqx e15t083i0")
  # for title in titles:
  #   print(title.text)
  paragraphs = soup.find_all('p', class_="css-1pga48a e15t083i1")
  # for paragraph in paragraphs:
  #   print(paragraph.text)
  links = soup.find_all('a', class_="css-8hzhxf")
  # for link in links:
  #   print(link.get('href'))
except requests.exceptions.RequestException as e:
  print(f'error fetching data from {url}: {e}')
except Exception as e:
  print(f'an error occurred: {e}')