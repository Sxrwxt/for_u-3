from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # อนุญาตให้ Frontend ส่งข้อมูลข้ามเซิร์ฟเวอร์มาหาได้

@app.route('/get-redirect-url', methods=['POST'])
def get_redirect_url():
    data = request.get_json()
    user_choice = data.get('choice')  # รับค่า 'yes' หรือ 'no' จาก Frontend
    
    # ประมวลผลใน Python เพื่อเลือกปลายทางเว็บ
    if user_choice == 'yes':
        redirect_url = "https://www.youtube.com/watch?si=JEOh-tw1heNgUD9c&v=DjvwDCw6pl4&feature=youtu.be"  # เว็บสำหรับคนกด "ใช่"
    else:
        redirect_url = "https://youtu.be/tUuqWFExZgY?si=Wrhctkh9R9KnXE43&t=190"  # เว็บสำหรับคนกด "ไม่ใช่"
        
    return jsonify({"target_url": redirect_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
