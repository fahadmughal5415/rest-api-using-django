# REST API Using Django

This project is a simple REST API built using Django and Django REST Framework. It serves as a basic backend for managing movie data, including different categories such as Action, Comedy, and Horror.

## Features

- CRUD operations for movie data.
- Categorized movie endpoints (Action, Comedy, and Horror).
- Modular and scalable design using Django ViewSets and Routers.

## Requirements

- Python 3.12 or higher
- Django 5.1.6
- Django REST Framework

## Installation

1. Clone the repository:

- git clone https://github.com/fahadmughal5415/rest-api-using-django.

- cd rest-api-using-django

2. Set up a virtual environment:
- python -m venv .venv source .venv/bin/activate # For macOS/Linux.
- venv\Scripts\activate # For Windows

3. Install the required dependencies:
- pip install -r requirements.txt

4. Apply the migrations:
- python manage.py migrate

5. Run the development server:
- python manage.py runserver


## API Endpoints

- **Base URL:** `http://127.0.0.1:8000/`
- **Movies:** `GET /movies/`
- **Action Movies:** `GET /action/`
- **Comedy Movies:** `GET /comedy/`
- **Horror Movies:** `GET /horror/`


## Usage

Use Postman or similar tools to test the API endpoints for retrieving and managing movie data.

## License

This project is open-source and available under the MIT License.
