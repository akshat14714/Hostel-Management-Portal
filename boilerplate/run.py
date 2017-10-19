from app import app
from flask_cors import CORS
CORS(app)

app.run(host='127.0.0.1', port = 5000, debug =True)
