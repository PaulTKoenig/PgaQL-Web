from flask import Flask, jsonify, abort, request
import subprocess
import sqlite3
import json
import re

app = Flask(__name__)

@app.route('/api/get-player-details', methods=['POST'])
def get_player_details():
    data = request.get_json()

    if not data or 'player_ids' not in data:
        return jsonify({'error': 'Missing player_ids in request body'}), 400

    player_ids = data['player_ids']

    if not isinstance(player_ids, list) or not all(isinstance(pid, str) for pid in player_ids):
        return jsonify({'error': 'player_ids must be a list of strings'}), 400

    if len(player_ids) == 0:
        return jsonify({'error': 'player_ids list is empty'}), 400

    placeholders = ','.join(['?'] * len(player_ids))
    query = f"""
        SELECT playerId, firstName, lastName, playerTeamCity, playerTeamName
        FROM player_stats
        WHERE rowid IN (
            SELECT MIN(rowid)
            FROM player_stats
            WHERE playerId IN ({placeholders})
            GROUP BY playerId
        )
    """

    connection = sqlite3.connect('./src/db/player_stats.db')
    cursor = connection.cursor()
    cursor.execute(query, player_ids)
    results = cursor.fetchall()

    cursor.close()
    connection.close()

    players = [
        {
            "playerId": row[0],
            "firstName": row[1],
            "lastName": row[2],
            "playerTeamCity": row[3],
            "playerTeamName": row[4]
        }
        for row in results
    ]

    return jsonify(players), 200


@app.route('/api/get-player-details/<string:player_id>', methods=['GET'])
def getPlayerDetails(player_id):
    connection = sqlite3.connect('./src/db/player_stats.db')
    cursor = connection.cursor()

    cursor.execute(
        "SELECT playerId, firstName, lastName, playerTeamCity, playerTeamName FROM player_stats WHERE playerId = ?",
        (player_id,)
    )


    results = cursor.fetchone()

    cursor.close()
    connection.close()

    return jsonify(results), 200

@app.route('/api/get-all-field-values/<string:field_name>', methods=['GET'])
def getFieldValues(field_name):
    connection = sqlite3.connect('./src/db/player_stats.db')
    cursor = connection.cursor()

    cursor.execute("PRAGMA table_info(player_stats)")
    columns_info = cursor.fetchall()
    column_names = {col[1] for col in columns_info}

    if field_name not in column_names:
        raise ValueError(f"Invalid field name: {field_name}")

    query = f"SELECT {field_name} FROM player_stats"
    cursor.execute(query)


    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results), 200

@app.route('/api/interpret-query', methods=['GET'])
def interpret_query():

    # message = "CHART player_stats IN scatter_plot FOR blk VS fgm WHERE game_id = '0022300061'"

    query_string = request.args.get('query')

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

                connection = sqlite3.connect('./src/db/player_stats.db')
                cursor = connection.cursor()

                cursor.execute(result["message"]["query"] + " LIMIT 500;")

                results = cursor.fetchall()

                cursor.close()
                connection.close()

                return jsonify({ "rowData": results, "x_column_name": result["message"]["x_column_name"], "y_column_name": result["message"]["y_column_name"]}), 200
            else:
                print("The process failed with error code", result["error_code"], ":", result["message"])
                return result["message"], 400
                # abort(400)
        except json.JSONDecodeError:
            print("Failed to decode JSON response")
            abort(500)

    else:
        return "No query provided", 400