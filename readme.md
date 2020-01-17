# Trivia Master Backend
Trivia Master Backend is a Python Django Rest Framework database API designed to work with a front end, Trivia Master Frontend. It provides user authentication, and api access points to register new users, and to store into the database answers (information for a specific trivia question about the category, user, correctness of answer, and time to answer) and quizes (series of multiple answers)

## Dependency Installation
Using the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements:

```bash
pip install -r requirements.txt
```

## Usage
With all dependencies installed, ensure existance of a db called trivia_backend, and migrate models into the database using:
```bash
python manage.py migrate
```

a superuser can be created by using:
```bash
python manage.py createsuperuser
```

Then run the server using:

```bash
python manage.py runserver
```
With the server running, access to the admin panel can be obtained at

/admin/

With the server running the following api routes are available:

/api/users/

/api/quiz/
/api/quiz/<quiz_id>/

/api/answer/
