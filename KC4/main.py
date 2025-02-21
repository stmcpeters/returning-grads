# import requests module for HTTP requests
import requests
# import BeautifulSoup
from bs4 import BeautifulSoup
# import sqlite3 for database
import sqlite3
# import json to work with JSON data
import json

# set the URL you want to webscrape from
URL = 'https://books.toscrape.com/'
# set the API URL you want data from
api_url = 'https://uselessfacts.jsph.pl/api/v2/facts/random'

try: 
  api_response = requests.get(api_url)

  data = api_response.json()

  identifier = data['id']
  fact = data['text']
  source_name = data['source']
  source_url = data['source_url']
  language = data['language']
  permalink = data['permalink']

  # print(f'''
  #       identifier: {identifier}, 
  #       fact: {fact},
  #       source_name: {source_name}, 
  #       source_url: {source_url}, 
  #       language: {language}, 
  #       permalink: {permalink}
  # ''')

  # create a connection to the database, if it doesn't exist it will be created
  connection = sqlite3.connect('random_facts.db')
  # create a cursor object to execute SQL queries
  cursor = connection.cursor()

  # drop table if already exists 
  cursor.execute('DROP TABLE IF EXISTS facts')

  # facts table schema
  table = ''' CREATE TABLE facts (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              identifier TEXT,
              fact TEXT,
              source_name TEXT,
              source_url TEXT,
              language TEXT,
              permalink TEXT
          ); '''
  # creates table in database
  cursor.execute(table)
  # 'saves' table being created
  connection.commit()
  # message to make sure table is created
  print('random facts table has been created')

  # iterate through data and insert it into the table
  cursor.execute('''INSERT INTO facts (identifier, fact, source_name, source_url, language, permalink) VALUES (?, ?, ?, ?, ?, ?)''', (identifier, fact, source_name, source_url, language, permalink))
  # commit changes
  connection.commit()

  # select all data from the table
  cursor.execute('''SELECT * FROM facts''')
  # fetch data from the table
  result = cursor.fetchall()
  # checks to see if data was fetched
  #print('random facts database data: ', result)

# catches exceptions for HTTP requests (invalid URLs, etc)
except requests.exceptions.RequestException as e:
  print(f"Error fetching data from {URL}: {e}")
# catches exceptions related to SQLite database
except sqlite3.Error as e:
  print(f"Database error: {e}")
# catches any other error
except Exception as e:
  print(f"An error occurred: {e}")
# closes the connection to the database whether data is successful or an exception occurred
finally:
  if 'connection' in locals():
      connection.close()

############################################################################################################
try:
  # use the requests module to get the HTML content of the webpage
  response = requests.get(URL)
    
    # check the status code of request to see success/fail
    # print(response.status_code) // prints 200 - success

  # parse the HTML content using BeautifulSoup
  soup = BeautifulSoup(response.content, 'html.parser')

    # test to see if content is being printed
    # prettify() will return BeautifulSoup parse tree into a formatted Unicode string
    # print(soup.prettify())

  # find all elements with a specific class name (title, price, availability)
  titles = soup.find_all('h3')
  prices = soup.find_all('p', class_='price_color')
  availability = soup.find_all('p', class_='instock availability')

  # create a connection to the database, if it doesn't exist it will be created
  connection = sqlite3.connect('bookstore.db')
  # create a cursor object to execute SQL queries
  cursor = connection.cursor()

  # drop table if already exists 
  cursor.execute('DROP TABLE IF EXISTS top_books')

  # top_books table schema
  table = ''' CREATE TABLE top_books (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              title TEXT,
              price TEXT,
              availability TEXT
          ); '''
  # creates table in database
  cursor.execute(table)
  # 'saves' table being created
  connection.commit()
  # message to make sure table is created
  print('books table has been created')

  # iterate through data and insert it into the table
  # uses zip() to insert data all in one command which is best practice for matching data
  for title, price, available in zip(titles, prices, availability):
    cursor.execute('''INSERT INTO top_books (title, price, availability) VALUES (?, ?, ?)''', (title.text, price.text, available.text))
  # commit changes
  connection.commit()

  # select all data from the table
  cursor.execute('''SELECT * FROM top_books''')
  # fetch data from the table
  result = cursor.fetchall()
  # checks to see if data was fetched
  #print('database data: ', result)

# catches exceptions for HTTP requests (invalid URLs, etc)
except requests.exceptions.RequestException as e:
  print(f"Error fetching data from {URL}: {e}")
# catches exceptions related to SQLite database
except sqlite3.Error as e:
  print(f"Database error: {e}")
# catches any other error
except Exception as e:
  print(f"An error occurred: {e}")
# closes the connection to the database whether data is successful or an exception occurred
finally:
  if 'connection' in locals():
      connection.close()