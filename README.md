# BookFacts

### Overview of project
BookFacts is a Python-based web application built with Flask that scrapes book data and fetches random facts from an API. The app stores book data in a SQLite database called bookstore and random facts in another database called random_facts. The frontend is styled using Bootstrap, ensuring a clean and responsive user interface.
### Demo


https://github.com/user-attachments/assets/4d132f54-1336-460d-b3bf-fa8da0f29acf


### Features
- Web Scraping: Collects book data from online sources and stores it in the bookstore database.
- API Integration: Fetches random facts from an API and stores them in the random_facts database.
- Flask Framework: Lightweight and efficient backend handling.
- Bootstrap Styling: Clean, responsive, and modern user interface.
### Technologies Used
- Python
- Flask
- SQLite
- BeautifulSoup (for web scraping)
- Requests (for API calls)
- Bootstrap Styling
### Database Schemas
<img width="500" alt="Screenshot 2025-02-07 at 6 13 10 PM" src="https://github.com/user-attachments/assets/c79b9fab-b0eb-4add-b24d-e66efc4548ea" />
<img width="500" alt="Screenshot 2025-02-07 at 6 12 25 PM" src="https://github.com/user-attachments/assets/ece96ea7-5e02-4009-8913-f9f2723c838c" />

### Installation Instructions
#### Prerequisites 
Python 3.x

1. Clone the Repository:
`git clone https://github.com/yourusername/bookfacts.git <project-name>`
`cd bookfacts`
2. Create a Virtual Environment:
`python -m venv venv`
`source venv/bin/activate`  
3. Install Dependencies:
`pip install -r requirements.txt`
4. Run the Application:
`python3 app.py`
The app will be available at `http://127.0.0.1:5000/`.
### Contributing
Contributions are welcomed to this project! If you have an idea for a new feature or a bug fix, please open an issue or a pull request.
