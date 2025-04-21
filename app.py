# from flask import Flask
# from database import db, create_app

# app = create_app()

# if __name__ == "__main__":
#     print("server starting")
#     app.run(debug=True)
#     print("server started")
from flask import Flask
from flask_migrate import Migrate 
from models.models import Country, User
from dotenv import load_dotenv
from flask_cors import CORS
from database import db
load_dotenv() 
import os 
from views.farmer_views import farmer_bp
from views.farm_views import farm_bp
from views.schedule_views import schedule_bp
from views.fertilizer_views import fertilizer_bp  
from views.user_views import user_bp
from flask import request


app = Flask(__name__)
# CORS(app)
# CORS(app, supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4200"}})
# CORS(app, supports_credentials=True)
# CORS(app,supports_credentials=True, resources={r"/*": {"origins": "http://localhost:4200"}}) 
# Updated the SQLAlchemy connection string
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:Aditi2101@localhost/farmerdb"

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI", "postgresql://postgres:Aditi2101@db:5433/farmerdb")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] =f"{os.getenv('SECRET_KEY')}"
app.register_blueprint(farmer_bp, url_prefix="/farmer")
app.register_blueprint(farm_bp, url_prefix="/farm")
app.register_blueprint(schedule_bp, url_prefix="/schedule")
app.register_blueprint(fertilizer_bp, url_prefix="/fertilizer")  # Changed spelling
app.register_blueprint(user_bp, url_prefix="/user")

# Allow all origins (instead of restricting to localhost:4200)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# cors=CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})
# CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}}, supports_credentials=True)
# CORS(app, origins=["http://localhost:4200"], supports_credentials=True)
cors = CORS(app,supports_credentials=True, resources={r"/*": {"origins": "https://farmerpoint-abb84.web.app"}})
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def hello():
    return "hello!"

@app.before_request
def log_request():
    print(f"Incoming request: {request.method} to {request.url}")

@app.after_request
def after_request(response):
    # response.headers.add('Access-Control-Allow-Origin', '*')  # Allow all origins
    # response.headers.add('Access-Control-Allow-Origin', 'http://localhost:4200')
    response.headers.add("Access-Control-Allow-Origin", request.headers.get("Origin"))
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,role')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

with app.app_context():
    db.create_all()
    superuser = User.query.filter_by(name='aditisuper').first()
    if not superuser:
        # new_superuser = User(name='aditisuper', password_hash='$2b$12$NTT0kA9aBDBZ3L7KFMjQuuW4m284f6vO/zvqLuyf1HUtbx7HGz2L.', phonenumber="9425654742", role=["super"])
        new_superuser = User(name='aditisuper', password_hash='pbkdf2:sha256:600000$YaCkGxI4$87ff1a0e50bd8b66048644a5c20faeb50bbad9656a432345a84df38dfc6ce152', phonenumber="8717943006", role=["super"])
        db.session.add(new_superuser)
        db.session.commit()
        print("Superuser created.")
    else:
        print("Superuser already exists.")

if __name__ == "__main__":
    app.run(debug=True)
