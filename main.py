from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def admin_home():
    return send_from_directory('.', 'admin.html')

@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    print("Admin server running on http://localhost:5001")
    app.run(port=5001, debug=True)