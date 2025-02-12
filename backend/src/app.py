from flask import Flask, jsonify
import subprocess
import sqlite3

app = Flask(__name__)

@app.route('/api/hello')
def home():
    return jsonify([{"message": "Hello from Flasks!"}])

@app.route('/api/interpret-query')
def interpret_query():

    message = 'CHART box_score IN scatter_plot FOR mins VS fgm WHERE game_id = "0022300061"'

    process = subprocess.Popen(
        ['./src/interpreter/main'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    response, errors = process.communicate(input=message)

    try:
        result = json.loads(response)
        if result["status"] == "success":
            print("The process was successful:", result["message"])

            connection = sqlite3.connect('./src/db/box_score.db')
            cursor = connection.cursor()

            cursor.execute(result["message"])


            results = cursor.fetchall()

            cursor.close()
            connection.close()

            return jsonify(results)
        else:
            print("The process failed with error code", result["error_code"], ":", result["message"])
            return result["error_code"]
    except json.JSONDecodeError:
        print("Failed to decode JSON response")