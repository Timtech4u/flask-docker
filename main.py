import os
from flask import Flask, request

app = Flask(__name__, static_url_path='', static_folder='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

PORT = int(os.environ.get("PORT", 8080))
if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=PORT)
