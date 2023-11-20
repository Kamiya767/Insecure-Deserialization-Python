from flask import Flask, request
import json
app = Flask(__name__)

@app.route("/")
def page():
    json_data = request.values.get('str')
    return str(json.loads(json_data))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
