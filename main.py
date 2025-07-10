from flask import Flask, request, jsonify

app = Flask(__name__)

# Exemple de "base de données" temporaire (dictionnaire en mémoire)
users = {}

@app.route("/")
def home():
    return "Serveur Devine le nombre actif !"

@app.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username = data.get("username")

    if username in users:
        return jsonify({"status": "error", "message": "Ce pseudo existe déjà."}), 400

    # Crée un nouveau compte avec 0 XP et 0 scores
    users[username] = {"xp": 0, "scores": {}}
    return jsonify({"status": "success", "message": f"Compte {username} créé."})

@app.route("/add_xp", methods=["POST"])
def add_xp():
    data = request.get_json()
    username = data.get("username")
    xp = data.get("xp")

    if username not in users:
        return jsonify({"status": "error", "message": "Utilisateur inconnu."}), 404

    users[username]["xp"] += xp
    return jsonify({"status": "success", "message": f"{xp} XP ajoutés à {username}."})

@app.route("/get_user", methods=["GET"])
def get_user():
    username = request.args.get("username")

    if username not in users:
        return jsonify({"status": "error", "message": "Utilisateur inconnu."}), 404

    return jsonify({"status": "success", "user": users[username]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
