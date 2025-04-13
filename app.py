from flask import Flask, render_template, request, jsonify
import requests  # Use requests to make HTTP calls
import os  # Import os to access environment variables

app = Flask(__name__)

# Fetch the Groq API key from an environment variable
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")  # Ensure this is set in your environment
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"  # Groq API endpoint

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/simplify", methods=["POST"])
def simplify():
    topic = request.json.get("topic")
    if not topic:
        return jsonify({"error": "Topic is required"}), 400

    try:
        # Prepare the payload for the Groq API
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant.Answer like you are explaining to a 10 year old."},
                {"role": "user", "content": f"Explain the concept of {topic} in simple terms."}
            ]
        }

        # Make the POST request to the Groq API
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {GROQ_API_KEY}"
        }
        response = requests.post(GROQ_API_URL, json=payload, headers=headers)

        # Check if the response is successful
        if response.status_code == 200:
            data = response.json()
            concept = data["choices"][0]["message"]["content"]
            return jsonify({"concept": concept})
        else:
            # Handle API errors
            return jsonify({"error": "Failed to fetch response from Groq API", "details": response.text}), response.status_code

    except Exception as e:
        print("Error while calling Groq API:", str(e))  # Debugging
        return jsonify({"error": "An internal server error occurred.", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)