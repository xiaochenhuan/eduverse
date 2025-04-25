Final Project Report: US Public Schools Data Viewer (Django Application)
Overview
This project is a Django-based web application developed to present open data on public schools in the United States. The application allows users to view detailed information about each school, including its name, address, and city. It also includes a user authentication system for login functionality.

Data Source
The data source used in this application consists of open public data from US schools. The dataset includes 5000 records and was loaded into the Django app using custom management commands.

Database Design
The application uses a single database model School, which stores details such as:

Name
Address
City
State
ZIP code
Functionality
Homepage listing schools
Detail page for each school
Search/filter by city (optional)
Login page for user authentication
Enrolment graph
Testing
We implemented unit tests to validate the School model and its data integrity.

Deployment
Deployment to a cloud provider is in progress.

Technologies Used
Django (Python)
HTML / Django templates
Bootstrap (for styling)
SQLite (for development database)
Installation
Clone the repository
git clone https://github.com/tarekaust/yourrepo.git
cd yourrepo
python -m venv env
source env/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata schools.json
python manage.py runserver

##Run unit tests with:
python manage.py

100%
(2:1)
