# Development environment

Docker setup that creates

- a docker volume db-data
- a postgres db on port 5432
- nginx server on port 80
- flask + gunicorn app server on port 8000

## Get started

Assuming you have Docker installed, execute in this directory
```
docker-compose up
```

On the first start the database exists but is empty. Initialize it from the app by
```
docker-compose run flask-gunicorn project/scripts/init_db.sh
```

Browse to [localhost](http://localhost).


To get a shell in the app server, execute
```
docker-compose run flask-gunicorn bash
```


To force rebuild of images (for example if you change the python requirements)
```
docker-compose down
docker-compose build
```

If you only change docker-compose.yml, say for environment variables to app, restart with
```
docker compose down && docker-compose up
```

## Description

### Database

Postgres image with one db called 'projectdb', and one user 'dbuser' with password 'dbpassword'.

/var/lib/postgresql/data is bound to the docker volume db-data for persistence.

See
```
docker volume ls
```

To remove the data and start over, stop the containers and purge unused volumes:
```
docker-compose down
docker volume prune
```

### App server

A python3 image that binds /src/project to the project folder on the host to allow hot-reloading of code.

pip installs requirements in project/requirements/dev.txt when image is built.

Runs gunicorn server serving flask app on start.

### Nginx

Listens on :80

Binds project/www/static to /www/static, and tries that first, if not found forwards to app server.



