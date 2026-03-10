import os
from flask import Flask, render_template, request, jsonify

# Path fix for Vercel deployment
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit-lead', methods=['POST'])
def submit_lead():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    
    # In a real startup, you would send this to a database or HubSpot
    print(f"New Lead Captured: {name} ({email})")
    
    return jsonify({
        "status": "success",
        "message": f"Thanks {name}! Our team will reach out to {email} shortly."
    })

# Export for Vercel
app_handler = app
