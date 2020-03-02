from flask import Flask, render_template, redirect, request, url_for , send_file

app = Flask(__name__)
# app.debug = True;
# @app.route('/')
@app.route('/')
def index():
    return render_template('Love.html')



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
            port=80,
            debug=False)
