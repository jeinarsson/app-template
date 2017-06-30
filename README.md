# Project template with Flask, nginx, postgres

Minimal useful project template and Docker development environment with

 - Postgres DB
 - Flask app (via gunicorn) with SQLAlchemy
 - Nginx web server

## Quickstart

Assuming you have [Docker](https://store.docker.com/search?type=edition&offering=community) installed. 

Start development environment:
```
cd environments/dev
docker-compose up -d
```
(`-d` means run in background, if you omit it start a new terminal for the following.)

On the first start the database is empty. Initialize the SQLAlchemy models from the app server by
```
docker-compose run flask-gunicorn project/scripts/init_db.sh
```

Browse to [localhost](http://localhost). You should see a well-known poem delivered from the database backend.

Start hacking in [/project](project/).

When done, take down containers with
```
docker-compose down
```

For more details see [environments/dev/README.md](environments/dev/README.md).


## Data persistence

The database data is stored in a docker volume db-data, see
```
docker volume ls
```

Should you want to remove that and start over, remove the volume by
```
docker volume prune
```
while the containers are down. Next time you start you will have to initialize the database again.



## Container names

If you use this template for more than one project your container names may clash (dev_db, dev_nginx and so forth.)

Set the environment variable [COMPOSE_PROJECT_NAME](https://docs.docker.com/compose/reference/envvars/#compose_project_name) to a unique project name, and docker-compose will name your containers unique_name_* instead.

Alternatively use flag `-p` for docker-compose,
```
docker-compose -p unique_name [command]
```

## Acknowledgements

[@joharohl](https://github.com/joharohl) for getting me started on this.

## License

Use any code in this repository as you please according to the [MIT License](LICENSE).
