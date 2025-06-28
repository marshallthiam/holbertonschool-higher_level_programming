from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Secret key for JWT
app.config['JWT_SECRET_KEY'] = 'your-super-secret-key'
jwt = JWTManager(app)

# In-memory user store
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

### ========== BASIC AUTHENTICATION ==========

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return username

@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")


### ========== JWT AUTHENTICATION ==========

# Login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity={
            "username": username,
            "role": user["role"]
        })
        return jsonify(access_token=access_token), 200

    return jsonify(error="Invalid credentials"), 401

# JWT Protected route
@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

# Admin-only route
@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify(error="Admin access required"), 403
    return jsonify(message="Admin Access: Granted")


### ========== ERROR HANDLING FOR JWT ==========

@jwt.unauthorized_loader
def handle_missing_token(err):
    return jsonify(error="Missing or invalid token"), 401

@jwt.invalid_token_loader
def handle_invalid_token(err):
    return jsonify(error="Invalid token"), 401

@jwt.expired_token_loader
def handle_expired_token(jwt_header, jwt_payload):
    return jsonify(error="Token has expired"), 401

@jwt.revoked_token_loader
def handle_revoked_token(jwt_header, jwt_payload):
    return jsonify(error="Token has been revoked"), 401

@jwt.needs_fresh_token_loader
def handle_fresh_token_required(jwt_header, jwt_payload):
    return jsonify(error="Fresh token required"), 401


### ========== RUN ==========

if __name__ == '__main__':
    app.run(debug=True)
