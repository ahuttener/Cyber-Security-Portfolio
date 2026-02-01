from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated Database (In-Memory)
database = {
    "1001": {"name": "Admin", "balance": 1500000000.00, "role": "admin"}, # Target Account
    "1002": {"name": "Guest User", "balance": 50.00, "role": "user"}      # Attacker Account
}

@app.route('/')
def home():
    return jsonify({"message": "Welcome to API Digital Bank. Vulnerable Endpoint running."})

# 🚨 VULNERABILITY: IDOR / BOLA (Broken Object Level Authorization)
# The API does not check if the requester is the owner of the account ID.
@app.route('/api/balance/<user_id>', methods=['GET'])
def get_balance(user_id):
    user = database.get(user_id)
    if user:
        # FLAW: Returning sensitive data without token validation
        return jsonify({
            "status": "success",
            "user_id": user_id,
            "owner": user['name'],
            "balance_brl": user['balance']
        })
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    print("🔥 VULNERABLE BANK API STARTED...")
    print("listening on port 5000")
    print("[*] Target Account (ID 1001): R$ 1,500,000,000.00")
    app.run(debug=True, port=5000)
