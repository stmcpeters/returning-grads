# KC5

### Overview of project
This project is a Python-based web application built with Flask that scrapes trending technology articles from the [New York Times](https://www.nytimes.com/section/technology) and fetches tech jokes from a [Joke API](https://github.com/15Dkatz/official_joke_api?tab=readme-ov-file). The app stores article data in a SQLite database called `tech_news` and random tech jokes in another database called `jokes_api`. The frontend is styled using Tailwind CSS, ensuring a clean and responsive user interface.

### Demo


https://github.com/user-attachments/assets/46cddd26-9800-4823-97f1-4d95b8d1672b



### Features
- Web Scraping: Collects news article data from online sources and stores it in the `tech_news` database.
- API Integration: Fetches random jokes from an API and stores them in the `jokes_api` database.
- Flask Framework: Lightweight and efficient backend handling.
- Tailwind Styling: Clean, responsive, and modern user interface.
- Unittest: Integrated testing of connections to databases and routes using Unittest and generates coverage report

### Technologies Used
- Python
- Flask
- SQLite
- BeautifulSoup (for web scraping)
- Requests (for API calls)
- Tailwind Styling
- Unittest

### Installation Instructions
#### Prerequisites 
Python 3.x


1. Clone the Repository:
`git clone https://github.com/yourusername/returning-grades.git <project-name>`
`cd KC5`
2. Create a Virtual Environment:
`python -m venv venv`
`source venv/bin/activate`  
3. Install Dependencies:
`pip install -r requirements.txt`
4. Run the Application:
`python3 app.py`
The app will be available at `http://127.0.0.1:8000/`.

### Testing
Unittest coverage report can be generated using `coverage run -m unittest tests/test_app.py`

### Screenshots of Databases
<img width="1030" alt="Screenshot 2025-02-19 at 10 53 34 PM" src="https://github.com/user-attachments/assets/f5732a77-2e07-4fb8-b61a-de8d00ad91d1" />
<img width="1030" alt="Screenshot 2025-02-19 at 10 53 12 PM" src="https://github.com/user-attachments/assets/dc1be9da-1f01-4e6e-bd82-6fa9c8e148d8" />

### Contributing
Contributions are welcomed to this project! If you have an idea for a new feature or a bug fix, please open an issue or a pull request.
