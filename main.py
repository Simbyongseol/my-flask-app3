from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Render!"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_favorites = data.get('favorites', [])
    exclude_numbers = data.get('excludes', [])

    if len(user_favorites) > 5:
        return jsonify({"error": "행운의 숫자는 최대 5개까지 입력할 수 있습니다."}), 400

    lotto_sets = []
    for _ in range(10):
        lotto_numbers = generate_lotto_numbers(past_lotto_numbers, user_favorites, exclude_numbers)
        lotto_sets.append(lotto_numbers)

    return jsonify({"lotto_sets": lotto_sets})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
