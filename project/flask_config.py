import os
import multiprocessing

DATABASE_URL = os.environ['DATABASE_URL']

THREADS_PER_PAGE = multiprocessing.cpu_count() * 2

CSRF_ENABLED     = True
CSRF_SESSION_KEY = os.environ['CSRF_SESSION_KEY']

# Secret key for signing cookies
SECRET_KEY = os.environ['SECRET_KEY']
