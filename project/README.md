# Flask / SQLAlchemy app template

## Database

 - Database models are defined in db/models.py.
 - db is a module, and db/__init__.py contains helpers to make database sessions for the flask app (`make_www_session`) or other programs (`make_session`).
 - `initial_setup.py` drops existing tables and initializes db. This is nominally called from scripts/init_db.py once on setup.

## WWW

 - Minimal Flask app with SQLAlchemy database structured as a module
 - gunicorn server starts project.www:app
 - files in the folder static served by nginx
 - flask config values in flask_config.py
 - app depends on environment variables for database url and other secrets

## Requirements

 - structured by common.txt (always needed), and those specific for development (dev.txt) or production (prod.txt)