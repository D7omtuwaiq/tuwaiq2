from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup

app = Flask(__name__)

# Fetch data from the local HTML file
def fetch_data():
    with open('academy.html', 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    # Extracting course information
    courses = []
    for course in soup.find_all(class_='course'):
        courses.append(course.get_text(strip=True))
    return courses

# Simple chatbot response function
def get_response(user_input, data):
    if "دورات" in user_input:
        return "إليك الدورات المتاحة:\n" + "\n".join(data)
    elif "مرحبا" in user_input:
        return "مرحبًا! كيف يمكنني مساعدتك اليوم؟"
    else:
        return "آسف، لا أفهم ذلك."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def chat_response():
    user_input = request.form['user_input']
    data = fetch_data()
    response = get_response(user_input, data)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
