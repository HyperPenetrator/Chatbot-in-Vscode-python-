import google.generativeai as genai

API_KEY = "Use your own API Key"     #Api key can be obtained from: https://aistudio.google.com/apikey edit "Use your own API Key" and enter the Api key to run the program ;)
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat.")
        break
    try:
        response = model.generate_content(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", e)
