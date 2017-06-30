from flask import render_template, request, escape, redirect, abort, jsonify
from project.www import app, db_session

from project.db.models import *


##
## routes
## 
@app.route("/")
def index():
    poems = db_session.query(Poem).all()
    return render_template('index.html', title="Project", poems=poems)

@app.route("/api/")
def api_index():
    poems = db_session.query(Poem).all()

    result = [{
                'author': poem.author,
                'lines': [line.text for line in poem.lines]
              } for poem in poems ]
    
    return jsonify(result)
