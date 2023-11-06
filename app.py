from flask import Flask, render_template, jsonify
from dotenv import load_dotenv

load_dotenv()

from models.db import init_db
from models.user import User
from routes.computeRoutes import api_routes
from routes.users import user_routes

app = Flask(__name__)

# Initialize the database
init_db(app)

@app.route('/')
def index():
    data = {"message": "Welcome to the homepage"}
    return render_template('index.html', data=data)

app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)



