from flask import Flask, render_template, jsonify
from models.db import init_db
from models.user import User
from routes.computeRoutes import api_routes
from routes.users import user_routes

app = Flask(__name__)

# Initialize the database
init_db(app)

@app.route('/')
def index():
    # Replace this with your data retrieval logic
    data = {"message": "Welcome to the homepage"}
    return render_template('index.html', data=data)

# app.register_blueprint(api_data)
app.register_blueprint(user_routes, url_prefix='/users')
app.register_blueprint(api_routes, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)



# from flask import Flask, render_template, jsonify
# from flask_restful import Api
# from models.user import User
# from models.db import init_db
# # from resources.api import ExampleAPI
# from decouple import config


# app = Flask(__name__)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # SECRET_KEY = config('SECRET_KEY')
# # DATABASE_URI = config('DATABASE_URI')

# app.config['SECRET_KEY'] = 'secret_inspecthoa'
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://shugupta:@localhost/inspecthoa'

# api = Api(app)
# # api.add_resource(ExampleAPI, '/api')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/api/data')
# def get_api_data():
#     # Replace this with actual data retrieval logic
#     data = [{'id': 1, 'name': 'Item 1'}, {'id': 2, 'name': 'Item 2'}]
#     return jsonify(data)

# if __name__ == '__main__':
#     init_db(app)
#     app.run(debug=True)
