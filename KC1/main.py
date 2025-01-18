# import requests module to make HTTP requests
import requests
# import BeautifulSoup
from bs4 import BeautifulSoup
# import sqlite3
import sqlite3

# set the URL you want to webscrape from
URL = 'https://www.cnn.com/entertainment/celebrities'
# use the requests module to get the HTML content of the webpage specified
response = requests.get(URL)

  # check the status code of the request (200 means the request was successful)
  #print(response.status_code) 

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

  # test to see if the content is being printed
  # prettify() method will turn a Beautiful Soup parse tree into a nicely formatted Unicode string, with a separate line for each tag and each string:
  # print(soup.prettify())

# find all the elements with a specific class name
headlines = soup.find_all('span', class_='container__headline-text')
# display the headlines
# iterate through the headlines and print each headline on a new line
for headline in headlines:
  print(headline.text, '\n')

# create a connection to the database
# if the database does not exist, it will be created
conn = sqlite3.connect('news.db')
# create a cursor object using the cursor() method so we can execute SQL queries
c = conn.cursor()

# create a table in the database
# c.execute('''
#           CREATE TABLE celebrities (
#           ID INTEGER PRIMARY KEY AUTOINCREMENT, 
#           headline TEXT)
#           ''')

# iterate through each headline and insert it into the table
for headline in headlines:
  # the comma is necessary to make it a tuple, SQLite requires a tuple for the second argument (is treated like a string without the comma)
  c.execute('''INSERT INTO celebrities (headline) VALUES (?)''', (headline.text,))
# commit the inserted data to the database
# conn.commit()

# select all the data from the table
c.execute('''SELECT * FROM celebrities''')
# fetch all the data from the table
result = c.fetchall()
print(result)

# close the connection to the database
conn.close()