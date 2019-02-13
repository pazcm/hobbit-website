import os
from flask import Flask, render_template

app = Flask(__name__)

"""
Routing: Allows us to swith between views using URLs 
create a route and a view
"""
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
debug=True)