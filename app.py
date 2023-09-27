from flask import Flask, request, jsonify
import sentiment_analysis_model as sam

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.json
    text = data['text']
    sentiment = sam.predict_sentiment(text)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
