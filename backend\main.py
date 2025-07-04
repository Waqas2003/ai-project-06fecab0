from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/api/projects', methods=['GET'])
def get_projects():
  projects = [
    {'id': 1, 'name': 'Project 1'},
    {'id': 2, 'name': 'Project 2'},
    {'id': 3, 'name': 'Project 3'}
  ]
  return jsonify(projects)

if __name__ == '__main__':
  app.run(debug=True)