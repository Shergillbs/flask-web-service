from flask import Flask, request, jsonify, send_from_directory, abort
import pandas as pd
import os

app = Flask(__name__)

@app.route('/upload_data', methods=['POST'])
def upload_data():
    try:
        # Get JSON data from the POST request
        data = request.get_json()

        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Save the DataFrame as a CSV file with the current date
        filename = f"data_{df['DateTime'][0][:10]}.csv"
        df.to_csv(filename, index=False)

        return jsonify({"message": "Data successfully saved."}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/<date>', methods=['GET'])
def download_data(date):
    directory = os.path.abspath('.')  # Using an absolute path for clarity
    filename = f"data_{date}.csv"
    full_path = os.path.join(directory, filename)
    
    # Check if the file exists
    if not os.path.exists(full_path):
        abort(404, description="Resource not found")
    
    return send_from_directory(directory=directory, filename=filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

