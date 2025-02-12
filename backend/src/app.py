from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api')
def home():
    return jsonify([{"message": "Hello from Flasks!"}])

@app.route('/interpret-query')
def interpret_query():

    message = 'CHART box_score IN scatter_plot FOR mins VS fgm WHERE game_id = "0022300061"'

    process = subprocess.Popen(
        ['./main'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    response, errors = process.communicate(input=message)

    connection = sqlite3.connect('box_score.db')
    cursor = connection.cursor()

    cursor.execute(response)


    results = cursor.fetchall()

    cursor.close()
    connection.close()

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
