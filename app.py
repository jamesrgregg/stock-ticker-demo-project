from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/stock', methods=['GET'])
def get_stock_data():
  api_key = request.args.get('apikey')
  ticker = request.args.get('ticker')
  if not api_key or not ticker:
    return jsonify({'error': 'API key and ticker symbol are required'}), 400

  url = f'https://financialmodelingprep.com/api/v3/quote/{ticker}?apikey={api_key}'
  response = requests.get(url)

  if response.status_code != 200:
    return jsonify({'error': 'Failed to fetch data from FMP API'}), response.status_code

  return jsonify(response.json())

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8081, debug=True)
