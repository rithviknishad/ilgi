# ilgi

Digital Journal
## Quickstart

1. Set up a Python virtual environment and install the required Python dependencies:

        pipenv install

2. Create `.env` configuration file based on `env.sample`:

        cp env.sample .env
        vim .env

3. Set up the database

    You'll need to create the database and set `DATABASE_URL` in
    the configuration file before you can run migrations and use the code.

    To use SQLite (supported out of the box), set the `DATABASE_URL` to
    the location of database file (it will be created on the first run),
    either relative to the project directory:

        DATABASE_URL=sqlite:///sqlite.db

    Or absolutely positioned in the file system:

        DATABASE_URL=sqlite:////full/path/to/sqlite.db

    (Note the three or four dashes in the URL, respectively).

    To use PostgreSQL or MariaDB databases, install the appropriate
    driver and create database and user as needed. Example for
    PostgreSQL (this assumes you already have PostgreSQL installed
    on your system via package manager such as apt, rpm, or brew):

    1. Connect to the database as admin and create a new user and database

        CREATE USER 'appuser' WITH PASSWORD 'secretpassword';
        CREATE DATABASE 'dbname' WITH OWNER 'appuser';

    2. Install Python database driver for PostgreSQL

        pipenv install psycopg

    3. Set up `DATABASE_URL` in your `.env`:

        DATABASE_URL=postgres://appuser:secretpassword@localhost/dbname

4. Run migrations:

        pipenv run python manage.py makemigrations
        pipenv run python manage.py migrate

5. Run the server:

        pipenv run python manage.py runserver

6. Visit the browsable API at http://localhost:8000/api/v1/

## Creating superuser

A superuser account can be created using the Django management command:

    pipenv run python manage.py createsuperuser

## Tests, linters and code coverage

Activate your pipenv environment with `pipenv shell` so you
don't need to prefix every command with `pipenv run`.

To run the test suite:

    python manage.py test

To run the test suite and get code coverage statistics:

    coverage run manage.py test
    coverage report

To generate HTML reports, run this and open `htmlcov/index.html`
afterwards:

    coverage html

To format the code automatically using `ruff`, run it
from the project root directory:

    ruff format .

To check for common programming errors or style problems,
run `ruff` linter in the project root directory:

    ruff check --fix .

To automatically run `ruff` (formatter and linter)
on every git commit, set up a git `pre-commit` hook:

    pre-commit install

Note that you'll need to have initialized your git repository for
the git pre-commit hook to be available. To test it without installation,
you can run:

    pre-commit run --all-files

## Continuous integration with GitHub Actions

This project comes with a GitHub Actions workflow that runs
the test suite and linters on every push to the repository.

See the `.github/workflows/django.yml` file for details.

## Background tasks using Celery

Use `CELERY_BROKER_URL` and `CELERY_BACKEND` environment variables to
configure broker and optional results backend to use for the background
jobs, see `env.sample` for details.

Tasks are defined in `tasks.py` in the appropriate app module.

To run the worker, in the project root, run:

        celery -A project worker

Logging from the tasks will be shown/hidden based on the celery worker
log level (default is `WARNING`, can be changed with `-l LEVEL` worker
option), not based on Django logging configuration.

To show `INFO` or higher-priority messages, use:

        celery -A project worker -l INFO

To run periodic tasks using Celery Beat, specify beat entries
in `settings/base.py` and run celery beat:

        celery -A project beat -l INFO

## Docker support

Build the docker image with:

        docker build -t ilgi .

The default command is to start the web server (gunicorn). Run the image
with `-P` docker option to expose the internal port and check the exposed
port with `docker ps`:

        docker run --env-file .env --P ilgi
        docker ps

Make sure you provide the correct path to the env file (this example assumes
it's located in the local directory).

To run a custom command using the image (for example, db migrations):

        docker run --env-file .env ilgi python manage.py migrate

To run a Django shell inside the container:

        docker run --env-file .env -t ilgi

Note that any changes inside the container will be lost. For that reason,
running `collectstatic` or using a SQLite database within a container will
have no effect. If you want to use SQLite with docker, mount a docker
volume and place the SQLite database inside it.

For more information on the docker build process, see the included `Dockerfile`.
