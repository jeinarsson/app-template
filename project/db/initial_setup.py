from sqlalchemy import create_engine
import project.db as db
import os

from project.db.models import *

def create_from_empty(database_url = None):
    import project.db.models

    if database_url is None:
        database_url = os.environ['DATABASE_URL']
    
    

    engine = create_engine(database_url)

    # create schema
    print('Initializing DB in\n{}'.format(database_url))
    db.Base.metadata.drop_all(bind=engine)
    db.Base.metadata.create_all(bind=engine, checkfirst=True)
    
    print('Adding some initial data.')
    # add any initial data
    s = db.make_session(database_url)

    p = Poem(author='Lord Tennyson')
    text = [
    	"'Tis better to have loved and lost", 
    	"Than never to have loved at all."
    	]
    for l in text:
    	p.lines.append(PoemLine(text=l))

    s.add(p)
    
    s.commit()

    print('Done.')

    