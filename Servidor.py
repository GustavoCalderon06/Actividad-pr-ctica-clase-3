from flask import Flask, jsonify, request

app = Flask(__name__)
tareas = []

@app.route('/tareas', methods=['GET'])
def get_tareas():
    return jsonify(tareas)

@app.route('/tareas', methods=['POST'])
def add_tarea():
    data = request.json
    tareas.append(data)
    return jsonify({'message': 'Tarea agregada exitosamente'})

@app.route('/tareas/<int:tarea_id>', methods=['PUT'])
def update_tarea(tarea_id):
    if 0 <= tarea_id < len(tareas):
        data = request.json
        tareas[tarea_id] = data
        return jsonify({'message': 'Tarea actualizada exitosamente'})
    else:
        return jsonify({'error': 'La tarea no existe'}), 404

@app.route('/tareas/<int:tarea_id>', methods=['DELETE'])
def delete_tarea(tarea_id):
    if 0 <= tarea_id < len(tareas):
        del tareas[tarea_id]
        return jsonify({'message': 'Tarea eliminada exitosamente'})
    else:
        return jsonify({'error': 'La tarea no existe'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

