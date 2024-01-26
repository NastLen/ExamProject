from flask import Flask, render_template, url_for, request, Response 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')
print('Hi')
if __name__ == 'main':
    app.run(port=5001, debug=True)