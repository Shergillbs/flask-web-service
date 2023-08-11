from flask import Flask, request, jsonify
import csv

app = Flask(__name__)

@app.route('/data-endpoint', methods=['POST'])
def receive_data():
    # Get JSON data from request
    data = request.json

    # Save data to CSV file
    with open('data.csv', 'a', newline='') as csvfile:
        fieldnames = ['EndTime', 'Open', 'High', 'Low', 'Close', 'Volume', 'RSI']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Uncomment the next line if you want to write headers to the file
        # writer.writeheader()  
        
        writer.writerow(data)

    return jsonify({'message': 'Data saved successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)