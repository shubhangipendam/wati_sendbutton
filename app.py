from flask import Flask, jsonify, render_template, request
import requests
from flask_cors import CORS
import os 

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (needed for frontend)

# ✅ Replace with your actual WATI API details
WATI_API_KEY = os.getenv("WATI_API_KEY")
WATI_API_URL = os.getenv("WATI_API_URL")


@app.route("/")
def index():
    return render_template("index.html")

# ✅ Fetch available WATI templates
@app.route("/get-templates", methods=["GET"])
def get_templates():
    page = request.args.get("page", 1, type=int)  # Get page number from request
    limit = 10
    
    headers = {"Authorization": f"Bearer {WATI_API_KEY}"}
    response = requests.get(WATI_API_URL, headers=headers)

    if response.status_code == 200:
        templates_data = response.json().get("messageTemplates", [])
        templates = [{"id": t["id"], "name": t["elementName"]} for t in templates_data]
        print("Processed Templates:", templates)
        return jsonify({"templates": templates})

    return jsonify({"error": "Failed to fetch templates"}), 500

@app.route("/send-message", methods=["POST"])
def send_message():
    data = request.json
    template_id = data.get("template_id")

    if not template_id:
        return jsonify({"error": "Template ID is required"}), 400

    return jsonify({"message": "Message sent successfully!"})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port, debug=True)
    
