
from flask import Flask, request, jsonify

app = Flask(__name__)

data_store = {}

@app.route('/api/resource', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def resource():
    if request.method == 'GET':
        return jsonify(data_store), 200

    elif request.method == 'POST':
        data = request.get_json()
        item_id = len(data_store) + 1
        data_store[item_id] = data
        return jsonify({'id': item_id, 'data': data}), 201

    elif request.method == 'PUT':
        item_id = int(request.args.get('id'))
        data = request.get_json()
        if item_id in data_store:
            data_store[item_id] = data
            return jsonify({'id': item_id, 'data': data}), 200
        else:
            return jsonify({'error': 'Resource not found'}), 404

    elif request.method == 'DELETE':
        item_id = int(request.args.get('id'))
        if item_id in data_store:
            del data_store[item_id]
            return jsonify({'message': 'Resource deleted'}), 200
        else:
            return jsonify({'error': 'Resource not found'}), 404

    elif request.method == 'PATCH':
        item_id = int(request.args.get('id'))
        data = request.get_json()
        if item_id in data_store:
            data_store[item_id].update(data)
            return jsonify({'id': item_id, 'data': data_store[item_id]}), 200
        else:
            return jsonify({'error': 'Resource not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)

