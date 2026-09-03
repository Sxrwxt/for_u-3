from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # อนุญาตให้ Frontend บน GitHub Pages ส่งข้อมูลมาหาได้

@app.route('/check-answer', methods=['POST'])
def check_answer():
    data = request.get_json()
    user_choice = data.get('choice')  # รับค่า 'yes' หรือ 'no'
    
    if user_choice == 'yes':
        response_text = "เลิกฝันครับน้อง"
    else:
        response_text = "เดี๋ยวโชก็กลับมา"
        
    return jsonify({"message": response_text})

if __name__ == '__main__':
    app.run(port=5000)
