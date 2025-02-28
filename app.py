from flask import Flask, jsonify, render_template, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (needed for frontend)

# ✅ Replace with your actual WATI API details
WATI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI3MmI1ZDI5NC1mMGVmLTQ5MjctYmRlZS01NjE5MWZiNzM1OTgiLCJ1bmlxdWVfbmFtZSI6Imt1bGthcm5pcmFodWw4OEBnbWFpbC5jb20iLCJuYW1laWQiOiJrdWxrYXJuaXJhaHVsODhAZ21haWwuY29tIiwiZW1haWwiOiJrdWxrYXJuaXJhaHVsODhAZ21haWwuY29tIiwiYXV0aF90aW1lIjoiMDIvMjAvMjAyNSAxMDo0NDozOCIsInRlbmFudF9pZCI6IjEwNTUyMCIsImRiX25hbWUiOiJtdC1wcm9kLVRlbmFudHMiLCJodHRwOi8vc2NoZW1hcy5taWNyb3NvZnQuY29tL3dzLzIwMDgvMDYvaWRlbnRpdHkvY2xhaW1zL3JvbGUiOiJBRE1JTklTVFJBVE9SIiwiZXhwIjoyNTM0MDIzMDA4MDAsImlzcyI6IkNsYXJlX0FJIiwiYXVkIjoiQ2xhcmVfQUkifQ.UgnjWDuRf6QOFjpoXxgN0tFfo7bQx-pTfqCXIseVGuc"
WATI_API_URL = "https://live-mt-server.wati.io/105520/api/v1/getMessageTemplates"

# ✅ Replace with your Zoho Bigin API details
# ZOHO_ACCESS_TOKEN = "your_zoho_access_token"
# ZOHO_BIGIN_API_URL = "https://www.zohoapis.com/bigin/v1/Contacts"

# ✅ Fetch available WATI templates
@app.route("/get-templates", methods=["GET"])
def get_templates():
    headers = {"Authorization": f"Bearer {WATI_API_KEY}"}
    response = requests.get(WATI_API_URL, headers=headers)

    if response.status_code == 200:
        templates_data = response.json().get("messageTemplates", [])
        templates = [{"id": t["id"], "name": t["elementName"]} for t in templates_data]
        print("Processed Templates:", templates)
        return jsonify({"templates": templates})

    return jsonify({"error": "Failed to fetch templates"}), 500

# ✅ Fetch contact details from Zoho Bigin
# @app.route("/get-contact/<contact_id>", methods=["GET"])
# def get_contact(contact_id):
#     headers = {"Authorization": f"Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}"}
#     response = requests.get(f"{ZOHO_BIGIN_API_URL}/{contact_id}", headers=headers)

#     if response.status_code == 200:
#         contact_data = response.json().get("data", [])[0]
#         print("Fetched Contact:", contact_data)
#         return jsonify(contact_data)

#     return jsonify({"error": "Failed to fetch contact"}), 500

# ✅ Send a message using WATI API
# @app.route("/send-message", methods=["POST"])
# def send_message():
#     data = request.json
#     template_id = data.get("template_id")
#     phone_number = "your_phone_number"  # You can update this dynamically

#     if not template_id:
#         return jsonify({"error": "Template ID is required"}), 400

#     headers = {"Authorization": f"Bearer {WATI_API_KEY}", "Content-Type": "application/json"}
#     payload = {"template_id": template_id, "receiver": phone_number}

#     response = requests.post("https://live-mt-server.wati.io/api/v1/sendTemplate", json=payload, headers=headers)

#     if response.status_code == 200:
#         return jsonify({"message": "Message sent successfully!"})
    
#     return jsonify({"error": "Failed to send message"}), 500

# ✅ Serve HTML page
@app.route("/")
def index():
    return render_template("index.html")

def handler(event, context):
    return app(event, context)
    
