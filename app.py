from flask import Flask, request, jsonify
import joblib

# Start Flask app
app = Flask(__name__)

# Load trained AI model
model = joblib.load("severity_model.pkl")

# Home route (for testing)
@app.route("/", methods=["GET"])
def home():
 return jsonify({"message": "ResQMe AI Server Running"})


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if "message" not in data:
        return jsonify({"error": "Message is required"}), 400
    message = data["message"].lower()
 # AI prediction
    prediction = model.predict([message])
    severity = str(prediction[0])

 # MASTER SAFETY RULES (Always included)
    general_rules = [
 "Ensure the area is safe before approaching (watch for traffic)",
 "Do not move the victim unless there is danger",
 "wait for help" ]


 # FIRST AID RULE ENGINE
    first_aid = []
 # NOT BREATHING (Highest Priority)

    if "not breathing" in message or "no breathing" or "no dey breathe" or "no breathe" or "no get breathe" in message:
        first_aid = [
        "Lay the victim flat on their back",
        "Tilt the head back gently",
        "Check breathing again",
         "Begin chest compressions if trained",
    ]

  # UNCONSCIOUS
    elif "unconscious" in message or "not responding" in message:
        first_aid = [
  "Check if the victim is breathing",
  "If breathing, gently turn the victim on their side",
  "Keep the head tilted slightly back",
  "Do not give food or water",
  "Monitor breathing continuously",
     ]

 # SEVERE BLEEDING
    elif "bleeding" in message or severity in  "Critical":
     first_aid = [
  "Apply firm pressure to the bleeding area using a cloth or clothing",
  "Do not remove the cloth if soaked; add another cloth",
  "Raise the injured area slightly if possible",
  "Keep the victim lying down",
  "Continue pressure until help arrives",
  "Use clean clothing, a scarf, or a towel if a bandage is unavailable",
    ]

 # MOTORCYCLE ACCIDENTS
    elif "bike" in message or "motorcycle" in message or "okada" in message:
        first_aid = [
  "Do not remove helmet unless breathing is blocked",
  "Keep the victim still",
 "Check for bleeding",
  "Monitor breathing",
  "Wait for help."
    ]

 # FRACTURE
    elif "broken" in message or "cannot move" in message or "leg pain" in message or "arm pain" in message:
         first_aid = [
  "Do not move the injured limb",
  "Support the limb using cloth or clothing",
  "Keep the victim still",
  "Do not straighten the limb",
  "Wait for help",
    ]

 # MEDIUM SEVERITY
    elif severity == "Medium":
        first_aid = [
  "Help the victim sit or lie safely",
  "Keep the victim calm and still",
  "Check for bleeding or fractures",
  "Avoid unnecessary movement",
  "Wait for help",
     ]

 # LOW SEVERITY
    elif severity == 'Low':
         first_aid = [
 "Check for visible injuries",
 "Clean small wounds if possible",
 "Keep the victim comfortable",
 "Monitor for dizziness",
 "Stay with the victim"]

    else:
   first_aid_steps = [
 "Ensure the area is safe before approaching (watch for traffic)",
 "Do not move the victim unless there is danger",
 "wait for help" ]



 # ACTION DECISION
    if severity == "Critical":
        action = "Send help immediately"
        priority = 1
    elif severity == "Medium":
        action = "Send help quickly"
        priority = 2
    else:
        action = "Display first aid message"
        priority = 3

 # Combine general + specific rules
    all_instructions = general_rules + first_aid

 # Final Response
    return jsonify({
    "severity": severity,
    "recommended_action": action,
    "priority_level": priority,
    "first_aid_steps": all_instructions
         })
    

 # Run server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
 

## STEP 2: Put Your Files on GitHub  Render deploys from GitHub, so she needs to upload her project there.  1. Go to [github.com](https://github.com) and create a free account2. Click the **"+"** button at the top right → **"New repository"** 3. Give it a name like `resqmission-model`4. Set it to **Public**, click **Create repository** 5. Follow the instructions GitHub shows to upload your files (or use GitHub Desktop if she's not comfortable with terminal)  ---  ## STEP 3: Create a Render Account  1. Go to [render.com](https://render.com) 2. Click **"Get Started for Free"** 3. Sign up using her **GitHub account** — this connects the two together ---  ## STEP 4: Create a New Web Service on Render  1. Once logged in, click **"New +"** at the top2. Select **"Web Service"** 3. Render will show her GitHub repositories — select `resqmission-model`4. Click **"Connect"**  ---  ## STEP 5: Configure the Service  Render will ask her to fill in some settings:  | Field | What to type | |---|---| | **Name** | `resqmission-model` (or anything she likes) | | **Region** | Choose the closest to her location | | **Branch** | `main` | | **Runtime** | `Python 3` | | **Build Command** | `pip install -r requirements.txt` | | **Start Command** | `gunicorn app:

















