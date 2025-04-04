from flask import Flask, jsonify, abort, request
import subprocess
import sqlite3
import json
import re

app = Flask(__name__)

@app.route('/api/get-all-field-values/<string:field_name>', methods=['GET'])
def getFieldValues(field_name):
    connection = sqlite3.connect('./src/db/box_score.db')
    cursor = connection.cursor()

    cursor.execute(f"SELECT {field_name} FROM box_score")


    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results), 200

@app.route('/api/interpret-query', methods=['GET'])
def interpret_query():

    # message = "CHART box_score IN scatter_plot FOR blk VS fgm WHERE game_id = '0022300061'"

    query_string = request.args.get('query')  # Get the query parameter from the URL

    if query_string:

        process = subprocess.Popen(
            ['./src/interpreter/main'],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        response, errors = process.communicate(input=query_string)
        
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

                return jsonify(results), 200
            else:
                print("The process failed with error code", result["error_code"], ":", result["message"])
                return result["message"], 400
                # abort(400)
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
            abort(500)

    else:
        return "No query provided", 400