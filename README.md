# Flask Stock API

This is a simple yfinance integration and REST API. 
This app is written in Python 3.7 with Postgres 10 as the chosen data persistence. All backed up by Docker.
## Goal

The goal of this app is to have a task fetching stock information using yfinance and store it on an PostgreSQL docker
 instance, and then consume this stored data thru an API.

## Usage

Here are some quickstart instructions:

First start a postgres docker container and persist the data with a volume `flask-app-db`:

```
make start_dev_db
```

Another option is to create a postgres instance on a cloud service like elephantsql and connect it to this app. Remember to change the postgres url and don't hard code it in!

Then, start your virtual environment

```
$ pip3 install virtualenv
$ virtualenv venv
$ source venv/bin/activate
```
Now, install the python dependencies and run the server:
```
(venv) $ pip install -r requirements.txt
(venv) $ pip install -r requirements-dev.txt
(venv) $ python manage.py recreate_db
(venv) $ python manage.py runserver
```

To exit the virtual environment:
```
(venv) $ deactivate
$
```

For ease of setup, I have hard-coded postgres URLs for development and docker configurations. If you are using a separate postgres instance as mentioned above, _do not hardcode_ the postgres url including the credentials to your code. Instead, create a file called `creds.ini` in the same directory level as `manage.py` and write something like this:

```
[pg_creds]
pg_url = postgresql://testusr:password@127.0.0.1:5432/testdb
```
Note: you will need to call `api.core.get_pg_url` in the Config file.

For production, you should do something similar with the flask `SECRET_KEY`.

#### Easier setup

I've created a makefile to make this entire process easier but purposely provided verbose instructions there to show you what is necessary to start this application. To do so:
```
$ make setup
```

If you like to destroy your docker postgres database and start over, run:
```
$ make recreate_db
```
This is under the assumption that you have only set up one postgres container that's linked to the `flask-app-db` volume.

#### Super Easier setup
Just Install docker and docker compose to your machine, then go to the project folder in your command line and type:

```
docker-compose up --build
```

And the API should be available at localhost:5000/company-info for example

#### Deployment

You may use Heroku or Zeit Now to do it.

### Repository Contents

- `api/helpers/` - Holds files that define your helper classes
- `api/services/` - Holds files that define your service classes
- `api/views/` - Holds files that define your endpoints
- `api/models/` - Holds files that defines your database schema
- `api/__init__.py` - What is initially ran when you start your application
- `api/core.py` - includes core functionality including error handlers and logger
- `api/tasks.py` - includes our app tasks
- `tests/` - Folder holding tests

#### Others

- `config.py` - Provides Configuration for the application. There are two configurations: one for development and one for production using Heroku.
- `manage.py` - Command line interface that allows you to perform common functions with a command
- `requirements.txt` - A list of python package dependencies the application requires
- `Dockerfile` - instructions for Docker to build the Flask app
- `docker-compose.yml` - config to setup this Flask app and a Database
- `migrations/` - Holds migration files – doesn't exist until you `python manage.py db init` if you decide to not use docker

### MISC

If you're annoyed by the **pycache** files

```
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
```