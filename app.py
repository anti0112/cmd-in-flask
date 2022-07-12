import os
from flask import Flask, request, abort
from werkzeug.exceptions import BadRequest
from urls import get_query

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

@app.route("/perform_query")
def perform_query():
    cmd1 = request.args.get("cmd1")
    val1 = request.args.get("val1")
    cmd2 = request.args.get("cmd2")
    val2 = request.args.get("val2")
    filename = request.args.get("filename")
    
    if not(cmd1 and val1 and filename):
        abort(400)

    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        return abort(400, 'Not file')
    
    with open(file_path) as file:
        result = get_query(cmd1, val1, file)
        if cmd2 and val2:
            result = get_query(cmd2, val2, result)
     
        return app.response_class('\n'.join(result), content_type="text/plain")


if __name__ == "__main__":
    app.run(debug=True)
