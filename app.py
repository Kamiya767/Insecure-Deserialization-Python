from flask import Flask, request
import pickle, base64
app = Flask(__name__)

@app.route("/")
def page():
    pickle_data = request.values.get('str')
    return str(pickle.loads(base64.b64decode(pickle_data)))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)