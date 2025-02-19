# import requests module for HTTP requests
import requests
# import beautifulsoup 
from bs4 import BeautifulSoup
# import sqlite3 for database
import sqlite3

url = 'https://www.nytimes.com/section/technology'

try:
############ webscraping NYT articles ################
  # uses the requests module to fetch HTML content from specified URL
  response = requests.get(url)

  # parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(response.content, "html.parser")
  # print(soup.prettify())

  # find all elements needed to display articles (title, paragraph and links)
  titles = soup.find_all('h3', class_="css-1j88qqx e15t083i0")
  # for title in titles:
  #   print(title.text)
  paragraphs = soup.find_all('p', class_="css-1pga48a e15t083i1")
  # for paragraph in paragraphs:
  #   print(paragraph.text)
  links = soup.find_all('a', class_="css-8hzhxf")
  # for link in links:
  #   print(link.get('href'))

# ######### creating database and table ############
  # create connection to sqlite database, if it doesn't exist it will be created
  connection = sqlite3.connect('tech_news.db')
  # create a cursor object to execute SQL queries
  cursor = connection.cursor()

  # drop table if it already exists
  cursor.execute('DROP TABLE IF EXISTS articles')

  # articles database schema
  table = '''CREATE TABLE articles (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              paragraph TEXT,
              article_link TEXT
              );'''
  # creates table in database
  cursor.execute(table)
  # 'commits' table being created
  connection.commit()
  # message to console showing table has been created
  print('articles table has been created')

  # iterate through data and insert into articles table
  # zip() inserts all data in one command (best practice for matching data)
  for title, paragraph, article_link in zip(titles, paragraphs, links):
    cursor.execute('''INSERT INTO articles (title, paragraph, article_link) VALUES (?, ?, ?)''', (title.text, paragraph.text, article_link.get('href')))
  # commit changes
  connection.commit()

  # select all data from articles table
  cursor.execute('''SELECT * FROM articles''')
  # fetch data from table
  result = cursor.fetchall()
  # message in console to confirm database data has been fetched
  print(f'database data has been fetched: {result}')

############# error handling ###############
# error handling for HTTP requests
except requests.exceptions.RequestException as e:
  print(f'error fetching data from {url}: {e}')

# error handling for sqlite 
except sqlite3.Error as e:
  print(f'database error: {e}')

# catch all error handling
except Exception as e:
  print(f'an error occurred: {e}')

########### close database connection ############
# closes connection to database whether data is successful or error is thrown
finally:
  if 'connection' in locals():
    connection.close()