# SoftDesk

An OpenClassrooms Project, the [10th project of the v2 Python path](https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python#path-tabs)


## Tech Stack

* Python 3.9
* Django 4.1
* PostgreSQL
* Love 💙

Further information in `requierements.txt` or `Pipfile.lock`

## Environment

Add an `.env` file at the root of the project to manage your environment variables


## Run Locally

👉 Before, you need to install [Pipenv](https://pypi.org/project/pipenv/)

Clone the project

```bash
  git clone https://github.com/CamClrt/softdesk
```

Go to the root of the project and start the server

```bash
  pipenv run manage.py runserver
```

## Running Migrations

To run migrations, run the following commands

```bash
  pipenv run manage.py makemigrations && pipenv run manage.py migrate
```

## Author

- **Camille Clarret** aka **Camoulty** or **CamClrt** : https://github.com/CamClrt