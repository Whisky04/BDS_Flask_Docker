from flask import Flask, jsonify, request
from models import get_db_connection

app = Flask(__name__)

@app.route('/getAllObjects', methods=['GET'])
def get_all_objects():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS objects (id SERIAL PRIMARY KEY, name TEXT);')
    conn.commit()

    cur.execute('SELECT * FROM objects;')
    rows = cur.fetchall()
    cur.close()
    conn.close()

    objects = [{"id": row[0], "name": row[1]} for row in rows]
    return jsonify(objects)

@app.route('/addObject', methods=['POST'])
def add_object():
    conn = get_db_connection()
    cur = conn.cursor()

    name = request.json.get('name')
    cur.execute('INSERT INTO objects (name) VALUES (%s);', (name,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Object added successfully"})

@app.route('/deleteObject/<int:id>', methods=['DELETE'])
def delete_object(id):
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('DELETE FROM objects WHERE id = %s;', (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"message": "Object deleted successfully"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
