from flask import Flask
from flask import request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return "Hello World!"

@app.route("/about")
def about():
    return "This is a About Page!"

@app.route("/greet", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.json.get("name")
        return f"Hello {name}!"
    return "Send POST request with your name in JSON format!"

@app.route('/users', methods=["GET"])
def get_all_users():
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 2, type=int)
    start = (page - 1) * per_page
    end = start + per_page
    paginated_users = list(users.values())[start:end]
    return {
        "users": paginated_users,
        "page": page,
        "per_page": per_page,
        "total": len(users)
    }

@app.route('/user', methods=["POST"])
def create_user():
    data = request.json
    user_id = data.get("id")
    name = data.get("name")
    email = data.get("email")
    if not user_id or not name or not email:
        return {"error": "Id, name and email are required"}, 400
    if user_id in users:
        return {"error": "User already exists"}, 400
    users[user_id] = {"id": user_id, "name": name, "email": email}
    return {"message": "User created!", "user": users[user_id]}, 201

@app.route('/user/<int:id>', methods=["GET"])
def get_user(id):
    user = users.get(id)
    if user:
        return {"user": user}
    return {"error": "User not found"}, 404

@app.route('/user/<int:id>', methods=["PUT"])
def update_user(id):
    if id not in users:
        return {"error": "User not found"}, 404
    name = request.json.get("name")
    email = request.json.get("email")
    if not name or not email:
        return {"error": "Name and email are required"}, 400
    users[id]["name"] = name
    users[id]["email"] = email
    return {"message": "User updated", "user": users[id]}

@app.route('/user/<int:id>', methods=["DELETE"])
def delete_user(id):
    if id not in users:
        return {"error": "User not found"}, 404
    del users[id]
    return {"message": "User deleted"}

@app.errorhandler(404)
def not_found_error(error):
    return {"error": "Resource not found"}, 404

@app.errorhandler(400)
def bad_request_error(error):
    return {"error": "Bad request"}, 400

if(__name__ == "__main__"):
    app.run(debug=True)