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
    if "دورات" in user_input or "كورسات" in user_input or "تدريب" in user_input:
        return "إليك الدورات المتاحة:\n" + "\n".join(data)
    elif "مرحبا" in user_input or "هلا" in user_input or "أهلاً" in user_input:
        return "مرحبًا! كيف يمكنني مساعدتك اليوم؟"
    elif "كيف الحال" in user_input or "كيفك" in user_input:
        return "أنا بخير، شكرًا لسؤالك! وأنت؟"
    elif "ما هي خدماتك" in user_input or "وش خدماتك" in user_input:
        return "أنا هنا لمساعدتك في العثور على معلومات حول الدورات والمساعدة في استفساراتك."
    elif "شكراً" in user_input or "يعطيك العافية" in user_input:
        return "عفواً! إذا كنت بحاجة إلى شيء آخر، فلا تتردد في إخباري."
    elif "أوقات الدورات" in user_input or "متى تبدأ الدورات" in user_input:
        return "يمكنك العثور على مواعيد الدورات في الموقع. هل لديك دورة معينة في ذهنك؟"
    elif "شهادات" in user_input or "هل تحصل على شهادة" in user_input:
        return "نعم، جميع الدورات تقدم شهادات عند الانتهاء منها بنجاح."
    elif "أخبار الأكاديمية" in user_input or "تحديثات" in user_input:
        return "تابع موقعنا للحصول على آخر التحديثات والأخبار حول الأكاديمية."
    elif "التسجيل" in user_input or "كيف أسجل" in user_input:
        return "يمكنك التسجيل عبر الموقع الإلكتروني. هل تحتاج مساعدة في عملية التسجيل؟"
    elif "وداعًا" in user_input or "مع السلامة" in user_input:
        return "وداعًا! أتمنى لك يومًا سعيدًا!"
    else:
        return "آسف، لا أفهم ذلك. يمكنك طرح سؤال آخر!"


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
