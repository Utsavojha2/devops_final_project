from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def show_image():
    return '''
    <h1>My Image</h1>
    <img src="/static/image.jpg" width="400">
    '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888)
