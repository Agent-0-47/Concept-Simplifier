# Concept Simplifier

## Description
This application simplifies complex engineering topics using a Flask backend, Tailwind CSS for styling, and CSS animations for interactivity. It integrates with the **Groq API** to generate simplified concepts.

## How to Run

### Backend
1. Navigate to the `backend` directory:
   ```bash
   cd backend
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:
   ```bash
   python app.py
   ```

### API Configuration
- The application uses the **Groq API** for generating simplified concepts.
- The API key is hardcoded in the backend for testing purposes. Ensure the following configuration is present in the `app.py` file:
  ```python
  client = openai.OpenAI(
      base_url="https://api.groq.com/openai/v1",
      api_key="your_actual_groq_api_key"  # Replace with your actual API key
  )
  ```

### Testing the Application
1. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

2. Enter a topic in the input field and click "Simplify" to see the simplified concept.

### Notes
- For production environments, it is recommended to use environment variables to store the API key instead of hardcoding it in the code.
- Refer to the [Groq API Documentation](https://console.groq.com/docs) for more details on supported models and API usage.


